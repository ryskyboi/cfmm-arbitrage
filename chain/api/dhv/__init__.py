from dataclasses import dataclass
from datetime import datetime as dt
from collections import defaultdict

from chain.abi import AbiManager
from chain.abi.types import cast_e6_to_float, cast_e18_to_float, cast_e27_to_float
from chain.api.reader import ChainReader
from chain.chains import ChainDefinition
from chain.web3_api import Web3Endpoint

from chain.api.dhv.spreadparams import FeeIvSpreadParams, CollateralSpreadParams,\
    DeltaSpreadParams
from chain.api.dhv.positions import Positions, Position
from chain.api.dhv.collatparams import CollateralParams
from chain.api.dhv.slippageparams import SlippageParams

from chain.abi.ARBITRUM_GOERLI.DHV.volFeed import volFeed
from chain.abi.ARBITRUM_GOERLI.DHV.beyondPricer import beyondPricer
from chain.abi.ARBITRUM_GOERLI.DHV.lens import lens, DHVLensMK1_OptionChain
from chain.abi.ARBITRUM_GOERLI.DHV.OpynNewCalculator import OpynNewCalculator

##Testnet token contracts
from chain.abi.ARBITRUM_GOERLI.DHV.weth import weth
from chain.abi.ARBITRUM_GOERLI.DHV.usdc import usdc

@dataclass
class SabrModelParam:
    alpha: float
    beta: float
    rho: float
    nu: float

@dataclass
class SabrExpiryParams:
    expiry_timestamp_s: float
    call_sabr: SabrModelParam
    put_sabr: SabrModelParam
    rate: float


class DhvChainReader(ChainReader):
    def __init__(self, chain_def: ChainDefinition,
                 web3_endpoint: Web3Endpoint, abi_manager: AbiManager):
        super().__init__(chain_def, web3_endpoint, abi_manager)
        self.protocol_def = "DHV"
        self._vol_feed: volFeed = self._contract(volFeed)
        self._beyond_pricer: beyondPricer = self._contract(beyondPricer)
        self._lens : lens = self._contract(lens)
        self._opyn_calculator : OpynNewCalculator = self._contract(OpynNewCalculator)

    def expiry_timestamps_s(self, is_include_expired=False) -> list[int]:
        """
        List of expiries (optionally include expired ones) as timestamps, in (int) seconds.
        :return:
        """
        return [t for t in self._vol_feed.getExpiries()
                if t > int(dt.now().timestamp()) or is_include_expired]

    def sabr_param_data(self, is_include_expired=False) -> list[SabrExpiryParams]:
        """
        List of all sabr data, including rate, optionally include expired dates.
        :return:
        """
        sabrs: list[SabrExpiryParams] = []
        for t in self.expiry_timestamps_s(is_include_expired):
            chain_sabr = self._vol_feed.sabrParams(t)
            sabrs.append(
                SabrExpiryParams(
                    t,
                    SabrModelParam(
                        cast_e6_to_float(chain_sabr[0]),
                        cast_e6_to_float(chain_sabr[1]),
                        cast_e6_to_float(chain_sabr[2]),
                        cast_e6_to_float(chain_sabr[3]),
                    ),
                    SabrModelParam(
                        cast_e6_to_float(chain_sabr[4]),
                        cast_e6_to_float(chain_sabr[5]),
                        cast_e6_to_float(chain_sabr[6]),
                        cast_e6_to_float(chain_sabr[7]),
                    ),
                    float(chain_sabr[8])
                )
            )
        return sabrs

    def position_data(self) -> Positions:
        """This takes the current positions that we
        have on chain and converts them to a nested dict

        Returns:
            A list of position objects
            where position is (expiry_timestamp_s, is_call, strike, position)
        """
        _position_data : Positions = []
        option_chain : DHVLensMK1_OptionChain = self._lens.getOptionChain()
        #expirations = option_chain[0]
        data = option_chain[1]
        for _by_expiration in data:
            expiry = _by_expiration[0]
            for _by_strike_calls in _by_expiration[2]:
                strike = cast_e18_to_float(_by_strike_calls[0])
                _position_data.append(Position(expiry, True, strike,
                                               cast_e18_to_float(_by_strike_calls[4])))
            for _by_strike_puts in _by_expiration[4]:
                strike = cast_e18_to_float(_by_strike_puts[0])
                _position_data.append(Position(expiry, False, strike,
                                               cast_e18_to_float(_by_strike_puts[4])))
        return _position_data

    def collat_param_data(self, is_usd_collateral: bool = False) -> CollateralParams:
        """
        https://www.notion.so/rysk/DHV-Parameters-numbers-7e79e9ffb88e4bc9bcc9c8b813233424
        Takes in the collat that we are using and outputs current collat params
        Returns:
            CollateralParams: spot shocks and maps of DTE to premium curves for both calls and puts
        """
        usdc_address = usdc.address
        weth_address = weth.address
        collat = usdc_address if is_usd_collateral else weth_address
        call_spot_shock = cast_e27_to_float(self._opyn_calculator.getSpotShock(
            weth_address, usdc_address, collat, False))
        put_spot_shock = cast_e27_to_float(self._opyn_calculator.getSpotShock(
            weth_address, usdc_address, collat, True))
        times_to_exp_calls = self._opyn_calculator.getTimesToExpiry(
            weth_address, usdc_address, collat, False)
        times_to_exp_puts = self._opyn_calculator.getTimesToExpiry(
            weth_address, usdc_address, collat, True)
        max_prices_calls = [cast_e27_to_float(self._opyn_calculator.getMaxPrice(
            weth_address, usdc_address, collat, False, t)) for t in times_to_exp_calls]
        max_prices_puts = [cast_e27_to_float(self._opyn_calculator.getMaxPrice(
            weth_address, usdc_address, collat, True, t)) for t in times_to_exp_puts]
        return CollateralParams(call_spot_shock,
                                dict(zip([t/(60*60*24) for t in times_to_exp_calls],
                                         max_prices_calls)),
                                put_spot_shock,
                                dict(zip([t/(60*60*24) for t in times_to_exp_puts],
                                         max_prices_puts)))

    def slippage_param_data(self) -> SlippageParams:
        """Takes slippage params that we are currently using on chain and outputs them

        Returns:
            SlippageGradientMultipliers: slippage gradient multipliers for calls and puts
            SlippageGradient; number we multiply all parsnms by
        """
        call_slippage_gradient_multipliers =\
            self._beyond_pricer.getCallSlippageGradientMultipliers()
        put_slippage_gradient_multipliers =\
            self._beyond_pricer.getPutSlippageGradientMultipliers()
        slippage_gradient = self._beyond_pricer.slippageGradient()
        return SlippageParams([cast_e18_to_float(multiplier) for multiplier
                               in put_slippage_gradient_multipliers],
                              [cast_e18_to_float(multiplier) for multiplier
                               in call_slippage_gradient_multipliers],
                              cast_e18_to_float(slippage_gradient))

    def fee_iv_spread_param_data(self) -> FeeIvSpreadParams:
        """returns: feeivspreadparsms contains a fee per contract a relative myltiplier
        that allows us to pay less in IV than we buy it for
        """
        fee_per_contract = self._beyond_pricer.feePerContract()
        iv_relative_spread = self._beyond_pricer.bidAskIVSpread()
        return FeeIvSpreadParams(cast_e6_to_float(fee_per_contract),
                                 cast_e6_to_float(iv_relative_spread))

    def delta_spread_param_data(self) -> DeltaSpreadParams:
        """returns: delta_spread_params contains 4 rates charged when buying/sellig
        calls and puts and their related hedging activities"""
        delta_borrow_rates = self._beyond_pricer.deltaBorrowRates()
        return DeltaSpreadParams(cast_e6_to_float(delta_borrow_rates[1]),
                                  cast_e6_to_float(delta_borrow_rates[0]),
                                  cast_e6_to_float(delta_borrow_rates[2]),
                                  cast_e6_to_float(delta_borrow_rates[3]))

    def collat_spread_param_data(self):
        """returns: collat_spread_params contains the rate paid on
            collat that the DHV has to lock up"""
        collat_lending_rate = self._beyond_pricer.collateralLendingRate()
        return CollateralSpreadParams(cast_e6_to_float(collat_lending_rate))

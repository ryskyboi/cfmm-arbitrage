from datetime import datetime as dt

from chain.abi import AbiManager
from chain.abi.ARBITRUM_GOERLI.DHV.OpynNewCalculator import OpynNewCalculator
from chain.abi.ARBITRUM_GOERLI.DHV.beyondPricer import beyondPricer
from chain.abi.ARBITRUM_GOERLI.DHV.lens import lens, DHVLensMK1_OptionStrikeDrill
from chain.abi.ARBITRUM_GOERLI.DHV.usdc import usdc
from chain.abi.ARBITRUM_GOERLI.DHV.volFeed import volFeed
# Testnet token contracts
from chain.abi.ARBITRUM_GOERLI.DHV.weth import weth
from chain.abi.types import int_e18, uint_e18
from chain.api.dhv_comp.collatparams import CollateralParams
from chain.api.dhv_comp.positions import OptionPosition
from chain.api.dhv_comp.sabrparams import SabrModelParam, SabrExpiryParams
from chain.api.dhv_comp.slippagegradient import SlippageGradient
from chain.api.dhv_comp.spreadparams import FeeIvSpreadParams, CollateralSpreadParams, \
    DeltaSpreadParams
from chain.api.reader import ChainReader
from chain.chains import ChainDefinition
from chain.web3_api import Web3Endpoint


class DhvCompChainReader(ChainReader):
    def __init__(self, chain_def: ChainDefinition,
                 web3_endpoint: Web3Endpoint, abi_manager: AbiManager):
        super().__init__(chain_def, web3_endpoint, abi_manager)
        self.protocol_def = "DHV"
        self._vol_feed: volFeed = self._contract(volFeed)
        self._beyond_pricer: beyondPricer = self._contract(beyondPricer)
        self._lens: lens = self._contract(lens)
        self._opyn_calculator: OpynNewCalculator = self._contract(OpynNewCalculator)

    def expiry_timestamps_s(self, is_include_expired=False) -> list[int]:
        """
        List of expiries (optionally include expired ones) as timestamps, in (int) seconds.
        :return:
        """
        return [t for t in self._vol_feed.getExpiries()
                if t > int(dt.now().timestamp()) or is_include_expired]

    def sabrs(self, is_include_expired=False) -> list[SabrExpiryParams]:
        """
        List of all sabr parameter data, including rate, optionally include expired dates.
        :return:
        """
        sabrs: list[SabrExpiryParams] = []
        for t in self.expiry_timestamps_s(is_include_expired):
            chain_sabr = self._vol_feed.sabrParams(uint_e18(t))
            sabrs.append(
                SabrExpiryParams(
                    t,
                    SabrModelParam(
                        chain_sabr[0].to_float_e6(),
                        chain_sabr[1].to_float_e6(),
                        chain_sabr[2].to_float_e6(),
                        chain_sabr[3].to_float_e6(),
                    ),
                    SabrModelParam(
                        chain_sabr[4].to_float_e6(),
                        chain_sabr[5].to_float_e6(),
                        chain_sabr[6].to_float_e6(),
                        chain_sabr[7].to_float_e6(),
                    ),
                    chain_sabr[8].to_float_e18()
                )
            )
        return sabrs

    def option_positions(self) -> list[OptionPosition]:
        """
        All open (not yet expired) option positions in the DHV
        :return: list of OptionPosition objects.
        """
        option_chain = self._lens.getOptionChain()
        pos: list[OptionPosition] = []

        def opt_pos(is_call: bool, options: list[DHVLensMK1_OptionStrikeDrill]) -> list[OptionPosition]:
            return [
                OptionPosition(
                    smile.expiration.to_float_e0(),
                    is_call,
                    o.strike.to_float_e18(),
                    o.exposure.to_float_e18()
                ) for o in options
            ]

        for smile in option_chain.optionExpirationDrills:
            pos += opt_pos(True, smile.callOptionDrill) + \
                   opt_pos(False, smile.putOptionDrill)
        return pos

    def collateral_params(self, is_usd_collateral: bool = False) -> CollateralParams:
        """
        https://www.notion.so/rysk/DHV-Parameters-numbers-7e79e9ffb88e4bc9bcc9c8b813233424
        Takes in the collateral currency and outputs collateral params
        :return:
            CollateralParams: spot shocks and maps of DTE to premium curves for both calls and puts
        """
        usdc_address = usdc.address
        weth_address = weth.address
        collat = usdc_address if is_usd_collateral else weth_address
        opyn = self._opyn_calculator
        call_spot_shock: float = opyn.getSpotShock(weth_address, usdc_address, collat, False).to_float_e27()
        put_spot_shock: float = opyn.getSpotShock(weth_address, usdc_address, collat, True).to_float_e27()
        times_to_exp_calls = opyn.getTimesToExpiry(weth_address, usdc_address, collat, False)
        times_to_exp_puts = self._opyn_calculator.getTimesToExpiry(weth_address, usdc_address, collat, True)
        max_prices_calls = [
            opyn.getMaxPrice(weth_address, usdc_address, collat, False, t).to_float_e27()
            for t in times_to_exp_calls
        ]
        max_prices_puts = [
            opyn.getMaxPrice(weth_address, usdc_address, collat, True, t).to_float_e27()
            for t in times_to_exp_puts
        ]
        return CollateralParams(
            call_spot_shock,
            dict(zip([t / (60 * 60 * 24) for t in times_to_exp_calls], max_prices_calls)),
            put_spot_shock,
            dict(zip([t / (60 * 60 * 24) for t in times_to_exp_puts], max_prices_puts))
        )

    def slippage_params(self) -> SlippageGradient:
        """
        :return:
            SlippageGradientMultipliers: slippage gradient multipliers for calls and puts
            SlippageGradient; number we multiply all parsnms by
        """
        call_slippage_gradient_multipliers = self._beyond_pricer.getCallSlippageGradientMultipliers()
        put_slippage_gradient_multipliers = self._beyond_pricer.getPutSlippageGradientMultipliers()
        slippage_gradient = self._beyond_pricer.slippageGradient()
        return SlippageGradient(
            [multiplier.to_float_e18() for multiplier in put_slippage_gradient_multipliers],
            [multiplier.to_float_e18() for multiplier in call_slippage_gradient_multipliers],
            slippage_gradient.to_float_e18()
        )

    def fee(self) -> float:
        """
        Fee. The fixed dollar amount a trader pays to make a trade.
        """
        return self._beyond_pricer.feePerContract().to_float_e6()

    def iv_spread(self) -> float:
        """
        An additional volatility spread to charge traders. Aka *the handbrake*.
        """
        return self._beyond_pricer.bidAskIVSpread().to_float_e6()

    def delta_rates(self) -> DeltaSpreadParams:
        """returns: delta_spread_params contains 4 rates charged when buying/selling
        calls and puts and their related hedging activities"""
        sellLong: int_e18  # when someone sells puts to DHV (we need to long to hedge)
        sellShort: int_e18  # when someone sells calls to DHV (we need to short to hedge)
        buyLong: int_e18  # when someone buys calls from DHV (we need to long to hedge)
        buyShort: int_e18  # when someone buys puts from DHV (we need to short to hedge)
        sellLong, sellShort, buyLong, buyShort = self._beyond_pricer.deltaBorrowRates()

        dhv_buy_call_rate: float = sellShort.to_float_e6()
        dhv_buy_put_rate: float = sellLong.to_float_e6()
        dhv_sell_call_rate: float = buyLong.to_float_e6()
        dhv_sell_put_rate: float = buyShort.to_float_e6()

        return DeltaSpreadParams(dhv_buy_call_rate, dhv_buy_put_rate, dhv_sell_call_rate, dhv_sell_put_rate)

    def collateral_rate(self) -> float:
        """Collateral spread param: the rate charged to traders for
            the cost of capital on the collat that the DHV has to lock up to mint a short position."""
        return self._beyond_pricer.collateralLendingRate().to_float_e6()

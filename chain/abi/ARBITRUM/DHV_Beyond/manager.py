
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class Types_Option:
    expiration: uint64
    strike: uint128
    isPut: bool
    isBuyable: bool
    isSellable: bool

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            bool(args[2]),
            bool(args[3]),
            bool(args[4]),
        )



@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            bool(args[2]),
            Address.from_tuple(args[3]),
            Address.from_tuple(args[4]),
            Address.from_tuple(args[5]),
        )



@dataclass
class BeyondPricer_DeltaBandMultipliers:
    callSlippageGradientMultipliers: list[int80]
    putSlippageGradientMultipliers: list[int80]
    callSpreadCollateralMultipliers: list[int80]
    putSpreadCollateralMultipliers: list[int80]
    callSpreadDeltaMultipliers: list[int80]
    putSpreadDeltaMultipliers: list[int80]

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            [int80.from_tuple(arg_0) for arg_0 in args[0]],
            [int80.from_tuple(arg_0) for arg_0 in args[1]],
            [int80.from_tuple(arg_0) for arg_0 in args[2]],
            [int80.from_tuple(arg_0) for arg_0 in args[3]],
            [int80.from_tuple(arg_0) for arg_0 in args[4]],
            [int80.from_tuple(arg_0) for arg_0 in args[5]],
        )



@dataclass
class BeyondPricer_DeltaBorrowRates:
    sellLong: int_e18
    sellShort: int_e18
    buyLong: int_e18
    buyShort: int_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            int_e18.from_tuple(args[0]),
            int_e18.from_tuple(args[1]),
            int_e18.from_tuple(args[2]),
            int_e18.from_tuple(args[3]),
        )



class manager(BaseAbi):
    address: Address = Address("0xD404D0eD7fe1EB1Cd6388610F9e5B5E6b6E41E72")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def beyondPricer(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "beyondPricer"
        )
        return Address.from_tuple(my_var_0)
        
    def changeOptionBuyOrSell(
        self,
        options: list[Types_Option],
    ) -> None:
        self._call(
            "changeOptionBuyOrSell",
            options=options
        )
        
    def createOrder(
        self,
        _optionSeries: Types_OptionSeries,
        _amount: uint_e18,
        _price: uint_e18,
        _orderExpiry: uint_e18,
        _buyerAddress: Address,
        _isBuyBack: bool,
        _spotMovementRange: list[uint_e18],
    ) -> uint_e18:
        my_var_0 = self._call(
            "createOrder",
            _optionSeries=_optionSeries,
            _amount=_amount,
            _price=_price,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _isBuyBack=_isBuyBack,
            _spotMovementRange=_spotMovementRange
        )
        return uint_e18.from_tuple(my_var_0)
        
    def createStrangle(
        self,
        _optionSeriesCall: Types_OptionSeries,
        _optionSeriesPut: Types_OptionSeries,
        _amountCall: uint_e18,
        _amountPut: uint_e18,
        _priceCall: uint_e18,
        _pricePut: uint_e18,
        _orderExpiry: uint_e18,
        _buyerAddress: Address,
        _callSpotMovementRange: list[uint_e18],
        _putSpotMovementRange: list[uint_e18],
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "createStrangle",
            _optionSeriesCall=_optionSeriesCall,
            _optionSeriesPut=_optionSeriesPut,
            _amountCall=_amountCall,
            _amountPut=_amountPut,
            _priceCall=_priceCall,
            _pricePut=_pricePut,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _callSpotMovementRange=_callSpotMovementRange,
            _putSpotMovementRange=_putSpotMovementRange
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def deltaLimit(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "deltaLimit",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def initializeTenorParams(
        self,
        _deltaBandWidth: uint_e18,
        _numberOfTenors: uint16,
        _maxTenorValue: uint16,
        _tenorPricingParams: list[BeyondPricer_DeltaBandMultipliers],
    ) -> None:
        self._call(
            "initializeTenorParams",
            _deltaBandWidth=_deltaBandWidth,
            _numberOfTenors=_numberOfTenors,
            _maxTenorValue=_maxTenorValue,
            _tenorPricingParams=_tenorPricingParams
        )
        
    def issueNewSeries(
        self,
        options: list[Types_Option],
    ) -> None:
        self._call(
            "issueNewSeries",
            options=options
        )
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "keeper",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def optionCatalogue(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "optionCatalogue"
        )
        return Address.from_tuple(my_var_0)
        
    def optionExchange(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "optionExchange"
        )
        return Address.from_tuple(my_var_0)
        
    def optionHandler(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "optionHandler"
        )
        return Address.from_tuple(my_var_0)
        
    def proxyManager(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "proxyManager"
        )
        return Address.from_tuple(my_var_0)
        
    def pullManager(
        self,
    ) -> None:
        self._call(
            "pullManager"
        )
        
    def rebalancePortfolioDelta(
        self,
        delta: int_e18,
        reactorIndex: uint_e18,
    ) -> None:
        self._call(
            "rebalancePortfolioDelta",
            delta=delta,
            reactorIndex=reactorIndex
        )
        
    def redeem(
        self,
        _series: list[Address],
        amountOutMinimums: list[uint_e18],
    ) -> None:
        self._call(
            "redeem",
            _series=_series,
            amountOutMinimums=amountOutMinimums
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setBidAskIVSpread(
        self,
        _bidAskIVSpread: uint_e18,
    ) -> None:
        self._call(
            "setBidAskIVSpread",
            _bidAskIVSpread=_bidAskIVSpread
        )
        
    def setCollateralLendingRate(
        self,
        _collateralLendingRate: uint_e18,
    ) -> None:
        self._call(
            "setCollateralLendingRate",
            _collateralLendingRate=_collateralLendingRate
        )
        
    def setDeltaBorrowRates(
        self,
        _deltaBorrowRates: BeyondPricer_DeltaBorrowRates,
    ) -> None:
        self._call(
            "setDeltaBorrowRates",
            _deltaBorrowRates=_deltaBorrowRates
        )
        
    def setDeltaLimit(
        self,
        _delta: list[uint_e18],
        _keeper: list[Address],
    ) -> None:
        self._call(
            "setDeltaLimit",
            _delta=_delta,
            _keeper=_keeper
        )
        
    def setKeeper(
        self,
        _keeper: Address,
        _auth: bool,
    ) -> None:
        self._call(
            "setKeeper",
            _keeper=_keeper,
            _auth=_auth
        )
        
    def setLowDeltaSellOptionFlatIV(
        self,
        _lowDeltaSellOptionFlatIV: uint_e18,
    ) -> None:
        self._call(
            "setLowDeltaSellOptionFlatIV",
            _lowDeltaSellOptionFlatIV=_lowDeltaSellOptionFlatIV
        )
        
    def setLowDeltaThreshold(
        self,
        _lowDeltaThreshold: uint_e18,
    ) -> None:
        self._call(
            "setLowDeltaThreshold",
            _lowDeltaThreshold=_lowDeltaThreshold
        )
        
    def setNewOptionParams(
        self,
        _newMinCallStrike: uint128,
        _newMaxCallStrike: uint128,
        _newMinPutStrike: uint128,
        _newMaxPutStrike: uint128,
        _newMinExpiry: uint128,
        _newMaxExpiry: uint128,
    ) -> None:
        self._call(
            "setNewOptionParams",
            _newMinCallStrike=_newMinCallStrike,
            _newMaxCallStrike=_newMaxCallStrike,
            _newMinPutStrike=_newMinPutStrike,
            _newMaxPutStrike=_newMaxPutStrike,
            _newMinExpiry=_newMinExpiry,
            _newMaxExpiry=_newMaxExpiry
        )
        
    def setProxyManager(
        self,
        _proxyManager: Address,
    ) -> None:
        self._call(
            "setProxyManager",
            _proxyManager=_proxyManager
        )
        
    def setRiskFreeRate(
        self,
        _riskFreeRate: uint_e18,
    ) -> None:
        self._call(
            "setRiskFreeRate",
            _riskFreeRate=_riskFreeRate
        )
        
    def setSlippageGradient(
        self,
        _slippageGradient: uint_e18,
    ) -> None:
        self._call(
            "setSlippageGradient",
            _slippageGradient=_slippageGradient
        )
        
    def setSlippageGradientMultipliers(
        self,
        _tenorIndex: uint16,
        _callSlippageGradientMultipliers: list[int80],
        _putSlippageGradientMultipliers: list[int80],
    ) -> None:
        self._call(
            "setSlippageGradientMultipliers",
            _tenorIndex=_tenorIndex,
            _callSlippageGradientMultipliers=_callSlippageGradientMultipliers,
            _putSlippageGradientMultipliers=_putSlippageGradientMultipliers
        )
        
    def setSpreadCollateralMultipliers(
        self,
        _tenorIndex: uint16,
        _callSpreadCollateralMultipliers: list[int80],
        _putSpreadCollateralMultipliers: list[int80],
    ) -> None:
        self._call(
            "setSpreadCollateralMultipliers",
            _tenorIndex=_tenorIndex,
            _callSpreadCollateralMultipliers=_callSpreadCollateralMultipliers,
            _putSpreadCollateralMultipliers=_putSpreadCollateralMultipliers
        )
        
    def setSpreadDeltaMultipliers(
        self,
        _tenorIndex: uint16,
        _callSpreadDeltaMultipliers: list[int80],
        _putSpreadDeltaMultipliers: list[int80],
    ) -> None:
        self._call(
            "setSpreadDeltaMultipliers",
            _tenorIndex=_tenorIndex,
            _callSpreadDeltaMultipliers=_callSpreadDeltaMultipliers,
            _putSpreadDeltaMultipliers=_putSpreadDeltaMultipliers
        )
    
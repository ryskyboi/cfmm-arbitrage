
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

@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

@dataclass
class BeyondPricer_DeltaBorrowRates:
    sellLong: int_e18
    sellShort: int_e18
    buyLong: int_e18
    buyShort: int_e18

class manager(BaseAbi):
    address: Address = Address("0xB8Cb70cf67EF7d7dFb1C70bc7A169DFCcCF0753c")
    
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def beyondPricer(
        self,
    ) -> Address:
        return self._call(
            "beyondPricer"
        )
        
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
        return self._call(
            "createOrder",
            _optionSeries=_optionSeries,
            _amount=_amount,
            _price=_price,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _isBuyBack=_isBuyBack,
            _spotMovementRange=_spotMovementRange
        )
        
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
        return self._call(
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
        
    def deltaLimit(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "deltaLimit",
            x_0=x_0
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
        return self._call(
            "keeper",
            x_0=x_0
        )
        
    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )
        
    def optionCatalogue(
        self,
    ) -> Address:
        return self._call(
            "optionCatalogue"
        )
        
    def optionExchange(
        self,
    ) -> Address:
        return self._call(
            "optionExchange"
        )
        
    def optionHandler(
        self,
    ) -> Address:
        return self._call(
            "optionHandler"
        )
        
    def proxyManager(
        self,
    ) -> Address:
        return self._call(
            "proxyManager"
        )
        
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
        
    def setCollateralLendingRate(
        self,
        _collateralLendingRate: uint_e18,
    ) -> None:
        self._call(
            "setCollateralLendingRate",
            _collateralLendingRate=_collateralLendingRate
        )
        
    def setDeltaBandWidth(
        self,
        _deltaBandWidth: uint_e18,
        _callSlippageGradientMultipliers: list[uint_e18],
        _putSlippageGradientMultipliers: list[uint_e18],
    ) -> None:
        self._call(
            "setDeltaBandWidth",
            _deltaBandWidth=_deltaBandWidth,
            _callSlippageGradientMultipliers=_callSlippageGradientMultipliers,
            _putSlippageGradientMultipliers=_putSlippageGradientMultipliers
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
        _callSlippageGradientMultipliers: list[uint_e18],
        _putSlippageGradientMultipliers: list[uint_e18],
    ) -> None:
        self._call(
            "setSlippageGradientMultipliers",
            _callSlippageGradientMultipliers=_callSlippageGradientMultipliers,
            _putSlippageGradientMultipliers=_putSlippageGradientMultipliers
        )
    
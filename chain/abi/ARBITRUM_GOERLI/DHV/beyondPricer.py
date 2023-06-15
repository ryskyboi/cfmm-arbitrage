
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
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

class beyondPricer(BaseAbi):
    address: Address = Address("0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259")
    
    def addressBook(
        self,
    ) -> Address:
        return self._call(
            "addressBook"
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def bidAskIVSpread(
        self,
    ) -> uint_e18:
        return self._call(
            "bidAskIVSpread"
        )
        
    def callSlippageGradientMultipliers(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        return self._call(
            "callSlippageGradientMultipliers",
            x_0=x_0
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def collateralLendingRate(
        self,
    ) -> uint_e18:
        return self._call(
            "collateralLendingRate"
        )
        
    def deltaBandWidth(
        self,
    ) -> uint_e18:
        return self._call(
            "deltaBandWidth"
        )
        
    def deltaBorrowRates(
        self,
    ) -> tuple[int_e18, int_e18, int_e18, int_e18]:
        return self._call(
            "deltaBorrowRates"
        )
        
    def feePerContract(
        self,
    ) -> uint_e18:
        return self._call(
            "feePerContract"
        )
        
    def getCallSlippageGradientMultipliers(
        self,
    ) -> list[uint_e18]:
        return self._call(
            "getCallSlippageGradientMultipliers"
        )
        
    def getPutSlippageGradientMultipliers(
        self,
    ) -> list[uint_e18]:
        return self._call(
            "getPutSlippageGradientMultipliers"
        )
        
    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )
        
    def protocol(
        self,
    ) -> Address:
        return self._call(
            "protocol"
        )
        
    def putSlippageGradientMultipliers(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        return self._call(
            "putSlippageGradientMultipliers",
            x_0=x_0
        )
        
    def quoteOptionPrice(
        self,
        _optionSeries: Types_OptionSeries,
        _amount: uint_e18,
        isSell: bool,
        netDhvExposure: int_e18,
    ) -> tuple[uint_e18, int_e18, uint_e18]:
        return self._call(
            "quoteOptionPrice",
            _optionSeries=_optionSeries,
            _amount=_amount,
            isSell=isSell,
            netDhvExposure=netDhvExposure
        )
        
    def riskFreeRate(
        self,
    ) -> uint_e18:
        return self._call(
            "riskFreeRate"
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
        
    def setFeePerContract(
        self,
        _feePerContract: uint_e18,
    ) -> None:
        self._call(
            "setFeePerContract",
            _feePerContract=_feePerContract
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
        _callSlippageGradientMultipliers: list[uint_e18],
        _putSlippageGradientMultipliers: list[uint_e18],
    ) -> None:
        self._call(
            "setSlippageGradientMultipliers",
            _callSlippageGradientMultipliers=_callSlippageGradientMultipliers,
            _putSlippageGradientMultipliers=_putSlippageGradientMultipliers
        )
        
    def slippageGradient(
        self,
    ) -> uint_e18:
        return self._call(
            "slippageGradient"
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        return self._call(
            "strikeAsset"
        )
        
    def underlyingAsset(
        self,
    ) -> Address:
        return self._call(
            "underlyingAsset"
        )
    
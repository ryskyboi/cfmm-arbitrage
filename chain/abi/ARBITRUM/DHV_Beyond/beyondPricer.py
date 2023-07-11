
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
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



class beyondPricer(BaseAbi):
    address: Address = Address("0xeA5Fb118862876f249Ff0b3e7fb25fEb38158def")
    
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def bidAskIVSpread(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "bidAskIVSpread"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralLendingRate(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "collateralLendingRate"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def deltaBandWidth(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "deltaBandWidth"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def deltaBorrowRates(
        self,
    ) -> tuple[int_e18, int_e18, int_e18, int_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3 = self._call(
            "deltaBorrowRates"
        )
        return int_e18.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), int_e18.from_tuple(my_var_2), int_e18.from_tuple(my_var_3)
        
    def feePerContract(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "feePerContract"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getCallSlippageGradientMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getCallSlippageGradientMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getCallSpreadCollateralMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getCallSpreadCollateralMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getCallSpreadDeltaMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getCallSpreadDeltaMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPutSlippageGradientMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getPutSlippageGradientMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPutSpreadCollateralMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getPutSpreadCollateralMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPutSpreadDeltaMultipliers(
        self,
        _tenorIndex: uint16,
    ) -> list[int80]:
        my_var_0 = self._call(
            "getPutSpreadDeltaMultipliers",
            _tenorIndex=_tenorIndex
        )
        return [int80.from_tuple(arg_0) for arg_0 in my_var_0]
        
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
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def lowDeltaSellOptionFlatIV(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "lowDeltaSellOptionFlatIV"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def lowDeltaThreshold(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "lowDeltaThreshold"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxTenorValue(
        self,
    ) -> uint16:
        my_var_0 = self._call(
            "maxTenorValue"
        )
        return uint16.from_tuple(my_var_0)
        
    def numberOfTenors(
        self,
    ) -> uint16:
        my_var_0 = self._call(
            "numberOfTenors"
        )
        return uint16.from_tuple(my_var_0)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def quoteOptionPrice(
        self,
        _optionSeries: Types_OptionSeries,
        _amount: uint_e18,
        isSell: bool,
        netDhvExposure: int_e18,
    ) -> tuple[uint_e18, int_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "quoteOptionPrice",
            _optionSeries=_optionSeries,
            _amount=_amount,
            isSell=isSell,
            netDhvExposure=netDhvExposure
        )
        return uint_e18.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2)
        
    def riskFreeRate(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "riskFreeRate"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        
    def setFeePerContract(
        self,
        _feePerContract: uint_e18,
    ) -> None:
        self._call(
            "setFeePerContract",
            _feePerContract=_feePerContract
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
        
    def slippageGradient(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "slippageGradient"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
    
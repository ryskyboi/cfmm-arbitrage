
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
    address: Address = Address("0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259")
    
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
        
    def callSlippageGradientMultipliers(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "callSlippageGradientMultipliers",
            x_0=x_0
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
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getCallSlippageGradientMultipliers"
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPutSlippageGradientMultipliers(
        self,
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getPutSlippageGradientMultipliers"
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def putSlippageGradientMultipliers(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "putSlippageGradientMultipliers",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
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
    
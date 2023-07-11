
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class MarginVault_Vault:
    shortOtokens: list[Address]
    longOtokens: list[Address]
    collateralAssets: list[Address]
    shortAmounts: list[uint_e18]
    longAmounts: list[uint_e18]
    collateralAmounts: list[uint_e18]

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            [Address.from_tuple(arg_0) for arg_0 in args[0]],
            [Address.from_tuple(arg_0) for arg_0 in args[1]],
            [Address.from_tuple(arg_0) for arg_0 in args[2]],
            [uint_e18.from_tuple(arg_0) for arg_0 in args[3]],
            [uint_e18.from_tuple(arg_0) for arg_0 in args[4]],
            [uint_e18.from_tuple(arg_0) for arg_0 in args[5]],
        )



@dataclass
class FixedPointInt256_FixedPointInt:
    value: int_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            int_e18.from_tuple(args[0]),
        )



class OpynNewCalculator(BaseAbi):
    address: Address = Address("0x749a3624ad2a001F935E3319743f53Ecc7466358")
    
    def AUCTION_TIME(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "AUCTION_TIME"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def getCollateralDust(
        self,
        _collateral: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getCollateralDust",
            _collateral=_collateral
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getExcessCollateral(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[uint_e18, bool]:
        my_var_0, my_var_1 = self._call(
            "getExcessCollateral",
            _vault=_vault,
            _vaultType=_vaultType
        )
        return uint_e18.from_tuple(my_var_0), bool(my_var_1)
        
    def getExpiredPayoutRate(
        self,
        _otoken: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getExpiredPayoutRate",
            _otoken=_otoken
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getMarginRequired(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[FixedPointInt256_FixedPointInt, FixedPointInt256_FixedPointInt]:
        my_var_0, my_var_1 = self._call(
            "getMarginRequired",
            _vault=_vault,
            _vaultType=_vaultType
        )
        return FixedPointInt256_FixedPointInt.from_tuple(my_var_0), FixedPointInt256_FixedPointInt.from_tuple(my_var_1)
        
    def getMaxPrice(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
        _timeToExpiry: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getMaxPrice",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut,
            _timeToExpiry=_timeToExpiry
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getNakedMarginRequired(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _shortAmount: uint_e18,
        _strikePrice: uint_e18,
        _underlyingPrice: uint_e18,
        _shortExpiryTimestamp: uint_e18,
        _collateralDecimals: uint_e18,
        _isPut: bool,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNakedMarginRequired",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _shortAmount=_shortAmount,
            _strikePrice=_strikePrice,
            _underlyingPrice=_underlyingPrice,
            _shortExpiryTimestamp=_shortExpiryTimestamp,
            _collateralDecimals=_collateralDecimals,
            _isPut=_isPut
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getOracleDeviation(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getOracleDeviation"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getSpotShock(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getSpotShock",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getTimesToExpiry(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getTimesToExpiry",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def isLiquidatable(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[bool, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "isLiquidatable",
            _vault=_vault,
            _vaultType=_vaultType
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2)
        
    def liquidationMultiplier(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "liquidationMultiplier"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def oracle(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "oracle"
        )
        return Address.from_tuple(my_var_0)
        
    def owner(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "owner"
        )
        return Address.from_tuple(my_var_0)
        
    def renounceOwnership(
        self,
    ) -> None:
        self._call(
            "renounceOwnership"
        )
        
    def setCollateralDust(
        self,
        _collateral: Address,
        _dust: uint_e18,
    ) -> None:
        self._call(
            "setCollateralDust",
            _collateral=_collateral,
            _dust=_dust
        )
        
    def setLiquidationMultiplier(
        self,
        _liquidationMultiplier: uint_e18,
    ) -> None:
        self._call(
            "setLiquidationMultiplier",
            _liquidationMultiplier=_liquidationMultiplier
        )
        
    def setOracleDeviation(
        self,
        _deviation: uint_e18,
    ) -> None:
        self._call(
            "setOracleDeviation",
            _deviation=_deviation
        )
        
    def setSpotShock(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
        _shockValue: uint_e18,
    ) -> None:
        self._call(
            "setSpotShock",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut,
            _shockValue=_shockValue
        )
        
    def setUpperBoundValues(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
        _timesToExpiry: list[uint_e18],
        _values: list[uint_e18],
    ) -> None:
        self._call(
            "setUpperBoundValues",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut,
            _timesToExpiry=_timesToExpiry,
            _values=_values
        )
        
    def transferOwnership(
        self,
        newOwner: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            newOwner=newOwner
        )
        
    def updateUpperBoundValue(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
        _timeToExpiry: uint_e18,
        _value: uint_e18,
    ) -> None:
        self._call(
            "updateUpperBoundValue",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut,
            _timeToExpiry=_timeToExpiry,
            _value=_value
        )
    
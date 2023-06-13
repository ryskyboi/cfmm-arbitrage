
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

@dataclass
class FixedPointInt256_FixedPointInt:
    value: int_e18

class OpynNewCalculator(BaseAbi):
    address: Address = Address("0xcD270e755C2653e806e16dD3f78E16C89B7a1c9e")

    def AUCTION_TIME(
        self,
    ) -> uint_e18:
        return self._call(
            "AUCTION_TIME"
        )

    def addressBook(
        self,
    ) -> Address:
        return self._call(
            "addressBook"
        )

    def getCollateralDust(
        self,
        _collateral: Address,
    ) -> uint_e18:
        return self._call(
            "getCollateralDust",
            _collateral=_collateral
        )

    def getExcessCollateral(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[uint_e18, bool]:
        return self._call(
            "getExcessCollateral",
            _vault=_vault,
            _vaultType=_vaultType
        )

    def getExpiredPayoutRate(
        self,
        _otoken: Address,
    ) -> uint_e18:
        return self._call(
            "getExpiredPayoutRate",
            _otoken=_otoken
        )

    def getMarginRequired(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[FixedPointInt256_FixedPointInt, FixedPointInt256_FixedPointInt]:
        return self._call(
            "getMarginRequired",
            _vault=_vault,
            _vaultType=_vaultType
        )

    def getMaxPrice(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
        _timeToExpiry: uint_e18,
    ) -> uint_e18:
        return self._call(
            "getMaxPrice",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut,
            _timeToExpiry=_timeToExpiry
        )

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
        return self._call(
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

    def getOracleDeviation(
        self,
    ) -> uint_e18:
        return self._call(
            "getOracleDeviation"
        )

    def getSpotShock(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> uint_e18:
        return self._call(
            "getSpotShock",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )

    def getTimesToExpiry(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> list[uint_e18]:
        return self._call(
            "getTimesToExpiry",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )

    def isLiquidatable(
        self,
        _vault: MarginVault_Vault,
        _vaultType: uint_e18,
    ) -> tuple[bool, uint_e18, uint_e18]:
        return self._call(
            "isLiquidatable",
            _vault=_vault,
            _vaultType=_vaultType
        )

    def liquidationMultiplier(
        self,
    ) -> uint_e18:
        return self._call(
            "liquidationMultiplier"
        )

    def oracle(
        self,
    ) -> Address:
        return self._call(
            "oracle"
        )

    def owner(
        self,
    ) -> Address:
        return self._call(
            "owner"
        )

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

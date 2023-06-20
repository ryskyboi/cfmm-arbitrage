
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



class OpynOptionRegistry(BaseAbi):
    address: Address = Address("0x4E89cc3215AF050Ceb63Ca62470eeC7C1A66F737")
    
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def adjustCollateral(
        self,
        vaultId: uint_e18,
    ) -> None:
        self._call(
            "adjustCollateral",
            vaultId=vaultId
        )
        
    def adjustCollateralCaller(
        self,
        vaultId: uint_e18,
    ) -> None:
        self._call(
            "adjustCollateralCaller",
            vaultId=vaultId
        )
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def callLowerHealthFactor(
        self,
    ) -> uint64:
        my_var_0 = self._call(
            "callLowerHealthFactor"
        )
        return uint64.from_tuple(my_var_0)
        
    def callUpperHealthFactor(
        self,
    ) -> uint64:
        my_var_0 = self._call(
            "callUpperHealthFactor"
        )
        return uint64.from_tuple(my_var_0)
        
    def checkVaultHealth(
        self,
        vaultId: uint_e18,
    ) -> tuple[bool, bool, uint_e18, uint_e18, uint_e18, Address]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5 = self._call(
            "checkVaultHealth",
            vaultId=vaultId
        )
        return bool(my_var_0), bool(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4), Address.from_tuple(my_var_5)
        
    def close(
        self,
        _series: Address,
        amount: uint_e18,
    ) -> tuple[bool, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "close",
            _series=_series,
            amount=amount
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def getCollateral(
        self,
        series: Types_OptionSeries,
        amount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getCollateral",
            series=series,
            amount=amount
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getIssuanceHash(
        self,
        _series: Types_OptionSeries,
    ) -> bytes32:
        my_var_0 = self._call(
            "getIssuanceHash",
            _series=_series
        )
        return bytes32.from_tuple(my_var_0)
        
    def getOtoken(
        self,
        underlying: Address,
        strikeAsset: Address,
        expiration: uint_e18,
        isPut: bool,
        strike: uint_e18,
        collateral: Address,
    ) -> Address:
        my_var_0 = self._call(
            "getOtoken",
            underlying=underlying,
            strikeAsset=strikeAsset,
            expiration=expiration,
            isPut=isPut,
            strike=strike,
            collateral=collateral
        )
        return Address.from_tuple(my_var_0)
        
    def getSeries(
        self,
        _series: Types_OptionSeries,
    ) -> Address:
        my_var_0 = self._call(
            "getSeries",
            _series=_series
        )
        return Address.from_tuple(my_var_0)
        
    def getSeriesAddress(
        self,
        issuanceHash: bytes32,
    ) -> Address:
        my_var_0 = self._call(
            "getSeriesAddress",
            issuanceHash=issuanceHash
        )
        return Address.from_tuple(my_var_0)
        
    def getSeriesInfo(
        self,
        series: Address,
    ) -> Types_OptionSeries:
        my_var_0 = self._call(
            "getSeriesInfo",
            series=series
        )
        return Types_OptionSeries.from_tuple(my_var_0)
        
    def issue(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        my_var_0 = self._call(
            "issue",
            optionSeries=optionSeries
        )
        return Address.from_tuple(my_var_0)
        
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
        
    def open(
        self,
        _series: Address,
        amount: uint_e18,
        collateralAmount: uint_e18,
    ) -> tuple[bool, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "open",
            _series=_series,
            amount=amount,
            collateralAmount=collateralAmount
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def putLowerHealthFactor(
        self,
    ) -> uint64:
        my_var_0 = self._call(
            "putLowerHealthFactor"
        )
        return uint64.from_tuple(my_var_0)
        
    def putUpperHealthFactor(
        self,
    ) -> uint64:
        my_var_0 = self._call(
            "putUpperHealthFactor"
        )
        return uint64.from_tuple(my_var_0)
        
    def redeem(
        self,
        _series: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "redeem",
            _series=_series
        )
        return uint_e18.from_tuple(my_var_0)
        
    def registerLiquidatedVault(
        self,
        vaultId: uint_e18,
    ) -> None:
        self._call(
            "registerLiquidatedVault",
            vaultId=vaultId
        )
        
    def seriesInfo(
        self,
        x_0: Address,
    ) -> tuple[uint64, uint128, bool, Address, Address, Address]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5 = self._call(
            "seriesInfo",
            x_0=x_0
        )
        return uint64.from_tuple(my_var_0), uint128.from_tuple(my_var_1), bool(my_var_2), Address.from_tuple(my_var_3), Address.from_tuple(my_var_4), Address.from_tuple(my_var_5)
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setHealthThresholds(
        self,
        _putLower: uint64,
        _putUpper: uint64,
        _callLower: uint64,
        _callUpper: uint64,
    ) -> None:
        self._call(
            "setHealthThresholds",
            _putLower=_putLower,
            _putUpper=_putUpper,
            _callLower=_callLower,
            _callUpper=_callUpper
        )
        
    def setKeeper(
        self,
        _target: Address,
        _auth: bool,
    ) -> None:
        self._call(
            "setKeeper",
            _target=_target,
            _auth=_auth
        )
        
    def setLiquidityPool(
        self,
        _newLiquidityPool: Address,
    ) -> None:
        self._call(
            "setLiquidityPool",
            _newLiquidityPool=_newLiquidityPool
        )
        
    def setOperator(
        self,
        _operator: Address,
        _isOperator: bool,
    ) -> None:
        self._call(
            "setOperator",
            _operator=_operator,
            _isOperator=_isOperator
        )
        
    def setSeriesInfoAndAddress(
        self,
        _optionSeries: Types_OptionSeries,
        _seriesAddress: Address,
        _issuanceHash: bytes32,
    ) -> None:
        self._call(
            "setSeriesInfoAndAddress",
            _optionSeries=_optionSeries,
            _seriesAddress=_seriesAddress,
            _issuanceHash=_issuanceHash
        )
        
    def setVaultIds(
        self,
        _seriesAddress: Address,
        _id: uint_e18,
    ) -> None:
        self._call(
            "setVaultIds",
            _seriesAddress=_seriesAddress,
            _id=_id
        )
        
    def settle(
        self,
        _series: Address,
    ) -> tuple[bool, uint_e18, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3 = self._call(
            "settle",
            _series=_series
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3)
        
    def vaultCount(
        self,
    ) -> uint64:
        my_var_0 = self._call(
            "vaultCount"
        )
        return uint64.from_tuple(my_var_0)
        
    def vaultIds(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "vaultIds",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def wCollatLiquidatedVault(
        self,
        vaultId: uint_e18,
    ) -> None:
        self._call(
            "wCollatLiquidatedVault",
            vaultId=vaultId
        )
    
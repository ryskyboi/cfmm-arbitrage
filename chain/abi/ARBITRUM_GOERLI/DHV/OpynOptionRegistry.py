
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

class OpynOptionRegistry(BaseAbi):
    address: Address = Address("0x4E89cc3215AF050Ceb63Ca62470eeC7C1A66F737")
    
    def addressBook(
        self,
    ) -> Address:
        return self._call(
            "addressBook"
        )
        
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
        return self._call(
            "authority"
        )
        
    def callLowerHealthFactor(
        self,
    ) -> uint64:
        return self._call(
            "callLowerHealthFactor"
        )
        
    def callUpperHealthFactor(
        self,
    ) -> uint64:
        return self._call(
            "callUpperHealthFactor"
        )
        
    def checkVaultHealth(
        self,
        vaultId: uint_e18,
    ) -> tuple[bool, bool, uint_e18, uint_e18, uint_e18, Address]:
        return self._call(
            "checkVaultHealth",
            vaultId=vaultId
        )
        
    def close(
        self,
        _series: Address,
        amount: uint_e18,
    ) -> tuple[bool, uint_e18]:
        return self._call(
            "close",
            _series=_series,
            amount=amount
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def getCollateral(
        self,
        series: Types_OptionSeries,
        amount: uint_e18,
    ) -> uint_e18:
        return self._call(
            "getCollateral",
            series=series,
            amount=amount
        )
        
    def getIssuanceHash(
        self,
        _series: Types_OptionSeries,
    ) -> bytes32:
        return self._call(
            "getIssuanceHash",
            _series=_series
        )
        
    def getOtoken(
        self,
        underlying: Address,
        strikeAsset: Address,
        expiration: uint_e18,
        isPut: bool,
        strike: uint_e18,
        collateral: Address,
    ) -> Address:
        return self._call(
            "getOtoken",
            underlying=underlying,
            strikeAsset=strikeAsset,
            expiration=expiration,
            isPut=isPut,
            strike=strike,
            collateral=collateral
        )
        
    def getSeries(
        self,
        _series: Types_OptionSeries,
    ) -> Address:
        return self._call(
            "getSeries",
            _series=_series
        )
        
    def getSeriesAddress(
        self,
        issuanceHash: bytes32,
    ) -> Address:
        return self._call(
            "getSeriesAddress",
            issuanceHash=issuanceHash
        )
        
    def getSeriesInfo(
        self,
        series: Address,
    ) -> Types_OptionSeries:
        return self._call(
            "getSeriesInfo",
            series=series
        )
        
    def issue(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        return self._call(
            "issue",
            optionSeries=optionSeries
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
        
    def open(
        self,
        _series: Address,
        amount: uint_e18,
        collateralAmount: uint_e18,
    ) -> tuple[bool, uint_e18]:
        return self._call(
            "open",
            _series=_series,
            amount=amount,
            collateralAmount=collateralAmount
        )
        
    def putLowerHealthFactor(
        self,
    ) -> uint64:
        return self._call(
            "putLowerHealthFactor"
        )
        
    def putUpperHealthFactor(
        self,
    ) -> uint64:
        return self._call(
            "putUpperHealthFactor"
        )
        
    def redeem(
        self,
        _series: Address,
    ) -> uint_e18:
        return self._call(
            "redeem",
            _series=_series
        )
        
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
        return self._call(
            "seriesInfo",
            x_0=x_0
        )
        
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
        return self._call(
            "settle",
            _series=_series
        )
        
    def vaultCount(
        self,
    ) -> uint64:
        return self._call(
            "vaultCount"
        )
        
    def vaultIds(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "vaultIds",
            x_0=x_0
        )
        
    def wCollatLiquidatedVault(
        self,
        vaultId: uint_e18,
    ) -> None:
        self._call(
            "wCollatLiquidatedVault",
            vaultId=vaultId
        )
    
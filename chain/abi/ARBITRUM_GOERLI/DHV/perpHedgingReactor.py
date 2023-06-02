
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class perpHedgingReactor(BaseAbi):
    address: Address = Address("0x361B6Fb536588E87F0CEE1eb9Ac5a26Ef7108d9B")
    
    def accountId(
        self,
    ) -> uint_e18:
        return self._call(
            "accountId"
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def checkVaultHealth(
        self,
    ) -> tuple[bool, bool, uint_e18, uint_e18]:
        return self._call(
            "checkVaultHealth"
        )
        
    def clearingHouse(
        self,
    ) -> Address:
        return self._call(
            "clearingHouse"
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def collateralId(
        self,
    ) -> uint32:
        return self._call(
            "collateralId"
        )
        
    def getDelta(
        self,
    ) -> int_e18:
        return self._call(
            "getDelta"
        )
        
    def getPoolDenominatedValue(
        self,
    ) -> uint_e18:
        return self._call(
            "getPoolDenominatedValue"
        )
        
    def healthFactor(
        self,
    ) -> uint_e18:
        return self._call(
            "healthFactor"
        )
        
    def hedgeDelta(
        self,
        _delta: int_e18,
    ) -> int_e18:
        return self._call(
            "hedgeDelta",
            _delta=_delta
        )
        
    def initialiseReactor(
        self,
    ) -> None:
        self._call(
            "initialiseReactor"
        )
        
    def internalDelta(
        self,
    ) -> int_e18:
        return self._call(
            "internalDelta"
        )
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "keeper",
            x_0=x_0
        )
        
    def parentLiquidityPool(
        self,
    ) -> Address:
        return self._call(
            "parentLiquidityPool"
        )
        
    def poolId(
        self,
    ) -> uint32:
        return self._call(
            "poolId"
        )
        
    def priceFeed(
        self,
    ) -> Address:
        return self._call(
            "priceFeed"
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setHealthFactor(
        self,
        _healthFactor: uint_e18,
    ) -> None:
        self._call(
            "setHealthFactor",
            _healthFactor=_healthFactor
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
        
    def setSyncOnChange(
        self,
        _syncOnChange: bool,
    ) -> None:
        self._call(
            "setSyncOnChange",
            _syncOnChange=_syncOnChange
        )
        
    def sync(
        self,
    ) -> None:
        self._call(
            "sync"
        )
        
    def syncAndUpdate(
        self,
    ) -> None:
        self._call(
            "syncAndUpdate"
        )
        
    def syncOnChange(
        self,
    ) -> bool:
        return self._call(
            "syncOnChange"
        )
        
    def update(
        self,
    ) -> uint_e18:
        return self._call(
            "update"
        )
        
    def wETH(
        self,
    ) -> Address:
        return self._call(
            "wETH"
        )
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        return self._call(
            "withdraw",
            _amount=_amount
        )
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class perpHedgingReactor(BaseAbi):
    address: Address = Address("0xf013767D55954EcCCacb4914d52D2ef8f95d82C5")
    
    def LPcollateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "LPcollateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def accountId(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "accountId"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def checkVaultHealth(
        self,
    ) -> tuple[bool, bool, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3 = self._call(
            "checkVaultHealth"
        )
        return bool(my_var_0), bool(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3)
        
    def clearingHouse(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "clearingHouse"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralId(
        self,
    ) -> uint32:
        my_var_0 = self._call(
            "collateralId"
        )
        return uint32.from_tuple(my_var_0)
        
    def getDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "getDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def getPoolDenominatedValue(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPoolDenominatedValue"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def healthFactor(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "healthFactor"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def hedgeDelta(
        self,
        _delta: int_e18,
    ) -> int_e18:
        my_var_0 = self._call(
            "hedgeDelta",
            _delta=_delta
        )
        return int_e18.from_tuple(my_var_0)
        
    def initialiseReactor(
        self,
    ) -> None:
        self._call(
            "initialiseReactor"
        )
        
    def internalDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "internalDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "keeper",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def parentLiquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "parentLiquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def poolId(
        self,
    ) -> uint32:
        my_var_0 = self._call(
            "poolId"
        )
        return uint32.from_tuple(my_var_0)
        
    def priceFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeed"
        )
        return Address.from_tuple(my_var_0)
        
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
        
    def swapRouter(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "swapRouter"
        )
        return Address.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "syncOnChange"
        )
        return bool(my_var_0)
        
    def update(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "update"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def wETH(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "wETH"
        )
        return Address.from_tuple(my_var_0)
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdraw",
            _amount=_amount
        )
        return uint_e18.from_tuple(my_var_0)
    
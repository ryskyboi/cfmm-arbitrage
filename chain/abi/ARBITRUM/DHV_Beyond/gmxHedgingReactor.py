
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class gmxHedgingReactor(BaseAbi):
    address: Address = Address("0xbCd871faAf2c36D57B0F4C006c6B0Cc2E1929736")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def bridgedCollateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "bridgedCollateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def checkVaultHealth(
        self,
    ) -> tuple[bool, bool, int_e18, uint_e18, list[uint_e18], bool]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5 = self._call(
            "checkVaultHealth"
        )
        return bool(my_var_0), bool(my_var_1), int_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), [uint_e18.from_tuple(arg_0) for arg_0 in my_var_4], bool(my_var_5)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralRemovalPercentage(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "collateralRemovalPercentage"
        )
        return int_e18.from_tuple(my_var_0)
        
    def collateralSwapPriceTolerance(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "collateralSwapPriceTolerance"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def decreaseOrderDeltaChange(
        self,
        x_0: bytes32,
    ) -> int_e18:
        my_var_0 = self._call(
            "decreaseOrderDeltaChange",
            x_0=x_0
        )
        return int_e18.from_tuple(my_var_0)
        
    def executeDecreasePosition(
        self,
        positionKey: bytes32,
    ) -> None:
        self._call(
            "executeDecreasePosition",
            positionKey=positionKey
        )
        
    def executeIncreasePosition(
        self,
        positionKey: bytes32,
    ) -> None:
        self._call(
            "executeIncreasePosition",
            positionKey=positionKey
        )
        
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
        
    def gmxPositionCallback(
        self,
        positionKey: bytes32,
        isExecuted: bool,
        isIncrease: bool,
    ) -> None:
        self._call(
            "gmxPositionCallback",
            positionKey=positionKey,
            isExecuted=isExecuted,
            isIncrease=isIncrease
        )
        
    def gmxPositionRouter(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "gmxPositionRouter"
        )
        return Address.from_tuple(my_var_0)
        
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
        
    def increaseOrderDeltaChange(
        self,
        x_0: bytes32,
    ) -> int_e18:
        my_var_0 = self._call(
            "increaseOrderDeltaChange",
            x_0=x_0
        )
        return int_e18.from_tuple(my_var_0)
        
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
        
    def longAndShortOpen(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "longAndShortOpen"
        )
        return bool(my_var_0)
        
    def openLongDelta(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "openLongDelta"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def openShortDelta(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "openShortDelta"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def parentLiquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "parentLiquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def pendingDecreaseCallback(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "pendingDecreaseCallback"
        )
        return uint8.from_tuple(my_var_0)
        
    def pendingDecreaseOrders(
        self,
        x_0: bytes32,
    ) -> bool:
        my_var_0 = self._call(
            "pendingDecreaseOrders",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def pendingIncreaseCallback(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "pendingIncreaseCallback"
        )
        return uint8.from_tuple(my_var_0)
        
    def pendingIncreaseCollateralValue(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "pendingIncreaseCollateralValue"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def pendingIncreaseOrders(
        self,
        x_0: bytes32,
    ) -> bool:
        my_var_0 = self._call(
            "pendingIncreaseOrders",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def positionPriceTolerance(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "positionPriceTolerance"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def priceFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeed"
        )
        return Address.from_tuple(my_var_0)
        
    def reader(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "reader"
        )
        return Address.from_tuple(my_var_0)
        
    def resetPendingPositionCallbacks(
        self,
    ) -> None:
        self._call(
            "resetPendingPositionCallbacks"
        )
        
    def router(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "router"
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
        
    def setCollateralRemovalPercentage(
        self,
        _collateralRemovalPercentage: int_e18,
    ) -> None:
        self._call(
            "setCollateralRemovalPercentage",
            _collateralRemovalPercentage=_collateralRemovalPercentage
        )
        
    def setCollateralSwapPriceTolerance(
        self,
        _collateralSwapPriceTolerance: uint_e18,
    ) -> None:
        self._call(
            "setCollateralSwapPriceTolerance",
            _collateralSwapPriceTolerance=_collateralSwapPriceTolerance
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
        
    def setPositionPriceTolerance(
        self,
        _positionPriceTolerance: uint_e18,
    ) -> None:
        self._call(
            "setPositionPriceTolerance",
            _positionPriceTolerance=_positionPriceTolerance
        )
        
    def setPositionRouter(
        self,
        _gmxPositionRouter: Address,
    ) -> None:
        self._call(
            "setPositionRouter",
            _gmxPositionRouter=_gmxPositionRouter
        )
        
    def setPriceFeed(
        self,
        _priceFeed: Address,
    ) -> None:
        self._call(
            "setPriceFeed",
            _priceFeed=_priceFeed
        )
        
    def setReader(
        self,
        _reader: Address,
    ) -> None:
        self._call(
            "setReader",
            _reader=_reader
        )
        
    def setRouter(
        self,
        _router: Address,
    ) -> None:
        self._call(
            "setRouter",
            _router=_router
        )
        
    def swapRouter(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "swapRouter"
        )
        return Address.from_tuple(my_var_0)
        
    def sweepFunds(
        self,
        _amount: uint_e18,
        _receiver: Address,
    ) -> None:
        self._call(
            "sweepFunds",
            _amount=_amount,
            _receiver=_receiver
        )
        
    def sync(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "sync"
        )
        return int_e18.from_tuple(my_var_0)
        
    def update(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "update"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def vault(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "vault"
        )
        return Address.from_tuple(my_var_0)
        
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
    
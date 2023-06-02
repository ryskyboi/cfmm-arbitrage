
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class OpynAddressBook(BaseAbi):
    address: Address = Address("0xd6e67bF0b1Cdb34C37f31A2652812CB30746a94A")
    
    def getAddress(
        self,
        _key: bytes32,
    ) -> Address:
        return self._call(
            "getAddress",
            _key=_key
        )
        
    def getController(
        self,
    ) -> Address:
        return self._call(
            "getController"
        )
        
    def getLiquidationManager(
        self,
    ) -> Address:
        return self._call(
            "getLiquidationManager"
        )
        
    def getMarginCalculator(
        self,
    ) -> Address:
        return self._call(
            "getMarginCalculator"
        )
        
    def getMarginPool(
        self,
    ) -> Address:
        return self._call(
            "getMarginPool"
        )
        
    def getOracle(
        self,
    ) -> Address:
        return self._call(
            "getOracle"
        )
        
    def getOtokenFactory(
        self,
    ) -> Address:
        return self._call(
            "getOtokenFactory"
        )
        
    def getOtokenImpl(
        self,
    ) -> Address:
        return self._call(
            "getOtokenImpl"
        )
        
    def getWhitelist(
        self,
    ) -> Address:
        return self._call(
            "getWhitelist"
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
        
    def setAddress(
        self,
        _key: bytes32,
        _address: Address,
    ) -> None:
        self._call(
            "setAddress",
            _key=_key,
            _address=_address
        )
        
    def setController(
        self,
        _controller: Address,
    ) -> None:
        self._call(
            "setController",
            _controller=_controller
        )
        
    def setLiquidationManager(
        self,
        _liquidationManager: Address,
    ) -> None:
        self._call(
            "setLiquidationManager",
            _liquidationManager=_liquidationManager
        )
        
    def setMarginCalculator(
        self,
        _marginCalculator: Address,
    ) -> None:
        self._call(
            "setMarginCalculator",
            _marginCalculator=_marginCalculator
        )
        
    def setMarginPool(
        self,
        _marginPool: Address,
    ) -> None:
        self._call(
            "setMarginPool",
            _marginPool=_marginPool
        )
        
    def setOracle(
        self,
        _oracle: Address,
    ) -> None:
        self._call(
            "setOracle",
            _oracle=_oracle
        )
        
    def setOtokenFactory(
        self,
        _otokenFactory: Address,
    ) -> None:
        self._call(
            "setOtokenFactory",
            _otokenFactory=_otokenFactory
        )
        
    def setOtokenImpl(
        self,
        _otokenImpl: Address,
    ) -> None:
        self._call(
            "setOtokenImpl",
            _otokenImpl=_otokenImpl
        )
        
    def setWhitelist(
        self,
        _whitelist: Address,
    ) -> None:
        self._call(
            "setWhitelist",
            _whitelist=_whitelist
        )
        
    def transferOwnership(
        self,
        newOwner: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            newOwner=newOwner
        )
        
    def updateImpl(
        self,
        _id: bytes32,
        _newAddress: Address,
    ) -> None:
        self._call(
            "updateImpl",
            _id=_id,
            _newAddress=_newAddress
        )
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class OpynAddressBook(BaseAbi):
    address: Address = Address("0xCa19F26c52b11186B4b1e76a662a14DA5149EA5a")
    
    def getAddress(
        self,
        _key: bytes32,
    ) -> Address:
        my_var_0 = self._call(
            "getAddress",
            _key=_key
        )
        return Address.from_tuple(my_var_0)
        
    def getController(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getController"
        )
        return Address.from_tuple(my_var_0)
        
    def getLiquidationManager(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getLiquidationManager"
        )
        return Address.from_tuple(my_var_0)
        
    def getMarginCalculator(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getMarginCalculator"
        )
        return Address.from_tuple(my_var_0)
        
    def getMarginPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getMarginPool"
        )
        return Address.from_tuple(my_var_0)
        
    def getOracle(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getOracle"
        )
        return Address.from_tuple(my_var_0)
        
    def getOtokenFactory(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getOtokenFactory"
        )
        return Address.from_tuple(my_var_0)
        
    def getOtokenImpl(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getOtokenImpl"
        )
        return Address.from_tuple(my_var_0)
        
    def getWhitelist(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getWhitelist"
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
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class OpynController(BaseAbi):
    address: Address = Address("0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2")
    
    def implementation(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "implementation"
        )
        return Address.from_tuple(my_var_0)
        
    def proxyOwner(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "proxyOwner"
        )
        return Address.from_tuple(my_var_0)
        
    def transferProxyOwnership(
        self,
        _newOwner: Address,
    ) -> None:
        self._call(
            "transferProxyOwnership",
            _newOwner=_newOwner
        )
        
    def upgradeTo(
        self,
        _implementation: Address,
    ) -> None:
        self._call(
            "upgradeTo",
            _implementation=_implementation
        )
        
    def upgradeToAndCall(
        self,
        _implementation: Address,
        _data: BaseBytes,
    ) -> None:
        self._call(
            "upgradeToAndCall",
            _implementation=_implementation,
            _data=_data
        )
    
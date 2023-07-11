
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class clearinghouse(BaseAbi):
    address: Address = Address("0x4521916972a76d5bfa65fb539cf7a0c2592050ac")
    
    def admin(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "admin"
        )
        return Address.from_tuple(my_var_0)
        
    def changeAdmin(
        self,
        newAdmin: Address,
    ) -> None:
        self._call(
            "changeAdmin",
            newAdmin=newAdmin
        )
        
    def implementation(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "implementation"
        )
        return Address.from_tuple(my_var_0)
        
    def upgradeTo(
        self,
        newImplementation: Address,
    ) -> None:
        self._call(
            "upgradeTo",
            newImplementation=newImplementation
        )
        
    def upgradeToAndCall(
        self,
        newImplementation: Address,
        data: BaseBytes,
    ) -> None:
        self._call(
            "upgradeToAndCall",
            newImplementation=newImplementation,
            data=data
        )
    
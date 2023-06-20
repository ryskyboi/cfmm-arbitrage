
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class authority(BaseAbi):
    address: Address = Address("0x68256a51a6777129968b88bd21b6f657eCE8B0E6")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def governor(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "governor"
        )
        return Address.from_tuple(my_var_0)
        
    def guardian(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "guardian",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def manager(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "manager"
        )
        return Address.from_tuple(my_var_0)
        
    def newGovernor(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "newGovernor"
        )
        return Address.from_tuple(my_var_0)
        
    def newManager(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "newManager"
        )
        return Address.from_tuple(my_var_0)
        
    def pullGovernor(
        self,
    ) -> None:
        self._call(
            "pullGovernor"
        )
        
    def pullManager(
        self,
    ) -> None:
        self._call(
            "pullManager"
        )
        
    def pushGovernor(
        self,
        _newGovernor: Address,
    ) -> None:
        self._call(
            "pushGovernor",
            _newGovernor=_newGovernor
        )
        
    def pushGuardian(
        self,
        _newGuardian: Address,
    ) -> None:
        self._call(
            "pushGuardian",
            _newGuardian=_newGuardian
        )
        
    def pushManager(
        self,
        _newManager: Address,
    ) -> None:
        self._call(
            "pushManager",
            _newManager=_newManager
        )
        
    def revokeGuardian(
        self,
        _guardian: Address,
    ) -> None:
        self._call(
            "revokeGuardian",
            _guardian=_guardian
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
    
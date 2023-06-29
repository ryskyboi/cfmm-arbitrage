
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class UserPositionLensMK1_VaultDrill:
    vaultId: uint_e18
    otoken: Address

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint_e18.from_tuple(args[0]),
            Address.from_tuple(args[1]),
        )



class UserPositionlens(BaseAbi):
    address: Address = Address("0x02eFd4e61C1883A0FfF1044ACd61c9100859336c")
    
    def addressbook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressbook"
        )
        return Address.from_tuple(my_var_0)
        
    def getVaultsForUser(
        self,
        user: Address,
    ) -> list[UserPositionLensMK1_VaultDrill]:
        my_var_0 = self._call(
            "getVaultsForUser",
            user=user
        )
        return [UserPositionLensMK1_VaultDrill.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getVaultsForUserAndOtoken(
        self,
        user: Address,
        otoken: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getVaultsForUserAndOtoken",
            user=user,
            otoken=otoken
        )
        return uint_e18.from_tuple(my_var_0)
    
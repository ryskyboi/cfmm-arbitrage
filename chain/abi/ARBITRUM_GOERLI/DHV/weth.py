
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class weth(BaseAbi):
    address: Address = Address("0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3")
    
    def DOMAIN_SEPARATOR(
        self,
    ) -> bytes32:
        my_var_0 = self._call(
            "DOMAIN_SEPARATOR"
        )
        return bytes32.from_tuple(my_var_0)
        
    def allowance(
        self,
        x_0: Address,
        x_1: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "allowance",
            x_0=x_0,
            x_1=x_1
        )
        return uint_e18.from_tuple(my_var_0)
        
    def approve(
        self,
        spender: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "approve",
            spender=spender,
            amount=amount
        )
        return bool(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def balanceOf(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "balanceOf",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def decimals(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "decimals"
        )
        return uint8.from_tuple(my_var_0)
        
    def mint(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "mint",
            to_=to_,
            amount=amount
        )
        return bool(my_var_0)
        
    def name(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "name"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def nonces(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "nonces",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def permit(
        self,
        owner: Address,
        spender: Address,
        value: uint_e18,
        deadline: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "permit",
            owner=owner,
            spender=spender,
            value=value,
            deadline=deadline,
            v=v,
            r=r,
            s=s
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def symbol(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "symbol"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def totalSupply(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "totalSupply"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def transfer(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transfer",
            to_=to_,
            amount=amount
        )
        return bool(my_var_0)
        
    def transferFrom(
        self,
        from_: Address,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transferFrom",
            from_=from_,
            to_=to_,
            amount=amount
        )
        return bool(my_var_0)
    
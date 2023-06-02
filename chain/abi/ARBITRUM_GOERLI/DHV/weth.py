
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class weth(BaseAbi):
    address: Address = Address("0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3")
    
    def DOMAIN_SEPARATOR(
        self,
    ) -> bytes32:
        return self._call(
            "DOMAIN_SEPARATOR"
        )
        
    def allowance(
        self,
        x_0: Address,
        x_1: Address,
    ) -> uint_e18:
        return self._call(
            "allowance",
            x_0=x_0,
            x_1=x_1
        )
        
    def approve(
        self,
        spender: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "approve",
            spender=spender,
            amount=amount
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def balanceOf(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "balanceOf",
            x_0=x_0
        )
        
    def decimals(
        self,
    ) -> uint8:
        return self._call(
            "decimals"
        )
        
    def mint(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "mint",
            to_=to_,
            amount=amount
        )
        
    def name(
        self,
    ) -> str:
        return self._call(
            "name"
        )
        
    def nonces(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "nonces",
            x_0=x_0
        )
        
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
    ) -> str:
        return self._call(
            "symbol"
        )
        
    def totalSupply(
        self,
    ) -> uint_e18:
        return self._call(
            "totalSupply"
        )
        
    def transfer(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "transfer",
            to_=to_,
            amount=amount
        )
        
    def transferFrom(
        self,
        from_: Address,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "transferFrom",
            from_=from_,
            to_=to_,
            amount=amount
        )
    
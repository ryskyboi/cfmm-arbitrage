
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class otoken(BaseAbi):
    address: Address = Address("0x1d96E828e0Aa743783919B24ccDB971504a96C77")
    
    def DOMAIN_SEPARATOR(
        self,
    ) -> bytes32:
        my_var_0 = self._call(
            "DOMAIN_SEPARATOR"
        )
        return bytes32.from_tuple(my_var_0)
        
    def allowance(
        self,
        owner: Address,
        spender: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "allowance",
            owner=owner,
            spender=spender
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
        
    def balanceOf(
        self,
        account: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "balanceOf",
            account=account
        )
        return uint_e18.from_tuple(my_var_0)
        
    def burnOtoken(
        self,
        account: Address,
        amount: uint_e18,
    ) -> None:
        self._call(
            "burnOtoken",
            account=account,
            amount=amount
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def controller(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "controller"
        )
        return Address.from_tuple(my_var_0)
        
    def decimals(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "decimals"
        )
        return uint8.from_tuple(my_var_0)
        
    def decreaseAllowance(
        self,
        spender: Address,
        subtractedValue: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "decreaseAllowance",
            spender=spender,
            subtractedValue=subtractedValue
        )
        return bool(my_var_0)
        
    def expiryTimestamp(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "expiryTimestamp"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getOtokenDetails(
        self,
    ) -> tuple[Address, Address, Address, uint_e18, uint_e18, bool]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5 = self._call(
            "getOtokenDetails"
        )
        return Address.from_tuple(my_var_0), Address.from_tuple(my_var_1), Address.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4), bool(my_var_5)
        
    def increaseAllowance(
        self,
        spender: Address,
        addedValue: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "increaseAllowance",
            spender=spender,
            addedValue=addedValue
        )
        return bool(my_var_0)
        
    def init(
        self,
        _addressBook: Address,
        _underlyingAsset: Address,
        _strikeAsset: Address,
        _collateralAsset: Address,
        _strikePrice: uint_e18,
        _expiryTimestamp: uint_e18,
        _isPut: bool,
    ) -> None:
        self._call(
            "init",
            _addressBook=_addressBook,
            _underlyingAsset=_underlyingAsset,
            _strikeAsset=_strikeAsset,
            _collateralAsset=_collateralAsset,
            _strikePrice=_strikePrice,
            _expiryTimestamp=_expiryTimestamp,
            _isPut=_isPut
        )
        
    def isPut(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isPut"
        )
        return bool(my_var_0)
        
    def mintOtoken(
        self,
        account: Address,
        amount: uint_e18,
    ) -> None:
        self._call(
            "mintOtoken",
            account=account,
            amount=amount
        )
        
    def name(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "name"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def nonces(
        self,
        owner: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "nonces",
            owner=owner
        )
        return uint_e18.from_tuple(my_var_0)
        
    def permit(
        self,
        owner: Address,
        spender: Address,
        amount: uint_e18,
        deadline: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "permit",
            owner=owner,
            spender=spender,
            amount=amount,
            deadline=deadline,
            v=v,
            r=r,
            s=s
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def strikePrice(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "strikePrice"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        recipient: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transfer",
            recipient=recipient,
            amount=amount
        )
        return bool(my_var_0)
        
    def transferFrom(
        self,
        sender: Address,
        recipient: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transferFrom",
            sender=sender,
            recipient=recipient,
            amount=amount
        )
        return bool(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
    
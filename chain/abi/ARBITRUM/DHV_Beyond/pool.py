
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class pool(BaseAbi):
    address: Address = Address("0xb9F33349db1d0711d95c1198AcbA9511B8269626")
    
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def batchTransferToPool(
        self,
        _asset: list[Address],
        _user: list[Address],
        _amount: list[uint_e18],
    ) -> None:
        self._call(
            "batchTransferToPool",
            _asset=_asset,
            _user=_user,
            _amount=_amount
        )
        
    def batchTransferToUser(
        self,
        _asset: list[Address],
        _user: list[Address],
        _amount: list[uint_e18],
    ) -> None:
        self._call(
            "batchTransferToUser",
            _asset=_asset,
            _user=_user,
            _amount=_amount
        )
        
    def farm(
        self,
        _asset: Address,
        _receiver: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "farm",
            _asset=_asset,
            _receiver=_receiver,
            _amount=_amount
        )
        
    def farmer(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "farmer"
        )
        return Address.from_tuple(my_var_0)
        
    def getStoredBalance(
        self,
        _asset: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getStoredBalance",
            _asset=_asset
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        
    def setFarmer(
        self,
        _farmer: Address,
    ) -> None:
        self._call(
            "setFarmer",
            _farmer=_farmer
        )
        
    def transferOwnership(
        self,
        newOwner: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            newOwner=newOwner
        )
        
    def transferToPool(
        self,
        _asset: Address,
        _user: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "transferToPool",
            _asset=_asset,
            _user=_user,
            _amount=_amount
        )
        
    def transferToUser(
        self,
        _asset: Address,
        _user: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "transferToUser",
            _asset=_asset,
            _user=_user,
            _amount=_amount
        )
    
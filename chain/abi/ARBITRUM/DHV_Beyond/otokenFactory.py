
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class otokenFactory(BaseAbi):
    address: Address = Address("0xBa1952eCdbA02de66fCf73f29068e8cf072644ec")
    
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def createOtoken(
        self,
        _underlyingAsset: Address,
        _strikeAsset: Address,
        _collateralAsset: Address,
        _strikePrice: uint_e18,
        _expiry: uint_e18,
        _isPut: bool,
    ) -> Address:
        my_var_0 = self._call(
            "createOtoken",
            _underlyingAsset=_underlyingAsset,
            _strikeAsset=_strikeAsset,
            _collateralAsset=_collateralAsset,
            _strikePrice=_strikePrice,
            _expiry=_expiry,
            _isPut=_isPut
        )
        return Address.from_tuple(my_var_0)
        
    def getOtoken(
        self,
        _underlyingAsset: Address,
        _strikeAsset: Address,
        _collateralAsset: Address,
        _strikePrice: uint_e18,
        _expiry: uint_e18,
        _isPut: bool,
    ) -> Address:
        my_var_0 = self._call(
            "getOtoken",
            _underlyingAsset=_underlyingAsset,
            _strikeAsset=_strikeAsset,
            _collateralAsset=_collateralAsset,
            _strikePrice=_strikePrice,
            _expiry=_expiry,
            _isPut=_isPut
        )
        return Address.from_tuple(my_var_0)
        
    def getOtokensLength(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getOtokensLength"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getTargetOtokenAddress(
        self,
        _underlyingAsset: Address,
        _strikeAsset: Address,
        _collateralAsset: Address,
        _strikePrice: uint_e18,
        _expiry: uint_e18,
        _isPut: bool,
    ) -> Address:
        my_var_0 = self._call(
            "getTargetOtokenAddress",
            _underlyingAsset=_underlyingAsset,
            _strikeAsset=_strikeAsset,
            _collateralAsset=_collateralAsset,
            _strikePrice=_strikePrice,
            _expiry=_expiry,
            _isPut=_isPut
        )
        return Address.from_tuple(my_var_0)
        
    def otokens(
        self,
        x_0: uint_e18,
    ) -> Address:
        my_var_0 = self._call(
            "otokens",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0)
    
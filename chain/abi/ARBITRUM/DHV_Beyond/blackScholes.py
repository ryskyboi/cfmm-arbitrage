
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class blackScholes(BaseAbi):
    address: Address = Address("0x85C100Eb32C3e2F6EA0444E553f3A9bCE468cb8C")
    
    def blackScholesCalc(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> uint_e18:
        my_var_0 = self._call(
            "blackScholesCalc",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        return uint_e18.from_tuple(my_var_0)
        
    def blackScholesCalcGreeks(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> tuple[uint_e18, int_e18]:
        my_var_0, my_var_1 = self._call(
            "blackScholesCalcGreeks",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        return uint_e18.from_tuple(my_var_0), int_e18.from_tuple(my_var_1)
        
    def callOptionPrice(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "callOptionPrice",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        return uint_e18.from_tuple(my_var_0)
        
    def callOptionPriceGreeks(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> tuple[uint_e18, int_e18]:
        my_var_0, my_var_1 = self._call(
            "callOptionPriceGreeks",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        return uint_e18.from_tuple(my_var_0), int_e18.from_tuple(my_var_1)
        
    def getDelta(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> int_e18:
        my_var_0 = self._call(
            "getDelta",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        return int_e18.from_tuple(my_var_0)
        
    def putOptionPrice(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "putOptionPrice",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        return uint_e18.from_tuple(my_var_0)
        
    def putOptionPriceGreeks(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> tuple[uint_e18, int_e18]:
        my_var_0, my_var_1 = self._call(
            "putOptionPriceGreeks",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        return uint_e18.from_tuple(my_var_0), int_e18.from_tuple(my_var_1)
    
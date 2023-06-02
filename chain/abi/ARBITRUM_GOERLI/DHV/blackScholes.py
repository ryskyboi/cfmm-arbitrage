
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class blackScholes(BaseAbi):
    address: Address = Address("0x0D7776e816E774D5d8Ce0af78F6C51582846a66c")
    
    def blackScholesCalc(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> uint_e18:
        return self._call(
            "blackScholesCalc",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        
    def blackScholesCalcGreeks(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> tuple[uint_e18, int_e18]:
        return self._call(
            "blackScholesCalcGreeks",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        
    def callOptionPrice(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> uint_e18:
        return self._call(
            "callOptionPrice",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        
    def callOptionPriceGreeks(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> tuple[uint_e18, int_e18]:
        return self._call(
            "callOptionPriceGreeks",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        
    def getDelta(
        self,
        price: uint_e18,
        strike: uint_e18,
        expiration: uint_e18,
        vol: uint_e18,
        rfr: uint_e18,
        isPut: bool,
    ) -> int_e18:
        return self._call(
            "getDelta",
            price=price,
            strike=strike,
            expiration=expiration,
            vol=vol,
            rfr=rfr,
            isPut=isPut
        )
        
    def putOptionPrice(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> uint_e18:
        return self._call(
            "putOptionPrice",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
        
    def putOptionPriceGreeks(
        self,
        d1: int_e18,
        d1Denominator: int_e18,
        price: int_e18,
        strike: int_e18,
        eToNegRT: int_e18,
    ) -> tuple[uint_e18, int_e18]:
        return self._call(
            "putOptionPriceGreeks",
            d1=d1,
            d1Denominator=d1Denominator,
            price=price,
            strike=strike,
            eToNegRT=eToNegRT
        )
    
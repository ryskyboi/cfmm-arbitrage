
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class DHVLensMK1_TradingSpec:
    iv: uint_e18
    quote: uint_e18
    fee: uint_e18
    disabled: bool
    premiumTooSmall: bool

@dataclass
class DHVLensMK1_OptionStrikeDrill:
    strike: uint128
    sell: DHVLensMK1_TradingSpec
    buy: DHVLensMK1_TradingSpec
    delta: int_e18
    exposure: int_e18

@dataclass
class DHVLensMK1_OptionExpirationDrill:
    expiration: uint64
    callStrikes: list[uint128]
    callOptionDrill: list[DHVLensMK1_OptionStrikeDrill]
    putStrikes: list[uint128]
    putOptionDrill: list[DHVLensMK1_OptionStrikeDrill]
    underlyingPrice: uint_e18

@dataclass
class DHVLensMK1_OptionChain:
    expirations: list[uint64]
    optionExpirationDrills: list[DHVLensMK1_OptionExpirationDrill]

class lens(BaseAbi):
    address: Address = Address("0xe1805262E848945C8E545D1F82809Ba5bc5Ad7c0")
    
    def catalogue(
        self,
    ) -> Address:
        return self._call(
            "catalogue"
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def getExpirations(
        self,
    ) -> list[uint64]:
        return self._call(
            "getExpirations"
        )
        
    def getOptionChain(
        self,
    ) -> DHVLensMK1_OptionChain:
        return self._call(
            "getOptionChain"
        )
        
    def getOptionExpirationDrill(
        self,
        expiration: uint64,
    ) -> DHVLensMK1_OptionExpirationDrill:
        return self._call(
            "getOptionExpirationDrill",
            expiration=expiration
        )
        
    def pricer(
        self,
    ) -> Address:
        return self._call(
            "pricer"
        )
        
    def protocol(
        self,
    ) -> Address:
        return self._call(
            "protocol"
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        return self._call(
            "strikeAsset"
        )
        
    def underlyingAsset(
        self,
    ) -> Address:
        return self._call(
            "underlyingAsset"
        )
    
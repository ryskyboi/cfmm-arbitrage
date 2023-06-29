
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

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint_e18.from_tuple(args[0]),
            uint_e18.from_tuple(args[1]),
            uint_e18.from_tuple(args[2]),
            bool(args[3]),
            bool(args[4]),
        )



@dataclass
class DHVLensMK1_OptionStrikeDrill:
    strike: uint128
    sell: DHVLensMK1_TradingSpec
    buy: DHVLensMK1_TradingSpec
    delta: int_e18
    exposure: int_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint128.from_tuple(args[0]),
            DHVLensMK1_TradingSpec.from_tuple(args[1]),
            DHVLensMK1_TradingSpec.from_tuple(args[2]),
            int_e18.from_tuple(args[3]),
            int_e18.from_tuple(args[4]),
        )



@dataclass
class DHVLensMK1_OptionExpirationDrill:
    expiration: uint64
    callStrikes: list[uint128]
    callOptionDrill: list[DHVLensMK1_OptionStrikeDrill]
    putStrikes: list[uint128]
    putOptionDrill: list[DHVLensMK1_OptionStrikeDrill]
    underlyingPrice: uint_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            [uint128.from_tuple(arg_0) for arg_0 in args[1]],
            [DHVLensMK1_OptionStrikeDrill.from_tuple(arg_0) for arg_0 in args[2]],
            [uint128.from_tuple(arg_0) for arg_0 in args[3]],
            [DHVLensMK1_OptionStrikeDrill.from_tuple(arg_0) for arg_0 in args[4]],
            uint_e18.from_tuple(args[5]),
        )



@dataclass
class DHVLensMK1_OptionChain:
    expirations: list[uint64]
    optionExpirationDrills: list[DHVLensMK1_OptionExpirationDrill]

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            [uint64.from_tuple(arg_0) for arg_0 in args[0]],
            [DHVLensMK1_OptionExpirationDrill.from_tuple(arg_0) for arg_0 in args[1]],
        )



class DHVlens(BaseAbi):
    address: Address = Address("0xa306C00e08ebC84a5F4F67b561B8F6EDeb77600D")
    
    def catalogue(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "catalogue"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def getExpirations(
        self,
    ) -> list[uint64]:
        my_var_0 = self._call(
            "getExpirations"
        )
        return [uint64.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getOptionChain(
        self,
    ) -> DHVLensMK1_OptionChain:
        my_var_0 = self._call(
            "getOptionChain"
        )
        return DHVLensMK1_OptionChain.from_tuple(my_var_0)
        
    def getOptionExpirationDrill(
        self,
        expiration: uint64,
    ) -> DHVLensMK1_OptionExpirationDrill:
        my_var_0 = self._call(
            "getOptionExpirationDrill",
            expiration=expiration
        )
        return DHVLensMK1_OptionExpirationDrill.from_tuple(my_var_0)
        
    def pricer(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "pricer"
        )
        return Address.from_tuple(my_var_0)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
    
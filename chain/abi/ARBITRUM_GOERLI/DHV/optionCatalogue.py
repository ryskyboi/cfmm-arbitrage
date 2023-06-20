
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class Types_Option:
    expiration: uint64
    strike: uint128
    isPut: bool
    isBuyable: bool
    isSellable: bool

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            bool(args[2]),
            bool(args[3]),
            bool(args[4]),
        )



@dataclass
class OptionCatalogue_OptionStores:
    approvedOption: bool
    isBuyable: bool
    isSellable: bool

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            bool(args[0]),
            bool(args[1]),
            bool(args[2]),
        )



class optionCatalogue(BaseAbi):
    address: Address = Address("0xde458dD32651F27A8895D4a92B7798Cdc4EbF2f0")
    
    def approvedOptions(
        self,
        oHash: bytes32,
    ) -> bool:
        my_var_0 = self._call(
            "approvedOptions",
            oHash=oHash
        )
        return bool(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def changeOptionBuyOrSell(
        self,
        options: list[Types_Option],
    ) -> None:
        self._call(
            "changeOptionBuyOrSell",
            options=options
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def expirations(
        self,
        x_0: uint_e18,
    ) -> uint64:
        my_var_0 = self._call(
            "expirations",
            x_0=x_0
        )
        return uint64.from_tuple(my_var_0)
        
    def getExpirations(
        self,
    ) -> list[uint64]:
        my_var_0 = self._call(
            "getExpirations"
        )
        return [uint64.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getOptionDetails(
        self,
        expiration: uint64,
        isPut: bool,
    ) -> list[uint128]:
        my_var_0 = self._call(
            "getOptionDetails",
            expiration=expiration,
            isPut=isPut
        )
        return [uint128.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getOptionStores(
        self,
        oHash: bytes32,
    ) -> OptionCatalogue_OptionStores:
        my_var_0 = self._call(
            "getOptionStores",
            oHash=oHash
        )
        return OptionCatalogue_OptionStores.from_tuple(my_var_0)
        
    def isBuyable(
        self,
        oHash: bytes32,
    ) -> bool:
        my_var_0 = self._call(
            "isBuyable",
            oHash=oHash
        )
        return bool(my_var_0)
        
    def isSellable(
        self,
        oHash: bytes32,
    ) -> bool:
        my_var_0 = self._call(
            "isSellable",
            oHash=oHash
        )
        return bool(my_var_0)
        
    def issueNewSeries(
        self,
        options: list[Types_Option],
    ) -> None:
        self._call(
            "issueNewSeries",
            options=options
        )
        
    def optionDetails(
        self,
        x_0: uint_e18,
        x_1: bool,
        x_2: uint_e18,
    ) -> uint128:
        my_var_0 = self._call(
            "optionDetails",
            x_0=x_0,
            x_1=x_1,
            x_2=x_2
        )
        return uint128.from_tuple(my_var_0)
        
    def optionStores(
        self,
        x_0: bytes32,
    ) -> tuple[bool, bool, bool]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "optionStores",
            x_0=x_0
        )
        return bool(my_var_0), bool(my_var_1), bool(my_var_2)
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
    
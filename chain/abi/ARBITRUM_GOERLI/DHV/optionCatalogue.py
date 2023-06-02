
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

@dataclass
class OptionCatalogue_OptionStores:
    approvedOption: bool
    isBuyable: bool
    isSellable: bool

class optionCatalogue(BaseAbi):
    address: Address = Address("0xde458dD32651F27A8895D4a92B7798Cdc4EbF2f0")
    
    def approvedOptions(
        self,
        oHash: bytes32,
    ) -> bool:
        return self._call(
            "approvedOptions",
            oHash=oHash
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
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
        return self._call(
            "collateralAsset"
        )
        
    def expirations(
        self,
        x_0: uint_e18,
    ) -> uint64:
        return self._call(
            "expirations",
            x_0=x_0
        )
        
    def getExpirations(
        self,
    ) -> list[uint64]:
        return self._call(
            "getExpirations"
        )
        
    def getOptionDetails(
        self,
        expiration: uint64,
        isPut: bool,
    ) -> list[uint128]:
        return self._call(
            "getOptionDetails",
            expiration=expiration,
            isPut=isPut
        )
        
    def getOptionStores(
        self,
        oHash: bytes32,
    ) -> OptionCatalogue_OptionStores:
        return self._call(
            "getOptionStores",
            oHash=oHash
        )
        
    def isBuyable(
        self,
        oHash: bytes32,
    ) -> bool:
        return self._call(
            "isBuyable",
            oHash=oHash
        )
        
    def isSellable(
        self,
        oHash: bytes32,
    ) -> bool:
        return self._call(
            "isSellable",
            oHash=oHash
        )
        
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
        return self._call(
            "optionDetails",
            x_0=x_0,
            x_1=x_1,
            x_2=x_2
        )
        
    def optionStores(
        self,
        x_0: bytes32,
    ) -> tuple[bool, bool, bool]:
        return self._call(
            "optionStores",
            x_0=x_0
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
    
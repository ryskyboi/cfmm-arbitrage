
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class opynInteractions(BaseAbi):
    address: Address = Address("0xC9d8859bb5E7aC7e9A8c175bf79cecc008f7D39e")
    
    def getOtoken(
        self,
        oTokenFactory: Address,
        collateral: Address,
        underlying: Address,
        strikeAsset: Address,
        strike: uint_e18,
        expiration: uint_e18,
        isPut: bool,
    ) -> Address:
        my_var_0 = self._call(
            "getOtoken",
            oTokenFactory=oTokenFactory,
            collateral=collateral,
            underlying=underlying,
            strikeAsset=strikeAsset,
            strike=strike,
            expiration=expiration,
            isPut=isPut
        )
        return Address.from_tuple(my_var_0)
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class VolatilityFeed_SABRParams:
    callAlpha: int_e6
    callBeta: int_e6
    callRho: int_e6
    callVolvol: int_e6
    putAlpha: int_e6
    putBeta: int_e6
    putRho: int_e6
    putVolvol: int_e6
    interestRate: int_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            int_e6.from_tuple(args[0]),
            int_e6.from_tuple(args[1]),
            int_e6.from_tuple(args[2]),
            int_e6.from_tuple(args[3]),
            int_e6.from_tuple(args[4]),
            int_e6.from_tuple(args[5]),
            int_e6.from_tuple(args[6]),
            int_e6.from_tuple(args[7]),
            int_e18.from_tuple(args[8]),
        )



class volFeed(BaseAbi):
    address: Address = Address("0xf058Fe438AAF22617C30997579E89176e19635Dc")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def expiries(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "expiries",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getExpiries(
        self,
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getExpiries"
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getImpliedVolatility(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getImpliedVolatility",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getImpliedVolatilityWithForward(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getImpliedVolatilityWithForward",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "keeper",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def sabrParams(
        self,
        x_0: uint_e18,
    ) -> tuple[int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6, my_var_7, my_var_8 = self._call(
            "sabrParams",
            x_0=x_0
        )
        return int_e6.from_tuple(my_var_0), int_e6.from_tuple(my_var_1), int_e6.from_tuple(my_var_2), int_e6.from_tuple(my_var_3), int_e6.from_tuple(my_var_4), int_e6.from_tuple(my_var_5), int_e6.from_tuple(my_var_6), int_e6.from_tuple(my_var_7), int_e18.from_tuple(my_var_8)
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setKeeper(
        self,
        _keeper: Address,
        _auth: bool,
    ) -> None:
        self._call(
            "setKeeper",
            _keeper=_keeper,
            _auth=_auth
        )
        
    def setSabrParameters(
        self,
        _sabrParams: VolatilityFeed_SABRParams,
        _expiry: uint_e18,
    ) -> None:
        self._call(
            "setSabrParameters",
            _sabrParams=_sabrParams,
            _expiry=_expiry
        )
    

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

class volFeed(BaseAbi):
    address: Address = Address("0xf058Fe438AAF22617C30997579E89176e19635Dc")
    
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def expiries(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        return self._call(
            "expiries",
            x_0=x_0
        )
        
    def getExpiries(
        self,
    ) -> list[uint_e18]:
        return self._call(
            "getExpiries"
        )
        
    def getImpliedVolatility(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> uint_e18:
        return self._call(
            "getImpliedVolatility",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        
    def getImpliedVolatilityWithForward(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> tuple[uint_e18, uint_e18]:
        return self._call(
            "getImpliedVolatilityWithForward",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "keeper",
            x_0=x_0
        )
        
    def sabrParams(
        self,
        x_0: uint_e18,
    ) -> tuple[int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e6, int_e18]:
        return self._call(
            "sabrParams",
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
    
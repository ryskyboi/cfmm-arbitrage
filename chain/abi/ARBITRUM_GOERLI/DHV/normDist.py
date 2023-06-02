
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class normDist(BaseAbi):
    address: Address = Address("0x27810907FD5B3427567fF12c1412952EC7d04E80")
    
    def cdf(
        self,
        x: int_e18,
    ) -> int_e18:
        return self._call(
            "cdf",
            x=x
        )
        
    def getScoresFromT(
        self,
        t: int_e18,
    ) -> int_e18:
        return self._call(
            "getScoresFromT",
            t=t
        )
        
    def phi(
        self,
        x: int_e18,
    ) -> int_e18:
        return self._call(
            "phi",
            x=x
        )
    
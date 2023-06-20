
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
        my_var_0 = self._call(
            "cdf",
            x=x
        )
        return int_e18.from_tuple(my_var_0)
        
    def getScoresFromT(
        self,
        t: int_e18,
    ) -> int_e18:
        my_var_0 = self._call(
            "getScoresFromT",
            t=t
        )
        return int_e18.from_tuple(my_var_0)
        
    def phi(
        self,
        x: int_e18,
    ) -> int_e18:
        my_var_0 = self._call(
            "phi",
            x=x
        )
        return int_e18.from_tuple(my_var_0)
    
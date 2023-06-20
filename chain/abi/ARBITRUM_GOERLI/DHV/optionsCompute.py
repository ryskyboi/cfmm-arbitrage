
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class Types_PortfolioValues:
    delta: int_e18
    gamma: int_e18
    vega: int_e18
    theta: int_e18
    callPutsValue: int_e18
    timestamp: uint_e18
    spotPrice: uint_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            int_e18.from_tuple(args[0]),
            int_e18.from_tuple(args[1]),
            int_e18.from_tuple(args[2]),
            int_e18.from_tuple(args[3]),
            int_e18.from_tuple(args[4]),
            uint_e18.from_tuple(args[5]),
            uint_e18.from_tuple(args[6]),
        )



class optionsCompute(BaseAbi):
    address: Address = Address("0x1f9E2596037dC1727AbeA03085E92Ef65641949f")
    
    def formatStrikePrice(
        self,
        strikePrice: uint_e18,
        collateral: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "formatStrikePrice",
            strikePrice=strikePrice,
            collateral=collateral
        )
        return uint_e18.from_tuple(my_var_0)
        
    def validatePortfolioValues(
        self,
        spotPrice: uint_e18,
        portfolioValues: Types_PortfolioValues,
        maxTimeDeviationThreshold: uint_e18,
        maxPriceDeviationThreshold: uint_e18,
    ) -> None:
        self._call(
            "validatePortfolioValues",
            spotPrice=spotPrice,
            portfolioValues=portfolioValues,
            maxTimeDeviationThreshold=maxTimeDeviationThreshold,
            maxPriceDeviationThreshold=maxPriceDeviationThreshold
        )
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class L2ChainlinkPricer(BaseAbi):
    address: Address = Address("0x7a71f218003d2DbF25337d072FA096099B50E0F0")
    
    def aggregator(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "aggregator"
        )
        return Address.from_tuple(my_var_0)
        
    def aggregatorDecimals(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "aggregatorDecimals"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def asset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "asset"
        )
        return Address.from_tuple(my_var_0)
        
    def bot(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "bot"
        )
        return Address.from_tuple(my_var_0)
        
    def getHistoricalPrice(
        self,
        _roundId: uint80,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getHistoricalPrice",
            _roundId=_roundId
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getPrice(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPrice"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def oracle(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "oracle"
        )
        return Address.from_tuple(my_var_0)
        
    def sequencerUptimeFeedAddress(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "sequencerUptimeFeedAddress"
        )
        return Address.from_tuple(my_var_0)
        
    def setExpiryPriceInOracle(
        self,
        _expiryTimestamp: uint_e18,
        _roundId: uint80,
    ) -> None:
        self._call(
            "setExpiryPriceInOracle",
            _expiryTimestamp=_expiryTimestamp,
            _roundId=_roundId
        )
    
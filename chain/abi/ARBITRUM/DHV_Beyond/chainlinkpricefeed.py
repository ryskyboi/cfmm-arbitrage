
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class chainlinkpricefeed(BaseAbi):
    address: Address = Address("0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612")
    
    def acceptOwnership(
        self,
    ) -> None:
        self._call(
            "acceptOwnership"
        )
        
    def accessController(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "accessController"
        )
        return Address.from_tuple(my_var_0)
        
    def aggregator(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "aggregator"
        )
        return Address.from_tuple(my_var_0)
        
    def confirmAggregator(
        self,
        _aggregator: Address,
    ) -> None:
        self._call(
            "confirmAggregator",
            _aggregator=_aggregator
        )
        
    def decimals(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "decimals"
        )
        return uint8.from_tuple(my_var_0)
        
    def description(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "description"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def getAnswer(
        self,
        _roundId: uint_e18,
    ) -> int_e18:
        my_var_0 = self._call(
            "getAnswer",
            _roundId=_roundId
        )
        return int_e18.from_tuple(my_var_0)
        
    def getRoundData(
        self,
        _roundId: uint80,
    ) -> tuple[uint80, int_e18, uint_e18, uint_e18, uint80]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4 = self._call(
            "getRoundData",
            _roundId=_roundId
        )
        return uint80.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint80.from_tuple(my_var_4)
        
    def getTimestamp(
        self,
        _roundId: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getTimestamp",
            _roundId=_roundId
        )
        return uint_e18.from_tuple(my_var_0)
        
    def latestAnswer(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "latestAnswer"
        )
        return int_e18.from_tuple(my_var_0)
        
    def latestRound(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "latestRound"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def latestRoundData(
        self,
    ) -> tuple[uint80, int_e18, uint_e18, uint_e18, uint80]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4 = self._call(
            "latestRoundData"
        )
        return uint80.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint80.from_tuple(my_var_4)
        
    def latestTimestamp(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "latestTimestamp"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def owner(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "owner"
        )
        return Address.from_tuple(my_var_0)
        
    def phaseAggregators(
        self,
        x_0: uint16,
    ) -> Address:
        my_var_0 = self._call(
            "phaseAggregators",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0)
        
    def phaseId(
        self,
    ) -> uint16:
        my_var_0 = self._call(
            "phaseId"
        )
        return uint16.from_tuple(my_var_0)
        
    def proposeAggregator(
        self,
        _aggregator: Address,
    ) -> None:
        self._call(
            "proposeAggregator",
            _aggregator=_aggregator
        )
        
    def proposedAggregator(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "proposedAggregator"
        )
        return Address.from_tuple(my_var_0)
        
    def proposedGetRoundData(
        self,
        _roundId: uint80,
    ) -> tuple[uint80, int_e18, uint_e18, uint_e18, uint80]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4 = self._call(
            "proposedGetRoundData",
            _roundId=_roundId
        )
        return uint80.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint80.from_tuple(my_var_4)
        
    def proposedLatestRoundData(
        self,
    ) -> tuple[uint80, int_e18, uint_e18, uint_e18, uint80]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4 = self._call(
            "proposedLatestRoundData"
        )
        return uint80.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint80.from_tuple(my_var_4)
        
    def setController(
        self,
        _accessController: Address,
    ) -> None:
        self._call(
            "setController",
            _accessController=_accessController
        )
        
    def transferOwnership(
        self,
        _to: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            _to=_to
        )
        
    def version(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "version"
        )
        return uint_e18.from_tuple(my_var_0)
    
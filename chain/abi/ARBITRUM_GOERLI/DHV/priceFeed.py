
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class priceFeed(BaseAbi):
    address: Address = Address("0xf7B1e3a7856067BEcee81FdE0DD38d923b99554D")
    
    def addPriceFeed(
        self,
        underlying: Address,
        strike: Address,
        feed: Address,
    ) -> None:
        self._call(
            "addPriceFeed",
            underlying=underlying,
            strike=strike,
            feed=feed
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def getNormalizedRate(
        self,
        underlying: Address,
        strike: Address,
    ) -> uint_e18:
        return self._call(
            "getNormalizedRate",
            underlying=underlying,
            strike=strike
        )
        
    def getRate(
        self,
        underlying: Address,
        strike: Address,
    ) -> uint_e18:
        return self._call(
            "getRate",
            underlying=underlying,
            strike=strike
        )
        
    def priceFeeds(
        self,
        x_0: Address,
        x_1: Address,
    ) -> Address:
        return self._call(
            "priceFeeds",
            x_0=x_0,
            x_1=x_1
        )
        
    def sequencerUptimeFeedAddress(
        self,
    ) -> Address:
        return self._call(
            "sequencerUptimeFeedAddress"
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setSequencerUptimeFeedAddress(
        self,
        _sequencerUptimeFeedAddress: Address,
    ) -> None:
        self._call(
            "setSequencerUptimeFeedAddress",
            _sequencerUptimeFeedAddress=_sequencerUptimeFeedAddress
        )
    
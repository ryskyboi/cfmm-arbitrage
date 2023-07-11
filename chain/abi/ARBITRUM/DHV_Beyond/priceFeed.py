
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class priceFeed(BaseAbi):
    address: Address = Address("0x7f86AC0c38bbc3211c610abE3841847fe19590A4")
    
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
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def getNormalizedRate(
        self,
        underlying: Address,
        strike: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNormalizedRate",
            underlying=underlying,
            strike=strike
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getRate(
        self,
        underlying: Address,
        strike: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getRate",
            underlying=underlying,
            strike=strike
        )
        return uint_e18.from_tuple(my_var_0)
        
    def priceFeeds(
        self,
        x_0: Address,
        x_1: Address,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeeds",
            x_0=x_0,
            x_1=x_1
        )
        return Address.from_tuple(my_var_0)
        
    def sequencerUptimeFeedAddress(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "sequencerUptimeFeedAddress"
        )
        return Address.from_tuple(my_var_0)
        
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
    

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

@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

class pvFeed(BaseAbi):
    address: Address = Address("0x84fbb7C0a210e5e3A9f7707e1Fb725ADcf0CF528")
    
    def accountLiquidatedSeries(
        self,
        _series: Address,
    ) -> None:
        self._call(
            "accountLiquidatedSeries",
            _series=_series
        )
        
    def addressAtIndexInSet(
        self,
        _i: uint_e18,
    ) -> Address:
        return self._call(
            "addressAtIndexInSet",
            _i=_i
        )
        
    def addressSetLength(
        self,
    ) -> uint_e18:
        return self._call(
            "addressSetLength"
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def cleanLooperManually(
        self,
        _series: Address,
    ) -> None:
        self._call(
            "cleanLooperManually",
            _series=_series
        )
        
    def fulfill(
        self,
        _underlying: Address,
        _strikeAsset: Address,
    ) -> None:
        self._call(
            "fulfill",
            _underlying=_underlying,
            _strikeAsset=_strikeAsset
        )
        
    def getAddressSet(
        self,
    ) -> list[Address]:
        return self._call(
            "getAddressSet"
        )
        
    def getPortfolioValues(
        self,
        underlying: Address,
        strike: Address,
    ) -> Types_PortfolioValues:
        return self._call(
            "getPortfolioValues",
            underlying=underlying,
            strike=strike
        )
        
    def handler(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "handler",
            x_0=x_0
        )
        
    def isAddressInSet(
        self,
        _a: Address,
    ) -> bool:
        return self._call(
            "isAddressInSet",
            _a=_a
        )
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "keeper",
            x_0=x_0
        )
        
    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )
        
    def maxNetDhvExposure(
        self,
    ) -> uint_e18:
        return self._call(
            "maxNetDhvExposure"
        )
        
    def migrate(
        self,
        _migrateContract: Address,
    ) -> None:
        self._call(
            "migrate",
            _migrateContract=_migrateContract
        )
        
    def netDhvExposure(
        self,
        x_0: bytes32,
    ) -> int_e18:
        return self._call(
            "netDhvExposure",
            x_0=x_0
        )
        
    def protocol(
        self,
    ) -> Address:
        return self._call(
            "protocol"
        )
        
    def requestPortfolioData(
        self,
        _underlying: Address,
        _strike: Address,
    ) -> bytes32:
        return self._call(
            "requestPortfolioData",
            _underlying=_underlying,
            _strike=_strike
        )
        
    def rfr(
        self,
    ) -> uint_e18:
        return self._call(
            "rfr"
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setHandler(
        self,
        _handler: Address,
        _auth: bool,
    ) -> None:
        self._call(
            "setHandler",
            _handler=_handler,
            _auth=_auth
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
        
    def setLiquidityPool(
        self,
        _liquidityPool: Address,
    ) -> None:
        self._call(
            "setLiquidityPool",
            _liquidityPool=_liquidityPool
        )
        
    def setMaxNetDhvExposure(
        self,
        _maxNetDhvExposure: uint_e18,
    ) -> None:
        self._call(
            "setMaxNetDhvExposure",
            _maxNetDhvExposure=_maxNetDhvExposure
        )
        
    def setProtocol(
        self,
        _protocol: Address,
    ) -> None:
        self._call(
            "setProtocol",
            _protocol=_protocol
        )
        
    def setRFR(
        self,
        _rfr: uint_e18,
    ) -> None:
        self._call(
            "setRFR",
            _rfr=_rfr
        )
        
    def storesForAddress(
        self,
        x_0: Address,
    ) -> tuple[Types_OptionSeries, int_e18, int_e18]:
        return self._call(
            "storesForAddress",
            x_0=x_0
        )
        
    def syncLooper(
        self,
    ) -> None:
        self._call(
            "syncLooper"
        )
        
    def updateStores(
        self,
        _optionSeries: Types_OptionSeries,
        shortExposure: int_e18,
        longExposure: int_e18,
        _seriesAddress: Address,
    ) -> None:
        self._call(
            "updateStores",
            _optionSeries=_optionSeries,
            shortExposure=shortExposure,
            longExposure=longExposure,
            _seriesAddress=_seriesAddress
        )
    
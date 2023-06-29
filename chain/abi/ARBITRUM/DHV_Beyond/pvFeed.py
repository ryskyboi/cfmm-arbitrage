
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



@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            bool(args[2]),
            Address.from_tuple(args[3]),
            Address.from_tuple(args[4]),
            Address.from_tuple(args[5]),
        )



class pvFeed(BaseAbi):
    address: Address = Address("0x7f9d820CFc109686F2ca096fFA93dd497b91C073")
    
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
        my_var_0 = self._call(
            "addressAtIndexInSet",
            _i=_i
        )
        return Address.from_tuple(my_var_0)
        
    def addressSetLength(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "addressSetLength"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "getAddressSet"
        )
        return [Address.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPortfolioValues(
        self,
        underlying: Address,
        strike: Address,
    ) -> Types_PortfolioValues:
        my_var_0 = self._call(
            "getPortfolioValues",
            underlying=underlying,
            strike=strike
        )
        return Types_PortfolioValues.from_tuple(my_var_0)
        
    def handler(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "handler",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def isAddressInSet(
        self,
        _a: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isAddressInSet",
            _a=_a
        )
        return bool(my_var_0)
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "keeper",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def maxNetDhvExposure(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxNetDhvExposure"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "netDhvExposure",
            x_0=x_0
        )
        return int_e18.from_tuple(my_var_0)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def requestPortfolioData(
        self,
        _underlying: Address,
        _strike: Address,
    ) -> bytes32:
        my_var_0 = self._call(
            "requestPortfolioData",
            _underlying=_underlying,
            _strike=_strike
        )
        return bytes32.from_tuple(my_var_0)
        
    def rfr(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "rfr"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        
    def setNetDhvExposures(
        self,
        _optionHashes: list[bytes32],
        _netDhvExposures: list[int_e18],
    ) -> None:
        self._call(
            "setNetDhvExposures",
            _optionHashes=_optionHashes,
            _netDhvExposures=_netDhvExposures
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
        my_var_0, my_var_1, my_var_2 = self._call(
            "storesForAddress",
            x_0=x_0
        )
        return Types_OptionSeries.from_tuple(my_var_0), int_e18.from_tuple(my_var_1), int_e18.from_tuple(my_var_2)
        
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
    
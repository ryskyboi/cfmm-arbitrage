
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class OpynOracle(BaseAbi):
    address: Address = Address("0x35578F5A49E1f1Cf34ed780B46A0BdABA23D4C0b")
    
    def disputeExpiryPrice(
        self,
        _asset: Address,
        _expiryTimestamp: uint_e18,
        _price: uint_e18,
    ) -> None:
        self._call(
            "disputeExpiryPrice",
            _asset=_asset,
            _expiryTimestamp=_expiryTimestamp,
            _price=_price
        )
        
    def endMigration(
        self,
    ) -> None:
        self._call(
            "endMigration"
        )
        
    def getChainlinkRoundData(
        self,
        _asset: Address,
        _roundId: uint80,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getChainlinkRoundData",
            _asset=_asset,
            _roundId=_roundId
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getDisputer(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getDisputer"
        )
        return Address.from_tuple(my_var_0)
        
    def getExpiryPrice(
        self,
        _asset: Address,
        _expiryTimestamp: uint_e18,
    ) -> tuple[uint_e18, bool]:
        my_var_0, my_var_1 = self._call(
            "getExpiryPrice",
            _asset=_asset,
            _expiryTimestamp=_expiryTimestamp
        )
        return uint_e18.from_tuple(my_var_0), bool(my_var_1)
        
    def getPrice(
        self,
        _asset: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPrice",
            _asset=_asset
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPricer(
        self,
        _asset: Address,
    ) -> Address:
        my_var_0 = self._call(
            "getPricer",
            _asset=_asset
        )
        return Address.from_tuple(my_var_0)
        
    def getPricerDisputePeriod(
        self,
        _pricer: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPricerDisputePeriod",
            _pricer=_pricer
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPricerLockingPeriod(
        self,
        _pricer: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPricerLockingPeriod",
            _pricer=_pricer
        )
        return uint_e18.from_tuple(my_var_0)
        
    def isDisputePeriodOver(
        self,
        _asset: Address,
        _expiryTimestamp: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "isDisputePeriodOver",
            _asset=_asset,
            _expiryTimestamp=_expiryTimestamp
        )
        return bool(my_var_0)
        
    def isLockingPeriodOver(
        self,
        _asset: Address,
        _expiryTimestamp: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "isLockingPeriodOver",
            _asset=_asset,
            _expiryTimestamp=_expiryTimestamp
        )
        return bool(my_var_0)
        
    def migrateOracle(
        self,
        _asset: Address,
        _expiries: list[uint_e18],
        _prices: list[uint_e18],
    ) -> None:
        self._call(
            "migrateOracle",
            _asset=_asset,
            _expiries=_expiries,
            _prices=_prices
        )
        
    def owner(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "owner"
        )
        return Address.from_tuple(my_var_0)
        
    def renounceOwnership(
        self,
    ) -> None:
        self._call(
            "renounceOwnership"
        )
        
    def setAssetPricer(
        self,
        _asset: Address,
        _pricer: Address,
    ) -> None:
        self._call(
            "setAssetPricer",
            _asset=_asset,
            _pricer=_pricer
        )
        
    def setDisputePeriod(
        self,
        _pricer: Address,
        _disputePeriod: uint_e18,
    ) -> None:
        self._call(
            "setDisputePeriod",
            _pricer=_pricer,
            _disputePeriod=_disputePeriod
        )
        
    def setDisputer(
        self,
        _disputer: Address,
    ) -> None:
        self._call(
            "setDisputer",
            _disputer=_disputer
        )
        
    def setExpiryPrice(
        self,
        _asset: Address,
        _expiryTimestamp: uint_e18,
        _price: uint_e18,
    ) -> None:
        self._call(
            "setExpiryPrice",
            _asset=_asset,
            _expiryTimestamp=_expiryTimestamp,
            _price=_price
        )
        
    def setLockingPeriod(
        self,
        _pricer: Address,
        _lockingPeriod: uint_e18,
    ) -> None:
        self._call(
            "setLockingPeriod",
            _pricer=_pricer,
            _lockingPeriod=_lockingPeriod
        )
        
    def setStablePrice(
        self,
        _asset: Address,
        _price: uint_e18,
    ) -> None:
        self._call(
            "setStablePrice",
            _asset=_asset,
            _price=_price
        )
        
    def transferOwnership(
        self,
        newOwner: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            newOwner=newOwner
        )
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class optionProtocol(BaseAbi):
    address: Address = Address("0x81267CBE2d605b7Ae2328462C1EAF51a1Ab57fFd")
    
    def accounting(
        self,
    ) -> Address:
        return self._call(
            "accounting"
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def changeAccounting(
        self,
        _accounting: Address,
    ) -> None:
        self._call(
            "changeAccounting",
            _accounting=_accounting
        )
        
    def changeOptionRegistry(
        self,
        _optionRegistry: Address,
    ) -> None:
        self._call(
            "changeOptionRegistry",
            _optionRegistry=_optionRegistry
        )
        
    def changePortfolioValuesFeed(
        self,
        _portfolioValuesFeed: Address,
    ) -> None:
        self._call(
            "changePortfolioValuesFeed",
            _portfolioValuesFeed=_portfolioValuesFeed
        )
        
    def changePriceFeed(
        self,
        _priceFeed: Address,
    ) -> None:
        self._call(
            "changePriceFeed",
            _priceFeed=_priceFeed
        )
        
    def changeVolatilityFeed(
        self,
        _volFeed: Address,
    ) -> None:
        self._call(
            "changeVolatilityFeed",
            _volFeed=_volFeed
        )
        
    def optionRegistry(
        self,
    ) -> Address:
        return self._call(
            "optionRegistry"
        )
        
    def portfolioValuesFeed(
        self,
    ) -> Address:
        return self._call(
            "portfolioValuesFeed"
        )
        
    def priceFeed(
        self,
    ) -> Address:
        return self._call(
            "priceFeed"
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def volatilityFeed(
        self,
    ) -> Address:
        return self._call(
            "volatilityFeed"
        )
    

from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class optionProtocol(BaseAbi):
    address: Address = Address("0x81267CBE2d605b7Ae2328462C1EAF51a1Ab57fFd")
    
    def accounting(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "accounting"
        )
        return Address.from_tuple(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "optionRegistry"
        )
        return Address.from_tuple(my_var_0)
        
    def portfolioValuesFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "portfolioValuesFeed"
        )
        return Address.from_tuple(my_var_0)
        
    def priceFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeed"
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
        
    def volatilityFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "volatilityFeed"
        )
        return Address.from_tuple(my_var_0)
    
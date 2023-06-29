
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class whitelist(BaseAbi):
    address: Address = Address("0x84CaCC4103CeE1Da9b79f9Ed0Ed97414240D9c6F")
    
    def addressBook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressBook"
        )
        return Address.from_tuple(my_var_0)
        
    def blacklistCallee(
        self,
        _callee: Address,
    ) -> None:
        self._call(
            "blacklistCallee",
            _callee=_callee
        )
        
    def blacklistCollateral(
        self,
        _collateral: Address,
    ) -> None:
        self._call(
            "blacklistCollateral",
            _collateral=_collateral
        )
        
    def blacklistOtoken(
        self,
        _otokenAddress: Address,
    ) -> None:
        self._call(
            "blacklistOtoken",
            _otokenAddress=_otokenAddress
        )
        
    def blacklistProduct(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> None:
        self._call(
            "blacklistProduct",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )
        
    def isCoveredWhitelistedCollateral(
        self,
        _collateral: Address,
        _underlying: Address,
        _isPut: bool,
    ) -> bool:
        my_var_0 = self._call(
            "isCoveredWhitelistedCollateral",
            _collateral=_collateral,
            _underlying=_underlying,
            _isPut=_isPut
        )
        return bool(my_var_0)
        
    def isNakedWhitelistedCollateral(
        self,
        _collateral: Address,
        _underlying: Address,
        _isPut: bool,
    ) -> bool:
        my_var_0 = self._call(
            "isNakedWhitelistedCollateral",
            _collateral=_collateral,
            _underlying=_underlying,
            _isPut=_isPut
        )
        return bool(my_var_0)
        
    def isWhitelistedCallee(
        self,
        _callee: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isWhitelistedCallee",
            _callee=_callee
        )
        return bool(my_var_0)
        
    def isWhitelistedCollateral(
        self,
        _collateral: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isWhitelistedCollateral",
            _collateral=_collateral
        )
        return bool(my_var_0)
        
    def isWhitelistedOtoken(
        self,
        _otoken: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isWhitelistedOtoken",
            _otoken=_otoken
        )
        return bool(my_var_0)
        
    def isWhitelistedProduct(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> bool:
        my_var_0 = self._call(
            "isWhitelistedProduct",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )
        return bool(my_var_0)
        
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
        
    def transferOwnership(
        self,
        newOwner: Address,
    ) -> None:
        self._call(
            "transferOwnership",
            newOwner=newOwner
        )
        
    def whitelistCallee(
        self,
        _callee: Address,
    ) -> None:
        self._call(
            "whitelistCallee",
            _callee=_callee
        )
        
    def whitelistCollateral(
        self,
        _collateral: Address,
    ) -> None:
        self._call(
            "whitelistCollateral",
            _collateral=_collateral
        )
        
    def whitelistCoveredCollateral(
        self,
        _collateral: Address,
        _underlying: Address,
        _isPut: bool,
    ) -> None:
        self._call(
            "whitelistCoveredCollateral",
            _collateral=_collateral,
            _underlying=_underlying,
            _isPut=_isPut
        )
        
    def whitelistNakedCollateral(
        self,
        _collateral: Address,
        _underlying: Address,
        _isPut: bool,
    ) -> None:
        self._call(
            "whitelistNakedCollateral",
            _collateral=_collateral,
            _underlying=_underlying,
            _isPut=_isPut
        )
        
    def whitelistOtoken(
        self,
        _otokenAddress: Address,
    ) -> None:
        self._call(
            "whitelistOtoken",
            _otokenAddress=_otokenAddress
        )
        
    def whitelistProduct(
        self,
        _underlying: Address,
        _strike: Address,
        _collateral: Address,
        _isPut: bool,
    ) -> None:
        self._call(
            "whitelistProduct",
            _underlying=_underlying,
            _strike=_strike,
            _collateral=_collateral,
            _isPut=_isPut
        )
    
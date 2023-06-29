
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class uniswapV3HedgingReactor(BaseAbi):
    address: Address = Address("0x0053849115783b9678DBB173BB852f06e950Fe05")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def buySlippage(
        self,
    ) -> uint16:
        my_var_0 = self._call(
            "buySlippage"
        )
        return uint16.from_tuple(my_var_0)
        
    def changePoolFee(
        self,
        _poolFee: uint24,
    ) -> None:
        self._call(
            "changePoolFee",
            _poolFee=_poolFee
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def getDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "getDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def getPoolDenominatedValue(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPoolDenominatedValue"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def hedgeDelta(
        self,
        _delta: int_e18,
    ) -> int_e18:
        my_var_0 = self._call(
            "hedgeDelta",
            _delta=_delta
        )
        return int_e18.from_tuple(my_var_0)
        
    def internalDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "internalDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def minAmount(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minAmount"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def parentLiquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "parentLiquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def poolFee(
        self,
    ) -> uint24:
        my_var_0 = self._call(
            "poolFee"
        )
        return uint24.from_tuple(my_var_0)
        
    def priceFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeed"
        )
        return Address.from_tuple(my_var_0)
        
    def sellSlippage(
        self,
    ) -> uint16:
        my_var_0 = self._call(
            "sellSlippage"
        )
        return uint16.from_tuple(my_var_0)
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setMinAmount(
        self,
        _minAmount: uint_e18,
    ) -> None:
        self._call(
            "setMinAmount",
            _minAmount=_minAmount
        )
        
    def setSlippage(
        self,
        _buySlippage: uint16,
        _sellSlippage: uint16,
    ) -> None:
        self._call(
            "setSlippage",
            _buySlippage=_buySlippage,
            _sellSlippage=_sellSlippage
        )
        
    def swapRouter(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "swapRouter"
        )
        return Address.from_tuple(my_var_0)
        
    def update(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "update"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def wETH(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "wETH"
        )
        return Address.from_tuple(my_var_0)
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdraw",
            _amount=_amount
        )
        return uint_e18.from_tuple(my_var_0)
    
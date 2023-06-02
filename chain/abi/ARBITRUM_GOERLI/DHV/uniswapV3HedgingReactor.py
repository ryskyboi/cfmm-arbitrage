
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class uniswapV3HedgingReactor(BaseAbi):
    address: Address = Address("0x7a3eEC265292044417CC873d7cb2dDbF613745bC")
    
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def buySlippage(
        self,
    ) -> uint16:
        return self._call(
            "buySlippage"
        )
        
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
        return self._call(
            "collateralAsset"
        )
        
    def getDelta(
        self,
    ) -> int_e18:
        return self._call(
            "getDelta"
        )
        
    def getPoolDenominatedValue(
        self,
    ) -> uint_e18:
        return self._call(
            "getPoolDenominatedValue"
        )
        
    def hedgeDelta(
        self,
        _delta: int_e18,
    ) -> int_e18:
        return self._call(
            "hedgeDelta",
            _delta=_delta
        )
        
    def internalDelta(
        self,
    ) -> int_e18:
        return self._call(
            "internalDelta"
        )
        
    def minAmount(
        self,
    ) -> uint_e18:
        return self._call(
            "minAmount"
        )
        
    def parentLiquidityPool(
        self,
    ) -> Address:
        return self._call(
            "parentLiquidityPool"
        )
        
    def poolFee(
        self,
    ) -> uint24:
        return self._call(
            "poolFee"
        )
        
    def priceFeed(
        self,
    ) -> Address:
        return self._call(
            "priceFeed"
        )
        
    def sellSlippage(
        self,
    ) -> uint16:
        return self._call(
            "sellSlippage"
        )
        
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
        return self._call(
            "swapRouter"
        )
        
    def update(
        self,
    ) -> uint_e18:
        return self._call(
            "update"
        )
        
    def wETH(
        self,
    ) -> Address:
        return self._call(
            "wETH"
        )
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        return self._call(
            "withdraw",
            _amount=_amount
        )
    
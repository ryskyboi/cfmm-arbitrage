
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class gmxvault(BaseAbi):
    address: Address = Address("0x489ee077994b6658eafa855c308275ead8097c4a")
    
    def BASIS_POINTS_DIVISOR(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "BASIS_POINTS_DIVISOR"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def FUNDING_RATE_PRECISION(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "FUNDING_RATE_PRECISION"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def MAX_FEE_BASIS_POINTS(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "MAX_FEE_BASIS_POINTS"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def MAX_FUNDING_RATE_FACTOR(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "MAX_FUNDING_RATE_FACTOR"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def MAX_LIQUIDATION_FEE_USD(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "MAX_LIQUIDATION_FEE_USD"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def MIN_FUNDING_RATE_INTERVAL(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "MIN_FUNDING_RATE_INTERVAL"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def MIN_LEVERAGE(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "MIN_LEVERAGE"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def PRICE_PRECISION(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "PRICE_PRECISION"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def USDG_DECIMALS(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "USDG_DECIMALS"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def addRouter(
        self,
        _router: Address,
    ) -> None:
        self._call(
            "addRouter",
            _router=_router
        )
        
    def adjustForDecimals(
        self,
        _amount: uint_e18,
        _tokenDiv: Address,
        _tokenMul: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "adjustForDecimals",
            _amount=_amount,
            _tokenDiv=_tokenDiv,
            _tokenMul=_tokenMul
        )
        return uint_e18.from_tuple(my_var_0)
        
    def allWhitelistedTokens(
        self,
        x_0: uint_e18,
    ) -> Address:
        my_var_0 = self._call(
            "allWhitelistedTokens",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0)
        
    def allWhitelistedTokensLength(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "allWhitelistedTokensLength"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def approvedRouters(
        self,
        x_0: Address,
        x_1: Address,
    ) -> bool:
        my_var_0 = self._call(
            "approvedRouters",
            x_0=x_0,
            x_1=x_1
        )
        return bool(my_var_0)
        
    def bufferAmounts(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "bufferAmounts",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def buyUSDG(
        self,
        _token: Address,
        _receiver: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "buyUSDG",
            _token=_token,
            _receiver=_receiver
        )
        return uint_e18.from_tuple(my_var_0)
        
    def clearTokenConfig(
        self,
        _token: Address,
    ) -> None:
        self._call(
            "clearTokenConfig",
            _token=_token
        )
        
    def cumulativeFundingRates(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "cumulativeFundingRates",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def decreasePosition(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _collateralDelta: uint_e18,
        _sizeDelta: uint_e18,
        _isLong: bool,
        _receiver: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "decreasePosition",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _collateralDelta=_collateralDelta,
            _sizeDelta=_sizeDelta,
            _isLong=_isLong,
            _receiver=_receiver
        )
        return uint_e18.from_tuple(my_var_0)
        
    def directPoolDeposit(
        self,
        _token: Address,
    ) -> None:
        self._call(
            "directPoolDeposit",
            _token=_token
        )
        
    def errorController(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "errorController"
        )
        return Address.from_tuple(my_var_0)
        
    def errors(
        self,
        x_0: uint_e18,
    ) -> BaseStr:
        my_var_0 = self._call(
            "errors",
            x_0=x_0
        )
        return BaseStr.from_tuple(my_var_0)
        
    def feeReserves(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "feeReserves",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def fundingInterval(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "fundingInterval"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def fundingRateFactor(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "fundingRateFactor"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getDelta(
        self,
        _indexToken: Address,
        _size: uint_e18,
        _averagePrice: uint_e18,
        _isLong: bool,
        _lastIncreasedTime: uint_e18,
    ) -> tuple[bool, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getDelta",
            _indexToken=_indexToken,
            _size=_size,
            _averagePrice=_averagePrice,
            _isLong=_isLong,
            _lastIncreasedTime=_lastIncreasedTime
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getFeeBasisPoints(
        self,
        _token: Address,
        _usdgDelta: uint_e18,
        _feeBasisPoints: uint_e18,
        _taxBasisPoints: uint_e18,
        _increment: bool,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getFeeBasisPoints",
            _token=_token,
            _usdgDelta=_usdgDelta,
            _feeBasisPoints=_feeBasisPoints,
            _taxBasisPoints=_taxBasisPoints,
            _increment=_increment
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getFundingFee(
        self,
        _token: Address,
        _size: uint_e18,
        _entryFundingRate: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getFundingFee",
            _token=_token,
            _size=_size,
            _entryFundingRate=_entryFundingRate
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getGlobalShortDelta(
        self,
        _token: Address,
    ) -> tuple[bool, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getGlobalShortDelta",
            _token=_token
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getMaxPrice(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getMaxPrice",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getMinPrice(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getMinPrice",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getNextAveragePrice(
        self,
        _indexToken: Address,
        _size: uint_e18,
        _averagePrice: uint_e18,
        _isLong: bool,
        _nextPrice: uint_e18,
        _sizeDelta: uint_e18,
        _lastIncreasedTime: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNextAveragePrice",
            _indexToken=_indexToken,
            _size=_size,
            _averagePrice=_averagePrice,
            _isLong=_isLong,
            _nextPrice=_nextPrice,
            _sizeDelta=_sizeDelta,
            _lastIncreasedTime=_lastIncreasedTime
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getNextFundingRate(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNextFundingRate",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getNextGlobalShortAveragePrice(
        self,
        _indexToken: Address,
        _nextPrice: uint_e18,
        _sizeDelta: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNextGlobalShortAveragePrice",
            _indexToken=_indexToken,
            _nextPrice=_nextPrice,
            _sizeDelta=_sizeDelta
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPosition(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
    ) -> tuple[uint_e18, uint_e18, uint_e18, uint_e18, uint_e18, uint_e18, bool, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6, my_var_7 = self._call(
            "getPosition",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4), uint_e18.from_tuple(my_var_5), bool(my_var_6), uint_e18.from_tuple(my_var_7)
        
    def getPositionDelta(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
    ) -> tuple[bool, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getPositionDelta",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong
        )
        return bool(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getPositionFee(
        self,
        _sizeDelta: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPositionFee",
            _sizeDelta=_sizeDelta
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPositionKey(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
    ) -> bytes32:
        my_var_0 = self._call(
            "getPositionKey",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong
        )
        return bytes32.from_tuple(my_var_0)
        
    def getPositionLeverage(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getPositionLeverage",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getRedemptionAmount(
        self,
        _token: Address,
        _usdgAmount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getRedemptionAmount",
            _token=_token,
            _usdgAmount=_usdgAmount
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getRedemptionCollateral(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getRedemptionCollateral",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getRedemptionCollateralUsd(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getRedemptionCollateralUsd",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getTargetUsdgAmount(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getTargetUsdgAmount",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getUtilisation(
        self,
        _token: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getUtilisation",
            _token=_token
        )
        return uint_e18.from_tuple(my_var_0)
        
    def globalShortAveragePrices(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "globalShortAveragePrices",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def globalShortSizes(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "globalShortSizes",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def gov(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "gov"
        )
        return Address.from_tuple(my_var_0)
        
    def guaranteedUsd(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "guaranteedUsd",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def hasDynamicFees(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "hasDynamicFees"
        )
        return bool(my_var_0)
        
    def inManagerMode(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "inManagerMode"
        )
        return bool(my_var_0)
        
    def inPrivateLiquidationMode(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "inPrivateLiquidationMode"
        )
        return bool(my_var_0)
        
    def includeAmmPrice(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "includeAmmPrice"
        )
        return bool(my_var_0)
        
    def increasePosition(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _sizeDelta: uint_e18,
        _isLong: bool,
    ) -> None:
        self._call(
            "increasePosition",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _sizeDelta=_sizeDelta,
            _isLong=_isLong
        )
        
    def initialize(
        self,
        _router: Address,
        _usdg: Address,
        _priceFeed: Address,
        _liquidationFeeUsd: uint_e18,
        _fundingRateFactor: uint_e18,
        _stableFundingRateFactor: uint_e18,
    ) -> None:
        self._call(
            "initialize",
            _router=_router,
            _usdg=_usdg,
            _priceFeed=_priceFeed,
            _liquidationFeeUsd=_liquidationFeeUsd,
            _fundingRateFactor=_fundingRateFactor,
            _stableFundingRateFactor=_stableFundingRateFactor
        )
        
    def isInitialized(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isInitialized"
        )
        return bool(my_var_0)
        
    def isLeverageEnabled(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isLeverageEnabled"
        )
        return bool(my_var_0)
        
    def isLiquidator(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isLiquidator",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def isManager(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isManager",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def isSwapEnabled(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isSwapEnabled"
        )
        return bool(my_var_0)
        
    def lastFundingTimes(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "lastFundingTimes",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def liquidatePosition(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
        _feeReceiver: Address,
    ) -> None:
        self._call(
            "liquidatePosition",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong,
            _feeReceiver=_feeReceiver
        )
        
    def liquidationFeeUsd(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "liquidationFeeUsd"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def marginFeeBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "marginFeeBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxGasPrice(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxGasPrice"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxLeverage(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxLeverage"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxUsdgAmounts(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxUsdgAmounts",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def minProfitBasisPoints(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minProfitBasisPoints",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def minProfitTime(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minProfitTime"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def mintBurnFeeBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "mintBurnFeeBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def poolAmounts(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "poolAmounts",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def positions(
        self,
        x_0: bytes32,
    ) -> tuple[uint_e18, uint_e18, uint_e18, uint_e18, uint_e18, int_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6 = self._call(
            "positions",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4), int_e18.from_tuple(my_var_5), uint_e18.from_tuple(my_var_6)
        
    def priceFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "priceFeed"
        )
        return Address.from_tuple(my_var_0)
        
    def removeRouter(
        self,
        _router: Address,
    ) -> None:
        self._call(
            "removeRouter",
            _router=_router
        )
        
    def reservedAmounts(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "reservedAmounts",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def router(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "router"
        )
        return Address.from_tuple(my_var_0)
        
    def sellUSDG(
        self,
        _token: Address,
        _receiver: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "sellUSDG",
            _token=_token,
            _receiver=_receiver
        )
        return uint_e18.from_tuple(my_var_0)
        
    def setBufferAmount(
        self,
        _token: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "setBufferAmount",
            _token=_token,
            _amount=_amount
        )
        
    def setError(
        self,
        _errorCode: uint_e18,
        _error: BaseStr,
    ) -> None:
        self._call(
            "setError",
            _errorCode=_errorCode,
            _error=_error
        )
        
    def setErrorController(
        self,
        _errorController: Address,
    ) -> None:
        self._call(
            "setErrorController",
            _errorController=_errorController
        )
        
    def setFees(
        self,
        _taxBasisPoints: uint_e18,
        _stableTaxBasisPoints: uint_e18,
        _mintBurnFeeBasisPoints: uint_e18,
        _swapFeeBasisPoints: uint_e18,
        _stableSwapFeeBasisPoints: uint_e18,
        _marginFeeBasisPoints: uint_e18,
        _liquidationFeeUsd: uint_e18,
        _minProfitTime: uint_e18,
        _hasDynamicFees: bool,
    ) -> None:
        self._call(
            "setFees",
            _taxBasisPoints=_taxBasisPoints,
            _stableTaxBasisPoints=_stableTaxBasisPoints,
            _mintBurnFeeBasisPoints=_mintBurnFeeBasisPoints,
            _swapFeeBasisPoints=_swapFeeBasisPoints,
            _stableSwapFeeBasisPoints=_stableSwapFeeBasisPoints,
            _marginFeeBasisPoints=_marginFeeBasisPoints,
            _liquidationFeeUsd=_liquidationFeeUsd,
            _minProfitTime=_minProfitTime,
            _hasDynamicFees=_hasDynamicFees
        )
        
    def setFundingRate(
        self,
        _fundingInterval: uint_e18,
        _fundingRateFactor: uint_e18,
        _stableFundingRateFactor: uint_e18,
    ) -> None:
        self._call(
            "setFundingRate",
            _fundingInterval=_fundingInterval,
            _fundingRateFactor=_fundingRateFactor,
            _stableFundingRateFactor=_stableFundingRateFactor
        )
        
    def setGov(
        self,
        _gov: Address,
    ) -> None:
        self._call(
            "setGov",
            _gov=_gov
        )
        
    def setInManagerMode(
        self,
        _inManagerMode: bool,
    ) -> None:
        self._call(
            "setInManagerMode",
            _inManagerMode=_inManagerMode
        )
        
    def setInPrivateLiquidationMode(
        self,
        _inPrivateLiquidationMode: bool,
    ) -> None:
        self._call(
            "setInPrivateLiquidationMode",
            _inPrivateLiquidationMode=_inPrivateLiquidationMode
        )
        
    def setIsLeverageEnabled(
        self,
        _isLeverageEnabled: bool,
    ) -> None:
        self._call(
            "setIsLeverageEnabled",
            _isLeverageEnabled=_isLeverageEnabled
        )
        
    def setIsSwapEnabled(
        self,
        _isSwapEnabled: bool,
    ) -> None:
        self._call(
            "setIsSwapEnabled",
            _isSwapEnabled=_isSwapEnabled
        )
        
    def setLiquidator(
        self,
        _liquidator: Address,
        _isActive: bool,
    ) -> None:
        self._call(
            "setLiquidator",
            _liquidator=_liquidator,
            _isActive=_isActive
        )
        
    def setManager(
        self,
        _manager: Address,
        _isManager: bool,
    ) -> None:
        self._call(
            "setManager",
            _manager=_manager,
            _isManager=_isManager
        )
        
    def setMaxGasPrice(
        self,
        _maxGasPrice: uint_e18,
    ) -> None:
        self._call(
            "setMaxGasPrice",
            _maxGasPrice=_maxGasPrice
        )
        
    def setMaxLeverage(
        self,
        _maxLeverage: uint_e18,
    ) -> None:
        self._call(
            "setMaxLeverage",
            _maxLeverage=_maxLeverage
        )
        
    def setPriceFeed(
        self,
        _priceFeed: Address,
    ) -> None:
        self._call(
            "setPriceFeed",
            _priceFeed=_priceFeed
        )
        
    def setTokenConfig(
        self,
        _token: Address,
        _tokenDecimals: uint_e18,
        _tokenWeight: uint_e18,
        _minProfitBps: uint_e18,
        _maxUsdgAmount: uint_e18,
        _isStable: bool,
        _isShortable: bool,
    ) -> None:
        self._call(
            "setTokenConfig",
            _token=_token,
            _tokenDecimals=_tokenDecimals,
            _tokenWeight=_tokenWeight,
            _minProfitBps=_minProfitBps,
            _maxUsdgAmount=_maxUsdgAmount,
            _isStable=_isStable,
            _isShortable=_isShortable
        )
        
    def setUsdgAmount(
        self,
        _token: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "setUsdgAmount",
            _token=_token,
            _amount=_amount
        )
        
    def shortableTokens(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "shortableTokens",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def stableFundingRateFactor(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "stableFundingRateFactor"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def stableSwapFeeBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "stableSwapFeeBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def stableTaxBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "stableTaxBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def stableTokens(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "stableTokens",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def swap(
        self,
        _tokenIn: Address,
        _tokenOut: Address,
        _receiver: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "swap",
            _tokenIn=_tokenIn,
            _tokenOut=_tokenOut,
            _receiver=_receiver
        )
        return uint_e18.from_tuple(my_var_0)
        
    def swapFeeBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "swapFeeBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def taxBasisPoints(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "taxBasisPoints"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def tokenBalances(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "tokenBalances",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def tokenDecimals(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "tokenDecimals",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def tokenToUsdMin(
        self,
        _token: Address,
        _tokenAmount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "tokenToUsdMin",
            _token=_token,
            _tokenAmount=_tokenAmount
        )
        return uint_e18.from_tuple(my_var_0)
        
    def tokenWeights(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "tokenWeights",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def totalTokenWeights(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "totalTokenWeights"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def updateCumulativeFundingRate(
        self,
        _token: Address,
    ) -> None:
        self._call(
            "updateCumulativeFundingRate",
            _token=_token
        )
        
    def upgradeVault(
        self,
        _newVault: Address,
        _token: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "upgradeVault",
            _newVault=_newVault,
            _token=_token,
            _amount=_amount
        )
        
    def usdToToken(
        self,
        _token: Address,
        _usdAmount: uint_e18,
        _price: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "usdToToken",
            _token=_token,
            _usdAmount=_usdAmount,
            _price=_price
        )
        return uint_e18.from_tuple(my_var_0)
        
    def usdToTokenMax(
        self,
        _token: Address,
        _usdAmount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "usdToTokenMax",
            _token=_token,
            _usdAmount=_usdAmount
        )
        return uint_e18.from_tuple(my_var_0)
        
    def usdToTokenMin(
        self,
        _token: Address,
        _usdAmount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "usdToTokenMin",
            _token=_token,
            _usdAmount=_usdAmount
        )
        return uint_e18.from_tuple(my_var_0)
        
    def usdg(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "usdg"
        )
        return Address.from_tuple(my_var_0)
        
    def usdgAmounts(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "usdgAmounts",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def useSwapPricing(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "useSwapPricing"
        )
        return bool(my_var_0)
        
    def validateLiquidation(
        self,
        _account: Address,
        _collateralToken: Address,
        _indexToken: Address,
        _isLong: bool,
        _raise: bool,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "validateLiquidation",
            _account=_account,
            _collateralToken=_collateralToken,
            _indexToken=_indexToken,
            _isLong=_isLong,
            _raise=_raise
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def whitelistedTokenCount(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "whitelistedTokenCount"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def whitelistedTokens(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "whitelistedTokens",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def withdrawFees(
        self,
        _token: Address,
        _receiver: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdrawFees",
            _token=_token,
            _receiver=_receiver
        )
        return uint_e18.from_tuple(my_var_0)
    
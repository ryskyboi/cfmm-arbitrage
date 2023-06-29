
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class gmxpositionrouter(BaseAbi):
    address: Address = Address("0xb87a436b93ffe9d75c5cfa7bacfff96430b09868")
    
    def BASIS_POINTS_DIVISOR(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "BASIS_POINTS_DIVISOR"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def admin(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "admin"
        )
        return Address.from_tuple(my_var_0)
        
    def approve(
        self,
        _token: Address,
        _spender: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "approve",
            _token=_token,
            _spender=_spender,
            _amount=_amount
        )
        
    def callbackGasLimit(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "callbackGasLimit"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def cancelDecreasePosition(
        self,
        _key: bytes32,
        _executionFeeReceiver: Address,
    ) -> bool:
        my_var_0 = self._call(
            "cancelDecreasePosition",
            _key=_key,
            _executionFeeReceiver=_executionFeeReceiver
        )
        return bool(my_var_0)
        
    def cancelIncreasePosition(
        self,
        _key: bytes32,
        _executionFeeReceiver: Address,
    ) -> bool:
        my_var_0 = self._call(
            "cancelIncreasePosition",
            _key=_key,
            _executionFeeReceiver=_executionFeeReceiver
        )
        return bool(my_var_0)
        
    def createDecreasePosition(
        self,
        _path: list[Address],
        _indexToken: Address,
        _collateralDelta: uint_e18,
        _sizeDelta: uint_e18,
        _isLong: bool,
        _receiver: Address,
        _acceptablePrice: uint_e18,
        _minOut: uint_e18,
        _executionFee: uint_e18,
        _withdrawETH: bool,
        _callbackTarget: Address,
    ) -> bytes32:
        my_var_0 = self._call(
            "createDecreasePosition",
            _path=_path,
            _indexToken=_indexToken,
            _collateralDelta=_collateralDelta,
            _sizeDelta=_sizeDelta,
            _isLong=_isLong,
            _receiver=_receiver,
            _acceptablePrice=_acceptablePrice,
            _minOut=_minOut,
            _executionFee=_executionFee,
            _withdrawETH=_withdrawETH,
            _callbackTarget=_callbackTarget
        )
        return bytes32.from_tuple(my_var_0)
        
    def createIncreasePosition(
        self,
        _path: list[Address],
        _indexToken: Address,
        _amountIn: uint_e18,
        _minOut: uint_e18,
        _sizeDelta: uint_e18,
        _isLong: bool,
        _acceptablePrice: uint_e18,
        _executionFee: uint_e18,
        _referralCode: bytes32,
        _callbackTarget: Address,
    ) -> bytes32:
        my_var_0 = self._call(
            "createIncreasePosition",
            _path=_path,
            _indexToken=_indexToken,
            _amountIn=_amountIn,
            _minOut=_minOut,
            _sizeDelta=_sizeDelta,
            _isLong=_isLong,
            _acceptablePrice=_acceptablePrice,
            _executionFee=_executionFee,
            _referralCode=_referralCode,
            _callbackTarget=_callbackTarget
        )
        return bytes32.from_tuple(my_var_0)
        
    def createIncreasePositionETH(
        self,
        _path: list[Address],
        _indexToken: Address,
        _minOut: uint_e18,
        _sizeDelta: uint_e18,
        _isLong: bool,
        _acceptablePrice: uint_e18,
        _executionFee: uint_e18,
        _referralCode: bytes32,
        _callbackTarget: Address,
    ) -> bytes32:
        my_var_0 = self._call(
            "createIncreasePositionETH",
            _path=_path,
            _indexToken=_indexToken,
            _minOut=_minOut,
            _sizeDelta=_sizeDelta,
            _isLong=_isLong,
            _acceptablePrice=_acceptablePrice,
            _executionFee=_executionFee,
            _referralCode=_referralCode,
            _callbackTarget=_callbackTarget
        )
        return bytes32.from_tuple(my_var_0)
        
    def decreasePositionRequestKeys(
        self,
        x_0: uint_e18,
    ) -> bytes32:
        my_var_0 = self._call(
            "decreasePositionRequestKeys",
            x_0=x_0
        )
        return bytes32.from_tuple(my_var_0)
        
    def decreasePositionRequestKeysStart(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "decreasePositionRequestKeysStart"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def decreasePositionRequests(
        self,
        x_0: bytes32,
    ) -> tuple[Address, Address, uint_e18, uint_e18, bool, Address, uint_e18, uint_e18, uint_e18, uint_e18, uint_e18, bool, Address]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6, my_var_7, my_var_8, my_var_9, my_var_10, my_var_11, my_var_12 = self._call(
            "decreasePositionRequests",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0), Address.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), bool(my_var_4), Address.from_tuple(my_var_5), uint_e18.from_tuple(my_var_6), uint_e18.from_tuple(my_var_7), uint_e18.from_tuple(my_var_8), uint_e18.from_tuple(my_var_9), uint_e18.from_tuple(my_var_10), bool(my_var_11), Address.from_tuple(my_var_12)
        
    def decreasePositionsIndex(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "decreasePositionsIndex",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def depositFee(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "depositFee"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def executeDecreasePosition(
        self,
        _key: bytes32,
        _executionFeeReceiver: Address,
    ) -> bool:
        my_var_0 = self._call(
            "executeDecreasePosition",
            _key=_key,
            _executionFeeReceiver=_executionFeeReceiver
        )
        return bool(my_var_0)
        
    def executeDecreasePositions(
        self,
        _endIndex: uint_e18,
        _executionFeeReceiver: Address,
    ) -> None:
        self._call(
            "executeDecreasePositions",
            _endIndex=_endIndex,
            _executionFeeReceiver=_executionFeeReceiver
        )
        
    def executeIncreasePosition(
        self,
        _key: bytes32,
        _executionFeeReceiver: Address,
    ) -> bool:
        my_var_0 = self._call(
            "executeIncreasePosition",
            _key=_key,
            _executionFeeReceiver=_executionFeeReceiver
        )
        return bool(my_var_0)
        
    def executeIncreasePositions(
        self,
        _endIndex: uint_e18,
        _executionFeeReceiver: Address,
    ) -> None:
        self._call(
            "executeIncreasePositions",
            _endIndex=_endIndex,
            _executionFeeReceiver=_executionFeeReceiver
        )
        
    def feeReserves(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "feeReserves",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getDecreasePositionRequestPath(
        self,
        _key: bytes32,
    ) -> list[Address]:
        my_var_0 = self._call(
            "getDecreasePositionRequestPath",
            _key=_key
        )
        return [Address.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getIncreasePositionRequestPath(
        self,
        _key: bytes32,
    ) -> list[Address]:
        my_var_0 = self._call(
            "getIncreasePositionRequestPath",
            _key=_key
        )
        return [Address.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getRequestKey(
        self,
        _account: Address,
        _index: uint_e18,
    ) -> bytes32:
        my_var_0 = self._call(
            "getRequestKey",
            _account=_account,
            _index=_index
        )
        return bytes32.from_tuple(my_var_0)
        
    def getRequestQueueLengths(
        self,
    ) -> tuple[uint_e18, uint_e18, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3 = self._call(
            "getRequestQueueLengths"
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3)
        
    def gov(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "gov"
        )
        return Address.from_tuple(my_var_0)
        
    def increasePositionBufferBps(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "increasePositionBufferBps"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def increasePositionRequestKeys(
        self,
        x_0: uint_e18,
    ) -> bytes32:
        my_var_0 = self._call(
            "increasePositionRequestKeys",
            x_0=x_0
        )
        return bytes32.from_tuple(my_var_0)
        
    def increasePositionRequestKeysStart(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "increasePositionRequestKeysStart"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def increasePositionRequests(
        self,
        x_0: bytes32,
    ) -> tuple[Address, Address, uint_e18, uint_e18, uint_e18, bool, uint_e18, uint_e18, uint_e18, uint_e18, bool, Address]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6, my_var_7, my_var_8, my_var_9, my_var_10, my_var_11 = self._call(
            "increasePositionRequests",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0), Address.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4), bool(my_var_5), uint_e18.from_tuple(my_var_6), uint_e18.from_tuple(my_var_7), uint_e18.from_tuple(my_var_8), uint_e18.from_tuple(my_var_9), bool(my_var_10), Address.from_tuple(my_var_11)
        
    def increasePositionsIndex(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "increasePositionsIndex",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def isLeverageEnabled(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isLeverageEnabled"
        )
        return bool(my_var_0)
        
    def isPositionKeeper(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "isPositionKeeper",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def maxGlobalLongSizes(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxGlobalLongSizes",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxGlobalShortSizes(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxGlobalShortSizes",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxTimeDelay(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxTimeDelay"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def minBlockDelayKeeper(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minBlockDelayKeeper"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def minExecutionFee(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minExecutionFee"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def minTimeDelayPublic(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "minTimeDelayPublic"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def referralStorage(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "referralStorage"
        )
        return Address.from_tuple(my_var_0)
        
    def router(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "router"
        )
        return Address.from_tuple(my_var_0)
        
    def sendValue(
        self,
        _receiver: Address,
        _amount: uint_e18,
    ) -> None:
        self._call(
            "sendValue",
            _receiver=_receiver,
            _amount=_amount
        )
        
    def setAdmin(
        self,
        _admin: Address,
    ) -> None:
        self._call(
            "setAdmin",
            _admin=_admin
        )
        
    def setCallbackGasLimit(
        self,
        _callbackGasLimit: uint_e18,
    ) -> None:
        self._call(
            "setCallbackGasLimit",
            _callbackGasLimit=_callbackGasLimit
        )
        
    def setDelayValues(
        self,
        _minBlockDelayKeeper: uint_e18,
        _minTimeDelayPublic: uint_e18,
        _maxTimeDelay: uint_e18,
    ) -> None:
        self._call(
            "setDelayValues",
            _minBlockDelayKeeper=_minBlockDelayKeeper,
            _minTimeDelayPublic=_minTimeDelayPublic,
            _maxTimeDelay=_maxTimeDelay
        )
        
    def setDepositFee(
        self,
        _depositFee: uint_e18,
    ) -> None:
        self._call(
            "setDepositFee",
            _depositFee=_depositFee
        )
        
    def setGov(
        self,
        _gov: Address,
    ) -> None:
        self._call(
            "setGov",
            _gov=_gov
        )
        
    def setIncreasePositionBufferBps(
        self,
        _increasePositionBufferBps: uint_e18,
    ) -> None:
        self._call(
            "setIncreasePositionBufferBps",
            _increasePositionBufferBps=_increasePositionBufferBps
        )
        
    def setIsLeverageEnabled(
        self,
        _isLeverageEnabled: bool,
    ) -> None:
        self._call(
            "setIsLeverageEnabled",
            _isLeverageEnabled=_isLeverageEnabled
        )
        
    def setMaxGlobalSizes(
        self,
        _tokens: list[Address],
        _longSizes: list[uint_e18],
        _shortSizes: list[uint_e18],
    ) -> None:
        self._call(
            "setMaxGlobalSizes",
            _tokens=_tokens,
            _longSizes=_longSizes,
            _shortSizes=_shortSizes
        )
        
    def setMinExecutionFee(
        self,
        _minExecutionFee: uint_e18,
    ) -> None:
        self._call(
            "setMinExecutionFee",
            _minExecutionFee=_minExecutionFee
        )
        
    def setPositionKeeper(
        self,
        _account: Address,
        _isActive: bool,
    ) -> None:
        self._call(
            "setPositionKeeper",
            _account=_account,
            _isActive=_isActive
        )
        
    def setReferralStorage(
        self,
        _referralStorage: Address,
    ) -> None:
        self._call(
            "setReferralStorage",
            _referralStorage=_referralStorage
        )
        
    def setRequestKeysStartValues(
        self,
        _increasePositionRequestKeysStart: uint_e18,
        _decreasePositionRequestKeysStart: uint_e18,
    ) -> None:
        self._call(
            "setRequestKeysStartValues",
            _increasePositionRequestKeysStart=_increasePositionRequestKeysStart,
            _decreasePositionRequestKeysStart=_decreasePositionRequestKeysStart
        )
        
    def shortsTracker(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "shortsTracker"
        )
        return Address.from_tuple(my_var_0)
        
    def vault(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "vault"
        )
        return Address.from_tuple(my_var_0)
        
    def weth(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "weth"
        )
        return Address.from_tuple(my_var_0)
        
    def withdrawFees(
        self,
        _token: Address,
        _receiver: Address,
    ) -> None:
        self._call(
            "withdrawFees",
            _token=_token,
            _receiver=_receiver
        )
    
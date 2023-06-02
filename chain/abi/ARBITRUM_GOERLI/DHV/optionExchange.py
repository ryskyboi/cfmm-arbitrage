
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

@dataclass
class CombinedActions_ActionArgs:
    actionType: uint_e18
    owner: Address
    secondAddress: Address
    asset: Address
    vaultId: uint_e18
    amount: uint_e18
    optionSeries: Types_OptionSeries
    indexOrAcceptablePremium: uint_e18
    data: bytes

@dataclass
class CombinedActions_OperationProcedures:
    operation: uint8
    operationQueue: list[CombinedActions_ActionArgs]

class optionExchange(BaseAbi):
    address: Address = Address("0xb672fE86693bF6f3b034730f5d2C77C8844d6b45")
    
    def addressbook(
        self,
    ) -> Address:
        return self._call(
            "addressbook"
        )
        
    def approvedCollateral(
        self,
        x_0: Address,
        x_1: bool,
    ) -> bool:
        return self._call(
            "approvedCollateral",
            x_0=x_0,
            x_1=x_1
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def catalogue(
        self,
    ) -> Address:
        return self._call(
            "catalogue"
        )
        
    def changeApprovedCollateral(
        self,
        collateral: Address,
        isPut: bool,
        isApproved: bool,
    ) -> None:
        self._call(
            "changeApprovedCollateral",
            collateral=collateral,
            isPut=isPut,
            isApproved=isApproved
        )
        
    def checkHash(
        self,
        optionSeries: Types_OptionSeries,
        strikeDecimalConverted: uint128,
        isSell: bool,
    ) -> bytes32:
        return self._call(
            "checkHash",
            optionSeries=optionSeries,
            strikeDecimalConverted=strikeDecimalConverted,
            isSell=isSell
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def createOtoken(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        return self._call(
            "createOtoken",
            optionSeries=optionSeries
        )
        
    def feeRecipient(
        self,
    ) -> Address:
        return self._call(
            "feeRecipient"
        )
        
    def getDelta(
        self,
    ) -> int_e18:
        return self._call(
            "getDelta"
        )
        
    def getOptionDetails(
        self,
        seriesAddress: Address,
        optionSeries: Types_OptionSeries,
    ) -> tuple[Address, Types_OptionSeries, uint128]:
        return self._call(
            "getOptionDetails",
            seriesAddress=seriesAddress,
            optionSeries=optionSeries
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
        
    def heldTokens(
        self,
        x_0: Address,
        x_1: Address,
    ) -> uint_e18:
        return self._call(
            "heldTokens",
            x_0=x_0,
            x_1=x_1
        )
        
    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )
        
    def maxTradeSize(
        self,
    ) -> uint_e18:
        return self._call(
            "maxTradeSize"
        )
        
    def migrateOtokens(
        self,
        newOptionExchange: Address,
        otokens: list[Address],
    ) -> None:
        self._call(
            "migrateOtokens",
            newOptionExchange=newOptionExchange,
            otokens=otokens
        )
        
    def minTradeSize(
        self,
    ) -> uint_e18:
        return self._call(
            "minTradeSize"
        )
        
    def operate(
        self,
        _operationProcedures: list[CombinedActions_OperationProcedures],
    ) -> None:
        self._call(
            "operate",
            _operationProcedures=_operationProcedures
        )
        
    def pause(
        self,
    ) -> None:
        self._call(
            "pause"
        )
        
    def paused(
        self,
    ) -> bool:
        return self._call(
            "paused"
        )
        
    def poolFees(
        self,
        x_0: Address,
    ) -> uint24:
        return self._call(
            "poolFees",
            x_0=x_0
        )
        
    def pricer(
        self,
    ) -> Address:
        return self._call(
            "pricer"
        )
        
    def protocol(
        self,
    ) -> Address:
        return self._call(
            "protocol"
        )
        
    def redeem(
        self,
        _series: list[Address],
        amountOutMinimums: list[uint_e18],
    ) -> None:
        self._call(
            "redeem",
            _series=_series,
            amountOutMinimums=amountOutMinimums
        )
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setFeeRecipient(
        self,
        _feeRecipient: Address,
    ) -> None:
        self._call(
            "setFeeRecipient",
            _feeRecipient=_feeRecipient
        )
        
    def setOptionCatalogue(
        self,
        _catalogue: Address,
    ) -> None:
        self._call(
            "setOptionCatalogue",
            _catalogue=_catalogue
        )
        
    def setPoolFee(
        self,
        asset: Address,
        fee: uint24,
    ) -> None:
        self._call(
            "setPoolFee",
            asset=asset,
            fee=fee
        )
        
    def setPricer(
        self,
        _pricer: Address,
    ) -> None:
        self._call(
            "setPricer",
            _pricer=_pricer
        )
        
    def setTradeSizeLimits(
        self,
        _minTradeSize: uint_e18,
        _maxTradeSize: uint_e18,
    ) -> None:
        self._call(
            "setTradeSizeLimits",
            _minTradeSize=_minTradeSize,
            _maxTradeSize=_maxTradeSize
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        return self._call(
            "strikeAsset"
        )
        
    def swapRouter(
        self,
    ) -> Address:
        return self._call(
            "swapRouter"
        )
        
    def underlyingAsset(
        self,
    ) -> Address:
        return self._call(
            "underlyingAsset"
        )
        
    def unpause(
        self,
    ) -> None:
        self._call(
            "unpause"
        )
        
    def update(
        self,
    ) -> uint_e18:
        return self._call(
            "update"
        )
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        return self._call(
            "withdraw",
            _amount=_amount
        )
    
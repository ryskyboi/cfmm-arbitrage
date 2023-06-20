
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



class liquidityPool(BaseAbi):
    address: Address = Address("0x0B1Bf5fb77AA36cD48Baa1395Bc2B5fa0f135d8C")
    
    def DOMAIN_SEPARATOR(
        self,
    ) -> bytes32:
        my_var_0 = self._call(
            "DOMAIN_SEPARATOR"
        )
        return bytes32.from_tuple(my_var_0)
        
    def adjustCollateral(
        self,
        lpCollateralDifference: uint_e18,
        addToLpBalance: bool,
    ) -> None:
        self._call(
            "adjustCollateral",
            lpCollateralDifference=lpCollateralDifference,
            addToLpBalance=addToLpBalance
        )
        
    def adjustVariables(
        self,
        collateralAmount: uint_e18,
        optionsValue: uint_e18,
        delta: int_e18,
        isSale: bool,
    ) -> None:
        self._call(
            "adjustVariables",
            collateralAmount=collateralAmount,
            optionsValue=optionsValue,
            delta=delta,
            isSale=isSale
        )
        
    def allowance(
        self,
        x_0: Address,
        x_1: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "allowance",
            x_0=x_0,
            x_1=x_1
        )
        return uint_e18.from_tuple(my_var_0)
        
    def approve(
        self,
        spender: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "approve",
            spender=spender,
            amount=amount
        )
        return bool(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def balanceOf(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "balanceOf",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def bufferPercentage(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "bufferPercentage"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def changeHandler(
        self,
        _handler: Address,
        auth: bool,
    ) -> None:
        self._call(
            "changeHandler",
            _handler=_handler,
            auth=auth
        )
        
    def checkBuffer(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "checkBuffer"
        )
        return int_e18.from_tuple(my_var_0)
        
    def collateralAllocated(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "collateralAllocated"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralCap(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "collateralCap"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def completeWithdraw(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "completeWithdraw"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def decimals(
        self,
    ) -> uint8:
        my_var_0 = self._call(
            "decimals"
        )
        return uint8.from_tuple(my_var_0)
        
    def deposit(
        self,
        _amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "deposit",
            _amount=_amount
        )
        return bool(my_var_0)
        
    def depositEpoch(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "depositEpoch"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def depositEpochPricePerShare(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "depositEpochPricePerShare",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def depositReceipts(
        self,
        x_0: Address,
    ) -> tuple[uint128, uint128, uint_e18]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "depositReceipts",
            x_0=x_0
        )
        return uint128.from_tuple(my_var_0), uint128.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2)
        
    def ephemeralDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "ephemeralDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def ephemeralLiabilities(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "ephemeralLiabilities"
        )
        return int_e18.from_tuple(my_var_0)
        
    def executeEpochCalculation(
        self,
    ) -> None:
        self._call(
            "executeEpochCalculation"
        )
        
    def getAssets(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getAssets"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getBalance(
        self,
        asset: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getBalance",
            asset=asset
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getExternalDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "getExternalDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def getHedgingReactors(
        self,
    ) -> list[Address]:
        my_var_0 = self._call(
            "getHedgingReactors"
        )
        return [Address.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getImpliedVolatility(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getImpliedVolatility",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getNAV(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getNAV"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPortfolioDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "getPortfolioDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def getVolatilityFeed(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "getVolatilityFeed"
        )
        return Address.from_tuple(my_var_0)
        
    def handler(
        self,
        x_0: Address,
    ) -> bool:
        my_var_0 = self._call(
            "handler",
            x_0=x_0
        )
        return bool(my_var_0)
        
    def handlerBuybackOption(
        self,
        optionSeries: Types_OptionSeries,
        amount: uint_e18,
        optionRegistry: Address,
        seriesAddress: Address,
        premium: uint_e18,
        delta: int_e18,
        seller: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "handlerBuybackOption",
            optionSeries=optionSeries,
            amount=amount,
            optionRegistry=optionRegistry,
            seriesAddress=seriesAddress,
            premium=premium,
            delta=delta,
            seller=seller
        )
        return uint_e18.from_tuple(my_var_0)
        
    def handlerIssue(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        my_var_0 = self._call(
            "handlerIssue",
            optionSeries=optionSeries
        )
        return Address.from_tuple(my_var_0)
        
    def handlerIssueAndWriteOption(
        self,
        optionSeries: Types_OptionSeries,
        amount: uint_e18,
        premium: uint_e18,
        delta: int_e18,
        recipient: Address,
    ) -> tuple[uint_e18, Address]:
        my_var_0, my_var_1 = self._call(
            "handlerIssueAndWriteOption",
            optionSeries=optionSeries,
            amount=amount,
            premium=premium,
            delta=delta,
            recipient=recipient
        )
        return uint_e18.from_tuple(my_var_0), Address.from_tuple(my_var_1)
        
    def handlerWriteOption(
        self,
        optionSeries: Types_OptionSeries,
        seriesAddress: Address,
        amount: uint_e18,
        optionRegistry: Address,
        premium: uint_e18,
        delta: int_e18,
        recipient: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "handlerWriteOption",
            optionSeries=optionSeries,
            seriesAddress=seriesAddress,
            amount=amount,
            optionRegistry=optionRegistry,
            premium=premium,
            delta=delta,
            recipient=recipient
        )
        return uint_e18.from_tuple(my_var_0)
        
    def hedgingReactors(
        self,
        x_0: uint_e18,
    ) -> Address:
        my_var_0 = self._call(
            "hedgingReactors",
            x_0=x_0
        )
        return Address.from_tuple(my_var_0)
        
    def initiateWithdraw(
        self,
        _shares: uint_e18,
    ) -> None:
        self._call(
            "initiateWithdraw",
            _shares=_shares
        )
        
    def isTradingPaused(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "isTradingPaused"
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
        
    def maxPriceDeviationThreshold(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxPriceDeviationThreshold"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def maxTimeDeviationThreshold(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxTimeDeviationThreshold"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def name(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "name"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def nonces(
        self,
        x_0: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "nonces",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def optionParams(
        self,
    ) -> tuple[uint128, uint128, uint128, uint128, uint128, uint128]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5 = self._call(
            "optionParams"
        )
        return uint128.from_tuple(my_var_0), uint128.from_tuple(my_var_1), uint128.from_tuple(my_var_2), uint128.from_tuple(my_var_3), uint128.from_tuple(my_var_4), uint128.from_tuple(my_var_5)
        
    def partitionedFunds(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "partitionedFunds"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def pause(
        self,
    ) -> None:
        self._call(
            "pause"
        )
        
    def pauseTradingAndRequest(
        self,
    ) -> bytes32:
        my_var_0 = self._call(
            "pauseTradingAndRequest"
        )
        return bytes32.from_tuple(my_var_0)
        
    def pauseUnpauseTrading(
        self,
        _pause: bool,
    ) -> None:
        self._call(
            "pauseUnpauseTrading",
            _pause=_pause
        )
        
    def paused(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "paused"
        )
        return bool(my_var_0)
        
    def pendingDeposits(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "pendingDeposits"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def pendingWithdrawals(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "pendingWithdrawals"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def permit(
        self,
        owner: Address,
        spender: Address,
        value: uint_e18,
        deadline: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "permit",
            owner=owner,
            spender=spender,
            value=value,
            deadline=deadline,
            v=v,
            r=r,
            s=s
        )
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def rebalancePortfolioDelta(
        self,
        delta: int_e18,
        reactorIndex: uint_e18,
    ) -> None:
        self._call(
            "rebalancePortfolioDelta",
            delta=delta,
            reactorIndex=reactorIndex
        )
        
    def redeem(
        self,
        _shares: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "redeem",
            _shares=_shares
        )
        return uint_e18.from_tuple(my_var_0)
        
    def removeHedgingReactorAddress(
        self,
        _index: uint_e18,
        _override: bool,
    ) -> None:
        self._call(
            "removeHedgingReactorAddress",
            _index=_index,
            _override=_override
        )
        
    def resetEphemeralValues(
        self,
    ) -> None:
        self._call(
            "resetEphemeralValues"
        )
        
    def riskFreeRate(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "riskFreeRate"
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
        
    def setBufferPercentage(
        self,
        _bufferPercentage: uint_e18,
    ) -> None:
        self._call(
            "setBufferPercentage",
            _bufferPercentage=_bufferPercentage
        )
        
    def setCollateralCap(
        self,
        _collateralCap: uint_e18,
    ) -> None:
        self._call(
            "setCollateralCap",
            _collateralCap=_collateralCap
        )
        
    def setHedgingReactorAddress(
        self,
        _reactorAddress: Address,
    ) -> None:
        self._call(
            "setHedgingReactorAddress",
            _reactorAddress=_reactorAddress
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
        
    def setMaxPriceDeviationThreshold(
        self,
        _maxPriceDeviationThreshold: uint_e18,
    ) -> None:
        self._call(
            "setMaxPriceDeviationThreshold",
            _maxPriceDeviationThreshold=_maxPriceDeviationThreshold
        )
        
    def setMaxTimeDeviationThreshold(
        self,
        _maxTimeDeviationThreshold: uint_e18,
    ) -> None:
        self._call(
            "setMaxTimeDeviationThreshold",
            _maxTimeDeviationThreshold=_maxTimeDeviationThreshold
        )
        
    def setNewOptionParams(
        self,
        _newMinCallStrike: uint128,
        _newMaxCallStrike: uint128,
        _newMinPutStrike: uint128,
        _newMaxPutStrike: uint128,
        _newMinExpiry: uint128,
        _newMaxExpiry: uint128,
    ) -> None:
        self._call(
            "setNewOptionParams",
            _newMinCallStrike=_newMinCallStrike,
            _newMaxCallStrike=_newMaxCallStrike,
            _newMinPutStrike=_newMinPutStrike,
            _newMaxPutStrike=_newMaxPutStrike,
            _newMinExpiry=_newMinExpiry,
            _newMaxExpiry=_newMaxExpiry
        )
        
    def setRiskFreeRate(
        self,
        _riskFreeRate: uint_e18,
    ) -> None:
        self._call(
            "setRiskFreeRate",
            _riskFreeRate=_riskFreeRate
        )
        
    def settleVault(
        self,
        seriesAddress: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "settleVault",
            seriesAddress=seriesAddress
        )
        return uint_e18.from_tuple(my_var_0)
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def symbol(
        self,
    ) -> BaseStr:
        my_var_0 = self._call(
            "symbol"
        )
        return BaseStr.from_tuple(my_var_0)
        
    def totalSupply(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "totalSupply"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def transfer(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transfer",
            to_=to_,
            amount=amount
        )
        return bool(my_var_0)
        
    def transferFrom(
        self,
        from_: Address,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        my_var_0 = self._call(
            "transferFrom",
            from_=from_,
            to_=to_,
            amount=amount
        )
        return bool(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def unpause(
        self,
    ) -> None:
        self._call(
            "unpause"
        )
        
    def withdrawalEpoch(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdrawalEpoch"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def withdrawalEpochPricePerShare(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdrawalEpochPricePerShare",
            x_0=x_0
        )
        return uint_e18.from_tuple(my_var_0)
        
    def withdrawalReceipts(
        self,
        x_0: Address,
    ) -> tuple[uint128, uint128]:
        my_var_0, my_var_1 = self._call(
            "withdrawalReceipts",
            x_0=x_0
        )
        return uint128.from_tuple(my_var_0), uint128.from_tuple(my_var_1)
    
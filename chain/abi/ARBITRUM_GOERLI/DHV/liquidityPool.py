
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

class liquidityPool(BaseAbi):
    address: Address = Address("0x0B1Bf5fb77AA36cD48Baa1395Bc2B5fa0f135d8C")
    
    def DOMAIN_SEPARATOR(
        self,
    ) -> bytes32:
        return self._call(
            "DOMAIN_SEPARATOR"
        )
        
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
        return self._call(
            "allowance",
            x_0=x_0,
            x_1=x_1
        )
        
    def approve(
        self,
        spender: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "approve",
            spender=spender,
            amount=amount
        )
        
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def balanceOf(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "balanceOf",
            x_0=x_0
        )
        
    def bufferPercentage(
        self,
    ) -> uint_e18:
        return self._call(
            "bufferPercentage"
        )
        
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
        return self._call(
            "checkBuffer"
        )
        
    def collateralAllocated(
        self,
    ) -> uint_e18:
        return self._call(
            "collateralAllocated"
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
    def collateralCap(
        self,
    ) -> uint_e18:
        return self._call(
            "collateralCap"
        )
        
    def completeWithdraw(
        self,
    ) -> uint_e18:
        return self._call(
            "completeWithdraw"
        )
        
    def decimals(
        self,
    ) -> uint8:
        return self._call(
            "decimals"
        )
        
    def deposit(
        self,
        _amount: uint_e18,
    ) -> bool:
        return self._call(
            "deposit",
            _amount=_amount
        )
        
    def depositEpoch(
        self,
    ) -> uint_e18:
        return self._call(
            "depositEpoch"
        )
        
    def depositEpochPricePerShare(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        return self._call(
            "depositEpochPricePerShare",
            x_0=x_0
        )
        
    def depositReceipts(
        self,
        x_0: Address,
    ) -> tuple[uint128, uint128, uint_e18]:
        return self._call(
            "depositReceipts",
            x_0=x_0
        )
        
    def ephemeralDelta(
        self,
    ) -> int_e18:
        return self._call(
            "ephemeralDelta"
        )
        
    def ephemeralLiabilities(
        self,
    ) -> int_e18:
        return self._call(
            "ephemeralLiabilities"
        )
        
    def executeEpochCalculation(
        self,
    ) -> None:
        self._call(
            "executeEpochCalculation"
        )
        
    def getAssets(
        self,
    ) -> uint_e18:
        return self._call(
            "getAssets"
        )
        
    def getBalance(
        self,
        asset: Address,
    ) -> uint_e18:
        return self._call(
            "getBalance",
            asset=asset
        )
        
    def getExternalDelta(
        self,
    ) -> int_e18:
        return self._call(
            "getExternalDelta"
        )
        
    def getHedgingReactors(
        self,
    ) -> list[Address]:
        return self._call(
            "getHedgingReactors"
        )
        
    def getImpliedVolatility(
        self,
        isPut: bool,
        underlyingPrice: uint_e18,
        strikePrice: uint_e18,
        expiration: uint_e18,
    ) -> uint_e18:
        return self._call(
            "getImpliedVolatility",
            isPut=isPut,
            underlyingPrice=underlyingPrice,
            strikePrice=strikePrice,
            expiration=expiration
        )
        
    def getNAV(
        self,
    ) -> uint_e18:
        return self._call(
            "getNAV"
        )
        
    def getPortfolioDelta(
        self,
    ) -> int_e18:
        return self._call(
            "getPortfolioDelta"
        )
        
    def getVolatilityFeed(
        self,
    ) -> Address:
        return self._call(
            "getVolatilityFeed"
        )
        
    def handler(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "handler",
            x_0=x_0
        )
        
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
        return self._call(
            "handlerBuybackOption",
            optionSeries=optionSeries,
            amount=amount,
            optionRegistry=optionRegistry,
            seriesAddress=seriesAddress,
            premium=premium,
            delta=delta,
            seller=seller
        )
        
    def handlerIssue(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        return self._call(
            "handlerIssue",
            optionSeries=optionSeries
        )
        
    def handlerIssueAndWriteOption(
        self,
        optionSeries: Types_OptionSeries,
        amount: uint_e18,
        premium: uint_e18,
        delta: int_e18,
        recipient: Address,
    ) -> tuple[uint_e18, Address]:
        return self._call(
            "handlerIssueAndWriteOption",
            optionSeries=optionSeries,
            amount=amount,
            premium=premium,
            delta=delta,
            recipient=recipient
        )
        
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
        return self._call(
            "handlerWriteOption",
            optionSeries=optionSeries,
            seriesAddress=seriesAddress,
            amount=amount,
            optionRegistry=optionRegistry,
            premium=premium,
            delta=delta,
            recipient=recipient
        )
        
    def hedgingReactors(
        self,
        x_0: uint_e18,
    ) -> Address:
        return self._call(
            "hedgingReactors",
            x_0=x_0
        )
        
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
        return self._call(
            "isTradingPaused"
        )
        
    def keeper(
        self,
        x_0: Address,
    ) -> bool:
        return self._call(
            "keeper",
            x_0=x_0
        )
        
    def maxPriceDeviationThreshold(
        self,
    ) -> uint_e18:
        return self._call(
            "maxPriceDeviationThreshold"
        )
        
    def maxTimeDeviationThreshold(
        self,
    ) -> uint_e18:
        return self._call(
            "maxTimeDeviationThreshold"
        )
        
    def name(
        self,
    ) -> str:
        return self._call(
            "name"
        )
        
    def nonces(
        self,
        x_0: Address,
    ) -> uint_e18:
        return self._call(
            "nonces",
            x_0=x_0
        )
        
    def optionParams(
        self,
    ) -> tuple[uint128, uint128, uint128, uint128, uint128, uint128]:
        return self._call(
            "optionParams"
        )
        
    def partitionedFunds(
        self,
    ) -> uint_e18:
        return self._call(
            "partitionedFunds"
        )
        
    def pause(
        self,
    ) -> None:
        self._call(
            "pause"
        )
        
    def pauseTradingAndRequest(
        self,
    ) -> bytes32:
        return self._call(
            "pauseTradingAndRequest"
        )
        
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
        return self._call(
            "paused"
        )
        
    def pendingDeposits(
        self,
    ) -> uint_e18:
        return self._call(
            "pendingDeposits"
        )
        
    def pendingWithdrawals(
        self,
    ) -> uint_e18:
        return self._call(
            "pendingWithdrawals"
        )
        
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
        return self._call(
            "protocol"
        )
        
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
        return self._call(
            "redeem",
            _shares=_shares
        )
        
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
        return self._call(
            "riskFreeRate"
        )
        
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
        return self._call(
            "settleVault",
            seriesAddress=seriesAddress
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        return self._call(
            "strikeAsset"
        )
        
    def symbol(
        self,
    ) -> str:
        return self._call(
            "symbol"
        )
        
    def totalSupply(
        self,
    ) -> uint_e18:
        return self._call(
            "totalSupply"
        )
        
    def transfer(
        self,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "transfer",
            to_=to_,
            amount=amount
        )
        
    def transferFrom(
        self,
        from_: Address,
        to_: Address,
        amount: uint_e18,
    ) -> bool:
        return self._call(
            "transferFrom",
            from_=from_,
            to_=to_,
            amount=amount
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
        
    def withdrawalEpoch(
        self,
    ) -> uint_e18:
        return self._call(
            "withdrawalEpoch"
        )
        
    def withdrawalEpochPricePerShare(
        self,
        x_0: uint_e18,
    ) -> uint_e18:
        return self._call(
            "withdrawalEpochPricePerShare",
            x_0=x_0
        )
        
    def withdrawalReceipts(
        self,
        x_0: Address,
    ) -> tuple[uint128, uint128]:
        return self._call(
            "withdrawalReceipts",
            x_0=x_0
        )
    
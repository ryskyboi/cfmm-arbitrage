
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass



@dataclass
class IAccounting_WithdrawalReceipt:
    epoch: uint128
    shares: uint128

@dataclass
class IAccounting_DepositReceipt:
    epoch: uint128
    amount: uint128
    unredeemedShares: uint_e18

class accounting(BaseAbi):
    address: Address = Address("0x8339B6AB2B573F0acdb43F9DD00f290A07aA8708")

    def amountForShares(
        self,
        _shares: uint_e18,
        _assetPerShare: uint_e18,
    ) -> uint_e18:
        return self._call(
            "amountForShares",
            _shares=_shares,
            _assetPerShare=_assetPerShare
        )

    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )

    def completeWithdraw(
        self,
        withdrawer: Address,
    ) -> tuple[uint_e18, uint_e18, IAccounting_WithdrawalReceipt]:
        return self._call(
            "completeWithdraw",
            withdrawer=withdrawer
        )

    def deposit(
        self,
        depositor: Address,
        _amount: uint_e18,
    ) -> tuple[uint_e18, uint_e18]:
        return self._call(
            "deposit",
            depositor=depositor,
            _amount=_amount
        )

    def executeEpochCalculation(
        self,
        totalSupply: uint_e18,
        assets: uint_e18,
        liabilities: int_e18,
    ) -> tuple[uint_e18, uint_e18, uint_e18, uint_e18, uint_e18]:
        return self._call(
            "executeEpochCalculation",
            totalSupply=totalSupply,
            assets=assets,
            liabilities=liabilities
        )

    def initiateWithdraw(
        self,
        withdrawer: Address,
        shares: uint_e18,
    ) -> IAccounting_WithdrawalReceipt:
        return self._call(
            "initiateWithdraw",
            withdrawer=withdrawer,
            shares=shares
        )

    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )

    def redeem(
        self,
        redeemer: Address,
        shares: uint_e18,
    ) -> tuple[uint_e18, IAccounting_DepositReceipt]:
        return self._call(
            "redeem",
            redeemer=redeemer,
            shares=shares
        )

    def sharesForAmount(
        self,
        _amount: uint_e18,
        assetPerShare: uint_e18,
    ) -> uint_e18:
        return self._call(
            "sharesForAmount",
            _amount=_amount,
            assetPerShare=assetPerShare
        )

    def strikeAsset(
        self,
    ) -> Address:
        return self._call(
            "strikeAsset"
        )

    def underlyingAsset(
        self,
    ) -> Address:
        return self._call(
            "underlyingAsset"
        )

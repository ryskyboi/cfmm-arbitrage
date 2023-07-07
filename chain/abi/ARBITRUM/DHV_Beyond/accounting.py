
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class IAccounting_WithdrawalReceipt:
    epoch: uint128
    shares: uint128

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint128.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
        )



@dataclass
class IAccounting_DepositReceipt:
    epoch: uint128
    amount: uint128
    unredeemedShares: uint_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint128.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            uint_e18.from_tuple(args[2]),
        )


class accounting(BaseAbi):
    address: Address = Address("0x48672a2885995cF3Ddc9Da633C22b262e0533f7C")
    
    def amountForShares(
        self,
        _shares: uint_e18,
        _assetPerShare: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "amountForShares",
            _shares=_shares,
            _assetPerShare=_assetPerShare
        )
        return uint_e18.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def completeWithdraw(
        self,
        withdrawer: Address,
    ) -> tuple[uint_e18, uint_e18, IAccounting_WithdrawalReceipt]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "completeWithdraw",
            withdrawer=withdrawer
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), IAccounting_WithdrawalReceipt.from_tuple(my_var_2)
        
    def deposit(
        self,
        depositor: Address,
        _amount: uint_e18,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "deposit",
            depositor=depositor,
            _amount=_amount
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def executeEpochCalculation(
        self,
        totalSupply: uint_e18,
        assets: uint_e18,
        liabilities: int_e18,
    ) -> tuple[uint_e18, uint_e18, uint_e18, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4 = self._call(
            "executeEpochCalculation",
            totalSupply=totalSupply,
            assets=assets,
            liabilities=liabilities
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), uint_e18.from_tuple(my_var_4)
        
    def initiateWithdraw(
        self,
        withdrawer: Address,
        shares: uint_e18,
    ) -> IAccounting_WithdrawalReceipt:
        my_var_0 = self._call(
            "initiateWithdraw",
            withdrawer=withdrawer,
            shares=shares
        )
        return IAccounting_WithdrawalReceipt.from_tuple(my_var_0)
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def redeem(
        self,
        redeemer: Address,
        shares: uint_e18,
    ) -> tuple[uint_e18, IAccounting_DepositReceipt]:
        my_var_0, my_var_1 = self._call(
            "redeem",
            redeemer=redeemer,
            shares=shares
        )
        return uint_e18.from_tuple(my_var_0), IAccounting_DepositReceipt.from_tuple(my_var_1)
        
    def sharesForAmount(
        self,
        _amount: uint_e18,
        assetPerShare: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "sharesForAmount",
            _amount=_amount,
            assetPerShare=assetPerShare
        )
        return uint_e18.from_tuple(my_var_0)
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
    
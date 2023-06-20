
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
    data: BaseBytes

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint_e18.from_tuple(args[0]),
            Address.from_tuple(args[1]),
            Address.from_tuple(args[2]),
            Address.from_tuple(args[3]),
            uint_e18.from_tuple(args[4]),
            uint_e18.from_tuple(args[5]),
            Types_OptionSeries.from_tuple(args[6]),
            uint_e18.from_tuple(args[7]),
            BaseBytes.from_tuple(args[8]),
        )



@dataclass
class CombinedActions_OperationProcedures:
    operation: uint8
    operationQueue: list[CombinedActions_ActionArgs]

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint8.from_tuple(args[0]),
            [CombinedActions_ActionArgs.from_tuple(arg_0) for arg_0 in args[1]],
        )



class optionExchange(BaseAbi):
    address: Address = Address("0xb672fE86693bF6f3b034730f5d2C77C8844d6b45")
    
    def addressbook(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "addressbook"
        )
        return Address.from_tuple(my_var_0)
        
    def approvedCollateral(
        self,
        x_0: Address,
        x_1: bool,
    ) -> bool:
        my_var_0 = self._call(
            "approvedCollateral",
            x_0=x_0,
            x_1=x_1
        )
        return bool(my_var_0)
        
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def catalogue(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "catalogue"
        )
        return Address.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "checkHash",
            optionSeries=optionSeries,
            strikeDecimalConverted=strikeDecimalConverted,
            isSell=isSell
        )
        return bytes32.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def createOtoken(
        self,
        optionSeries: Types_OptionSeries,
    ) -> Address:
        my_var_0 = self._call(
            "createOtoken",
            optionSeries=optionSeries
        )
        return Address.from_tuple(my_var_0)
        
    def feeRecipient(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "feeRecipient"
        )
        return Address.from_tuple(my_var_0)
        
    def getDelta(
        self,
    ) -> int_e18:
        my_var_0 = self._call(
            "getDelta"
        )
        return int_e18.from_tuple(my_var_0)
        
    def getOptionDetails(
        self,
        seriesAddress: Address,
        optionSeries: Types_OptionSeries,
    ) -> tuple[Address, Types_OptionSeries, uint128]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "getOptionDetails",
            seriesAddress=seriesAddress,
            optionSeries=optionSeries
        )
        return Address.from_tuple(my_var_0), Types_OptionSeries.from_tuple(my_var_1), uint128.from_tuple(my_var_2)
        
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
        
    def heldTokens(
        self,
        x_0: Address,
        x_1: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "heldTokens",
            x_0=x_0,
            x_1=x_1
        )
        return uint_e18.from_tuple(my_var_0)
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def maxTradeSize(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "maxTradeSize"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "minTradeSize"
        )
        return uint_e18.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "paused"
        )
        return bool(my_var_0)
        
    def poolFees(
        self,
        x_0: Address,
    ) -> uint24:
        my_var_0 = self._call(
            "poolFees",
            x_0=x_0
        )
        return uint24.from_tuple(my_var_0)
        
    def pricer(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "pricer"
        )
        return Address.from_tuple(my_var_0)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
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
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def swapRouter(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "swapRouter"
        )
        return Address.from_tuple(my_var_0)
        
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
        
    def update(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "update"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def withdraw(
        self,
        _amount: uint_e18,
    ) -> uint_e18:
        my_var_0 = self._call(
            "withdraw",
            _amount=_amount
        )
        return uint_e18.from_tuple(my_var_0)
    
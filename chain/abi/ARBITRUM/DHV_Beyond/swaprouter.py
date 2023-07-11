
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class ISwapRouter_ExactInputParams:
    path: BaseBytes
    recipient: Address
    deadline: uint_e18
    amountIn: uint_e18
    amountOutMinimum: uint_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            BaseBytes.from_tuple(args[0]),
            Address.from_tuple(args[1]),
            uint_e18.from_tuple(args[2]),
            uint_e18.from_tuple(args[3]),
            uint_e18.from_tuple(args[4]),
        )



@dataclass
class ISwapRouter_ExactInputSingleParams:
    tokenIn: Address
    tokenOut: Address
    fee: uint24
    recipient: Address
    deadline: uint_e18
    amountIn: uint_e18
    amountOutMinimum: uint_e18
    sqrtPriceLimitX96: uint160

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            Address.from_tuple(args[0]),
            Address.from_tuple(args[1]),
            uint24.from_tuple(args[2]),
            Address.from_tuple(args[3]),
            uint_e18.from_tuple(args[4]),
            uint_e18.from_tuple(args[5]),
            uint_e18.from_tuple(args[6]),
            uint160.from_tuple(args[7]),
        )



@dataclass
class ISwapRouter_ExactOutputParams:
    path: BaseBytes
    recipient: Address
    deadline: uint_e18
    amountOut: uint_e18
    amountInMaximum: uint_e18

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            BaseBytes.from_tuple(args[0]),
            Address.from_tuple(args[1]),
            uint_e18.from_tuple(args[2]),
            uint_e18.from_tuple(args[3]),
            uint_e18.from_tuple(args[4]),
        )



@dataclass
class ISwapRouter_ExactOutputSingleParams:
    tokenIn: Address
    tokenOut: Address
    fee: uint24
    recipient: Address
    deadline: uint_e18
    amountOut: uint_e18
    amountInMaximum: uint_e18
    sqrtPriceLimitX96: uint160

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            Address.from_tuple(args[0]),
            Address.from_tuple(args[1]),
            uint24.from_tuple(args[2]),
            Address.from_tuple(args[3]),
            uint_e18.from_tuple(args[4]),
            uint_e18.from_tuple(args[5]),
            uint_e18.from_tuple(args[6]),
            uint160.from_tuple(args[7]),
        )



class swaprouter(BaseAbi):
    address: Address = Address("0xe592427a0aece92de3edee1f18e0157c05861564")
    
    def WETH9(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "WETH9"
        )
        return Address.from_tuple(my_var_0)
        
    def exactInput(
        self,
        params: ISwapRouter_ExactInputParams,
    ) -> uint_e18:
        my_var_0 = self._call(
            "exactInput",
            params=params
        )
        return uint_e18.from_tuple(my_var_0)
        
    def exactInputSingle(
        self,
        params: ISwapRouter_ExactInputSingleParams,
    ) -> uint_e18:
        my_var_0 = self._call(
            "exactInputSingle",
            params=params
        )
        return uint_e18.from_tuple(my_var_0)
        
    def exactOutput(
        self,
        params: ISwapRouter_ExactOutputParams,
    ) -> uint_e18:
        my_var_0 = self._call(
            "exactOutput",
            params=params
        )
        return uint_e18.from_tuple(my_var_0)
        
    def exactOutputSingle(
        self,
        params: ISwapRouter_ExactOutputSingleParams,
    ) -> uint_e18:
        my_var_0 = self._call(
            "exactOutputSingle",
            params=params
        )
        return uint_e18.from_tuple(my_var_0)
        
    def factory(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "factory"
        )
        return Address.from_tuple(my_var_0)
        
    def multicall(
        self,
        data: list[BaseBytes],
    ) -> list[BaseBytes]:
        my_var_0 = self._call(
            "multicall",
            data=data
        )
        return [BaseBytes.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def refundETH(
        self,
    ) -> None:
        self._call(
            "refundETH"
        )
        
    def selfPermit(
        self,
        token: Address,
        value: uint_e18,
        deadline: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "selfPermit",
            token=token,
            value=value,
            deadline=deadline,
            v=v,
            r=r,
            s=s
        )
        
    def selfPermitAllowed(
        self,
        token: Address,
        nonce: uint_e18,
        expiry: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "selfPermitAllowed",
            token=token,
            nonce=nonce,
            expiry=expiry,
            v=v,
            r=r,
            s=s
        )
        
    def selfPermitAllowedIfNecessary(
        self,
        token: Address,
        nonce: uint_e18,
        expiry: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "selfPermitAllowedIfNecessary",
            token=token,
            nonce=nonce,
            expiry=expiry,
            v=v,
            r=r,
            s=s
        )
        
    def selfPermitIfNecessary(
        self,
        token: Address,
        value: uint_e18,
        deadline: uint_e18,
        v: uint8,
        r: bytes32,
        s: bytes32,
    ) -> None:
        self._call(
            "selfPermitIfNecessary",
            token=token,
            value=value,
            deadline=deadline,
            v=v,
            r=r,
            s=s
        )
        
    def sweepToken(
        self,
        token: Address,
        amountMinimum: uint_e18,
        recipient: Address,
    ) -> None:
        self._call(
            "sweepToken",
            token=token,
            amountMinimum=amountMinimum,
            recipient=recipient
        )
        
    def sweepTokenWithFee(
        self,
        token: Address,
        amountMinimum: uint_e18,
        recipient: Address,
        feeBips: uint_e18,
        feeRecipient: Address,
    ) -> None:
        self._call(
            "sweepTokenWithFee",
            token=token,
            amountMinimum=amountMinimum,
            recipient=recipient,
            feeBips=feeBips,
            feeRecipient=feeRecipient
        )
        
    def uniswapV3SwapCallback(
        self,
        amount0Delta: int_e18,
        amount1Delta: int_e18,
        _data: BaseBytes,
    ) -> None:
        self._call(
            "uniswapV3SwapCallback",
            amount0Delta=amount0Delta,
            amount1Delta=amount1Delta,
            _data=_data
        )
        
    def unwrapWETH9(
        self,
        amountMinimum: uint_e18,
        recipient: Address,
    ) -> None:
        self._call(
            "unwrapWETH9",
            amountMinimum=amountMinimum,
            recipient=recipient
        )
        
    def unwrapWETH9WithFee(
        self,
        amountMinimum: uint_e18,
        recipient: Address,
        feeBips: uint_e18,
        feeRecipient: Address,
    ) -> None:
        self._call(
            "unwrapWETH9WithFee",
            amountMinimum=amountMinimum,
            recipient=recipient,
            feeBips=feeBips,
            feeRecipient=feeRecipient
        )
    
from typing import TypeVar

from chain.types import Address

Self = TypeVar("Self")


class BaseInt(int):
    @classmethod
    def from_tuple(cls: type[Self], args: int) -> Self:
        return cls(args)

    def to_float_e0(self) -> float:
        """Convert int directly to float. `float(x)`"""
        return float(self)

    def to_float_e6(self) -> float:
        return float(self)/1e6

    def to_float_e18(self) -> float:
        return float(self)/1e18

    def to_float_e27(self) -> float:
        return float(self)/1e27

    def to_int(self) -> int:
        return int(self)


class int_e6(BaseInt):
    def to_float(self) -> float:
        return float(self) / 1e6


def cast_e6_to_float(x: int_e6) -> float:
    return float(x)/1e6


class int_e18(BaseInt):
    def to_float(self) -> float:
        return float(self) / 1e18


def cast_e18_to_float(x: int_e18) -> float:
    return float(x)/1e18


class uint_e18(BaseInt):
    def to_float(self) -> float:
        return float(self)


class int_e27(BaseInt):
    def to_float(self) -> float:
        return float(self) / 1e27


def cast_e27_to_float(x: int_e27) -> float:
    return float(x)/1e27


class uint160(BaseInt):
    ...


class uint128(BaseInt):
    ...


class uint64(BaseInt):
    ...


class int80(BaseInt):
    ...


class uint80(BaseInt):
    ...


class uint32(BaseInt):
    ...


class uint24(BaseInt):
    ...


class uint18(BaseInt):
    ...


class uint16(BaseInt):
    ...


class uint8(BaseInt):
    ...


# bool is marked as final.
# class BaseBool(bool):
#     @classmethod
#     def from_tuple(cls: type[Self], args: int) -> Self:
#         return cls(args)


class BaseBytes(bytes):
    @classmethod
    def from_tuple(cls: type[Self], args: bytes) -> Self:
        return cls(args)


class bytes32(BaseBytes):
    ...


class BaseStr(str):
    @classmethod
    def from_tuple(cls: type[Self], args: str) -> Self:
        return cls(args)


# Address.from_tuple = lambda args: Address(args)

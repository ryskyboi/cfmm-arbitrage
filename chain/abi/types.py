from typing import TypeVar

from chain.types import Address

Self = TypeVar("Self")


class BaseInt(int):
    @classmethod
    def from_tuple(cls: type[Self], args: int) -> Self:
        return cls(args)


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


class uint128(BaseInt):
    ...


class uint64(BaseInt):
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


class BaseAddress(Address):
    @classmethod
    def from_tuple(cls: type[Self], args: str) -> Self:
        return cls(args)

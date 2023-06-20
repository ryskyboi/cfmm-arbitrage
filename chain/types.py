from typing import TypeVar

Self = TypeVar("Self")


class AbiJson(dict):
    ...


class Address(str):
    @classmethod
    def from_tuple(cls: type[Self], args: bytes) -> Self:
        return cls(args)

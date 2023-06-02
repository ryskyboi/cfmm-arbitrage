
class int_e6(int):
    def to_float(self) -> float:
        return float(self) / 1e6


def cast_e6_to_float(x: int_e6) -> float:
    return float(x)/1e6


class int_e18(int):
    def to_float(self) -> float:
        return float(self) / 1e18


class uint_e18(int):
    def to_float(self) -> float:
        return float(self)


class uint128(int):
    ...


class uint64(int):
    ...

class uint80(int):
    ...


class uint32(int):
    ...


class uint24(int):
    ...


class uint16(int):
    ...


class uint8(int):
    ...


class bytes32(bytes):
    ...


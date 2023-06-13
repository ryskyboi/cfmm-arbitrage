
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

class int_e27(int):
    def to_float(self) -> float:
        return float(self) / 1e27

def cast_e18_to_float(x: int_e18) -> float:
    return float(x)/1e18

def cast_e27_to_float(x: int_e27) -> float:
    return float(x)/1e27

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

class uint18(int):
    ...

class uint16(int):
    ...


class uint8(int):
    ...

class bytes32(bytes):
    ...


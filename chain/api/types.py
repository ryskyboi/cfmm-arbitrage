class int_e6(int):
    def to_float(self) -> float:
        return float(self) / 1e6


class int_e18(int):
    def to_float(self) -> float:
        return float(self) / 1e18

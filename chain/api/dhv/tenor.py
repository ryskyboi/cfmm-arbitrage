from dataclasses import dataclass
from typing import List


@dataclass
class MultiplierTenor:
    put_multipliers: List[float]
    call_multipliers: List[float]

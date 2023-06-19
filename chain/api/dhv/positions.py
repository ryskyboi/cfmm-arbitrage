from dataclasses import dataclass
from dataclass_wizard import JSONWizard

@dataclass
class Position(JSONWizard):
    expiry_timestamp_s: float
    is_call: bool
    strike: float
    position: float

    def to_dict(self):
        return {
            'expiry': self.expiry_timestamp_s,
            'is_call': self.is_call,
            "strike": self.strike,
            "position": self.position
        }


@dataclass
class Positions(JSONWizard):
    positions : list[Position]



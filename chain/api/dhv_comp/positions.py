from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class OptionPosition(JSONWizard):
    expiry_timestamp_s: float
    is_call: bool
    strike: float
    position: float
    """Number of contracts the DHV is long (negative=short)."""

    # This isn't used anywhere?
    # def to_dict(self):
    #     return {
    #         'expiry': self.expiry_timestamp_s,
    #         'is_call': self.is_call,
    #         "strike": self.strike,
    #         "position": self.position
    #     }


# We should just use a list for this
#
# @dataclass
# class Positions(JSONWizard):
#     positions : list[OptionPosition]
#


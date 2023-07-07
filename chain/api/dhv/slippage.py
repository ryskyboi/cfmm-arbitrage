from dataclasses import dataclass

from dataclass_wizard import JSONWizard

from chain.api.dhv.tenor import MultiplierTenor


@dataclass
class SlippageSurface(JSONWizard):
    gradient: float
    multipliers: list[MultiplierTenor]



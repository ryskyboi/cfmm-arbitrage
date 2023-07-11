from dataclasses import dataclass
from dataclass_wizard import JSONWizard

from chain.api.dhv.tenor import MultiplierTenor


@dataclass
class DeltaSpreadParams(JSONWizard):
    """
    Rates applied when the DHV's side is long/short a call/put
    """
    dhv_buy_call_rate: float
    dhv_buy_put_rate: float
    dhv_sell_call_rate: float
    dhv_sell_put_rate: float


@dataclass
class SpreadDeltaSurface(JSONWizard):
    delta_rates: DeltaSpreadParams
    multipliers: list[MultiplierTenor]


@dataclass
class SpreadCollateralSurface(JSONWizard):
    collateral_rate: float
    """param: Interest charged on the minimum collateral DHV would use when minting a short contract
    Percentage, expressed as decimal."""
    multipliers: list[MultiplierTenor]
    low_delta_threshold: float
    low_delta_iv_cap: float

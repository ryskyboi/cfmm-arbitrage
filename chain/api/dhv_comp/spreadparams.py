from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class FeeIvSpreadParams(JSONWizard):
    """param fee_dollar: Dollar cost applied to every trade where it is less than 12.5% of trade val
    param iv_relative_spread: Percentage spread to apply to volatility.
    e.g. at 10%, for DHV buying a 50% vol position, DHV pays 45% vol."""
    fee_dollar: float
    iv_relative_spread: float


@dataclass
class CollateralSpreadParams(JSONWizard):
    collateral_rate: float
    """param: Interest charged on the minimum collateral DHV would use when minting a short contract
    Percentage, expressed as decimal."""


@dataclass
class DeltaSpreadParams(JSONWizard):
    """
    Rates applied when the DHV's side is long/short a call/put
    """
    dhv_buy_call_rate: float
    dhv_buy_put_rate: float
    dhv_sell_call_rate: float
    dhv_sell_put_rate: float

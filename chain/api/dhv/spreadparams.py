from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class FeeIvSpreadParams(JSONWizard):
    fee_dollar: float
    """Dollar cost applied to every trade where it is less than 12.5% of trade value"""
    iv_relative_spread: float
    """Percentage spread to apply to volatility. e.g. at 10%, for DHV buying a 50% vol position, DHV pays 45% vol."""

@dataclass
class CollateralSpreadParams(JSONWizard):
    collateral_rate: float
    """Interest charged on the minimum collateral DHV would use when minting a short contract.
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

@dataclass
class SpreadParams(JSONWizard):
    fee_iv_spread_Params: FeeIvSpreadParams
    collateral_spread_Params: CollateralSpreadParams
    delta_spread_Params: DeltaSpreadParams

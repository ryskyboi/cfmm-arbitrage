from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class CollateralParams(JSONWizard):
    """
    spot_shock: percentage move applied to spot against option to simulate stress test
    premium_curve: map of DTE (tenor, in days) to shocked ATM premium (in ETH) e.g. volatility of 250%
    """
    call_spot_shock: float
    call_premium_curve: dict[float, float]
    put_spot_shock: float
    put_premium_curve: dict[float, float]
from dataclasses import dataclass
from typing import List

from dataclass_wizard import JSONWizard

@dataclass
class SlippageGradient(JSONWizard):
    """
    The multiplies for calls and puts needed to calculate spread

    param put_gradient_multiplier: a list of 100/delta_band_width values for the slippage to be
        multiplied on put option traded, list is from
        [0, 100/delta_band_width] to [100 - delta_band_width, 100]
    param call_gradient_multiplier: a list of 100/delta_band_width values for the slippage to be
        multiplied on put option traded, list is from
        [0, 100/delta_band_width] to [100 - delta_band_width, 100]
    param delta_band_width: with between the delta bands
    param slippage_gradient: a multiplier applied to all gradient multiplier to get the
        multiplier we use e.g your used multiplier is slippage_gradient*put_gradient_multipler[n]

    """
    put_slippage_gradient_multipliers: List[float]
    call_slippage_gradient_multipliers: List[float]
    slippage_gradient: float

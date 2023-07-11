from dataclasses import dataclass


@dataclass
class SabrModelParam:
    alpha: float
    beta: float
    rho: float
    nu: float


@dataclass
class SabrExpiryParams:
    expiry_timestamp_s: float
    call_sabr: SabrModelParam
    put_sabr: SabrModelParam
    rate: float

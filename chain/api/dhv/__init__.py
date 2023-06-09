from dataclasses import dataclass
from datetime import datetime as dt

from chain.abi import AbiManager
from chain.abi.types import cast_e6_to_float
from chain.api.reader import ChainReader
from chain.chains import ChainDefinition
from chain.web3_api import Web3Endpoint


@dataclass
class SabrModelParam:
    alpha: float
    beta: float
    rho: float
    nu: float

@dataclass
class SabrExpiryParams:
    call_sabr: SabrModelParam
    put_sabr: SabrModelParam
    rate: float


class DhvChainReader(ChainReader):
    def __init__(self, chain_def: ChainDefinition, web3_endpoint: Web3Endpoint, abi_manager: AbiManager):
        super().__init__(chain_def, web3_endpoint, abi_manager)
        self.protocol_def = "DHV"
        from chain.abi.ARBITRUM_GOERLI.DHV.volFeed import volFeed
        self._vol_feed: volFeed = self._contract(volFeed)

    def expiry_timestamps_s(self, is_include_expired=False) -> list[int]:
        """
        List of expiries (optionally include expired ones) as timestamps, in (int) seconds.
        :return:
        """
        return [t for t in self._vol_feed.getExpiries() if t > int(dt.now().timestamp()) or is_include_expired]

    def sabr_param_data(self, is_include_expired=False) -> list[SabrExpiryParams]:
        """
        List of all sabr data, including rate, optionally include expired dates.
        :return:
        """
        sabrs: list[SabrExpiryParams] = []
        for t in self.expiry_timestamps_s(is_include_expired):
            chain_sabr = self._vol_feed.sabrParams(t)
            sabrs.append(
                SabrExpiryParams(
                    SabrModelParam(
                        cast_e6_to_float(chain_sabr[0]),
                        cast_e6_to_float(chain_sabr[1]),
                        cast_e6_to_float(chain_sabr[2]),
                        cast_e6_to_float(chain_sabr[3]),
                    ),
                    SabrModelParam(
                        cast_e6_to_float(chain_sabr[4]),
                        cast_e6_to_float(chain_sabr[5]),
                        cast_e6_to_float(chain_sabr[6]),
                        cast_e6_to_float(chain_sabr[7]),
                    ),
                    float(chain_sabr[8])
                )
            )
        return sabrs

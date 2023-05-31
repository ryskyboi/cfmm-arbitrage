from chain.api import ChainReader
from chain.api.dhv.sabrparams import VolFeedContract
from chain.protocols import DHV


class DhvChainReader(ChainReader):
    @property
    def vol_feed(self) -> VolFeedContract:
        return self.web3_endpoint.build_contract(DHV.volFeed, VolFeedContract)


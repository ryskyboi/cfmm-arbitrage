from unittest import TestCase, skip, skipIf

from chain.abi import AbiManager
from chain.api.reader import ChainReader
from chain.chains import CHAIN
from chain.web3_api import Web3Endpoint
from test.config import my_test_config_mainnet


class TestDhvBeyond(TestCase):
    def chain_reader(self) -> ChainReader:
        return ChainReader.from_config(my_test_config_mainnet())

    def test_pricer(self) -> None:
        from chain.abi.ARBITRUM.DHV_Beyond.beyondPricer import beyondPricer
        # w3_ep = Web3Endpoint.from_config(my_test_config_mainnet())
        # abi_man = AbiManager(CHAIN.ARBITRUM.value, my_test_config_mainnet().abi_resource_folder)
        reader = self.chain_reader()
        bp = reader._contract(beyondPricer)
        print(bp.riskFreeRate())
        print(bp)
from unittest import TestCase

from chain.api.dhv import DhvChainReader
from chain.chains import CHAIN
from chain.web3_api import Web3Endpoint
from test import test_config


class TestDhvChainReader(TestCase):
    def test_sabr_param_data(self):
        dhv = DhvChainReader.from_config(
            test_config()
        )
        print(dhv.sabr_param_data())

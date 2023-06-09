from unittest import TestCase

from chain.api.dhv import DhvChainReader
from test import test_config


class TestDhvChainReader(TestCase):
    def test_sabr_param_data(self):
        dhv = DhvChainReader.from_config(
            test_config()
        )
        # TODO: make into proper unit test
        print(dhv.sabr_param_data())

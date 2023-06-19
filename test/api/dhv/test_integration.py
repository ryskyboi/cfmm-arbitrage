import unittest
from unittest import TestCase, skipIf

import test
from chain.api.dhv import DhvChainReader
from chain.config import Config


@skipIf(test.IS_DISABLE_LIVE_TESTING, "Skipping live integration tests")
class TestApiDhvIntegration(TestCase):
    def test_config(self) -> Config:
        from test.config import my_test_config as tc
        return tc()

    def test_dhv(self) -> DhvChainReader:
        return DhvChainReader.from_config(self.test_config())

    def test_sabr(self) -> None:
        sabr = self.test_dhv().sabr_param_data()
        print(sabr)

    def test_option_positions(self) -> None:
        pos = self.test_dhv().position_data()
        import datetime as dt

        for po in pos:
            print(po.expiry_timestamp_s, dt.datetime.now().timestamp())


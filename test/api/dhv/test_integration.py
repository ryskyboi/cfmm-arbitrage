from unittest import TestCase, skipIf

import test
from chain.api.dhv import DhvChainReader
from chain.config import Config
from chain.logger import log
from test.api.dhv.test_make_res import IS_ENABLE_WEB3_RECORDING, save_res


def save_response(func, response) -> None:
    if IS_ENABLE_WEB3_RECORDING:
        save_res(func, "response", "", response)


@skipIf(test.IS_DISABLE_LIVE_TESTING, "Skipping live integration tests")
class TestApiDhvIntegration(TestCase):
    def test_config(self) -> Config:
        from test.config import my_test_config_mainnet as tc
        return tc()

    def test_dhv(self) -> DhvChainReader:
        return DhvChainReader.from_config(self.test_config())

    def test_fee(self) -> None:
        fee = self.test_dhv().fee()
        save_response("test_fee", fee)
        log.debug(fee)

    def test_iv_spread(self) -> None:
        iv = self.test_dhv().iv_spread()
        save_response("test_iv_spread", iv)
        log.debug(iv)

    def test_sabr(self) -> None:
        sabr = self.test_dhv().sabrs(True)
        save_response("test_sabr", sabr)
        log.debug(sabr)

    def test_option_positions(self) -> None:
        pos = self.test_dhv().option_positions()
        save_response("test_option_positions", pos)
        for po in pos:
            log.debug(po)

    def test_collateral(self) -> None:
        collat = self.test_dhv().collateral_params(True)
        save_response("test_collateral", collat)
        log.debug(collat)

    def test_slippage_surface(self) -> None:
        slippage_surface = self.test_dhv().slippage_surface()
        save_response("test_slippage_surface", slippage_surface)
        log.debug(slippage_surface)

    def test_spread_delta_rates(self) -> None:
        delta_rates = self.test_dhv().delta_rates()
        save_response("test_spread_delta_rates", delta_rates)
        log.debug(delta_rates)

    def test_spread_delta_surface(self) -> None:
        spread_delta_surface = self.test_dhv().spread_delta_surface()
        save_response("test_spread_delta_surface", spread_delta_surface)
        log.debug(spread_delta_surface)

    def test_spread_collateral_rate(self) -> None:
        collat = self.test_dhv().collateral_rate()
        save_response("test_spread_collateral_rate", collat)
        log.debug(collat)

    def test_spread_collateral_surface(self) -> None:
        cs = self.test_dhv().spread_collateral_surface()
        save_response("test_spread_collateral_surface", cs)
        log.debug(cs)
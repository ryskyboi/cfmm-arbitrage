from unittest import TestCase

from chain.abi import AbiManager
from chain.abi.path import abi_resource_path
from chain.api.dhv import DhvChainReader
from chain.chains import CHAIN
from chain.logger import log
from test.api.make_res import MockW3E, load_res


def load_response(func) -> str:
    return load_res("dhv", func, "response", "", True)


class TestApiDhvIntegration(TestCase):
    def test_dhv(self) -> DhvChainReader:
        return DhvChainReader(
            CHAIN.ARBITRUM.value,
            MockW3E("dhv"),
            AbiManager(CHAIN.ARBITRUM.value, abi_resource_path())
        )

    def test_fee(self) -> None:
        fee = self.test_dhv().fee()
        self.assertEqual(
            repr(fee),
            load_response("test_fee"),
            "fee fail"
        )

    def test_iv_spread(self) -> None:
        iv = self.test_dhv().iv_spread()
        self.assertEqual(
            repr(iv),
            load_response("test_iv_spread"),
            "iv fail"
        )

    def test_sabr(self) -> None:
        sabr = self.test_dhv().sabrs(True)
        self.assertEqual(
            repr(sabr),
            load_response("test_sabr"),
            "Sabr fail"
        )

    def test_option_positions(self) -> None:
        pos = self.test_dhv().option_positions()
        self.assertEqual(
            repr(pos),
            load_response("test_option_positions"),
            "DHV Pos fail"
        )

    def test_collateral(self) -> None:
        collat = self.test_dhv().collateral_params(True)
        self.assertEqual(
            repr(collat),
            load_response("test_collateral"),
            "Collat param fail"
        )

    def test_slippage_surface(self) -> None:
        slippage_surface = self.test_dhv().slippage_surface()
        self.assertEqual(
            repr(slippage_surface),
            load_response("test_slippage_surface"),
            "slippage surface fail"
        )
        log.debug(slippage_surface)

    def test_spread_delta_rates(self) -> None:
        delta_rates = self.test_dhv().delta_rates()
        self.assertEqual(
            repr(delta_rates),
            load_response("test_spread_delta_rates"),
            "spread delta rate fail"
        )
        log.debug(delta_rates)

    def test_spread_delta_surface(self) -> None:
        spread_delta_surface = self.test_dhv().spread_delta_surface()
        self.assertEqual(
            repr(spread_delta_surface),
            load_response("test_spread_delta_surface"),
            "spread_delta_surface fail"
        )
        log.debug(spread_delta_surface)

    def test_spread_collateral_rate(self) -> None:
        spread_collateral_rate = self.test_dhv().collateral_rate()
        self.assertEqual(
            repr(spread_collateral_rate),
            load_response("test_spread_collateral_rate"),
            "spread_collateral_rate fail"
        )
        log.debug(spread_collateral_rate)

    def test_spread_collateral_surface(self) -> None:
        spread_collateral_surface = self.test_dhv().spread_collateral_surface()
        self.assertEqual(
            repr(spread_collateral_surface),
            load_response("test_spread_collateral_surface"),
            "spread_collateral_surface fail"
        )
        log.debug(spread_collateral_surface)

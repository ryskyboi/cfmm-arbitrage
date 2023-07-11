from unittest import TestCase

from chain.abi import AbiManager
from chain.abi.path import abi_resource_path
from chain.api.dhv_comp import DhvCompChainReader
from chain.chains import CHAIN
from chain.logger import log
from test.api.make_res import MockW3E, load_res


def load_response(func) -> str:
    return load_res("dhv_comp", func, "response", "", True)


class TestApiDhvIntegration(TestCase):
    def test_dhv(self) -> DhvCompChainReader:
        return DhvCompChainReader(
            CHAIN.ARBITRUM_GOERLI.value,
            MockW3E("dhv_comp"),
            AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path())
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

    def test_slippage(self) -> None:
        slippage = self.test_dhv().slippage_params()
        self.assertEqual(
            repr(slippage),
            load_response("test_slippage"),
            "slippage param fail"
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

    def test_delta_rates(self) -> None:
        delta_rates = self.test_dhv().delta_rates()
        self.assertEqual(
            repr(delta_rates),
            load_response("test_delta_rates"),
            "delta rate fail"
        )
        log.debug(delta_rates)

    def test_collateral_rate(self) -> None:
        collat = self.test_dhv().collateral_rate()
        self.assertEqual(
            repr(collat),
            load_response("test_collateral_rate"),
            "collat fail"
        )
        log.debug(collat)
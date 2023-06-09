# TODO: Remove when no longer needed.

# from unittest import TestCase, skip, skipIf
#
# import test
# from chain.api.dhv import DhvChainReader
# from chain.api.dhv.sabrparams import VolFeedContract
# from chain.protocols import DHV
# from test import test_config
#
#
# def vol_feed_contract() -> VolFeedContract:
#     dhv = DhvChainReader.from_config(test_config())
#     return dhv._vol_feed
#
#
# class TestSabrParamsContract(TestCase):
#     @skipIf(test.IS_DISABLE_LIVE_TESTING, "Live testing disabled.")
#     def test_get_expiries(self):
#         vf = vol_feed_contract()
#         expiries = vf.getExpiries()
#         self.assertIsInstance(expiries[0], int, "dhv get expiries fail")

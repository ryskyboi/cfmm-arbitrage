from dataclasses import dataclass


from chain.abi.types import *
from chain.contracts import Contract
import datetime as dt


@dataclass
class _SabrParams:
    ...


# TODO: remove when no longer needed
#
# class VolFeedContract(Contract):
#     def _getExpiries(self) -> list[int_e18]:
#         f = self._w3_contract.functions
#         return f.getExpiries().call()
#
#     def expiry_timestamps_s(self, is_include_expired=False) -> list[int]:
#         """
#         Fetch a list of all expiries by timestamp in whole seconds, optionally exclude those expired(default).
#         :param is_include_expired:
#         :return:
#         """
#         now = int(dt.datetime.now().timestamp())
#         return sorted([t for t in self._getExpiries() if t > now or is_include_expired])
#
#     def _sabrParams(self, expiry_timestamp_s: int) -> \
#             tuple[
#                 int_e6, int_e6, int_e6, int_e6,
#                 int_e6,int_e6, int_e6, int_e6,
#                 int_e18
#             ]:
#         ...
#
#

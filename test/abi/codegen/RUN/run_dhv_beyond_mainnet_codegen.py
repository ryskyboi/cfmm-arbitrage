from unittest import TestCase, skip

from chain.abi.codegen import ProtocolAbiCodegen
from chain.abi.codegen.utils import deserialise_contract_definitions
from chain.chains import CHAIN

contracts_str = """
"""


@skip("This code modifies the library codebase. DO NOT RUN!")
class RunMe(TestCase):
    def test_generate_package_source(self) -> None:
        contract_defs = deserialise_contract_definitions(contracts_str)
        gen = ProtocolAbiCodegen.create(
            CHAIN.ARBITRUM_GOERLI,
            "DHV",
            contract_defs
        )
        ps = gen.generate_package_source(
            # is_dry_run=False
        )
        for k, v in ps.items():
            print(k)
            print(v)

from unittest import TestCase

from chain.abi import AbiManager
from chain.abi.codegen.protocolspec import ProtocolSpec
from chain.abi.path import abi_resource_path
from chain.chains import CHAIN
from chain.protocols import ProtocolDefinition
from test.abi.codegen.RUN.run_dhv_beyond_competition_codegen import dhv_beyond_competition_contract_defs


class TestProtocolSpec(TestCase):
    def test_build_def(self):
        contracts = dhv_beyond_competition_contract_defs()
        abi_manager = AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path())
        protocol_spec = ProtocolSpec(
            ProtocolDefinition(
                "DHV", CHAIN.ARBITRUM_GOERLI,
                contracts
            ),
            abi_manager
        )
        # print(protocol_spec.generate_subpackage_source())

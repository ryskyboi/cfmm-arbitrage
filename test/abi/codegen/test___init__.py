from unittest import TestCase, skip

from chain.abi import AbiManager
from chain.abi.codegen import ProtocolAbiCodegen, AbiConfig
from chain.abi.path import abi_resource_path
from chain.chains import CHAIN
from chain.protocols import ProtocolDefinition
from chain.web3_api import Web3Endpoint
from test import test_config
from test.abi.codegen.test_protocolspec import test_dhv_contract_defs


@skip("Only for codegen!")
class TestProtocolAbiCodegen(TestCase):
    def test_generate_package_source(self):
        contracts = test_dhv_contract_defs()
        gen = ProtocolAbiCodegen(
            AbiConfig(),
            AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path()),
            ProtocolDefinition(
                "DHV",
                CHAIN.ARBITRUM_GOERLI,
                contracts
            )
        )
        ps = gen.generate_package_source(is_dry_run=False)
        for k, v in ps.items():
            print(k)
            print(v)

    # def test_generated_code(self) -> None:
    #     from chain.abi..DHV.volFeed import volFeed
    #     w3e = Web3Endpoint.from_config(test_config())
    #     vf = volFeed(w3e, AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path()))
    #     timestamps_s = vf.getExpiries()
    #     for t_s in timestamps_s:
    #         print(t_s, vf.sabrParams(t_s))

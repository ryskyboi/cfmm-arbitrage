from unittest import TestCase, skip

from chain.abi import AbiManager
from chain.abi.codegen import ProtocolAbiCodegen, AbiConfig
from chain.abi.path import abi_resource_path
from chain.chains import CHAIN
from chain.protocols import ProtocolDefinition
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
        ps = gen.generate_package_source(
            # is_dry_run=False,
        )
        for k, v in ps.items():
            print(k)
            print(v)

    # def test_generated_code(self) -> None:
    #     from chain.abi.ARBITRUM_GOERLI.DHV.volFeed import volFeed
    #     from test.config import my_test_config
    #     dhv = DhvChainReader.from_config(my_test_config())
    #     vf = dhv._vol_feed
    #     timestamps_s = vf.getExpiries()
    #     for t_s in timestamps_s:
    #         print(t_s, vf.sabrParams(t_s))

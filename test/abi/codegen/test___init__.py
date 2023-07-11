from unittest import TestCase, skip

from chain.abi.codegen import ProtocolAbiCodegen
from chain.chains import CHAIN
from test.abi.codegen.RUN.run_dhv_beyond_competition_codegen import \
    dhv_beyond_competition_contract_defs


@skip("Only for codegen!")
class TestProtocolAbiCodegen(TestCase):
    def test_generate_package_source(self):
        contracts = dhv_beyond_competition_contract_defs()
        gen = ProtocolAbiCodegen.create(
            CHAIN.ARBITRUM_GOERLI,
            "DHV",
            contracts
        )
        # gen = ProtocolAbiCodegen(
        #     AbiConfig(),
        #     AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path()),
        #     ProtocolDefinition(
        #         "DHV",
        #         CHAIN.ARBITRUM_GOERLI,
        #         contracts
        #     )
        # )
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

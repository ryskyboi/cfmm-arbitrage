from unittest import TestCase

from chain.abi import AbiManager
from chain.abi.codegen.protocolspec import ProtocolSpec
from chain.abi.path import abi_resource_path
from chain.chains import CHAIN
from chain.contracts import ContractDefinition
from chain.protocols import ProtocolDefinition



def test_dhv_contract_defs() -> list[ContractDefinition]:
    contracts_str = """
    OpynController: '0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2',
    OpynAddressBook: '0xd6e67bF0b1Cdb34C37f31A2652812CB30746a94A',
    OpynOracle: '0x35578F5A49E1f1Cf34ed780B46A0BdABA23D4C0b',
    OpynNewCalculator: '0xcD270e755C2653e806e16dD3f78E16C89B7a1c9e',
    OpynOptionRegistry: '0x4E89cc3215AF050Ceb63Ca62470eeC7C1A66F737',
    priceFeed: '0xf7B1e3a7856067BEcee81FdE0DD38d923b99554D',
    volFeed: '0xf058Fe438AAF22617C30997579E89176e19635Dc',
    optionProtocol: '0x81267CBE2d605b7Ae2328462C1EAF51a1Ab57fFd',
    liquidityPool: '0x0B1Bf5fb77AA36cD48Baa1395Bc2B5fa0f135d8C',
    authority: '0x68256a51a6777129968b88bd21b6f657eCE8B0E6',
    pvFeed: '0x84fbb7C0a210e5e3A9f7707e1Fb725ADcf0CF528',
    optionHandler: '0x1F63F3B37f818f05ebefaCa11086e5250958e0D8',
    opynInteractions: '0x502b02DD4bAdb4F2d104418DCb033606AC948e30',
    normDist: '0x27810907FD5B3427567fF12c1412952EC7d04E80',
    blackScholes: '0x0D7776e816E774D5d8Ce0af78F6C51582846a66c',
    optionsCompute: '0x1f9E2596037dC1727AbeA03085E92Ef65641949f',
    accounting: '0x8339B6AB2B573F0acdb43F9DD00f290A07aA8708',
    uniswapV3HedgingReactor: '0x7a3eEC265292044417CC873d7cb2dDbF613745bC',
    perpHedgingReactor: '0x361B6Fb536588E87F0CEE1eb9Ac5a26Ef7108d9B',
    optionCatalogue: '0xde458dD32651F27A8895D4a92B7798Cdc4EbF2f0',
    optionExchange: '0xb672fE86693bF6f3b034730f5d2C77C8844d6b45',
    beyondPricer: '0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259',
    manager: '0xB8Cb70cf67EF7d7dFb1C70bc7A169DFCcCF0753c',
    lens: '0xe1805262E848945C8E545D1F82809Ba5bc5Ad7c0',
    weth: '0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3',
    usdc: '0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d'
    """
    contract_map = {
        w[0]: w[1] for w in
        (
            line.split(":")
            for line in contracts_str.replace(" ", "").replace(",", "").replace("'", "").splitlines()
            if line
        )
        # if w[0] == "optionCatalogue"
    }
    contracts: list[ContractDefinition] = [
        ContractDefinition(k, v) for k, v in contract_map.items()
    ]
    return contracts

class TestProtocolSpec(TestCase):
    def test_build_def(self):
        contracts = test_dhv_contract_defs()
        abi_manager = AbiManager(CHAIN.ARBITRUM_GOERLI.value, abi_resource_path())
        protocol_spec = ProtocolSpec(
            ProtocolDefinition(
                "DHV", CHAIN.ARBITRUM_GOERLI,
                contracts
            ),
            abi_manager
        )
        # print(protocol_spec.generate_subpackage_source())

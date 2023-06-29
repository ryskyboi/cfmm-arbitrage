from unittest import TestCase, skip

from chain.abi.codegen import ProtocolAbiCodegen
from chain.abi.codegen.utils import deserialise_contract_definitions
from chain.chains import CHAIN

contracts_str = """
OpynController: 0x594bD4eC29F7900AE29549c140Ac53b5240d4019
OpynAddressBook: 0xCa19F26c52b11186B4b1e76a662a14DA5149EA5a
OpynOracle: 0xBA1880CFFE38DD13771CB03De896460baf7dA1E7
OpynNewCalculator: 0x749a3624ad2a001F935E3319743f53Ecc7466358

otokenFactory: 0xBa1952eCdbA02de66fCf73f29068e8cf072644ec
otoken: 0x1d96E828e0Aa743783919B24ccDB971504a96C77
whitelist: 0x84CaCC4103CeE1Da9b79f9Ed0Ed97414240D9c6F
pool: 0xb9F33349db1d0711d95c1198AcbA9511B8269626
OptionRegistry: 0x8Bc23878981a207860bA4B185fD065f4fd3c7725
priceFeed: 0x7f86AC0c38bbc3211c610abE3841847fe19590A4
volFeed: 0xF204B60A98B3be05914AeC46bcEd2476D13a0225
optionProtocol: 0x4e920e9A901069d9b211646B6E191d81BA40E5FB
liquidityPool: 0x217749d9017cB87712654422a1F5856AAA147b80
authority: 0x74948DAf8Beb3d14ddca66d205bE3bc58Df39aC9
pvFeed: 0x7f9d820CFc109686F2ca096fFA93dd497b91C073
optionHandler: 0xc63717c4436043781a63C8c64B02Ff774350e8F8
opynInteractions: 0xC9d8859bb5E7aC7e9A8c175bf79cecc008f7D39e
normDist: 0x67c7B1e0408365a1840663557bB255BB0F0a1a44
blackScholes: 0x85C100Eb32C3e2F6EA0444E553f3A9bCE468cb8C
optionsCompute: 0xCF263127E7dFF09018af1f803bd3F9db58587a1c
accounting: 0x48672a2885995cF3Ddc9Da633C22b262e0533f7C
uniswapV3HedgingReactor: 0x0053849115783b9678DBB173BB852f06e950Fe05
perpHedgingReactor: 0xf013767D55954EcCCacb4914d52D2ef8f95d82C5
gmxHedgingReactor: 0xbCd871faAf2c36D57B0F4C006c6B0Cc2E1929736
optionCatalogue: 0x44227Dc2a1d71FC07DC254Dfd42B1C44aFF12168
optionExchange: 0xC117bf3103bd09552F9a721F0B8Bce9843aaE1fa
beyondPricer: 0xeA5Fb118862876f249Ff0b3e7fb25fEb38158def
manager: 0xD404D0eD7fe1EB1Cd6388610F9e5B5E6b6E41E72
weth: 0x82aF49447D8a07e3bd95BD0d56f35241523fBab1
usdcNative: 0xaf88d065e77c8cC2239327C5EDb3A432268e5831
usdcBridged: 0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8
chainlink price feed: 0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612
sequencer uptime feed: 0xfdb631f5ee196f0ed6faa767959853a9f217697d
swap router: 0xe592427a0aece92de3edee1f18e0157c05861564
clearing house: 0x4521916972a76d5bfa65fb539cf7a0c2592050ac
gmx position router: 0xb87a436b93ffe9d75c5cfa7bacfff96430b09868
gmx reader: 0x22199a49a999c351ef7927602cfb187ec3cae489
gmx vault: 0x489ee077994b6658eafa855c308275ead8097c4a 
DHV lens: 0xa306C00e08ebC84a5F4F67b561B8F6EDeb77600D
User Position lens: 0x02eFd4e61C1883A0FfF1044ACd61c9100859336c
L2 Chainlink Pricer: 0x7a71f218003d2DbF25337d072FA096099B50E0F0
"""


# @skip("This code modifies the library codebase. DO NOT RUN!")
class RunMe(TestCase):
    def test_generate_package_source(self) -> None:
        contract_defs = deserialise_contract_definitions(contracts_str)
        gen = ProtocolAbiCodegen.create(
            CHAIN.ARBITRUM,
            "DHV_Beyond",
            contract_defs
        )
        ps = gen.generate_package_source(
            is_dry_run=False
        )
        for k, v in ps.items():
            print(k)
            print(v)

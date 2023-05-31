from chain.chains import CHAIN
from chain.protocols import DHV, ContractName


class AddressManager:
    def __init__(self, chain: CHAIN):
        self.chain = chain

    def address(self, contract_name: ContractName) -> str:
        return ADDRESS_REGISTER[self.chain][contract_name]


ADDRESS_REGISTER: dict[CHAIN, dict[ContractName, str]] = {
    CHAIN.ARBITRUM_TESTNET: {
        DHV.volFeed: "0xf058Fe438AAF22617C30997579E89176e19635Dc"
    }
}

from chain.contracts import ContractDefinition
from chain.types import Address


def deserialise_contract_definitions(contracts_str: str) -> list[ContractDefinition]:
    """
    Build contract definitions from address text in Notion, as text, and return python contract definitions
    :param contracts_str: multiline string of contracts, copied from notion
    :return:
    """
    contract_map = {
        w[0]: w[1] for w in
        (
            line.split(":")
            for line in contracts_str.replace(" ", "").replace(",", "").replace("'", "").splitlines()
            if line
        )
    }
    contracts: list[ContractDefinition] = [
        ContractDefinition(k, Address(v)) for k, v in contract_map.items()
    ]
    return contracts

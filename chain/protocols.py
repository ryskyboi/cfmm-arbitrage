from dataclasses import dataclass
from enum import Enum, auto

from chain.chains import CHAIN
from chain.contracts import ContractDefinition


class ContractName(Enum):
    ...


class DHV(ContractName):
    volFeed = auto()


@dataclass
class ProtocolDefinition:
    name: str
    chain: CHAIN
    contract_definitions: list[ContractDefinition]
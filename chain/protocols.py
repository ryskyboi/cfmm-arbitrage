from enum import Enum, auto


class ContractName(Enum):
    ...


class DHV(ContractName):
    volFeed = auto()

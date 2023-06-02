from chain.abi import AbiManager
from chain.abi.codegen import ContractSpec
from chain.protocols import ProtocolDefinition


class ProtocolSpec:
    def __init__(self, protocol_def: ProtocolDefinition, abi_manager: AbiManager) -> None:
        self._abi_manager = abi_manager
        self._protocol_def = protocol_def
        contract_specs: list[ContractSpec] = []
        for cd in protocol_def.contract_definitions:
            abi_json = self._abi_manager.abi_json_str(cd.address)
            contract_spec = ContractSpec.from_json(cd, abi_json)
            contract_specs.append(contract_spec)
        self._contract_specs = contract_specs

    def generate_subpackage_source(self) -> dict[str, str]:
        """
        Build a map of contract_name -> module source code
        """
        return {cs.name: cs.generate_module_source() for cs in self._contract_specs}

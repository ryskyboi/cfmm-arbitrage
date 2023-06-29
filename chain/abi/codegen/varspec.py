from dataclasses import dataclass
from typing import Any

from dataclass_wizard import JSONWizard

from chain.abi.types import *
from chain.types import Address
from chain.logger import log

_TYPE_LOOKUP = {
    "uint256": uint_e18,
    "uint160": uint160,
    "uint128": uint128,
    "uint80": uint80,
    "int80": int80,
    "uint64": uint64,
    "uint32": uint32,
    "uint24": uint24,
    "uint16": uint16,
    "uint8": uint8,
    "int256": int_e18,
    "int32": int_e6,
    "bool": bool,
    "address": Address,
    "bytes": BaseBytes,
    "bytes32": bytes32,
    "string": BaseStr
}


def build_type(arg_type: str, internal_type: str) -> str:
    if arg_type[-2:] == "[]":
        arg_type = build_type(arg_type[:-2], internal_type[:-2])
        return f"list[{arg_type}]"
    elif arg_type[-3:] in ("[2]",):
        # TODO: regex for array. The length can be more than two!
        arg_type = build_type(arg_type[:-3], internal_type[:-3])
        return f"list[{arg_type}]"
    if arg_type in _TYPE_LOOKUP:
        return _TYPE_LOOKUP[arg_type].__name__
    elif arg_type == "tuple":
        return internal_type.split(" ")[1].replace(".", "_")
    else:
        log.warning(f"Not able to generate def for {arg_type, internal_type}.")
        return "Any"


def validate_var_name(var_name: str):
    # TODO: check illegal variable names in python properly.
    # rename illegal variables in python
    if var_name in ("from", "to"):
        return var_name + "_"
    return var_name


def build_from_list_tuple_call(type_name: str, arg: str, stack:int=0) -> str:
    if type_name == "bool":
        return f"bool({arg})"
    if type_name[:5] != "list[":
        return f"{type_name}.from_tuple({arg})"
    inner_type_name = type_name[5:-1]
    arg_i = f"arg_{stack}"
    return f"[{build_from_list_tuple_call(inner_type_name, arg_i, stack+1)} for {arg_i} in {arg}]"

@dataclass
class VarSpec(JSONWizard):
    internal_type: str
    name: str
    type: str
    components: Any = None

    def __post_init__(self) -> None:
        if self.components:
            components = []
            for c in self.components:
                if isinstance(c, VarSpec):
                    component = c
                else:
                    component = VarSpec.from_dict(c)
                components.append(component)
            self.components = components
        else:
            self.components = []
        self.name = validate_var_name(self.name)

    def enrich_names(self, stem_name: str) -> None:
        if not self.name:
            self.name = stem_name
        component: VarSpec
        for i, component in enumerate(self.components):
            component.enrich_names(f"{stem_name}_{i}")

    def type_name(self) -> str:
        return build_type(self.type, self.internal_type)

    def generate_from_tuple_call(self, args: str) -> str:
        return build_from_list_tuple_call(self.type_name(), args)

    def generate_from_tuple_method(self) -> str:
        from_tuple_args = ""
        component: VarSpec
        for i, component in enumerate(self.components):
            from_tuple_args += f"""
            {component.generate_from_tuple_call(f"args[{i}]")},"""
        from_tuple = f"""
    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls({from_tuple_args}
        )
"""
        return from_tuple

    def generate_variable_source(self, class_definitions: list[str]) -> str:
        if self.type[:5] == "tuple":
            class_name = self.internal_type.split("[")[0].split(" ")[1].replace(".", "_")
            class_definition = f"""
@dataclass
class {class_name}:"""
            component: VarSpec
            from_tuple_args = ""
            for component in self.components:
                class_definition += f"""
    {component.generate_variable_source(class_definitions)}"""
                from_tuple_args += f"""
            {component.type_name()}
"""
            class_definition += f"""
{self.generate_from_tuple_method()}

"""
            class_definitions.append(class_definition)
        return f"{self.name}: {self.type_name()}"

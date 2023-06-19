from dataclasses import dataclass

from dataclass_wizard import JSONWizard

from chain.abi.codegen.varspec import VarSpec


# TODO: FuncSpec should create object from tuple before returning.
# TODO: see getOptionChain

@dataclass
class FuncSpec(JSONWizard):
    inputs: list[VarSpec]
    name: str
    outputs: list[VarSpec]
    state_mutability: str
    type: str

    def __post_init__(self):
        for j, i in enumerate(self.inputs):
            i.enrich_names(f"x_{j}")
        for j, i in enumerate(self.outputs):
            i.enrich_names(f"x_{j}")

    def generate_method_source(self, class_definitions: list[str]) -> str:
        func_def = f"""
def {self.name}(
    self,"""
        kwargs = ""
        for i in self.inputs:
            kwargs += f""",
        {i.name}={i.name}"""""
            func_def += f"""
    {i.generate_variable_source(class_definitions)},"""
        return_type: str
        if not len(self.outputs):
            return_type = "None"
        else:
            for o in self.outputs:
                # capture class definitions
                o.generate_variable_source(class_definitions)
            return_type = ", ".join([o.type_name() for o in self.outputs])
            if len(self.outputs) > 1:
                return_type = f"tuple[{return_type}]"
        func_def += f"""
) -> {return_type}:
    {"" if return_type == "None" else "return "}self._call(
        "{self.name}"{kwargs}
    )
"""

        return func_def

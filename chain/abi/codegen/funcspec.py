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
        call_code = f"""self._call(
        "{self.name}"{kwargs}
    )"""
        return_code = ""
        if not len(self.outputs):
            return_type = "None"
        else:
            j: int
            my_vars: list[str] = []
            my_calcs: list[str] = []
            for j, o in enumerate(self.outputs):
                my_var = f"my_var_{j}"
                my_vars.append(my_var)
                # capture class definitions
                o.generate_variable_source(class_definitions)
                my_calcs.append(o.generate_from_tuple_call(my_var))
            return_type = ", ".join([o.type_name() for o in self.outputs])
            if len(self.outputs) > 1:
                return_type = f"tuple[{return_type}]"
            call_code = f"{', '.join(my_vars)} = {call_code}"
            return_code = "return " + ", ".join(my_calcs)
        func_def += f"""
) -> {return_type}:
    {call_code}"""
        if return_code:
            func_def += f"""
    {return_code}"""
        return func_def + """
"""

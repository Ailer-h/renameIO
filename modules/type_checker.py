from colorama import Fore
from typing import Any

class TypeChecker():

    def __init__(self) -> None:
        self.conversion_functions = {

            "bool": self.convert_to_bool,
            "int": self.convert_to_int,
            "str": self.convert_to_str

        }

    def assert_value(self, value: Any, datatype: str, default: Any) -> Any:
        if datatype not in self.conversion_functions:
            print(f"{Fore.RED}[Error]{Fore.WHITE} This conversion is invalid")
            return None
        
        if type(default) != type(value):
            print(f"{Fore.RED}[Error]{Fore.WHITE} The value and default types don't match")
            return None
        
        return self.conversion_functions[datatype](value, default)

    def convert_to_bool(self, value: str) -> bool:
        return value.lower() == "true"
    
    def convert_to_int(self, value: str, default: int = 0) -> int:
        try:
            return int(value)
        
        except TypeError:
            return default
        
    def convert_to_str(self, value: Any) -> str:
        return str(value)
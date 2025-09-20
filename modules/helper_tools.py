import re
from typing import Any
from datetime import datetime

def is_pos_is_in_list(pos: int, list: list) -> bool:
    '''
    Given an index and a list,
    it checks weather or not that index is a valid index on that list
    '''

    return 0 <= pos < len(list)

def text_to_bool(text: str) -> bool:
    '''
    Given a string, it determines the boolean value based on the
    written value.
    '''

    return text.lower() == "true"

def extract_from_brackets(text: str) -> list[str]:
    '''
    Given a string, the function returns all parameters inside curly braces
    '''
    return re.findall(r'\{([^}]*)\}', text)

def getIndex(element: Any, iterable: list | tuple | str) -> int | None:

    try:
        return iterable.index(element)
    
    except ValueError:
        return None
    
def get_now(str_format: str) -> str:
    '''
    Given a date format, it returns a date string
    If the format is invalid, it returns the default as dd/mm/yyyy
    '''


    try:
        return datetime.now().strftime(str_format)
    
    except ValueError:
        return datetime.now().strftime("%d/%m/%Y")
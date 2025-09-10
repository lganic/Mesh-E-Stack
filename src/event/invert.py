from enum import Enum
from typing import Tuple, Any, List
from .mod_types import ModType

def invert_modification(modification: Tuple[ModType, Any]):

    if modification[0] == ModType.DELETE:
        return (ModType.ADD, modification[1])
    
    raise TypeError("The modification type is not recognized for inversion")

def invert_diff(diff: List[Tuple[ModType, Any]]):

    return [invert_modification(mod) for mod in diff]
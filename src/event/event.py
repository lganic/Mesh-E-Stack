from typing import List, Tuple, Any
from .mod_types import ModType

class Event:

    def diff(self) -> List[Tuple[ModType, Any]]:
        raise NotImplementedError()
    
    def inverted_diff(self) -> List[Tuple[ModType, Any]]:
        raise NotImplementedError()
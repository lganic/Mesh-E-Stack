from typing import Set

from .event import Event
from ..objects import Vertex, Triangle
from .mod_types import ModType
from .invert import invert_diff

class AddEvent(Event):

    def __init__(self, verts: Set[Vertex] = None, tris: Set[Triangle] = None):
        super().__init__()

        if verts is None:
            verts = set()
        
        if tris is None:
            tris = set()
        
        self._verts = verts
        self._tris = tris
    
    def diff(self):

        diff = []

        for vert in self._verts:
            diff.append((ModType.ADD, vert))
        
        for tri in self._tris:
            diff.append((ModType.ADD, tri))
        
        return diff
    
    def inverted_diff(self):
        
        forward_diff = self.diff()

        return invert_diff(forward_diff)
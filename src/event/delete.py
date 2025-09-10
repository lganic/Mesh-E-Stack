from typing import Set

from .event import Event
from ..objects import Vertex, Triangle

class DeleteEvent(Event):

    def __init__(self, verts: Set[Vertex] = None, tris: Set[Triangle] = None):
        super().__init__()

        if verts is None:
            verts = set()
        
        if tris is None:
            tris = set()
        
        self._verts = verts
        self._tris = tris
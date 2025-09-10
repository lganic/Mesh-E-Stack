from typing import List

from .event import Event
from ..objects import Vertex, Triangle

class DeleteEvent(Event):

    def __init__(self, verts: List[Vertex] = [], tris: List[Triangle] = []):
        super().__init__()
        
        self._verts = verts
        self._tris = tris
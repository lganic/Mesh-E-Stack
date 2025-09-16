from typing import Set, Any

from .event import Event
from ..objects import Vertex, Triangle
from .mod_types import ModType
from .invert import invert_diff

class ModifyEvent(Event):

    def __init__(self, vertex: Vertex, from_location: Any, to_location: Any):
        self.vertex = vertex
        self.from_location = from_location
        self.to_location = to_location

    def diff(self):

        return [(ModType.MOVE, (self.vertex, self.to_location))]

    def inverted_diff(self):

        return [(ModType.MOVE, (self.vertex, self.from_location))]
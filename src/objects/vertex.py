from .tagged_object import TaggedObject
from typing import Any

class Vertex(TaggedObject):

    def __init__(self, location: Any):

        super().__init__()

        self.location = location
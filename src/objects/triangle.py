from .tagged_object import TaggedObject
from .vertex import Vertex

from typing import List

class Triangle(TaggedObject):

    def __init__(self, vertex_1: Vertex, vertex_2: Vertex, vertex_3: Vertex):

        super().__init__()

        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
    
    def bake_from_vert_list(self, vertex_list: List[Vertex]):

        index_1 = vertex_list.index(self.vertex_1)
        index_2 = vertex_list.index(self.vertex_2)
        index_3 = vertex_list.index(self.vertex_3)

        return (index_1, index_2, index_3)
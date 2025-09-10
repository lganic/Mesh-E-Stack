from .tagged_object import TaggedObject
from .vertex import Vertex

from typing import List, Set

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
    
    def uses_vertex(self, vertex: Vertex):

        '''
        Return true if this triangle uses the specified vertex
        '''

        return self.vertex_1 == vertex or self.vertex_2 == vertex or self.vertex_3 == vertex
    
    def uses_these_verts(self, set_of_verts: Set[Vertex]):

        '''
        Return true if this triangle uses any of a specified set of vertices
        '''

        vertset = set((self.vertex_1, self.vertex_2, self.vertex_3))

        return len(vertset.intersection(set_of_verts)) > 0
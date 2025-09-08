from typing import List, Tuple, Any, Set
from .tagged_object import TaggedObject
from .triangle import Triangle
from .vertex import Vertex

class Mesh(TaggedObject): # I don't think this needs to be tagged, but might be useful later

    def __init__(self, initial_verts: List[Any] = [], initial_tris:List[Tuple[int, int, int]] = []):

        super().__init__()

        self._verts: Set[Vertex] = set()
        self._tris: Set[Triangle] = set()

        self.emplace_mesh(initial_verts, initial_tris)
    
    def emplace_mesh(self, verts: List[Any] = [], tris:List[Tuple[int, int, int]] = []):
        '''
        Replace the contents of the mesh with the new mesh specified.
        '''

        self._verts.clear()
        self._tris.clear()

        vert_list = []

        for vert_location in verts:

            vert_list.append(Vertex(vert_location))

        for tri_1, tri_2, tri_3 in tris:

            triangle_obj = Triangle(
                vert_list[tri_1],
                vert_list[tri_2],
                vert_list[tri_3],
            )

            self._tris.add(triangle_obj)
        
        self._verts.update(vert_list)
    
    def fetch_mesh(self):
        '''
        Compile, and return the list of verts and tris current contained. 
        '''

        all_verts = list(self._verts)
        all_tris = [tri.bake_from_vert_list(all_verts) for tri in self._tris]

        return all_verts, all_tris    
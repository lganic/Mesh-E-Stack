from typing import List, Tuple, Any, Set
from .tagged_object import TaggedObject
from .triangle import Triangle
from .vertex import Vertex
from ..event import DeleteEvent

class Mesh(TaggedObject): # I don't think this needs to be tagged, but might be useful later

    def __init__(self, initial_verts: List[Any] = [], initial_tris:List[Tuple[int, int, int]] = []):

        super().__init__()

        self.verts: Set[Vertex] = set()
        self.tris: Set[Triangle] = set()

        self.emplace_mesh(initial_verts, initial_tris)
    
    def emplace_mesh(self, verts: List[Any] = [], tris:List[Tuple[int, int, int]] = []):
        '''
        Replace the contents of the mesh with the new mesh specified.
        '''

        self.verts.clear()
        self.tris.clear()

        vert_list = []

        for vert_location in verts:

            vert_list.append(Vertex(vert_location))

        for tri_1, tri_2, tri_3 in tris:

            triangle_obj = Triangle(
                vert_list[tri_1],
                vert_list[tri_2],
                vert_list[tri_3],
            )

            self.tris.add(triangle_obj)
        
        self.verts.update(vert_list)
    
    def fetch_mesh(self):
        '''
        Compile, and return the list of verts and tris current contained. 
        '''

        all_verts = list(self.verts)
        all_tris = [tri.bake_from_vert_list(all_verts) for tri in self.tris]

        return all_verts, all_tris
    
    def locate_vert(self, location):

        '''find the vert that has the exact location specified.
        
        I wouldn't recommend using this, its more for easier testing.'''

        for vert in self.verts:

            if vert.location == location:
                return vert
        
        return None
    
    def delete_objects(self, verts_to_remove: Set[Vertex] = None, tris_to_remove: Set[Triangle] = None, remove_orphaned_verts = True):

        '''
        Delete some objects, and return the corresponding event. 
        '''

        if verts_to_remove is None:
            verts_to_remove = set()

        if tris_to_remove is None:
            tris_to_remove = set()

        for tri in self.tris:
            if tri.uses_these_verts(verts_to_remove):
                tris_to_remove.add(tri)

        self.verts -= verts_to_remove
        self.tris -= tris_to_remove

        return DeleteEvent(verts_to_remove, tris_to_remove)

        # TODO : Remove orphaned verts if flagged to do so. 
    
    def undo_delete(self, delete_event: DeleteEvent):

        '''
        Undo a deletion event, when given the event itself. 
        '''

        self.verts = self.verts.union(delete_event._verts)
        self.tris = self.tris.union(delete_event._tris)
    
    def redo_delete(self, delete_event: DeleteEvent):

        '''
        Redo a deletion event, when given the event itself. 
        '''

        # We don't need to do any fancy checks this time, since that was done when the event was intitially generated. 

        self.verts -= delete_event._verts
        self.tris -= delete_event._tris
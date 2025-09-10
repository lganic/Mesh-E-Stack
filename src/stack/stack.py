from collections import deque
from typing import Set

from ..objects import Mesh, Vertex, Triangle
from .. import Event

class Stack:

    def __init__(self, mesh_reference: Mesh = None):

        self.undo_stack = deque()
        self.redo_stack = deque()

        if mesh_reference is None:
            mesh_reference = Mesh()

        self.mesh_reference = mesh_reference

    def _add_event(self, event: Event):
        self.undo_stack.append(event)
        self.redo_stack.clear()

    def delete(self, verts_to_remove: Set[Vertex] = None, tris_to_remove: Set[Triangle] = None, remove_orphaned_verts = True):

        self._add_event(self.mesh_reference.delete_objects(verts_to_remove = verts_to_remove, tris_to_remove = tris_to_remove, remove_orphaned_verts = remove_orphaned_verts))
from collections import deque
from typing import Set

from ..objects import Mesh, Vertex, Triangle
from .. import event as Event

class Stack:

    def __init__(self, mesh: Mesh = None):

        self.undo_stack = deque()
        self.redo_stack = deque()

        if mesh is None:
            mesh = Mesh()

        self.mesh = mesh

    def _add_event(self, event: Event):
        self.undo_stack.append(event)
        self.redo_stack.clear()

    def delete(self, verts_to_remove: Set[Vertex] = None, tris_to_remove: Set[Triangle] = None, remove_orphaned_verts = True):

        new_event = self.mesh.delete_objects(verts_to_remove = verts_to_remove, tris_to_remove = tris_to_remove, remove_orphaned_verts = remove_orphaned_verts)

        self._add_event(new_event)

        return new_event

    def undo_event(self, event: Event):

        # Add the object to the redo stack
        self.redo_stack.append(event)

        if isinstance(event, Event.DeleteEvent):
            self.mesh.undo_delete(event)

    def undo(self):

        if len(self.undo_stack) == 0:
            # Nothing left to undo. Do nothing. 

            return

        event = self.undo_stack.pop()

        self.undo_event(event)
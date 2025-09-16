from collections import deque
from typing import Set, Any

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

        return new_event.diff()
    
    def add(self, verts_to_add: Set[Vertex] = None, tris_to_add: Set[Triangle] = None):

        new_event = self.mesh.add_objects(verts_to_add = verts_to_add, tris_to_add = tris_to_add)

        self._add_event(new_event)

        return new_event.diff()
    
    def move(self, vert: Vertex, location: Any):

        new_event = self.mesh.move_vertex(vert, location)

        self._add_event(new_event)

        return new_event.diff()

    def undo_event(self, event: Event):

        # Add the object to the redo stack
        self.redo_stack.append(event)

        if isinstance(event, Event.DeleteEvent):
            self.mesh.undo_delete(event)
        
        if isinstance(event, Event.AddEvent):
            self.mesh.undo_add(event)

        if isinstance(event, Event.ModifyEvent):
            self.mesh.undo_move(event)

    def redo_event(self, event: Event):

        # Add the object to the undo stack
        self.undo_stack.append(event)

        if isinstance(event, Event.DeleteEvent):
            self.mesh.redo_delete(event)

        if isinstance(event, Event.AddEvent):
            self.mesh.redo_add(event)
        
        if isinstance(event, Event.ModifyEvent):
            self.mesh.redo_move(event)

    def undo(self):

        if len(self.undo_stack) == 0:
            # Nothing left to undo. Do nothing. 

            return

        event: Event.Event

        event = self.undo_stack.pop()

        self.undo_event(event)

        return event.inverted_diff()
    
    def redo(self):

        if len(self.redo_stack) == 0:
            # Nothing to redo. Do nothing. 

            return
        
        event: Event.Event

        event = self.redo_stack.pop()

        self.redo_event(event)

        return event.diff()

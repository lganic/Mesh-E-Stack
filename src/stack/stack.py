from collections import deque

from ..objects import Mesh

class Stack:

    def __init__(self, mesh_reference: Mesh = None):

        self.events = deque()

        if mesh_reference is None:
            mesh_reference = Mesh()

        self.mesh_reference = mesh_reference
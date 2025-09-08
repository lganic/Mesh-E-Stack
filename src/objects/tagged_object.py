from uuid import uuid4

class TaggedObject:
    
    def __init__(self):

        self.id = uuid4()
    
    def __eq__(self, other: 'TaggedObject'):

        if not isinstance(other, TaggedObject):
            raise TypeError("Unrecognized object to compare")

        return self.id == other.id

    def __hash__(self):

        return self.id.__hash__()
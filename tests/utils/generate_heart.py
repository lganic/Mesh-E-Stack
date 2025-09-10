from src import Mesh

POINTS = [
    (0, 0), 
    (1, 1),  
    (2, 0),  
    (0, -3),  
    (-2, 0),  
    (-1, 1),  
]

TRIS = [
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 5),
]

def generate_heart():

    m = Mesh()

    m.emplace_mesh(POINTS, TRIS)

    return m
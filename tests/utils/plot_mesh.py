from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...src import Mesh

from .generate_heart import generate_heart
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np

def winding_order(p1, p2, p3):
    """
    Determine winding order of three 2D points.

    Returns:
        "CCW" if counter-clockwise,
        "CW" if clockwise,
        "COLINEAR" if the points are colinear
    """
    # Compute signed area (2D cross product of vectors p1->p2 and p1->p3)
    area = (p2[0] - p1[0]) * (p3[1] - p1[1]) - \
           (p2[1] - p1[1]) * (p3[0] - p1[0])

    if area > 0:
        return "CCW"
    elif area < 0:
        return "CW"
    else:
        return "COLINEAR"


def force_cw_order(points):

    order = winding_order(points[0], points[1], points[2])

    if order == "COLINEAR":
        return points # Throw error maybe? 

    if order == "CCW":
        return points[::-1]
    
    return points

def force_cw_point_group(polys):
    return [force_cw_order(group) for group in polys]

def plot_raw_mesh(points, triangles, show = True):
    """
    Plot a 2D triangular mesh from points and triangle indices.

    Parameters:
    - points: list or numpy array of shape (N, 2), coordinates of the vertices.
    - triangles: list of triplets (i, j, k) with indices into `points`.
    """

    points = np.array(points)
    # Build list of triangle vertex coordinates
    polys = [points[list(tri)] for tri in triangles]

    polys = force_cw_point_group(polys)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Add shaded triangles
    coll = PolyCollection(polys, facecolors="lightblue", edgecolors="k", linewidths=1)
    ax.add_collection(coll)

    # Plot vertices
    ax.scatter(points[:, 0], points[:, 1], c='red', zorder=5)

    if show:
        plt.show()

    return fig

def plot_mesh(mesh: "Mesh", show = True):

    vertices, triangles = mesh.fetch_mesh()

    points = [vertex.location for vertex in vertices]

    fig = plot_raw_mesh(points, triangles, show = show)

    return fig

if __name__ == '__main__':
    
    heart = generate_heart()
    plot_mesh(heart)

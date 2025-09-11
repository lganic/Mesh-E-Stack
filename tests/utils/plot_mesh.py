from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...src import Mesh

from .generate_heart import generate_heart
import matplotlib.pyplot as plt
import numpy as np

def plot_raw_mesh(points, triangles, show = True):
    """
    Plot a 2D triangular mesh from points and triangle indices.

    Parameters:
    - points: list or numpy array of shape (N, 2), coordinates of the vertices.
    - triangles: list of triplets (i, j, k) with indices into `points`.
    """
    points = np.array(points)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for tri in triangles:
        tri_points = points[list(tri) + [tri[0]]]  # close the triangle
        ax.plot(tri_points[:, 0], tri_points[:, 1], 'k-')

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

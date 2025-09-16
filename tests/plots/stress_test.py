# The goal of this test is to give a good "stress test" adding a bunch of modifications, and undos, and redos. Then we check the most permutated state, as well as if the stack can return the graph back to the original. 

# Also I don't feel like checking the diff of each change. Might do that later. :)

import matplotlib.pyplot as plt
import pytest

from ..utils import generate_heart, plot_mesh
from src import Mesh, Stack, Event, objects

@pytest.mark.mpl_image_compare
def test_most_permute():

    mesh = generate_heart()

    st = Stack(mesh)

    new_point = objects.Vertex((0, 2))

    point_1 = st.mesh.locate_vert((-1, 1))
    point_2 = st.mesh.locate_vert((1, 1))

    triangle = objects.Triangle(new_point, point_1, point_2)

    st.move(point_1, (-2, -2))

    st.add(verts_to_add = set([new_point]), tris_to_add = set([triangle]))

    st.move(point_2, (2, -1))

    st.delete(verts_to_remove = set([point_2]))

    st.undo()

    st.delete(verts_to_remove = set([point_1]))

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig


@pytest.mark.mpl_image_compare
def test_most_permute_undo():

    mesh = generate_heart()

    st = Stack(mesh)

    new_point = objects.Vertex((0, 2))

    point_1 = st.mesh.locate_vert((-1, 1))
    point_2 = st.mesh.locate_vert((1, 1))

    triangle = objects.Triangle(new_point, point_1, point_2)

    st.move(point_1, (-2, -2))

    st.add(verts_to_add = set([new_point]), tris_to_add = set([triangle]))

    st.move(point_2, (2, -1))

    st.delete(verts_to_remove = set([point_2]))

    st.undo()

    st.delete(verts_to_remove = set([point_1]))

    fig = plot_mesh(mesh, show = False, add_lines = False)


    for _ in range(len(st.undo_stack)):
        st.undo()

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig
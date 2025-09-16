import matplotlib.pyplot as plt
import pytest

from ...utils import generate_heart, plot_mesh
from src import Mesh, Stack, Event, objects

@pytest.mark.mpl_image_compare
def test_add_one_node():

    mesh = generate_heart()

    st = Stack(mesh)

    new_point = objects.Vertex((0, 2))

    point_1 = st.mesh.locate_vert((-1, 1))
    point_2 = st.mesh.locate_vert((1, 1))

    new_triangle = objects.Triangle(new_point, point_1, point_2)

    diff = st.add(verts_to_add = set([new_point]), tris_to_add = set([new_triangle]))

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.ADD

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (0, 2)

        if isinstance(item[1], objects.Triangle):

            assert new_point in (item[1].vertex_1, item[1].vertex_2, item[1].vertex_3)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig

@pytest.mark.mpl_image_compare
def test_add_one_node_undo():

    mesh = generate_heart()

    st = Stack(mesh)

    new_point = objects.Vertex((0, 2))

    point_1 = st.mesh.locate_vert((-1, 1))
    point_2 = st.mesh.locate_vert((1, 1))

    new_triangle = objects.Triangle(new_point, point_1, point_2)

    diff = st.add(verts_to_add = set([new_point]), tris_to_add = set([new_triangle]))

    diff = st.undo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.DELETE

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (0, 2)

        if isinstance(item[1], objects.Triangle):

            assert new_point in (item[1].vertex_1, item[1].vertex_2, item[1].vertex_3)

    assert len(st.redo_stack) == 1
    assert len(st.undo_stack) == 0

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig

@pytest.mark.mpl_image_compare
def test_add_one_node_redo():

    mesh = generate_heart()

    st = Stack(mesh)

    new_point = objects.Vertex((0, 2))

    point_1 = st.mesh.locate_vert((-1, 1))
    point_2 = st.mesh.locate_vert((1, 1))

    new_triangle = objects.Triangle(new_point, point_1, point_2)

    diff = st.add(verts_to_add = set([new_point]), tris_to_add = set([new_triangle]))

    diff = st.undo()

    diff = st.redo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.ADD

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (0, 2)

        if isinstance(item[1], objects.Triangle):

            assert new_point in (item[1].vertex_1, item[1].vertex_2, item[1].vertex_3)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1
    
    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig
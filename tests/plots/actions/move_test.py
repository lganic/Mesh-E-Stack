import matplotlib.pyplot as plt
import pytest

from ...utils import generate_heart, plot_mesh
from src import Mesh, Stack, Event, objects

@pytest.mark.mpl_image_compare
def test_move_one_node():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.move(point, (-3, 2))

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.MOVE

        assert isinstance(item[1], tuple)
        assert isinstance(item[1][0], objects.Vertex)
        assert item[1][0] == point
        assert isinstance(item[1][1], tuple)
        assert item[1][1] == (-3, 2)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig

@pytest.mark.mpl_image_compare
def test_move_one_node_undo():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.move(point, (-3, 2))

    diff = st.undo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.MOVE

        assert isinstance(item[1], tuple)
        assert isinstance(item[1][0], objects.Vertex)
        assert item[1][0] == point
        assert isinstance(item[1][1], tuple)
        assert item[1][1] == (-1, 1)

    assert len(st.redo_stack) == 1
    assert len(st.undo_stack) == 0

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig

@pytest.mark.mpl_image_compare
def test_move_one_node_redo():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.move(point, (-3, 2))

    diff = st.undo()

    diff = st.redo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.MOVE

        assert isinstance(item[1], tuple)
        assert isinstance(item[1][0], objects.Vertex)
        assert item[1][0] == point
        assert isinstance(item[1][1], tuple)
        assert item[1][1] == (-3, 2)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1

    fig = plot_mesh(mesh, show = False, add_lines = False)
    return fig
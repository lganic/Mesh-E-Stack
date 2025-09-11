import matplotlib.pyplot as plt
import pytest

from ...utils import generate_heart, plot_mesh
from src import Mesh, Stack, Event, objects

@pytest.mark.mpl_image_compare
def test_delete_one_node():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.delete(verts_to_remove = set([point]))

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.DELETE

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1

    fig = plot_mesh(mesh, show = False)
    return fig

@pytest.mark.mpl_image_compare
def test_delete_and_undo_one_node():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.delete(verts_to_remove = set([point]))

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.DELETE

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    diff = st.undo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.ADD

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    assert len(st.redo_stack) == 1
    assert len(st.undo_stack) == 0

    fig = plot_mesh(mesh, show = False)
    return fig


@pytest.mark.mpl_image_compare
def test_delete_and_undo_redo_one_node():

    mesh = generate_heart()

    st = Stack(mesh)

    point = st.mesh.locate_vert((-1, 1))

    diff = st.delete(verts_to_remove = set([point]))

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.DELETE

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    diff = st.undo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.ADD

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    diff = st.redo()

    # Check that the diff is what we expect it to be. 
    for item in diff:

        assert item[0] == Event.ModType.DELETE

        if isinstance(item[1], objects.Vertex):

            assert item[1].location == (-1, 1)

    assert len(st.redo_stack) == 0
    assert len(st.undo_stack) == 1

    fig = plot_mesh(mesh, show = False)
    return fig
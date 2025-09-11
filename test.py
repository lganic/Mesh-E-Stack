from src import Mesh, Stack
from tests.utils import generate_heart, plot_mesh

mesh = generate_heart()

st = Stack(mesh)

point = st.mesh.locate_vert((-1, 1))

plot_mesh(st.mesh)

diff = st.delete(verts_to_remove = set([point]))

print(diff)

plot_mesh(mesh)

diff = st.undo()

print(diff)

plot_mesh(mesh)

diff = st.redo()

print(diff)

plot_mesh(mesh)

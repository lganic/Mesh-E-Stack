import matplotlib.pyplot as plt
import pytest

from ..utils import generate_heart, plot_mesh

@pytest.mark.mpl_image_compare
def test_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 3, 300])
    return fig

@pytest.mark.mpl_image_compare
def test_heart_plot():
    fig = plot_mesh(generate_heart(), show = False)

    return fig
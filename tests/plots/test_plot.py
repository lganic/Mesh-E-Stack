import matplotlib.pyplot as plt
import pytest

@pytest.mark.mpl_image_compare
def test_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 3, 300])
    return fig
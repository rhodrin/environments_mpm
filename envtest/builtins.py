import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'array_summary']


def rand_array(shape):
    return np.random.rand(*shape)


def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)


def my_mat_solve(A, b):
    return A.inv()*b


def array_summary(a):
    """Summary statistics (count, mean, std, min, quartiles, max) of each column of a 2D array."""
    return pd.DataFrame(a).describe()

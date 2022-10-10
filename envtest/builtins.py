import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc


__all__ = ['rand_array','smooth_image','my_mat_solve','my_pandas']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)
    
def my_mat_solve(A, b):
    return A.inv()*b

def my_pandas(s):
    return s
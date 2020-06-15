# some helper functions
import sys
import re
import imageio
import numpy

if 'pysal' not in sys.modules:
    import pysal.lib
if 'numpy' not in sys.modules:
    import numpy as np
if 'pysal.explore.esad' not in sys.modules:
    from pysal.explore import esda


def round_any(value, limit):
    return round(value/limit)*limit


# function to get image generation and rep number
def get_image_names (x):
    assert "str" in str(type(x)), "input doesn't seem to be a filepath"
    assert "landscape" in x, "input is not a foodlandscape"
    names = ((x.split("foodlandscape")[1]).split(".")[0]).split("sim")
    return names


# function to calculate the moran local using esda moran local
# here x is any numpy array
def get_moran_local(landscape_file):
    # this uses regex
    landscape = imageio.imread(landscape_file)[:,:,3]
    assert "Array" in str(type(landscape)), "input is not an array"
    nrows = landscape.shape[1]
    landsize = landscape.size
    assert landsize/nrows == nrows, "input is not square"
    w = pysal.lib.weights.lat2W(nrows, nrows)
    moran_local = esda.Moran_Local(landscape, w, permutations=3)
    return moran_local


# function to calculate the proportions of each lisa class
# the only input is a moran local object made by get_moran_local
# counting only those where p < 0.05
def get_lisa_proportions(x):
    assert "Moran_Local" in str(type(x)), "input is not a moran local object"
    x_sig = x.q[(x.p_z_sim * 2.0) < 0.05]
    x_counts = []
    for i in numpy.arange(1, 5):
        x_counts.append(numpy.count_nonzero(x_sig == i)/x_sig.size)
    return x_counts
# to do: calculate fragmentation inspired by nelson et al 2008
# basic: sum of HL and LH as prop landscape in vicinity of significantly dissimilar values


# function to return moran local as an array for plotting
def get_moran_array(x):
    assert "Moran_Local" in str(type(x)), "input is not a moran local object"
    values = numpy.array(x.q)
    landsize = values.size
    nrows = int(numpy.sqrt(landsize))
    assert nrows % 1 == 0, "input cannot be converted to a square array"
    # reshape land
    values = values.reshape(nrows, nrows)
    return values


# ends here

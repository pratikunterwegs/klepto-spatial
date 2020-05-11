# some helper functions

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
    assert "foodlandscape" in x, "input is not a foodlandscape"
    names = ((x.split("foodlandscape")[1]).split(".")[0]).split("sim")
    return names


# function to calculate the moran local using esda moran local
# here x is any numpy array
def get_moran_local(x):
    assert "Array" in str(type(x)), "input is not an array"
    nrows = x.shape[1]
    landsize = x.size
    assert landsize/nrows == nrows, "input is not square"
    w = pysal.lib.weights.lat2W(nrows, nrows)
    # x_reshape = x.reshape(landsize*landsize, 1)
    # z = lag_spatial(w, x_reshape)
    # z = z.reshape(nrows, nrows)
    moran_local = esda.Moran_Local(x, w, permutations=3)
    return moran_local


# function to calculate the proportions of each lisa class
# the only input is a moran local object made by get_moran_local
# counting only those where p < 0.05
def get_lisa_proportions(x):
    assert "Moran_Local" in str(type(x)), "input is not a moran local object"
    x_sig = x.q[(x.p_z_sim * 2.0) < 0.05]
    x_counts = []
    for i in np.arange(1, 5):
        x_counts.append(np.count_nonzero(x_sig == i)/x_sig.size)
    return x_counts


# ends here
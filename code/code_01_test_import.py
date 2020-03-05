# code to summarise simulation landscapes with Moran's I ####

# importing libraries and paths
# check python path
import sys

# should yield python 3.7 file path
for p in sys.path:
    print(p)

import pandas as pd  # similar to dplyr! yay!
import os  # has list dir functions etc
import numpy as np  # some matrix functions
import imageio
import matplotlib.pyplot as plt

# check the current working directory
os.getcwd()
currentWd = p  # os.path.dirname(os.path.abspath(__file__)) #os.getcwd()

# check again
print(currentWd)

# gather image output
outputFolder = os.path.join(currentWd, "data")  # os.path.abspath("output")
# check for the right folder
if "data" not in outputFolder:
    raise Exception('seems like the wrong output folder...')

# list files and filter by name
# gather contents of the folder
imgFiles = list()
for root, directories, filenames in os.walk(outputFolder):
    for filename in filenames:
        imgFiles.append(os.path.join(root, filename))

# filter filenames to match foodlandscape
imgFiles = list(filter(lambda x: "foodlandscape" in x, imgFiles))


# function to get image generation and rep number
def funcImgNames (x):
    assert "str" in str(type(x)), "input doesn't seem to be a filepath"
    assert "foodlandscape" in x, "input is not a foodlandscape"
    names = ((x.split("foodlandscape")[1]).split(".")[0]).split("sim")
    return names


# test one image
image = imageio.imread(imgFiles[1])[:,:,1]
image = image[0:100, 0:100]
plt.imshow(image)

import pysal.lib
from pysal.explore.esda.moran import Moran_Local

landsize = (100)
w = pysal.lib.weights.lat2W(landsize/2, landsize/2)
some_moran = Moran_Local(image, w, permutations=3)

# now reshape
some_moran = np.array(some_moran.Is).reshape(100, 100)
x = np.arange(0, 100)
y = x
x, y = np.meshgrid(x, y)

from mpl_toolkits import mplot3d
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, some_moran, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')

plt.imshow(some_moran, cmap="viridis")
plt.savefig("figs/fig_example_moran_local.png")

# ends here

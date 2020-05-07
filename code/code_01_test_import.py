# code to summarise simulation landscapes with Moran's I ####

# importing libraries and paths
# check python path
import sys

# should yield python 3.7 file path
for p in sys.path:
    print(p)

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
imgFiles = list(filter(lambda x: "landscape" in x, imgFiles))


# function to get image generation and rep number
def funcImgNames (x):
    assert "str" in str(type(x)), "input doesn't seem to be a filepath"
    assert "foodlandscape" in x, "input is not a foodlandscape"
    names = ((x.split("foodlandscape")[1]).split(".")[0]).split("sim")
    return names


# test one image
resources = imageio.imread(imgFiles[1])[:,:,3]
# image = np.multiply(image, 500)
# image = image[100:300, 100:300]
plt.imshow(resources, cmap='viridis')
plt.colorbar()

# agents
foragers = imageio.imread(imgFiles[1])[:,:,2]
# image = np.multiply(image, 500)
# image = image[100:300, 100:300]
plt.imshow(foragers, cmap='cividis')
plt.colorbar()

import pysal.lib
from pysal.explore.esda.moran import Moran_Local
from pysal.lib.weights.spatial_lag import lag_spatial

landsize = (128)
w = pysal.lib.weights.lat2W(landsize, landsize)
image = image.reshape(landsize*landsize, 1)
z = lag_spatial(w, image)
z = z.reshape(landsize, landsize)
some_moran = Moran_Local(image, w, permutations=3)

# now reshape
some_moran = np.array(some_moran.q).reshape(128, 128)
x = np.arange(0, 128)
y = x
x, y = np.meshgrid(x, y)

plt.imshow(some_moran, cmap=plt.get_cmap('viridis', 4))
plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
cbar = plt.colorbar(ticks=[1,2,3,4], label='LISA class')
cbar.ax.set_yticklabels(['HH', 'LH', 'LL', 'HL'])

plt.savefig("figs/fig_example_moran_local_quadrant.png", dpi=300)

# ends here

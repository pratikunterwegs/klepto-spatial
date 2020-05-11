# code to summarise simulation landscapes with Moran's I ####

# importing libraries and paths
# check python path
import sys
from helper_functions import get_lisa_proportions
# should yield python 3.7 file path
for p in sys.path:
    print(p)

import os  # has list dir functions etc
import numpy as np  # some matrix functions
import imageio
import matplotlib
# may need to use the tkagg backend on some unix systems
matplotlib.use("TkAgg")
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

# test one image
resources = imageio.imread(imgFiles[1])[:,:,3]
# image = np.multiply(image, 500)
# image = image[100:300, 100:300]
plt.imshow(resources, cmap='hot')
plt.colorbar()
plt.show()



# now reshape
some_moran = np.array(tmp.Is).reshape(128, 128)
x = np.arange(0, 128)
y = x
x, y = np.meshgrid(x, y)

plt.imshow(some_moran, cmap=plt.get_cmap('viridis', 4))
plt.colorbar()
plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
cbar = plt.colorbar(ticks=[1,2,3,4], label='LISA class')
cbar.ax.set_yticklabels(['HH', 'LH', 'LL', 'HL'])

plt.savefig("figs/fig_example_moran_local_quadrant.png", dpi=300)

# ends here

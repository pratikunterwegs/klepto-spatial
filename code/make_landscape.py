from nlmpy import nlmpy
import matplotlib.pyplot as plt
import numpy as np
import imageio

# make zero array with centre as 1
b = np.zeros([100,100]).astype(int)
b[50,50] = 1
c = nlmpy.mpd(nRow=100, nCol=100, h=0.75)
c = np.interp(c, (c.min(), c.max()), (0, 255)).astype(int)
# make distance gradient as int of 0 - 255
a = nlmpy.distanceGradient(source=b)
a = np.interp(a, (a.min(), a.max()), (0, 255)).astype(int)
land = np.stack((b,b,a,c), axis=-1)
# save as png
imageio.imsave("test_small.png",land)

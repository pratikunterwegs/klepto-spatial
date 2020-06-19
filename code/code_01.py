# code to summarise simulation landscapes with Moran's I ####

# importing libraries and paths
# check python path
import sys
# should yield python 3.7 file path
for p in sys.path:
    print(p)

import os  # has listdir functions etc
import numpy as np  # some matrix and numerical functions
import imageio  # library to read images
import matplotlib  # import plotting library
import matplotlib.pyplot as plt  # assign a keyword
import seaborn as sns  # another plotting library
import re  # import regular expressions library
import pandas as pd  # import the dataframes library

from helper_functions import get_moran_local, get_lisa_proportions

# may need to use the tkagg backend on some unix systems
matplotlib.use("TkAgg")

# check the current working directory
p = os.getcwd()
currentWd = p
# check again
print(currentWd)

# gather image output
outputFolder = os.path.join(currentWd, "data")  # os.path.abspath("output")
# check for the right folder
if "data" not in outputFolder:
    raise Exception('seems like the wrong output folder...')


# gather the folders in the directory avoiding zip files
data_folders = os.listdir(outputFolder)
data_folders = list(filter(lambda x: "landscape" in x and ".zip" not in x, data_folders))

# here we go through all the subfolders in the data folder and
# list the files in those folders in the order of the generations
list_of_lists_images = []  # each element of the list is a 'run' or a replicate
for folder in data_folders:  # go through each run folder
    this_folder = os.path.join(outputFolder, folder)  # get the filepath to that folder
    for root, directories, filenames in os.walk(this_folder): # now look at all the files in that folder
        these_images = []
        for filename in filenames:
            these_images.append(os.path.join(root, filename))
        # sort the images in order of generations
        these_images.sort()
        these_images = list(filter(lambda x: "landscape" in x, these_images))
        list_of_lists_images.append(these_images)


# define a function to count the agents in each layer
# we also want to know which generation we are dealing with
def count_agents(landscape_file):
    # this uses regex
    replicate = int(re.findall(r'sim(\d{3})', landscape_file)[0])  # which run is it
    generation = int(re.findall(r'\\(\d{5})', landscape_file)[0])  # get the generation as an integer
    landscape = imageio.imread(landscape_file)
    # get the numbers of klepts, handlers, and foragers
    n_klepts = landscape[:,:,0].sum()
    n_handlers = landscape[:,:,1].sum()
    n_foragers = landscape[:,:,2].sum()
    total = n_klepts+n_foragers+n_handlers
    return [replicate, generation, n_klepts/total, n_handlers/total, n_foragers/total]


# map count agents over the folders
list_of_data = []
for i in list_of_lists_images:
    i = i[0::5]  # operate on every 5th generation
    print(len(i))
    tmp_list = list(map(count_agents, i))
    tmp_moran = list(map(get_moran_local, i))
    tmp_lisa = list(map(get_lisa_proportions, tmp_moran))
    tmp_data = list(map(lambda x, y: x + y, tmp_list, tmp_lisa))
    list_of_data.append(tmp_data)


# make single df
data = list(map(lambda x: pd.DataFrame(x, columns=['rep', 'gen', 'p_klepts',
                                     'p_handlers', 'p_forager',
                                     'HH', 'LH', 'LL', 'HL']),
                list_of_data))

# join all the data into a single dataframe
data = pd.concat(data)
data.gen = pd.Series([item for sublist in [np.arange(0, 1000, 5)]*25 for item in sublist])
data_pivot = pd.melt(data, id_vars=["gen", "rep"])


# write data to file
data_pivot.to_csv("data/data_strategy_lisa_generations.csv", index=False)

# now plot the strategies over the generations in facets
data_pivot = data_pivot.loc[data_pivot['variable'].isin(['p_klepts', 'p_forager', 'p_handlers', 'LH'])]

plt.rcParams["font.family"] = "Arial"
fig_strategy_generations = sns.FacetGrid(data_pivot[data_pivot.rep <= 5], col="rep",
                    hue='variable',
                    palette=['xkcd:red', 'xkcd:green', 'xkcd:blue', 'xkcd:purple'],
                    col_wrap = 5)
fig_strategy_generations = fig_strategy_generations.map(sns.lineplot, "gen", "value",
               linewidth = 1).add_legend()

fig_strategy_generations.savefig(fname='figs/fig_example_strategy_per_gen.png',
                                 dpi=300,
                                 quality=90)

# plot the relation between LISA classes and proportion of strategies
data_landscape_x = pd.melt(data.drop(columns=['gen','HH', 'LL', 'HL']),
                           id_vars=['rep', 'LH'],
                           value_name='p_strategy',
                           var_name='behav_strategy')
# data_landscape_x = pd.melt(data_landscape_x,
#                            id_vars=['rep', 'p_strategy', 'behav_strategy'],
#                            var_name = 'lisa_class',
#                            value_name = 'p_landscape')

# write data to file
data_landscape_x.to_csv("data/data_strategy_behaviour_landscape.csv", index=False)

fig_strategy_landscape = sns.FacetGrid(data_landscape_x, row="behav_strategy",
                                       hue='behav_strategy',
                                       palette=['xkcd:red', 'xkcd:green', 'xkcd:blue'])
fig_strategy_landscape = fig_strategy_landscape.map(plt.scatter,
                                                    'LH', 'p_strategy',s=0.1)

fig_strategy_landscape.savefig(fname='figs/fig_example_strategy_landscape.png',
                                 dpi=300,
                                 quality=90)

# ends here


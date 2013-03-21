# Loads data from molecular friction simulation (stored in .csv files)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

FRAME_RATE = 60

def circle(xy, radius, color="lightsteelblue", facecolor="green", alpha=.6, ax=None):

    e = plt.Circle(xy=xy, radius=radius)
    if ax is None:
        ax = plt.gca()
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_edgecolor(color)
    e.set_linewidth(3)
    e.set_facecolor(facecolor)
    e.set_alpha(alpha)



# x = pd.read_csv('aX_k100/x.csv', index_col=0).values    # read x.csv into a pandas DataFrame and then convert to a numpy array
# y = pd.read_csv('aX_k100/y.csv', index_col=0).values    # x/y are 2D numpy arrays -> x[timestep, particle]

# you can also get velocities, accelerations, aD, aX, aS and avg_sled_velocity_x:

# vx = pd.read_csv('vx.csv', index_col=0).values        # must add path ex: aX_k100/... for these
# vy = pd.read_csv('vy.csv', index_col=0).values

# ax = pd.read_csv('ax.csv, index_col=0).values
# ay = pd.read_csv('ay.csv, index_col=0).values

# aD_x = pd.read_csv('aD_x.csv', index_col=0).values
# aD_y = pd.read_csv('aD_y.csv', index_col=0).values

# aX_x = pd.read_csv('N9_W0.0/aX_x.csv', index_col=0).values
# aX_y = pd.read_csv('aX_y.csv', index_col=0).values

# aS_x = pd.read_csv('aS_x.csv', index_col=0).values
# aS_y = pd.read_csv('aS_y.csv', index_col=0).values

# avg_sled_vx = pd.read_csv('N9_W0.0/avg_sled_v_x.csv', index_col=0).values

#plt.clf()
#plt.plot(avg_sled_vx)
#plt.show()
# cheap animation below:

# setup the plot
#plt.figure(1)
#plt.clf()
#plt.ion()
#plt.xlim((0, 20.))
#plt.ylim((0, 20.))
#plt.grid()
#ax = plt.gca()
#plt.show()

# animation
#for timestep in range(np.size(x[:,0])):
#    if timestep % FRAME_RATE == 0:
#
#        for particle in range(np.size(x[0])):
#            circle((x[timestep, particle], y[timestep, particle]), radius=0.5*2**(1/6.), ax=ax, facecolor='green')
#
#        plt.draw()
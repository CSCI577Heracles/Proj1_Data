import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

def fit_mu():
    # for each N, for each W:
        # store Fs (max aX_x), W & N
        # plot Fs vs. W
        # find  slope, slope = mu

    LIST_OF_Ns = [9]
    LIST_OF_Ws = [-10.0, 0.0, 10.0, 20.0, 30.0, 40.0]

    # dict{ W: Fs}

    W_list = []
    Fs_list = []

    N = LIST_OF_Ns[0] # loop once has mult N

    for W in LIST_OF_Ws:
        path = "N" + str(N) + "_W" + str(W) + "/"
        aX_x = pd.read_csv(path + 'aX_x.csv', index_col=0).values
        W_list.append(W)
        Fs_list.append(np.amax(aX_x))

    x = np.array(W_list)
    y = np.array(Fs_list)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    print "slope: " + str(slope)
    print "intercept: " + str(intercept)
    print "r_value: " + str(r_value)
    print "p_value: " + str(p_value)
    print "std_err: " + str(std_err)

    plt.ion()
    plt.plot(x,y)
    plt.show()

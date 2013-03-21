import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import math

def fit_mu():
    # for each N, for each W:
        # store Fs (max aX_x), W & N
        # plot Fs vs. W
        # find  slope, slope = mu
    plt.ion()
    plt.clf()
    plt.xlabel('W')
    plt.ylabel("F_s")

    LIST_OF_Ns = [9, 13, 17]
    LIST_OF_As = [5, 7, 9]
    LIST_OF_Ws = [-10.0, 0.0, 10.0, 20.0, 30.0, 40.0]

    # dict{ W: Fs}



    mu_list = []

    #N = LIST_OF_Ns[0] # loop once has mult N
    print "---------------------------------------"
    print "|     Regression for F_s = mu * W     |"
    print "---------------------------------------"
    for N in LIST_OF_Ns:
        W_list = []
        Fs_list = []
        for W in LIST_OF_Ws:
            path = "N" + str(N) + "_W" + str(W) + "/"
            aX_x = pd.read_csv(path + 'aX_x.csv', index_col=0).values
            W_list.append(W)
            Fs_list.append(np.amax(aX_x))

        x = np.array(W_list)
        y = np.array(Fs_list)
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

        print "============= N = " + str(N) + "================"
        print "slope: " + str(slope)
        print "intercept: " + str(intercept)
        print "r_value: " + str(r_value)
        print "p_value: " + str(p_value)
        print "std_err: " + str(std_err)
        print "------------------------------------------------------"

        plt.plot(x,y, label='N = ' + str(N))
        plt.legend(loc='upper left')

        #plt.show()

        mu_list.append(slope)

    for mu in mu_list:
        print "mu: " + str(mu)

    mu = np.mean(mu_list)
    print "Average mu = " + str(mu)

    plt.figure(2)
    plt.ion()
    plt.clf()
    plt.xlabel('A')
    plt.ylabel("F_s")

    c_list = []

    print "-------------------------------------------"
    print "|   Regression for F_s = mu * W + c * A   |"
    print "-------------------------------------------"

    for W in LIST_OF_Ws:
        #print "W: " + str(W)
        A_list = []
        Fs_list = []
        for A in LIST_OF_As:
            pathN = A * 2 - 1
            path = "N" + str(pathN) + "_W" + str(W) + "/"
            aX_x = pd.read_csv(path + 'aX_x.csv', index_col=0).values
            A_list.append(A)
            Fs_list.append(np.amax(aX_x))
            #print "A_list: " + str(A_list)
            #print "F_s: " + str(Fs_list)

        x = np.array(A_list)
        y = np.array(Fs_list)
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        c_list.append(slope)
        print "============= W = " + str(W) + "================"
        print "slope: " + str(slope)
        print "intercept: " + str(intercept)
        print "r_value: " + str(r_value)
        print "p_value: " + str(p_value)
        print "std_err: " + str(std_err)
        print "------------------------------------------------------"

        plt.plot(x,y, label='W = ' + str(W))
        plt.legend(loc='upper left')


    print "============="
    print "c = " + str(np.mean(c_list))

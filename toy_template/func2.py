
# Sample a random number based on cdf
# cdf has 2 columns: x, F(x)
import numpy as np
from numpy.random import random_sample
def sample_cdf(cdf):
    while 1:
        x = random_sample()
#        idx = (np.abs(cdf[:,1]-x)).argmin()
#        if cdf[idx, 0]<75:
#            break
#    return cdf[idx, 0]
        d = np.interp(x, cdf[:,1], cdf[:,0])
        # Note d is in 200mas
        if d<75:
            break
    return d

def sample_cdf2(cdf):
    cdf = np.append(np.array([[0,0]]), cdf, axis=0)
    while 1:
        x = random_sample()
        d = np.interp(x, cdf[:,1], cdf[:,0])
        if d<75:
            break
    return d

def sample_cdf3(cdf):
    edges = cdf[:,0] + (cdf[1,0]-cdf[0,0])/2
    edges = np.append(cdf[0,0] - (cdf[1,0]-cdf[0,0])/2, edges)
    cdf = np.append(np.array([[0,0]]), cdf, axis=0)
    while 1:
        x = random_sample()
        d = np.interp(x, cdf[:,1], edges)
        if d<75:
            break
    return d
        

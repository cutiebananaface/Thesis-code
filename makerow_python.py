# Generated with SMOP  0.41
# from libsmop import *
# makerow.m
#status: rewritten(complete)
import numpy as np

def makerow(f=None):
   

    g=np.size(f, axis=None)
# makerow.m:2
    if np.min[g] > 1:
        g
        raise Exception('not row-able')
    
    if (g[1] > g[2]):
        f=f['T']
# makerow.m:8
    
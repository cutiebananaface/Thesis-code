# Generated with SMOP  0.41
# from libsmop import *
# isItTimeToQuit.m
#status: rewritten(complete)
import numpy as np

def isItTimeToQuit(elapsedtime=None,bestp=None,searchtimes=None):

    yesorno=0
# isItTimeToQuit.m:2
    for i in np.arange(1,np.size(searchtimes, axis=None)).reshape(-1):
        thisPair=searchtimes[i]
# isItTimeToQuit.m:4
        thisTime=thisPair(1)
# isItTimeToQuit.m:5
        thisLimit=thisPair(2)
# isItTimeToQuit.m:6
        if (elapsedtime > thisTime) and (bestp < thisLimit):
            yesorno=1
# isItTimeToQuit.m:8
    
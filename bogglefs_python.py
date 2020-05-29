# Generated with SMOP  0.41
# from libsmop import *
# bogglefs.m
from numpy import *
import math

def bogglefs(fs=None,*args,**kwargs):


    #returns fs that only appear once. like words in scoring boggle.
#bogglefs([1 2 3]) returns [1 2 3]
#bogglefs([1 2 2 3]) returns [1 3]
    is_=arange(1,size(fs))
# bogglefs.m:5
    fs=sort(fs)
# bogglefs.m:6
    diffs=diff(fs)
# bogglefs.m:7
    matches=np.where(diffs == 0)
# bogglefs.m:8
    fs[matches]=math.inf
# bogglefs.m:9
    fs[matches + 1]=math.inf
# bogglefs.m:10
    oldis=is_[math.inf < math.inf]
# bogglefs.m:11
    newfs=fs[fs < math.inf]
# bogglefs.m:12
    return newfs, oldis
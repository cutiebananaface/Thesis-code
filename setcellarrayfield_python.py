# Generated with SMOP  0.41
# from libsmop import *
# setcellarrayfield.m
from numpy import *
    

def setcellarrayfield(cellarray=None,fieldname=None,fieldvalue=None,*args,**kwargs):

    for i in arange(1,size(cellarray)).reshape(-1):
        thisp=cellarray[i]
# setcellarrayfield.m:4
        thisp=setfield(thisp,fieldname,fieldvalue)
# setcellarrayfield.m:5
        cellarray[i]=thisp
# setcellarrayfield.m:6
    return cellarray
    
# Generated with SMOP  0.41
# from libsmop import *
# fancystickies.m
from copy import *

def fancystickies(*args,**kwargs):


    dcmObj=copy(datacursormode)
# fancystickies.m:2
    
    ##   data cursor mode object 
    set(dcmObj,'UpdateFcn',fancycallback) #not sure what the equivalent function is
    
    ##   function so it uses updateFcn.m
    
    return
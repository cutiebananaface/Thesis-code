# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:38:50 2020

@author: rodri
"""
#status: rewritten (complete) needs to fix index

# Generated with SMOP  0.41
#from libsmop import *
from scipy import interpolate
# countfrommcounttool.m

    

def countfrommcounttool(counttool,h):

    #typical use is:
# for h = s.allhs
#     linecount = countfrommcounttool(s.counttool,h);
#     s.pvalprefactor = s.pvalprefactor * (linecount * 1.5);
# end
    
    if type(counttool) is not dict:
        count=1
        return count
# countfrommcounttool.m:9
        
    
    if h < min(counttool['hvalues']):
        h=min(counttool['hvalues'])
# countfrommcounttool.m:13
    
    count= interpolate.interp1d(counttool['hvalues'],counttool['countvalues'])
    # print(count)
    # print('h',h)
    # print(count(h))
    count=count(h)
    return count
# countfrommcounttool.m:15
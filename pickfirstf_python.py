# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:07:18 2020

@author: rodri
"""
import numpy as np

def pickfirstf(kit,d):
    
    fs = kit['onedpeakfsunassigned']
    hs = kit['onedpeakhsunassigned']
     
    frange = max(fs) - min(fs)
    fmin = min(fs) + 0.1* frange
    fmax = min(fs)  + 0.6*frange
    imin_temp=np.array((fs>fmin).nonzero())
    imin=imin_temp[0,0]
    imax_temp=np.array((fs>fmax).nonzero())
    imax=imax_temp[0,0]
    possf = fs[imin:imax]
    possh = hs[imin:imax]
    sorth=np.sort(possh)[::-1]
    X_i= possh.argsort()[::-1]
    
    if d > 2000: #interpret as a frequency
        ferrs = abs(fs - d)
    #    [mind besti] = min(ferrs);  %replaces my old besti code! amazing!
        mind, besti = ferrs.min(0),ferrs.argmin(0)
        fstart = fs[besti]
        hstart = hs[besti]
        istart = besti
  
        rank_temp=np.array((sorth<hstart).nonzero())
        rank=rank_temp[0,0]
     
        if np.size(rank, axis=None) == 0:
            rank = 0
        return fstart, hstart, istart, rank
            
    frange= fs[-1]-fs[0]
    fmin = fs[0] + frange/100
    fmax = fs[0] + 0.6*frange
    imin_temp=np.array((fs>fmin).nonzero())
    imin=imin_temp[0,0]
    imax_temp=np.array((fs>fmax).nonzero())
    imax=imax_temp[0,0]
    possf = fs[imin:imax]
    possh = hs[imin:imax]
    sorth=np.sort(possh)[::-1]
    X_i= possh.argsort()[::-1]
    
    if d < 1:
        d = 1 + np.floor(np.random.uniform() *np.size(possh, axis=None))
        
    d = min(d, np.size(possh, axis=None))
    besti = X_i[d-1] #subtract to move the index back by 1 
    fstart = possf[besti]
    hstart = possh[besti]
    istart = besti + imin ; ## these two i am unsure
    rank = d ## these two i am unsure
    return  fstart, hstart, istart, rank

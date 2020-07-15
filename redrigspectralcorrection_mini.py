# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:44:14 2020

@author: rodri
"""


# function [fs,hs] = redrigspectralcorrection(fs,rawhs)
# % [fs XI] = sort(fs);
# % rawhs = rawhs(XI);
# if max(fs) < 10000
#     hs = rawhs;
#     return;
# end


# envfreqs = 1000 * ...
#     [7 7.5 8  8.5 9  9.5 10  10.5 11  11.5 12  12.5  13  13.5 14  14.5 15  15.5 16  16.5 17  17.5 18  18.5 19  19.5 20   20.5 21 23 26];

# envamps = ...
#    [6 6  6 4  3  2   1.5  1.5   1.5   1.5    1  1    1    1    1    1   1    1    1   1   1    2   3   4   3  4    5  25 45 45 45];

# ampenv = interp1(envfreqs,envamps,fs,'linear','extrap');
# hs = rawhs .* ampenv;
# hs = hs * mean(rawhs) / mean(hs);
from scipy import interpolate
import numpy as np

def redrigspectralcorrection(fs, rawhs):
    if max(fs) <1000:
        hs = rawhs
        return 
    envfreqs = 1000 * [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 23, 26]
    envamps = [6, 6, 6, 4, 3, 2, 1.5, 1.5, 1.5, 1.5, 1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 3, 4, 5, 25, 45, 45, 45]
    ampenv= interpolate.interp1d( envfreqs, envamps, fill_value='extrapolate')
    hs= rawhs * ampenv
    hs= hs * np.mean(rawhs)/ np.mean(hs)
    return fs, hs
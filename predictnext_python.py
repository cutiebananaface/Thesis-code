# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:39:57 2020

@author: rodri
"""
#status: ported(complete)
# Generated with SMOP  0.41
#from libsmop import *
import numpy as np
# predictnext.m
from loadmatlab_workspace import load_mat
import copy as copy

# before= load_mat("before-predictnext-angelica")
# fullsquare= before['fullsquare']
# whichcorner= before['whichcorner']
def predictnext(fullsquare,whichcorner):
    '''
    c1, c2 are hard coded values in RAARR and they are unchanged in this verison, however their value should be adjusted
    whenever they are being used as an index
    '''
    coords={}
    coords['islegal'] = copy.copy(1)
# predictnext.m:2
    coords['isrecommended'] = 0
# predictnext.m:3
    coords['inrange'] = copy.copy(0)
# predictnext.m:4
    coords['fdist'] = copy.copy(10000000000.0)
# predictnext.m:5
    coords['whichcorner'] = copy.copy(whichcorner)
# predictnext.m:6
    energiesknown= abs(fullsquare['energies'][:,0] * fullsquare['energies'][:,1])
# predictnext.m:7
    energiesknown= np.where(energiesknown>1e-10)
# predictnext.m:8
    toprow=max(energiesknown[0])
# predictnext.m:9
    bottomrow=min(energiesknown[0])
# predictnext.m:10
    if 'ur' == whichcorner:
        r1=copy.copy(toprow)
# predictnext.m:13
        c1=4 # may need to reduce its index 
# predictnext.m:14
        c2=2
# predictnext.m:15
    else:
        if 'ul' == whichcorner:
            r1= copy.copy(toprow)
# predictnext.m:17
            c1=1
# predictnext.m:18
            c2=3
# predictnext.m:19
        else:
            if 'dr' == whichcorner:
                r1=bottomrow - 1
# predictnext.m:21
                c1=4
# predictnext.m:22
                c2=3
# predictnext.m:23
            else:
                if 'dl' == whichcorner:
                    r1=bottomrow - 1
# predictnext.m:25
                    c1=1
# predictnext.m:26
                    c2=2
# predictnext.m:27
    
    r2= copy.copy(r1)
# predictnext.m:29
    # raise Exception('whichcorner not yet implemented');
    
    if r1 == 0:
        1
    #this is where matlab differs
    #c1 and c2 are hardcoded, so a -1 one is needed to adjust for python
    if (r1 == 0) or (fullsquare['fgrid'][r1,c1-1] != 0) or (fullsquare['fgrid'][r2,c2-1] != 0):
        coords['islegal'] = copy.copy(0)
# predictnext.m:36
        coords['isrecommended'] = copy.copy(0)
# predictnext.m:37
        return coords
    
    nextcolumn= copy.copy(c1)
# predictnext.m:41
    nextrow= copy.copy(r1)
# predictnext.m:42
    nextline= fullsquare['nextline']
# predictnext.m:43
    correction=np.dot(fullsquare['templatenorm'][nextline],fullsquare['f1'])
# predictnext.m:45
    #uses a polynomial fit to extend the series f.
#this thing explodes when extending series of length one.  In this mode, if
#tightmode is turned on, it uses fs(1) + bplusc as a first guess
#if nothing is found, returns [[] []];
    # newseriesset= []
# predictnext.m:50
    if 1 == nextcolumn:
        s=fullsquare['column1']
# predictnext.m:54
    else:
        if 2 == nextcolumn:
            s=fullsquare['column2']
# predictnext.m:56
        else:
            if 3 == nextcolumn:
                s=fullsquare['column3']
# predictnext.m:58
            else:
                if 4 == nextcolumn:
                    s=fullsquare['column4']
# predictnext.m:60
    
    upordown=- 1
# predictnext.m:62
    if (nextrow <= np.size(s['fs'])) and (nextrow > 0) and (s['fs'][nextrow] != 0):
        1
        raise Exception('looking for a line I already have!')
    
    if (nextrow > 1) and (s['fs'][nextrow - 1] != 0):
        upordown=1
# predictnext.m:68
    
    if (nextrow < np.size(s['fs'])) and (s['fs'][nextrow + 1] != 0):
        upordown=0
# predictnext.m:71
    
    #f_allowed = s['tolerance;
    
    if ((c1 == 4) and (c2 == 2)) or ((c1 == 1) and (c2 == 3)):
        energydiff= fullsquare['energies'][r1,0] - fullsquare['energies'][r1,1]
# predictnext.m:77
        if (fullsquare['energies'][r1,0] == 0) or (fullsquare['energies'][r1,1] == 0):
            1
            raise Exception('energies below are not known')
    
    if ((c1 == 4) and (c2 == 3)) or ((c1 == 1) and (c2 == 2)):
        energydiff= fullsquare['energies'][r1 + 1,1] - fullsquare['energies'][r1 + 1,0]
# predictnext.m:84
        if (fullsquare['energies'][r1 + 1,0] == 0) or (fullsquare['energies'][r1 + 1,1] == 0):
            1
            raise Exception('energies above are not known')
    
    if c1 == 1:
        energydiff= -1 * energydiff
# predictnext.m:91
    
    if upordown == -1:
        if fullsquare['column1']['fs'][nextrow] != 0:
            predictf=fullsquare['column1']['fs'][nextrow]
# predictnext.m:97
        else:
            predictf=fullsquare['column4']['fs'][nextrow]
# predictnext.m:99
        if (nextcolumn == 2) or (nextcolumn == 3):
            fthresh=fullsquare['abtolerance']
# predictnext.m:102
        else:
            fthresh=fullsquare['aatolerance']
# predictnext.m:104
    else:
        n= np.size(s['realfs'])
# predictnext.m:107
        if n == 1:
            if upordown == 1:
                predictf=s['realfs'] + fullsquare['bpluscguess']
# predictnext.m:112
            else:
                predictf=s['realfs'] - fullsquare['bpluscguess']
# predictnext.m:114
            if (nextcolumn == 2) or (nextcolumn == 3):
                fthresh=np.dot(fullsquare['bpluscerror'],4)
# predictnext.m:117
            else:
                fthresh=np.dot(fullsquare['bpluscerror'],2)
# predictnext.m:119
        else:
            #         x = 1:n;
#         y = s['realfs;
#         polydegree = min(2,n-1);
#         [p] = polyfit(x,y,polydegree);
    #    fthresh = f_allowed(n);
            if upordown == 1:
                predictf=s['nextf']
# predictnext.m:128
                fthresh=s['nextfspread']
# predictnext.m:129
            else:
                predictf=s['prevf']
# predictnext.m:133
                fthresh=s['prevfspread']
# predictnext.m:134
                #             fthresh = f_allowed(n);
#         #    predictf2 = s['prevf;
    
    #if n == 0  #first line in a series..
    if fullsquare['usecorrection'] == 1:
        predictf=predictf + correction
# predictnext.m:142
    
    predictf2=predictf - energydiff
# predictnext.m:144
    minf=predictf - fthresh
# predictnext.m:145
    maxf=predictf + fthresh
# predictnext.m:146
    meanf= np.mean(np.array([predictf,predictf2], dtype=float))
# predictnext.m:148
    if (predictf < fullsquare['frecommendedmax']) and (predictf > fullsquare['frecommendedmin']) and (predictf2 < fullsquare['frecommendedmax']) and (predictf2 > fullsquare['frecommendedmin']):
        coords['inrange'] = copy.copy(1)
# predictnext.m:151
        coords['isrecommended'] = copy.copy(1)
# predictnext.m:152
        meanrange= np.mean(np.array((fullsquare['frecommendedmax'],fullsquare['frecommendedmin'])))
# predictnext.m:153
        coords['fdist'] = copy.copy(abs(meanf - meanrange))
# predictnext.m:154
    
    coords['r1'] = copy.copy(r1)
# predictnext.m:156
    coords['r2'] = copy.copy(r2)
# predictnext.m:157
    coords['c1'] = copy.copy(c1)
# predictnext.m:158
    coords['c2'] = copy.copy(c2)
# predictnext.m:159
    coords['f1'] = copy.copy(predictf)
# predictnext.m:160
    coords['f2'] = copy.copy(predictf2)
# predictnext.m:161
    coords['energydiff'] = copy.copy(energydiff)
# predictnext.m:162
    coords['minf'] = copy.copy(minf)
# predictnext.m:163
    coords['maxf'] = copy.copy(maxf)
# predictnext.m:164
    return coords


# output=predictnext(fullsquare, whichcorner)
# print('done :D')
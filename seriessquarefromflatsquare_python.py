# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:55:25 2020

@author: rodri
"""
#status: rewritten, not run yet
from updateseries_python import updateseries
import numpy as np
import math as math
from copy import *
from scipy import interpolate
#import operator as op
from predictnext_python import predictnext
from countfrommcounttool_python import countfrommcounttool
from loadmatlab_workspace import load_mat
from updateseriessquare_python_temp import updateseriessquare

# before=load_mat('before_seriessquarefromflatsquare-nopinone')
# flatsquare=before['flatsquare']
# flipd=before['flipd']
def seriessquarefromflatsquare(flatsquare, flipd=0):
#function s = seriessquarefromflatsquare(flatsquare,flipd)
#%a series square has three series which add up.  Series 1 is always
#%represented twice.  For example, series1(n) + series1(n+1) - series2(n) -
#%series3(n) = 0 for any n.  Series1 must be one longer than any other
#%series

#%the argument flatsquare is four frequencies[' f1 and f2 are assumed to be
#%the series  this is reasonable given how we found the square, but might
#%not be correct. Wait! this is a trap. two squares can be unique, as
#%defined by uniquesquares, but different, as seen by this function. Hm. ok.
#%
#%the central call we want to make eventually is
#%extendseriesbyone(s,allfs,allhs). This will let us extend the square by
#%one, either up or down..

    s={}
    s['flatsquare'] = flatsquare 
    series={}
    series1={}
    series2={}
    series3={}
    series4={}
    series1['fs'] = copy(flatsquare['fs'][0:2]) 
    series1['hs'] = copy(flatsquare['hs'][0:2]) 
    if flipd == 0:
        series2['fs'] = np.array([flatsquare['fs'][2], 0]) 
        series2['hs'] = np.array([flatsquare['hs'][2], 0]) 
        series3['fs'] = np.array( [0, flatsquare['fs'][3] ]) 
        series3['hs'] = np.array([0, flatsquare['hs'][3]]) 
    else:
        series2['fs'] = np.array([flatsquare['fs'][3], 0]) 
        series2['hs'] = np.array([flatsquare['hs'][3], 0])  
        series3['fs'] = np.array([0, flatsquare['fs'][2]]) 
        series3['hs'] = np.array([0, flatsquare['hs'][2]]) 

    series4['fs'] = [0, 0] 
    series4['hs'] = [0, 0] 
    series1['frange'] = copy(flatsquare['frange']) 
    series2['frange'] = copy(flatsquare['frange']) 
    series3['frange'] = copy(flatsquare['frange']) 
    series4['frange'] = copy(flatsquare['frange']) 

    dsigns = np.array([1, 1, -1, -1]) 
    slantupsigns = np.array([1, -1, -1, 1]) 


    s['signs'] = copy(flatsquare['signs']) 
    s['flipped'] = 0 

##stopped here
    if np.linalg.norm(s['signs'] - dsigns,2) == 0:  #dtype
        s['flattype'] = 'D' 
        s['dtype'] = 1 
        s['column1'] = copy(series1) 
        s['column2'] = copy(series2) 
        s['column3'] = copy(series3) 
        s['column4'] = copy(series4) 
    else:
        s['dtype'] = 0 
        if np.linalg.norm(s['signs'] - slantupsigns,2) == 0:  #%slantup
            s['column2'] = copy(series1) 
            s['column1'] = copy(series2) 
            s['column4'] = copy(series3) 
            s['column3'] = copy(series4) 
            s['flattype'] = '/' 
        else:
            s['column3'] = copy(series1) 
            s['column4'] = copy(series2) 
            s['column1'] = copy(series3) 
            s['column2'] = copy(series4) 
            s['flattype'] = "\\"
        
#     end 
# end
    s['usecorrection'] = flatsquare['usecorrection'] 
    s['laddermode'] = flatsquare['laddermode'] 
    s['signs'] = flatsquare['signs']   #%these are [S1(1) S1(2) S2(1) S3(1)]
    s['tightnesssettings'] = flatsquare['tightnesssettings'] 
    s['counttool'] = flatsquare['counttool'] 
    s['ordercutoff'] = 100 
    s['frange'] = flatsquare['frange'] 
    s['closedout'] = 0 
    # %s['secondsigns'] = [0, 0, 0, 0]    %these are [S1(1) S2(1) S3(1) S4(1)]
    s['originalf1'] = flatsquare['fs'][0] 
    # s['flatdescriptor'] = flatsquare['descriptor'] 
    # s['originstring'] = flatsquare['originstring'] 
    s['forcecorners'] = flatsquare['forcecorners'] 
    s['cornermap'] = flatsquare['cornermap'] 
    s['templateabsolute'] =  flatsquare['templateabsolute'] 
    s['templatenorm'] =  flatsquare['templatenorm'] 
    s['upterminated'] = 0 
    s['downterminated'] = 0 

    s['highsidetolerance'] = flatsquare['tightnesssettings']['highsidetolerance']  
    s['lowsidetolerance'] = flatsquare['tightnesssettings']['lowsidetolerance'] 
    s['btolerance'] = s['highsidetolerance'] * 0  
    s['aatolerance'] = flatsquare['tightnesssettings']['aatolerance'] 
    s['abtolerance'] = flatsquare['tightnesssettings']['abtolerance'] 

    #%s['atolerance(2)'] = s['atolerance(2) * 2 

    s['column1'] = settolerance(s['column1'],flatsquare['tightnesssettings'],'a',1) 
    s['column2'] = settolerance(s['column2'],flatsquare['tightnesssettings'],'b',2) 
    s['column3'] = settolerance(s['column3'],flatsquare['tightnesssettings'],'b',3) 
    s['column4'] = settolerance(s['column4'],flatsquare['tightnesssettings'],'a',4) 

    #% s['column1.type = 'a' 
    #% s['column1.highsidetolerance = s['highsidetolerance 
    #% s['column1.lowsidetolerance = s['lowsidetolerance 
    #% s['column2.type = 'b' 
    #% s['column2.highsidetolerance = s['highsidetolerance 
    #% s['column2.lowsidetolerance = s['lowsidetolerance 
    #% s['column3.type = 'b' 
    #% s['column3.highsidetolerance = s['highsidetolerance 
    #% s['column3.lowsidetolerance = s['lowsidetolerance 
    #% s['column4.type = 'a' 
    #% s['column4.highsidetolerance = s['highsidetolerance 
    #% s['column4.lowsidetolerance = s['lowsidetolerance 
    #
    #% s['column1.whichcolumn = 1 
    #% s['column2.whichcolumn = 2 
    #% s['column3.whichcolumn = 3 
    #% s['column4.whichcolumn = 4 
    s['frecommendedmin'] = flatsquare['frecommendedmin'] 
    s['frecommendedmax'] = flatsquare['frecommendedmax'] 


    s = updateseriessquare(s) 
    #%s['fgrid
    1
    return s


def settolerance(column,tightnesssettings,type1,whichcolumn):
    column['type'] = type1 
    column['highsidetolerance'] = tightnesssettings['highsidetolerance'] 
    column['lowsidetolerance'] = tightnesssettings['lowsidetolerance'] 
    column['lowjthresh'] = tightnesssettings['lowjthresh'] 
    column['whichcolumn'] = whichcolumn 
    return column

# output= seriessquarefromflatsquare(flatsquare, flipd)
# print('hewwo')
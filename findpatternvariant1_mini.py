# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:54:59 2020

@author: rodri
"""


# Generated with SMOP  0.41
# from libsmop import *
# findpatternvariant1.m

#status: rewritten(complete)
import numpy as np
from copy import *
from addsquaresfromlines_mini import addsquaresfromline

def findpatternvariant1(kit=None):
    
    #called by findallspecies.  this does the variant 1 described in the RAARR
#paper
    
    kit['candidateScaffolds'] = np.array([])
# findpatternvariant1.m:5
    
#     starttime=copy(now)
# # findpatternvariant1.m:8
#     kit['speciesStarttime'] = copy(starttime)
# # findpatternvariant1.m:9
#     kit['startCensus'] = copy(kit['totalCensus'])
# findpatternvariant1.m:10
    if kit['cheatCodes']['forcef1'] == 0:
        linestouse=kit['tightnesssettings']['lines']
# findpatternvariant1.m:12
    else:
        linestouse=kit['cheatCodes']['forcef1']
# findpatternvariant1.m:14
    
    for i in np.arange(1,np.size(linestouse,axis=None)).reshape(-1):
        linetouse=linestouse(i)
# findpatternvariant1.m:18
        kit=addsquaresfromline(kit,linetouse)
# findpatternvariant1.m:19
#         elapsedTime=dot((now - starttime),100000.0)
# # findpatternvariant1.m:20
#         timeToQuit=isItTimeToQuit(elapsedTime,kit['bestScaffoldp'],kit['tightnesssettings']['ladderSearchtimes'])
# # findpatternvariant1.m:21
#         if (kit['bogged'] == 1) or (timeToQuit == 1):
#             break
    
#     candidatePatterns=np.array([])
# # findpatternvariant1.m:26
#     for i in np.arange(1,np.size(kit['candidateScaffolds'], axis=None)).reshape(-1):
#         candidatePatterns[i]=patternFromScaffold(kit['candidateScaffolds'][i])
# # findpatternvariant1.m:28
    
#     kit['scaffoldEndtime'] = copy(now)
# # findpatternvariant1.m:30
#     if length(kit['candidateScaffolds']) == 0:
#         phase1report=sprintf('no scaffolds found, ran to line %d',i)
# # findpatternvariant1.m:32
#     else:
#         phase1report=sprintf('%d scaffolds, best scaffold %s, quads %s',np.size(kit['candidateScaffolds'], axis=None),kit['candidateScaffolds'][1]['pvalstring'],kit['candidateScaffolds'][1]['longquadstring'])
# # findpatternvariant1.m:34
    
    

# def patternFromScaffold(scaffold=None):
#     # varargin = patternFromscaffold['varargin
#     # nargin = patternFromscaffold['nargin

#     pattern['fgrid'] = copy(scaffold['usablefgrid'])
# # findpatternvariant1.m:39
    
#     pattern['pval'] = copy(scaffold['netpval'])
# # findpatternvariant1.m:40
    
#     pattern['patternType'] = copy('scaffold')
# # findpatternvariant1.m:41
    
#     pattern['archive'] = copy(scaffold)
# # findpatternvariant1.m:42
    
#     pattern['descriptor'] = copy(sprintf('scaffold, %s',scaffold['shortpvalstring']))
# # findpatternvariant1.m:43
    
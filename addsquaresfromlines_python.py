# Generated with SMOP  0.41
# from libsmop import *
# addsquaresfromline.m
#status: rewritten(complete)
import numpy as np
from pickfirstf_python import pickfirstf
from sortcellarraybyfield_python import sortcellarraybyfield
from extractfieldsfromcellarray_python import extractfieldsfromcellarray
from updateseries_python import updateseries
from predictnext_python import predictnext
from countfrommcounttool_python import countfrommcounttool
from loadmatlab_workspace import load_mat
from updateseriessquare_python_temp import updateseriessquare
from getflatsquares_python import getflatsquares
from seriessquarefromflatsquare_python import seriessquarefromflatsquare
# extendseriessquarealltheway.m
from loadmatlab_workspace import load_mat
from copy import *
    
# before=load_mat('input-addsquaresfromlines-nopinone')
# kit= before['kit']
# linetouse= before['linetouse']
def addsquaresfromline(kit=None,linetouse=None):
    
    f1=pickfirstf(kit,linetouse)
# addsquaresfromline.m:3
    
    newsquares,searchreport=squaresfromline(kit,linetouse)
# addsquaresfromline.m:4
    
    kit['searchedf1s'].append(f1)
# addsquaresfromline.m:8
    if searchreport['bogged'] == 0:
        kit=addtrialsquarestokit(kit,newsquares)
# addsquaresfromline.m:10
        kit['totalflatsquares'] = copy(kit['totalflatsquares'] + searchreport['numflatsquares'])
# addsquaresfromline.m:11
        kit['totalCensus'] = copy(kit['totalCensus'] + searchreport['census'])
# addsquaresfromline.m:12
    
    

def sortScaffolds(candidateScaffolds=None):

    newScoffoldList=np.array([])
# addsquaresfromline.m:16
    hashesUsed=np.array([])
# addsquaresfromline.m:17
    candidateScaffolds=sortcellarraybyfield(candidateScaffolds,'netpval','ascend')
# addsquaresfromline.m:18
    for i in np.arange(1,np.size(candidateScaffolds, axis=None)).reshape(-1):
        thisScaffold=candidateScaffolds[i]
# addsquaresfromline.m:20
        thisHash=thisScaffold['gridhash']
# addsquaresfromline.m:21
        if hashesUsed not in thisHash:
            newScoffoldList.append(thisScaffold)
# addsquaresfromline.m:23
            hashesUsed.append(thisHash)
# addsquaresfromline.m:24
    
    
    

def addtrialsquarestokit(kit=None,newsquares=None,):

    if np.size(newsquares, axis=None) > 0:
        newsquares=sortcellarraybyfield(newsquares,'netpval','ascend')
# addsquaresfromline.m:30
        numsquares=min(kit['tightnesssettings']['maxsquaresfromline'],np.size(newsquares,axis=None))
# addsquaresfromline.m:31
        for i in np.arange(1,numsquares).reshape(-1):
            thissquare=newsquares[i]
# addsquaresfromline.m:33
            kit['candidateScaffolds'].append(thissquare)
# addsquaresfromline.m:34
        kit['candidateScaffolds'] = copy(sortScaffolds(kit['candidateScaffolds']))
# addsquaresfromline.m:36
    
    if np.size(kit['candidateScaffolds']) == 0:
        kit['bestScaffoldp'] = copy(1)
# addsquaresfromline.m:39
    else:
        kit['bestScaffoldp'] = copy(kit['candidateScaffolds'][1]['netpval'])
# addsquaresfromline.m:41
    
    
    

def squaresfromline(kit=None,linetouse=None):

    ts=kit['tightnesssettings']
# addsquaresfromline.m:46
    # ts['starttime'] = copy(now)
# addsquaresfromline.m:47
    searchReport= {}
    searchReport['bogged'] = copy(0)
# addsquaresfromline.m:49
    searchReport['numflatsquares'] = copy(0)
# addsquaresfromline.m:50
    finalsquares= np.array([])
# addsquaresfromline.m:52
    allsquares,kit,f1=getflatsquares(kit,linetouse,ts)
# addsquaresfromline.m:56
    fs=kit['usefs']
# addsquaresfromline.m:57
    hs=kit['usehs']
# addsquaresfromline.m:58
    seriessquares=np.array([])
# addsquaresfromline.m:59
    searchReport['numflatsquares'] = copy(np.size(allsquares))
# addsquaresfromline.m:61
    for i in np.arange(1,np.size(allsquares)).reshape(-1):
        output_s= seriessquarefromflatsquare(allsquares[i],0)
        seriessquares= np.append(seriessquares, output_s)
# addsquaresfromline.m:63
        if seriessquares[-1]['dtype'] and kit['Dinverted']:
            # seriessquares.append(seriessquarefromflatsquare(allsquares[i],1))
            seriessquares= np.append(seriessquares, seriessquarefromflatsquare(allsquares[i],1))
# addsquaresfromline.m:65
    
    
    if np.size(seriessquares) > ts.flatsquarelimit:
        fprintf('%d is far too many flatsquares\\n',np.size(seriessquares))
        searchReport['bogged'] = copy(1)
# addsquaresfromline.m:72
        return finalsquares,searchReport
    
    if linetouse > 5000:
        if np.size(seriessquares) < 3:
            for i in np.arange(1,np.size(seriessquares)).reshape(-1):
                print(seriessquares[i]['bestfstring'])
                showseriessquare(seriessquares[i],kit)
                1 ##ask steve about this 
        1
    
    
    1
    #  seriessquares = {seriessquares{2}};
    seriessquares,bogged,census=extendseriessquarealltheway(seriessquares,fs,hs)
# addsquaresfromline.m:89
    searchReport['census'] = copy(census)
# addsquaresfromline.m:90
    if bogged == 1:
        searchReport['bogged'] = copy(1)
# addsquaresfromline.m:92
        return finalsquares,searchReport
    
    allps=extractfieldsfromcellarray(seriessquares,np.array(['netpval','testable']))
# addsquaresfromline.m:96
    alltests=allps['testable']
# addsquaresfromline.m:97
    allps=allps['netpval']
# addsquaresfromline.m:98
    for i in np.arange(1,np.size(seriessquares)).reshape(-1):
        s=seriessquares[i]
# addsquaresfromline.m:103
        if s['testable'] == 1:
            numps=np.size(np.where(alltests == 1))
# addsquaresfromline.m:106
            if s['netpval'] == min(allps):
                fprintf('adding %d squares from %3.1f of degree %d, pval %3.2e\\n',numps,s.originalf1,s.degree,s.netpval)
            finalsquares.append(s)
# addsquaresfromline.m:110
    
    finalsquares=sortcellarraybyfield(finalsquares,'netpval','ascend')
# addsquaresfromline.m:113
    if ts['trimends']:
        finalsquares=trimends(finalsquares)
# addsquaresfromline.m:115
    
    finalsquares=removeidentical(finalsquares)
# addsquaresfromline.m:117
    

def identicalseries(s1=None,s2=None):
    # varargin = identicalseries.varargin
    # nargin = identicalseries.nargin

    yesorno=1
# addsquaresfromline.m:120
    if (np.size(s1['fgrid'][:,1]) != np.size(s2['fgrid'](np.arange(),1))):
        yesorno=0
# addsquaresfromline.m:122
        return yesorno
    
    

def removeidentical(slist=None):

    newlist=np.array([])
# addsquaresfromline.m:127
    for i in np.arange(1,np.size(slist)).reshape(-1):
        isindy=1
# addsquaresfromline.m:129
        for j in np.arange(1,np.size(newlist)).reshape(-1):
            if identicalseries(slist[i],newlist[j]):
                isindy=0
# addsquaresfromline.m:132
        if isindy:
            sortfs=sort(slist[i]['allfs'])
# addsquaresfromline.m:136
            if min(diff(sortfs)) > 0.01:
                newlist.append(slist[i])
# addsquaresfromline.m:139

# output = addsquaresfromline(kit,linetouse)
# Generated with SMOP  0.41
from libsmop import *
# findSeriesPairsFromSpectrum.m
#status: rewritten(complete)
import numpy as np
import copy

def findSeriesPairsFromSpectrum(kit=None):
 

    if kit['cheatCodes']['forcef1'] == 0:
        linestouse=kit['tightnesssettings']['variant3']['lines']
# findSeriesPairsFromSpectrum.m:4
    else:
        linestouse=kit['cheatCodes']['forcef1']
# findSeriesPairsFromSpectrum.m:6
    
    if ('forcek' in kit['cheatCodes']) and (np.size(kit['cheatCodes']['forceka'])>0):
        katouse=kit['cheatCodes']['forceka']
# findSeriesPairsFromSpectrum.m:9
    else:
        katouse=kit['tightnesssettings']['variant3']['kaguesses']
# findSeriesPairsFromSpectrum.m:11
    
    allSeriesPairs={}
# findSeriesPairsFromSpectrum.m:14
    for ka in katouse.reshape(-1):
        #first find f0 lines
        #newSeriesPairs = seriesPairsFromLine(kit,linestouse,ka);
        newSeriesPairs=seriesPairsFromLineDepthfirst(kit,linestouse,ka)
# findSeriesPairsFromSpectrum.m:20
        allSeriesPairs=findUniqueSeriesPairs(np.concatenate((allSeriesPairs,newSeriesPairs)))
# findSeriesPairsFromSpectrum.m:21
    return allSeriesPairs
    
###################
def seriesPairsFromLineDepthfirst(kit=None,linestouse=None,ka=None):

    global ALLEVERTRIED
    seriesPairs=[]
# findSeriesPairsFromSpectrum.m:26
    for ll in linestouse.reshape(-1):
        newPairs,babyKit=babySeriesFromLine(kit,ll,ka)
# findSeriesPairsFromSpectrum.m:28
        seriesPairs=np.concatenate((seriesPairs,newPairs))
# findSeriesPairsFromSpectrum.m:29
    
    seriesPairs=sortcellarraybyfield(seriesPairs,'pval')
# findSeriesPairsFromSpectrum.m:31
    
    ALLEVERTRIED={}
# findSeriesPairsFromSpectrum.m:33
    seriesPairs=setPairListField(seriesPairs,'searchf0',0)
# findSeriesPairsFromSpectrum.m:35
    seriesPairs,alltried=extendAllf1Series(seriesPairs,babyKit)
# findSeriesPairsFromSpectrum.m:37
    
    
    seriesPairs=firstn(seriesPairs,babyKit['ts']['maxtof0'])
# findSeriesPairsFromSpectrum.m:40
    showPairList(seriesPairs)
    seriesPairs=setPairListField(seriesPairs,'searchf0',1)
# findSeriesPairsFromSpectrum.m:43
    
    
    seriesPairs,alltried=extendAllf1Series(seriesPairs,babyKit)
# findSeriesPairsFromSpectrum.m:46
    ALLEVERTRIED=addkeys(alltried,ALLEVERTRIED)
# findSeriesPairsFromSpectrum.m:47
    seriesPairs=firstn(seriesPairs,babyKit['ts']['maxPatterns'])
# findSeriesPairsFromSpectrum.m:48
    1
    return seriesPairs
    
 #########################   
def addkeys(smalldict=None,bigdict=None):

    k=smalldict.keys()
# findSeriesPairsFromSpectrum.m:53
    for i in np.arange(1,np.size(k)).reshape(-1):
        thiskey=k[i]
# findSeriesPairsFromSpectrum.m:55
        bigdict[thiskey]=smalldict[thiskey]
# findSeriesPairsFromSpectrum.m:56
    return bigdict
    
    
    
    
    
    

def setPairListField(cellarray=None,fieldname=None,fieldvalue=None):
    varargin = setPairListField.varargin
    nargin = setPairListField.nargin

    for i in np.arange(1,np.size(cellarray)).reshape(-1):
        thisp=cellarray[i]
# findSeriesPairsFromSpectrum.m:64
        thisp=setfield(thisp,fieldname,fieldvalue)
# findSeriesPairsFromSpectrum.m:65
        thisp['seenBefore'] = copy(0)
# findSeriesPairsFromSpectrum.m:66
        thisp=updateSeriesPair(thisp)
# findSeriesPairsFromSpectrum.m:67
        cellarray[i]=thisp
# findSeriesPairsFromSpectrum.m:68
    return cellarray
    
    

def seriesPairsFromLine(kit=None,linestouse=None,ka=None):
    

    seriesPairs=[]
# findSeriesPairsFromSpectrum.m:72
    for ll in linestouse.reshape(-1):
        newPairs,babyKit=babySeriesFromLine(kit,ll,ka,nargout=2)
# findSeriesPairsFromSpectrum.m:74
        seriesPairs=np.concatenate((seriesPairs,newPairs))
# findSeriesPairsFromSpectrum.m:75
    
    alltried={}
# findSeriesPairsFromSpectrum.m:77
    seriesPairs=setcellarrayfield(seriesPairs,'searchf0',0)
# findSeriesPairsFromSpectrum.m:79
    seriesPairs=extendAllf1Series(seriesPairs,babyKit,alltried)
# findSeriesPairsFromSpectrum.m:80
    seriesPairs=firstn(seriesPairs,babyKit['ts']['maxtof0'])
# findSeriesPairsFromSpectrum.m:81
    showPairList(seriesPairs)
    seriesPairs=setcellarrayfield(seriesPairs,'searchf0',1)
# findSeriesPairsFromSpectrum.m:84
    seriesPairs=extendAllf1Series(seriesPairs,babyKit,alltried)
# findSeriesPairsFromSpectrum.m:86
    seriesPairs=firstn(seriesPairs,babyKit['ts']['maxPatterns'])
# findSeriesPairsFromSpectrum.m:87
    1
    return seriesPairs
    

def babySeriesFromLine(kit=None,ll=None,ka=None):


    babySeriesList={}
# findSeriesPairsFromSpectrum.m:91
    fstart,hstart,istart,rank=pickfirstf(kit,ll)
# findSeriesPairsFromSpectrum.m:92
    print(f"{kit['molename']},jumping into series from f={fstart}, rank {rank}, height {hstart}\\n'")

    fs=kit['onedpeakfs']
# findSeriesPairsFromSpectrum.m:95
    hs=kit['onedpeakhs']
# findSeriesPairsFromSpectrum.m:96
    counttool=makecounttool(hs)
# findSeriesPairsFromSpectrum.m:98
    ts=kit['tightnesssettings']['variant3']
# findSeriesPairsFromSpectrum.m:99
    ts.gapmax = copy.copy(min(ts['gapmax'],(kit['maxf'] - kit['minf']) / (ts['minlines'] - 1)))
# findSeriesPairsFromSpectrum.m:101
    hthresh=hstart / ts['atolerance']
# findSeriesPairsFromSpectrum.m:102
    highenough=np.where(hs > hthresh)
# findSeriesPairsFromSpectrum.m:103
    babyKit['fs'] = copy.copy(fs[highenough])
# findSeriesPairsFromSpectrum.m:104
    babyKit['hs'] = copy.copy(hs[highenough])
# findSeriesPairsFromSpectrum.m:105
    maxheight=max(hs)
# findSeriesPairsFromSpectrum.m:106
    minheight=min(hs)
# findSeriesPairsFromSpectrum.m:107
    babyKit['ts'] = copy.copy(ts)
# findSeriesPairsFromSpectrum.m:108
    babyKit['cheatCodes'] = copy.copy(kit['cheatCodes'])
# findSeriesPairsFromSpectrum.m:109
    hthresh=hstart / ts['babytolerance']
# findSeriesPairsFromSpectrum.m:110
    highenough=np.where(hs > hthresh)
# findSeriesPairsFromSpectrum.m:112
    fs=fs[highenough]
# findSeriesPairsFromSpectrum.m:113
    hs=hs[highenough]
# findSeriesPairsFromSpectrum.m:114
    f2options=choosef2s(fs,fstart,ts,kit['cheatCodes'])
# findSeriesPairsFromSpectrum.m:116
    for jj in f2options.reshape(-1):
        freqs =np.sort(np.concatenate((fstart,fs[jj])))
        XI= np.argsort(np.concatenate((fstart,fs[jj])))
# findSeriesPairsFromSpectrum.m:119
        if ((freqs[2] - freqs[1]) > ts['gapmin']) and ((freqs[2] - freqs[1]) < ts['gapmax']):
            heights=np.concatenate((hstart,hs(jj)))
# findSeriesPairsFromSpectrum.m:121
            heights=heights[XI]
# findSeriesPairsFromSpectrum.m:122
            babyseries['f1Freqs'] = copy.copy(freqs)
# findSeriesPairsFromSpectrum.m:124
            babyseries['f1Heights'] = copy.copy(heights)
# findSeriesPairsFromSpectrum.m:125
            babyseries['maxheight'] = copy.copy(maxheight)
# findSeriesPairsFromSpectrum.m:126
            babyseries['minheight'] = copy.copy(minheight)
# findSeriesPairsFromSpectrum.m:127
            babyseries['maxf'] = copy.copy(kit['maxf'])
# findSeriesPairsFromSpectrum.m:128
            babyseries['minf'] = copy.copy(kit['minf'])
# findSeriesPairsFromSpectrum.m:129
            babyseries['ts'] = copy.copy(ts)
# findSeriesPairsFromSpectrum.m:130
            babyseries['ka'] = copy.copy(ka)
# findSeriesPairsFromSpectrum.m:131
            babyseries['searchf0'] = copy.copy(0)
# findSeriesPairsFromSpectrum.m:132
            babyseries['countTool'] = copy.copy(counttool)
# findSeriesPairsFromSpectrum.m:133
            #         babyseries.firsth = hstart;
            babyseries['firstRank'] = copy.copy(rank)
# findSeriesPairsFromSpectrum.m:136
            babyseries['originString'] = copy.copy(print(f"origin f= {fstart}, rank {rank}, height {hstart} \n"))
# findSeriesPairsFromSpectrum.m:137
            1
            if (max(heights) / min(heights)) < ts['babyatolerance']:
                try:
                    newSeries=updateSeriesPair(babyseries)
# findSeriesPairsFromSpectrum.m:141
                    babySeriesList.append(newSeries)
# findSeriesPairsFromSpectrum.m:142
                except:
                    print(f"skipping series {babyseries['originString']} {babyseries['f1Freqs'][1]} {babyseries['f1Freqs'][2]}")
    
    babySeriesList=sortcellarraybyfield(babySeriesList,'pval')
# findSeriesPairsFromSpectrum.m:149
    return babySeriesList,babyKit


def choosef2s(fs=None,firstline=None,ts=None,cheatCodes=None):

    minjj1=np.where(fs > (firstline - ts['gapmax']))[0]
# findSeriesPairsFromSpectrum.m:153
    maxjj1=np.where(fs > (firstline - ts['gapmin']))[0]
# findSeriesPairsFromSpectrum.m:154
    minjj2=np.where(fs > (firstline + ts['gapmin']))[0]
# findSeriesPairsFromSpectrum.m:155
    maxjj2=np.where(fs > (firstline + ts['gapmax']))[0]
# findSeriesPairsFromSpectrum.m:156
    if np.size(maxjj2) == 0:
        maxjj2=np.size(fs)
# findSeriesPairsFromSpectrum.m:158
    
    if np.size(minjj1) == 0:
        minjj1=1
# findSeriesPairsFromSpectrum.m:161
    
    f2options=np.concatenate((minjj1:maxjj1,minjj2:maxjj2))
# findSeriesPairsFromSpectrum.m:163
    if ('forcef2' in cheatCodes) and (cheatCodes['forcef2'][1]>0):
        f2options=np.array([])
# findSeriesPairsFromSpectrum.m:165
        for i in np.arange(1,np.size(cheatCodes.forcef2)).reshape(-1):
            f=cheatCodes['forcef2'][i]
# findSeriesPairsFromSpectrum.m:167
            ferrs=abs(fs - f)
# findSeriesPairsFromSpectrum.m:168
            f2options.append(np.where(ferrs == min(ferrs))[0])
# findSeriesPairsFromSpectrum.m:169
    return f2options
    
    
    
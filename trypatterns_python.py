# Generated with SMOP  0.41
# from libsmop import *
# trypatterns.m
from numpy import *
from copy import *
from settingsfromtightness_python import settingsfromtightness
from resetSPFITCOUNT_python import resetSPFITCOUNT

def trypatterns(kit=None,patternlist=None,*args,**kwargs):

    outputfit=0
# trypatterns.m:2
    bestqualityyet=0
# trypatterns.m:3
    if 'tightnesssettings' not in kit:
        kit['tightnesssettings'] = copy(settingsfromtightness(1))
# trypatterns.m:5
    
    numtotry=min(size(patternlist),kit['tightnesssettings']['patternfitting']['maxpatterns'])
# trypatterns.m:7
    resetSPFITCOUNT()
    for j in arange(1,numtotry).reshape(-1):
        thisPattern=patternlist[j]
# trypatterns.m:12
        print('trying %d/%d patterns, starting with %s\\n'% (j,numtotry,thisPattern['descriptor']))
        thisPattern['attemptIndex'] = copy(j)
# trypatterns.m:14
        foundFit=tryPattern(thisPattern,kit)
# trypatterns.m:16
        quality=foundFit['quality']
# trypatterns.m:18
        if quality > bestqualityyet:
            outputfit=copy(foundFit)
# trypatterns.m:20
            bestqualityyet=copy(quality)
# trypatterns.m:21
            if foundFit['yesvotes'] > kit.tightnesssettings['greathitvotecount']:
                break
    
    if type(outputfit) is dict:
        outputfit['spfitcount'] = copy(getSPFITCOUNT())
# trypatterns.m:29
    return outputfit
    
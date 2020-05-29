# Generated with SMOP  0.41
# from libsmop import *
# findpatternbowties.m
from numpy import *
    

def findpatternbowties(kit=None,*args,**kwargs):
 

    kit['tightnesssettings']['bowties']['weakAorB'] = copy(false)
# findpatternbowties.m:2
    fgridsf,timesf=findbowties(kit,10)
# findpatternbowties.m:3
    kit['tightnesssettings']['bowties']['weakAorB'] = copy(true)
# findpatternbowties.m:4
    fgridst,timest=findbowties(kit,10)
# findpatternbowties.m:5
    times,IX=sort(array([timesf,timest])), argsort(IX)
# findpatternbowties.m:6
    frgids=hstack(fgridsf, fgridst)
# findpatternbowties.m:7
    fgrids=fgrids[IX]
# findpatternbowties.m:8
    N=size(times)
# findpatternbowties.m:9
    hashes=zeros((1,N))
# findpatternbowties.m:10
    for j in arange(1,N).reshape(-1):
        hashes[j]=sum(sum(fgrids[j]))
# findpatternbowties.m:12
    
    __,IH=unique(hashes,'stable')
# findpatternbowties.m:14
    fgrids=fgrids[IH]
# findpatternbowties.m:15
    times=times[IH]
# findpatternbowties.m:16
    N=size(times)
# findpatternbowties.m:17
    candidatePatterns=empty(1,N)
# findpatternbowties.m:18
    for j in arange(1,N).reshape(-1):
        candidatePatterns[j]['fgrid'] = copy(fgrids[j])
# findpatternbowties.m:20
        candidatePatterns[j]['pval'] = copy(dot(times[j],1e-09))
# findpatternbowties.m:21
        candidatePatterns[j]['patternType'] = copy('bowties')
# findpatternbowties.m:22
        candidatePatterns[j]['archive'] = copy([])
# findpatternbowties.m:23
        candidatePatterns[j]['descriptor'] = copy('copyright 2019 RAARR')
# findpatternbowties.m:24
    
    1
    return candidatePatterns
    
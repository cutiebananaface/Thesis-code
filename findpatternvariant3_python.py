# Generated with SMOP  0.41
# from libsmop import *
# findpatternvariant3.m
#status: rewrittenn (complete)
import numpy as np
    

def findpatternvariant3(kit=None):
    

    #called by findallspecies.  this does the original a-series algorithm. to
#my knowledge it only works on hexanal.
    candidatePatterns=[]
# findpatternvariant3.m:4
    allseriespairs=findSeriesPairsFromSpectrum(kit)
# findpatternvariant3.m:5
    numtotry=findNumToTry(allseriespairs)
# findpatternvariant3.m:6
    if numtotry == 0:
        phase1report='No candidate a-series patterns found'
# findpatternvariant3.m:9
        return candidatePatterns,phase1report
    
    phase1report=print(f"found total of {np.size(allseriespairs)} series from {allseriespairs[1]['pval']}, trying {numtotry}\\n")
# findpatternvariant3.m:12
    print(phase1report)
    for i in np.arange(1,numtotry).reshape(-1):
        candidatePatterns.append(patternFromSeriesPair(allseriespairs[i]))
# findpatternvariant3.m:16
        1
    return candidatePatterns, phase1report
    
    

def patternFromSeriesPair(s=None):
    

    pattern['fgrid'][:,1]=s['fgrid'][:,1]
# findpatternvariant3.m:22
    
    pattern['fgrid'][:,4]=s['fgrid'][:,2]
# findpatternvariant3.m:23
    pattern['pval'] = copy.copy(s['pval'])
# findpatternvariant3.m:24
    
    pattern['patternType'] = copy.copy('aTypes')
# findpatternvariant3.m:25
    
    pattern['archive'] = copy.copy(s)
# findpatternvariant3.m:26
    
    pattern['descriptor'] = copy.copy(print(f"seriesPair, {s['residualString']}"))
# findpatternvariant3.m:27
    return pattern
    
    

def findNumToTry(thisSeriesList=None):

    if np.size(thisSeriesList) == 0:
        n=0
# findpatternvariant3.m:31
        return n
    
    ts=thisSeriesList[1]['ts']
# findpatternvariant3.m:34
    pvals=extractonefieldfromcellarray(thisSeriesList,'pval')
# findpatternvariant3.m:35
    qualified=length(find(pvals < ts.maxPval))
# findpatternvariant3.m:37
    n=min(ts['maxPatterns'],qualified)
# findpatternvariant3.m:38
    return n
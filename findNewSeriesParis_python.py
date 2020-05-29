# Generated with SMOP  0.41
# from libsmop import *
# findNewSeriesPairs.m
#status: rewritten complete
    

def findNewSeriesPairs(seriesList=None,oldDict=None):
    

    for i in np.arange(1,np.size(seriesList)).reshape(-1):
        thisSeries=seriesList[i]
# findNewSeriesPairs.m:4
        if thisSeries['hashInt'] in oldDict:
            thisSeries['seenBefore'] = copy(1)
# findNewSeriesPairs.m:6
            seriesList[i]=thisSeries
# findNewSeriesPairs.m:7
        else:
            oldDict[thisSeries['hashInt']]=1
# findNewSeriesPairs.m:9
    return seriesList,oldDict
# Generated with SMOP  0.41
# from libsmop import *
# findUniqueSeriesPairs.m
#status: rewritten(complete)
    

def findUniqueSeriesPairs(seriesList=None):
    

    newSeriesList=[]
# findUniqueSeriesPairs.m:2
    dict1={0:0}
# findUniqueSeriesPairs.m:3
    numfound=0
# findUniqueSeriesPairs.m:4
    for i in np.arange(1,np.size(seriesList)).reshape(-1):
        thisSeries=seriesList[i]
# findUniqueSeriesPairs.m:6
        if thisSeries['hashInt'] not in dict1:
            dict1[thisSeries['hashInt']]=1
# findUniqueSeriesPairs.m:8
            newSeriesList.append(thisSeries)
# findUniqueSeriesPairs.m:9
            numfound=numfound + 1
# findUniqueSeriesPairs.m:10
    
    newSeriesList=sortcellarraybyfield(newSeriesList,'pval')
    return newSeriesList
# findUniqueSeriesPairs.m:13
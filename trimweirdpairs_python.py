from numpy import *
def trimweirdpairs(pairlist):
	outpairs = []
	for (i = 1:length(pairlist))
	for i in range(1, size(pairlist)):
	    thispair = pairlist[i]
	    if (abs(thispair['delj']) <= 1) and (abs(thispair['delka']) <= 1) or (abs(thispair['delkc']) <= 1):
	        outpairs[end+1] = thispair

	return outpairs



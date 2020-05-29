from numpy import *
def trimpairs(pairlist,minf,maxf,smalldelk=0):
# %displays the list, sorted by f.

	numpairs = size(pairlist);

	nump = 0;
	sfi = arange(1:numpairs);
	outpairs = [];

	for i in arange(1,numpairs):
	    thispair = pairlist[i];
	    f = thispair['delf'];
	    if (f > minf) & (f < maxf):
	        if (smalldelk == 0) or ((abs(thispair['delka']) <= 1) && (abs(thispair['delkc']) <= 1)):	            
	            outpairs[end()+1] = thispair;
	return outpairs
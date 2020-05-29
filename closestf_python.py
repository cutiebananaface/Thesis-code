# status: rewritten(complete)
import numpy as np
def closestf(f=None,flist=None,n=None)
#returns the closes f and the error. if you want the closest and
#nextclosest, n= 2. for example
#closestf(12,[10 11 11.5 14],2) returns fs = [11.5 11] and errs = [0.5 1.0]
#and is = [3 2]
	if n=None:
	    n = 1
	ferrors = abs(flist -f)
	n = min(n,np.size(flist))
	for i in range(1,n):
	    besti = np.where(ferrors == min(ferrors))[0]
	    fs[i] = flist[besti]
	    errs[i] = ferrors[besti]
	    #in python 'is' is a special keyword so i have changed it to is_var
	    is_var[i] = besti
	    ferrors[besti] = Inf
	return fs , errs, is_var

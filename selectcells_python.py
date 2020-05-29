#rewritten(complete)
def selectcells(oldcells,whichi):
	newcells = [];
	for i in range(1,np.size(whichi)):
	    if whichi[i] <= np.size(oldcells):
	        newcells[i] = oldcells[whichi][i]; # not sure if syntax is correct may need to be oldcells[[whichi][i]]
    return newcells


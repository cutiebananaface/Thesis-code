from numpy import *
def trimweakpairs(pairlist, heightthresh=0.05):
	outpairs= []
	heights = extractfieldsfromcellarray(pairlist,['sixKweakpulsestrength']);
	heights = heights['sixKweakpulsestrength'];
	minheight = heights * heightthresh;

	for i in range(1,size(heights)):
	    if heights[i] >= minheight:
	        outpairs{end+1} = pairlist[i];
    return outpairs


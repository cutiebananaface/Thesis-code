#rewritten(complete)
import numpy as np
def stripcellarray(cellarray):

	s = np.zeros((1,np.size(cellarray)));
	for i in range(1, np.size(s)):
	    s[i] = cellarray[i];
	return s


#rewritten(complete)
def assesslines(thisfit):
	delABC = np.array([20, 10, 8]);  #could make c smaller?
	vvals = np.array([1, 1, 1],[1, 1, -1],[1, -1, 1],[1, -1, -1])
	for i in range(1, np.array(vvals)):
	    dABC =  (delABC * vvals[i]); 
	    linearerrors = testDerivatives(thisfit,dABC,0)
	    linearerrors = abs(linearerrors)
	    allerrors[i,:] = linearerrors
	allerrors = max(allerrors);
	for i in range(1,range(thisfit.lines)):
	    thisline = thisfit['lines'][i]
	    thisline['linearerror'] = allerrors(i);
	    thisfit['lines'][i] = thisline;
	1;
	return thisfit



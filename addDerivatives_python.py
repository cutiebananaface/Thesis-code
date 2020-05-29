#rewritten(complete)
def addDerivatives(thisfit=None,stretchABC=None):
	if stretchABC=None:
	    stretchABC = np.array([0, 0, 0])
	delA = 0.1  #small change in A, B, or C
	# %baseABC = thisfit.ABC;


	basefit = quickspcat(thisfit,stretchABC)
	plusAfit = quickspcat(thisfit,stretchABC + np.array([delA, 0, 0]))
	plusBfit = quickspcat(thisfit,stretchABC + np.array([0, delA, 0]))
	plusCfit = quickspcat(thisfit,stretchABC + np.array([0, 0, delA]))
	for i in range(1, np.size(thisfit['lines'])):
	    thisline = thisfit.lines{i};
	    thisline['theoryf'] = basefit['lines'][i]['stretchedf']
	    thisline['dfdA'] = (plusAfit['lines'][i]['stretchedf'] - basefit['lines'][i]['stretchedf'])/delA;
	    thisline['dfdB'] = (plusBfit['lines'][i]['stretchedf'] - basefit['lines'][i]['stretchedf'])/delA;
	    thisline['dfdC'] = (plusCfit['lines'][i]['stretchedf'] - basefit['lines'][i]['stretchedf'])/delA;
	    thisline['dfdABC'] = np.concatenate((thisline['dfdA'] thisline['dfdB'] thisline['dfdC']));
	    thisfit['lines'][i] = thisline;
	1
	return thisfit
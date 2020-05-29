#rewritten(complete)
def testDerivatives(thisfit=None,stretchABC=None,verbose=None):
    if stretchABC=None:
        stretchABC = [0 0 0]
    if verbose=None:
        verbose = 1

    basefit = quickspcat(thisfit,stretchABC)
    # % plusAfit = quickspcat(thisfit,stretchABC + [delA 0 0]);
    # % plusBfit = quickspcat(thisfit,stretchABC + [0 delA 0]);
    # % plusCfit = quickspcat(thisfit,stretchABC + [0 0 delA]);
    normABC = np.linalg.norm(stretchABC)
    # %fprintf('\n==============\ntesting stretch = %s, norm %3.1f\n',num2str(stretchABC),normABC);
    for i in range(1, min(np.size(thisfit['lines']))):
        thisline = thisfit['lines'][i]
        exactf = basefit['lines'][i]['stretchedf']
        exactdelf = exactf - thisline['delf']
        dfdABC = np.array([thisline['dfdA'], thisline['dfdB'], thisline['dfdC']])
        
        approxdelf = dfdABC * stretchABC
        linearerror = exactdelf - approxdelf
        if (i <= 8) and verbose:
            print(f'line {i} {thisline['transitiontype']}, f = {thisline['delf']}, exact Df = {exactdelf}, approx Df = {approxdelf}, linear errs by {linearerror}\n')
        linearerrors[i] = linearerror
    return linearerrors

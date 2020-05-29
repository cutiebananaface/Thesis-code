# Generated with SMOP  0.41
# from libsmop import *
# fitf1.m
#status: rewritten (partially) ** the 105, 109, 71, 73 need more examination
    
import matplotlib as mpl
def fitf1(f=None,J=None,ka=None,startk=None):
    

    #finds k1,k2,k3 such that k1(J+1) + k2(f1((J+1)/k3) \approx f. J is
        #optional - if not included, this uses the integer test
    
    #the best part is predicts: this calls what the next and previous
        #frequency in the sequence should be.  The core of series-building.
    
    #following the rather poorly coded example at
        #https://www.mathworks.com/help/optim/ug/nonlinear-data-fitting-example.html
        # they (awfully) use x for their fit parameters (and data!!)
        #we will use the vector k
        #k(1) = k1
    if (f==None) and (J==None) and (ka==None):
        ka=0
        if startk==None:
            startk=[]
# fitf1.m:14
# fitf1.m:17
    
    f=makerow(f)
# fitf1.m:19
    jguess=np.floor(f(1) / (f(2) - f(1))) - 1
# fitf1.m:20
    homeJ=(np.arange(1,np.size(f, axis=None))) + jguess - 1
# fitf1.m:21
    if (nargin == 1) or (np.size(J, axis=None) < np.size(f, axis=None)):
        J=copy.copy(homeJ)
# fitf1.m:23
    
    if np.size(startk, axis=None) == 3:
        k,residuals,predicts,exitflag,f0predicts=rawfitf1(f,J,ka,startk)
# fitf1.m:26
    else:
        z0fracs=np.concatenate([2,8])
# fitf1.m:28
        bestResidual=copy.copy(Inf)
# fitf1.m:29
        for i in np.arange(1,np.size(z0fracs, axis=None)).reshape(-1):
            k1,residuals1,predicts1,exitflag1,f0predicts1=rawfitf1(f,J,ka,np.concatenate([z0fracs[i],0]))
# fitf1.m:31
            if mpl.mlab.norm(residuals1) < bestResidual:
                bestResidual=mpl.mlab.norm(residuals1)
# fitf1.m:33
                k=copy.copy(k1)
# fitf1.m:34
                residuals=copy.copy(residuals1)
# fitf1.m:35
                predicts=copy.copy(predicts1)
# fitf1.m:36
                exitflag=copy(exitflag1)
# fitf1.m:37
                f0predicts=copy.copy(f0predicts1)
# fitf1.m:38
    
    
    
  
def rawfitf1(f=None,J=None,ka=None,startk=None):
    # varargin = rawfitf1.varargin
    # nargin = rawfitf1.nargin
# holding off on the anoymous functions to rewrite the rest of the function
    if 0 == ka:
        F1=lambda k=None,xdata=None: np.dot(k(1),(xdata + 1)) + np.dot(k(2),evalf1((xdata + 1) / (k(3) / 100),'ftablefilek0.mat'))
# fitf1.m:47
        F0=lambda k=None,xdata=None: np.dot(k(1),(xdata + 1)) + np.dot(k(2),evalf0((xdata + 1) / (k(3) / 100),'ftablefilek0.mat'))
# fitf1.m:48
    else:
        if 1 == ka:
            F1=lambda k=None,xdata=None: np.dot(k(1),(xdata + 1)) + np.dot(k(2),evalf1((xdata + 1) / (k(3) / 100),'ftablefilek1.mat'))
# fitf1.m:50
            F0=lambda k=None,xdata=None: np.dot(k(1),(xdata + 1)) + np.dot(k(2),evalf0((xdata + 1) / (k(3) / 100),'ftablefilek1.mat'))
# fitf1.m:51
    
    if np.size(startk) == 3:
        k0=copy.copy(startk)
# fitf1.m:54
    else:
        k1zero=np.mean(np.diff(f))
# fitf1.m:56
        if np.size(startk) == 2:
            k2zero=k1zero / startk[1]
# fitf1.m:58
        else:
            k2zero=k1zero / 2
# fitf1.m:60
        k3zero=800
# fitf1.m:62
        k0=np.concatenate([k1zero,k2zero,k3zero])
# fitf1.m:63
    
    kUpperBound=np.concatenate([np.dot(k0[1],2),np.dot(k0[2],2),5000])
# fitf1.m:65
    
    kLowerBound=np.concatenate([100,0,200])
# fitf1.m:66
    
    opts=optimoptions('lsqcurvefit','FunctionTolerance',1e-07,'MaxFunctionEvaluations',300,'Display','off')
# fitf1.m:68
    
    #opts = optimoptions('lsqcurvefit','Algorithm','levenberg-marquardt');
    k,resnorm,__,exitflag,output=lsqcurvefit(F1,k0,J,f,kLowerBound,kUpperBound,opts,nargout=5)
# fitf1.m:71
    residuals=F1(k,J) - f
# fitf1.m:73
    predicts=F1(k,np.concatenate([J(1) - 1,J(end()) + 1]))
# fitf1.m:74
    f0predicts=F0(k,J)
# fitf1.m:75
    
    if exitflag == 0:
        1

    return k, residuals, predicts, exitflag, f0predicts
    
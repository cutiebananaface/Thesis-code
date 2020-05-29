# Generated with SMOP  0.41
# from libsmop import *
# testfitonkit.m
#status: rewritten(complete)
    

def testfitonkit(fit=None,kit=None,verbose=None):

    #testfitonkit decides if the fit has preditive power.  returns fields like
#fit.yesvotes: the number of predicted lines
#fit.novotes: the number of lines it is MISSING
    
    if verbose=None and kit=None:
        verbose=0
# testfitonkit.m:7
    
    fcloseyes=0.06
# testfitonkit.m:9
    fcloseno=2.0
# testfitonkit.m:10
    explineset=observablelines(fit,kit)
# testfitonkit.m:12
    predictlist=pairlistnearfit(fit)
# testfitonkit.m:13
    predictlist=trimpairs(predictlist,explineset['fmin'],explineset['fmax'])
# testfitonkit.m:14
    predictlist=trimweirdpairs(predictlist)
# testfitonkit.m:15
    predictlist=trimweakpairs(predictlist)
# testfitonkit.m:16
    upvotes,expfs,newassignments,linepvals=numpredicted(explineset,predictlist,fit['lines'])
# testfitonkit.m:18
    typestring,branchstring,descriptor=transitiontypes(newassignments)
# testfitonkit.m:19
    fit['newassignments'] = copy(newassignments)
# testfitonkit.m:20
    fit['typestring'] = copy(typestring)
# testfitonkit.m:21
    fit['branchstring'] = copy(branchstring)
# testfitonkit.m:22
    fit['numtypes'] = copy(numaintypes(fit['typestring'],4))
# testfitonkit.m:23
    fit['branchtypestring'] = copy(descriptor)
# testfitonkit.m:24
    fit['yesvotes'] = copy(upvotes)
# testfitonkit.m:25
    fit['pval'] = copy(pval(linepvals,fit['numparams']))
# testfitonkit.m:26
    fit['fitdescriptor'] = copy(fitdescriptor(fit))
# testfitonkit.m:27
    fit['shortdescriptor'] = copy(shortdescriptor(fit))
# testfitonkit.m:28
    if verbose:
        print(fit['fitdescriptor'])
    
    fit=addhits(fit,kit,expfs)
# testfitonkit.m:32
    

def numaintypes(typestring=None,mincount=None):

    if mincount=None:
        mincount=3
# testfitonkit.m:36
    
    numa=np.size(np.where(typestring == 'a'))
# testfitonkit.m:38
    numb=np.size(np.where(typestring == 'b'))
# testfitonkit.m:39
    numc=np.size(np.where(typestring == 'c'))
# testfitonkit.m:40
    nums=np.concatenate((numa,numb,numc))
# testfitonkit.m:41
    n=np.size(np.where(nums >= mincount))
# testfitonkit.m:42
    return n
    

def pval(pvals=None,numparams=None):

    #if there are 7 parameters, throw out your best 7 lines, then take the
#rest.
    
    if numparams >= np.size(pvals):
        p=100000.0
# testfitonkit.m:49
        return p
    else:
        pvals=np.sort(pvals)
# testfitonkit.m:52
        p=np.prod(pvals(np.arange(numparams + 1,-1)))
# testfitonkit.m:53
    return p
    
    

def shortdescriptor(fit=None):

    s=print(f"FOUND: [{fit[ABC][1]}{fit[ABC][2]}{fit[ABC][3]}] {fit[yesvotes]} upvotes") # i will probably need to remove the print() and just store as a string
# testfitonkit.m:57
    return s
    

def fitdescriptor(fit=None):

    if 'pattern' in fit:
        s=print(f"FOUND: [{fit[ABC][1]}{fit[ABC][2]}{fit[ABC][3]}] {fit[yesvotes]} upvotes, pattern {fit['pattern']['attemptIndex']}, pattern p={fit['pattern']['pval']},fit p = {fit['pval']}")
# testfitonkit.m:61
    else:
        s=print(f"F: [{fit[ABC][1]}{fit[ABC][2]}{fit[ABC][3]}] {fit[yesvotes]} upvotes, fit p = {fit['pval']}")
# testfitonkit.m:63
    return s
    
    

def transitiontypes(pairlist=None):

    outputs=extractfieldsfromcellarray(pairlist,['transitiontype','delj'])
# testfitonkit.m:67
    types=outputs['transitiontype']
# testfitonkit.m:68
    deljs=outputs['delj']
# testfitonkit.m:69
    typestring=''
# testfitonkit.m:71
    branchstring=''
# testfitonkit.m:72
    for i in arange(1,np.size(pairlist)).reshape(-1):
        typestring=np.concatenate((typestring,types[i]))
# testfitonkit.m:74
        if deljs[i] == 0:
            branchstring=np.concatenate((branchstring,'Q'))
# testfitonkit.m:76
        else:
            if abs(deljs[i]) == 1:
                branchstring=np.concatenate((branchstring,'R'))
# testfitonkit.m:78
            else:
                branchstring=np.concatenate((branchstring,'X'))
# testfitonkit.m:80
    
    descriptor=print(f'{typestring}\\n{branchstring}')
# testfitonkit.m:83
    return typestring,branchstring,descriptor
    

def numpredicted(explineset=None,predictlist=None,lineset=None):

    assignedfs=np.array([])
# testfitonkit.m:87
    assignedis=np.array([])
# testfitonkit.m:88
    assignedps=np.array([])
# testfitonkit.m:89
    hashlist=extractonefieldfromcellarray(lineset,'hash')
# testfitonkit.m:90
    for i in np.arange(1,np.size(predictlist)).reshape(-1):
        thispair=predictlist[i]
# testfitonkit.m:92
        predictf=thispair['delf']
# testfitonkit.m:93
        fs,errs=closestf(predictf,explineset['fs'],3)
# testfitonkit.m:94
        if ((errs[1] < explineset['fthreshold'])) and (errs[1] < errs[-1] / 10):
            np.append(assignedfs, fs[1])
# testfitonkit.m:96
            np.append(assignedis,i)
# testfitonkit.m:97
            errs=errs + 0.001
# testfitonkit.m:98
            thispair['pval'] = copy.copy(np.dot(5,errs[1]) / mean(errs))
# testfitonkit.m:99
            thispair['expfreq'] = copy.copy(fs[1])
# testfitonkit.m:100
            thispair=updateline(thispair)
# testfitonkit.m:101
            if thispair['hash'] in hashlist:
                thispair['inoldfit'] = copy.copy(1)
# testfitonkit.m:103
            else:
                thispair['inoldfit'] = copy.copy(0)
# testfitonkit.m:105
            predictlist[i]=updateline(thispair)
# testfitonkit.m:107
    
    expfs,whichworked=bogglefs(assignedfs)
# testfitonkit.m:111
    pairsthatworked=assignedis(whichworked)
# testfitonkit.m:112
    newpairs=selectcells(predictlist,pairsthatworked)
# testfitonkit.m:113
    newpairs=assignfstopairs(newpairs,expfs)
# testfitonkit.m:114
    newpairs=sortcellarraybyfield(newpairs,'pval')
# testfitonkit.m:115
    psthatworked=extractonefieldfromcellarray(newpairs,'pval')
# testfitonkit.m:116
    upvotes=np.size(np.unique(assignedfs))
# testfitonkit.m:117
    return upvotes,expfs,newpairs,psthatworked
    

def assignfstopairs(pairs=None,expfs=None):

    for i in np.arange(1,np.size(pairs)).reshape(-1):
        thispair=pairs[i]
# testfitonkit.m:121
        thispair['expf'] = copy.copy(expfs[i])
# testfitonkit.m:122
        pairs[i]=thispair
# testfitonkit.m:123
    return pairs
    
    

def pairlistnearfit(fit=None):

    #calls SPCAT to return a list of pairs in and near the fit
    argsin=fit["info"]['argsout']
# testfitonkit.m:128
    jmin=fit["info"]['minj'] - 2
# testfitonkit.m:129
    jmax=fit["info"]["maxj"] + 4
# testfitonkit.m:130
    argsin['hasa'] = copy.copy(1)
# testfitonkit.m:131
    argsin['hasb'] = copy.copy(1)
# testfitonkit.m:132
    argsin['hasc'] = copy.copy(1)
# testfitonkit.m:133
    pairlist=spcatjrange(argsin,jmin,jmax,0,jmax)
# testfitonkit.m:135
    return pairlist
    

def addhits(fit=None,kit=None,expfs=None):

    #goes back to the experimental onedpeakfs, finds them, adds the lines.
#helps with plotting
    hitis=np.array([])
# testfitonkit.m:140
    for ii in np.arange(1,np.size(expfs)).reshape(-1):
        f,err,i=closestf(expfs[ii],kit['onedpeakfs'],1)
# testfitonkit.m:142
        hitis=np.append(hitis,i)
# testfitonkit.m:143
    
    fit['hitis'] = copy.copy(hitis)
# testfitonkit.m:145
    fit['hitfs'] = copy.copy(kit['onedpeakfs'][fit.hitis])
# testfitonkit.m:146
    fit['hiths'] = copy.copy(kit['onedpeakhs'][fit.hitis])
# testfitonkit.m:147
    return fit
    

def observablelines(fit=None,kit=None):

    expfs=extractonefieldfromcellarray(fit['lines'],'expfreq')
# testfitonkit.m:150
    fit=addhits(fit,kit,expfs)
# testfitonkit.m:151
    fcloseyes=0.06
# testfitonkit.m:153
    explineset['hthresh'] = copy.copy(min(fit.hiths) / 4)
# testfitonkit.m:154
    #explineset['hthresh'] = min(fit.pattern.allhs)/4;
    
    usablei=np.where(kit['onedpeakhsunassigned'] > explineset['hthresh'])
# testfitonkit.m:157
    explineset['fs'] = copy.copy(kit.onedpeakfsunassigned(usablei))
# testfitonkit.m:158
    explineset['hs'] = copy.copy(kit.onedpeakhsunassigned(usablei))
# testfitonkit.m:159
    explineset['fs']=np.sort(explineset['fs'])
    XI= np.argsort(explineset['fs'])
# testfitonkit.m:161
    explineset['hs'] = copy.copy(explineset['hs'][XI])
# testfitonkit.m:162
    explineset['fmin'] = copy.copy(min(explineset['fs']) + 50)
# testfitonkit.m:164
    explineset['fmax'] = copy.copy(max(explineset['fs']) - 50)
# testfitonkit.m:165
    explineset['meanspacing'] = copy.copy((explineset['fmax'] - explineset['fmin']) / np.size(explineset['fs']))
# testfitonkit.m:166
    explineset['fthreshold'] = copy.copy(max(fcloseyes,explineset['meanspacing'] / 20))
# testfitonkit.m:167
    return explineset
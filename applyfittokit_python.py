# Generated with SMOP  0.41
from libsmop import *
# applyfittokit.m
from numpy import *
from copy import *
#line 218    

def applyfittokit(fit=None,kit=None,verbose=None):

    #applyfittokit decides if the fit has preditive power.  returns fields like
    
    #fit.yesvotes: the number of predicted lines
#fit.novotes: the number of lines it is MISSING
#it also makes a list of lines, newassignments, which all the 'upvotes'
    
    if verbose= None:
        verbose=1
# applyfittokit.m:10
    
    fcloseyes=0.06
# applyfittokit.m:12
    fcloseno=2.0
# applyfittokit.m:13
    explineset=observablelines(fit,kit)
# applyfittokit.m:15
    predictlist=pairlistnearfit(fit)
# applyfittokit.m:16
    predictlist=trimpairs(predictlist,explineset['fmin'],explineset['fmax'])
# applyfittokit.m:17
    predictlist=trimweirdpairs(predictlist)
# applyfittokit.m:18
    predictlist=trimweakpairs(predictlist)
# applyfittokit.m:19
    upvotes,expfs,newassignments,linepvals=numpredicted(explineset,predictlist,fit['lines'])
# applyfittokit.m:21
    typestring,branchstring,descriptor=transitiontypes(newassignments)
# applyfittokit.m:22
    originallines=pulloriginals(newassignments)
# applyfittokit.m:23
    
    ratios=heightratios(originallines)
# applyfittokit.m:24
    newassignments=addscaledheights(newassignments,ratios)
# applyfittokit.m:25
    fit['lines'] = copy(pulloriginals(newassignments))
# applyfittokit.m:27
    fit['matches'] = copy(newassignments)
# applyfittokit.m:28
    fit['newassignments'] = copy(newassignments)
# applyfittokit.m:29
    fit['typestring'] = copy(typestring)
# applyfittokit.m:30
    fit['branchstring'] = copy(branchstring)
# applyfittokit.m:31
    fit['branchtypestring'] = copy(descriptor)
# applyfittokit.m:32
    fit['yesvotes'] = copy(upvotes)
# applyfittokit.m:33
    fit['pval'] = copy(pval(linepvals,fit['numparams']))
# applyfittokit.m:34
    fit['fitdescriptor'] = copy(fitdescriptor(fit))
# applyfittokit.m:35
    fit['shortdescriptor'] = copy(shortdescriptor(fit))
# applyfittokit.m:36
    if verbose:
        print(fit['fitdescriptor'])
    
    fit=addhits(fit,kit,expfs)
# applyfittokit.m:40
    return fit
    

def pval(pvals=None,numparams=None):

    #if there are 7 parameters, throw out your best 7 lines, then take the
#rest.
    
    if numparams >= size(pvals):
        p=100000.0
# applyfittokit.m:47
        return p
    else:
        pvals=pvals.sort()
# applyfittokit.m:50
        p=prod(pvals[numparams+1:-1])
# applyfittokit.m:51
    return p
    

def addscaledheights(linelist=None,ratios=None):

    for i in arange(1,np.size(linelist)).reshape(-1):
        thisline=linelist[i]
# applyfittokit.m:56
        thistype=thisline['transitiontype']
# applyfittokit.m:57
        if 'a' == thistype:
            thisline['predictedh'] = copy(thisline['sixKweakpulsestrength'] @ ratios[1])
# applyfittokit.m:60
        elif 'b' == thistype:
            thisline['predictedh'] = copy(thisline['sixKweakpulsestrength'] @ ratios[2])
# applyfittokit.m:62
        elif 'c' == thistype:
            thisline['predictedh'] = copy(thisline['sixKweakpulsestrength'] @ ratios[3])
# applyfittokit.m:64
        linelist[i]=thisline
# applyfittokit.m:66
    return linelist    
    

def heightratios(linelist=None,*args,**kwargs):

    outputs=extractfieldsfromcellarray(linelist,['transitiontype','sixKweakpulsestrength','expheight'])
# applyfittokit.m:70
    ctypes=outputs.transitiontype
# applyfittokit.m:71
    for i in arange(1,np.size(ctypes)).reshape(-1):
        types[i]=ctypes[i](1)
# applyfittokit.m:73
    
    unscaledh=outputs['sixKweakpulsestrength']
# applyfittokit.m:75
    exphs=outputs['expheight']
# applyfittokit.m:76
    ascale=0
# applyfittokit.m:77
    bscale=0
# applyfittokit.m:78
    cscale=0
# applyfittokit.m:79
    isa=np.where(types == 'a')
# applyfittokit.m:81
    isb=np.where(types == 'b')
# applyfittokit.m:82
    isc=np.where(types == 'c')
# applyfittokit.m:83
    if np.size(isa) > 0:
        ascale=mean(exphs[isa]) / mean(unscaledh[isa])
# applyfittokit.m:85
    
    if np.size(isb) > 0:
        bscale=mean(exphs[isb]) / mean(unscaledh[isb])
# applyfittokit.m:88
    
    if np.size(isc) > 0:
        cscale=mean(exphs[isc]) / mean(unscaledh[isc])
# applyfittokit.m:91
    
    ratios=np.array((ascale,bscale,cscale))
# applyfittokit.m:93
    return ratios
    

def pulloriginals(linelist=None,*args,**kwargs):

    originals=[]
# applyfittokit.m:96
    isold=extractonefieldfromcellarray(linelist,'inoldfit')
# applyfittokit.m:97
    oldi=np.where(isold == 1)
# applyfittokit.m:98
    for i in arange(1,np.size(oldi)).reshape(-1):
        originals[i]=linelist[oldi[i]]
# applyfittokit.m:100
    return originals
    

def shortdescriptor(fit=None,*args,**kwargs):
 

    s=print('FOUND: [%3.2f %3.2f %3.2f] %d upvotes' % (fit['ABC'][1],fit['ABC'][2],fit['ABC'][3],fit['yesvotes']))
# applyfittokit.m:104
    return s
    

def fitdescriptor(fit=None,*args,**kwargs):


    if 'pattern' in fit:
        s=print('FOUND: [%3.2f %3.2f %3.2f] %d upvotes, pattern %d, pattern p=%3.1e,fit p = %3.1e' % (fit['ABC'][1],fit['ABC'][2],fit['ABC'][3],fit['yesvotes'],fit['pattern']['attemptIndex'],fit['pattern']['pval'],fit['pval']))
# applyfittokit.m:108
    else:
        s=print('F:[%3.2f %3.2f %3.2f] %d upvotes,fit p = %3.1e'% (fit['ABC'][1],fit['ABC'][2],fit['ABC'][3],fit['yesvotes'], fit['pattern']['pval']))
# applyfittokit.m:110
    return s
    
    

def transitiontypes(pairlist=None,*args,**kwargs):

    outputs=extractfieldsfromcellarray(pairlist,['transitiontype','delj'])
# applyfittokit.m:114
    types=outputs['transitiontype']
# applyfittokit.m:115
    deljs=outputs['delj']
# applyfittokit.m:116
    typestring=''
# applyfittokit.m:118
    branchstring=''
# applyfittokit.m:119
    for i in arange(1,np.size(pairlist)).reshape(-1):
        typestring=np.size([typestring,types[i]])
# applyfittokit.m:121
        if deljs[i] == 0:
            branchstring=np.array([branchstring,'Q'])
# applyfittokit.m:123
        elif abs(deljs[i]) == 1:
            branchstring=np.array([branchstring,'R'])
# applyfittokit.m:125
        else:
            branchstring=np.array([branchstring,'X'])
# applyfittokit.m:127
    
    descriptor=print('%s\\n%s' % (typestring,branchstring))
# applyfittokit.m:130
    return typestring,branchstring,descriptor


def numpredicted(explineset=None,predictlist=None,lineset=None,*args,**kwargs):

    assignedfs=[]
# applyfittokit.m:134
    assignedis=[]
# applyfittokit.m:135
    assignedps=[]
# applyfittokit.m:136
    hashlist=extractonefieldfromcellarray(lineset,'hash')
# applyfittokit.m:137
    for i in arange(1,size(predictlist)).reshape(-1):
        thispair=predictlist[i]
# applyfittokit.m:139
        predictf=thispair.delf
# applyfittokit.m:140
        fs,errs,ivals=closestf(predictf,explineset['fs'],3,nargout=3)
# applyfittokit.m:141
        if ((errs[1] < explineset['fthreshold'])) and (errs[1] < errs[-1] / 10):
            assignedfs[end() + 1]=fs(1)
# applyfittokit.m:143
            assignedis[end() + 1]=i
# applyfittokit.m:144
            errs=errs + 0.001
# applyfittokit.m:145
            thispair['pval'] = copy(dot(5,errs[1]) / mean(errs))
# applyfittokit.m:146
            thispair['expfreq'] = copy(fs[1])
# applyfittokit.m:147
            thispair['expheight'] = copy(explineset['hs'][ivals][1])
# applyfittokit.m:148
            thispair['theoryf'] = copy(predictf)
# applyfittokit.m:149
            thispair['unstretchedpredictedf'] = copy(predictf)
# applyfittokit.m:150
            thispair=updateline(thispair)
# applyfittokit.m:151
            
            if hashlist in thispair['hash']:
                thispair['inoldfit'] = copy(1)
# applyfittokit.m:153
            else:
                thispair['inoldfit'] = copy(0)
# applyfittokit.m:155
            predictlist[i]=updateline(thispair)
# applyfittokit.m:157
    
    expfs,whichworked=bogglefs(assignedfs)
# applyfittokit.m:161
    pairsthatworked=assignedis(whichworked)
# applyfittokit.m:162
    newpairs=selectcells(predictlist,pairsthatworked)
# applyfittokit.m:163
    newpairs=assignfstopairs(newpairs,expfs)
# applyfittokit.m:164
    newpairs=sortcellarraybyfield(newpairs,'pval')
# applyfittokit.m:165
    psthatworked=extractonefieldfromcellarray(newpairs,'pval')
# applyfittokit.m:166
    upvotes=size(unique(assignedfs))
# applyfittokit.m:167
    return upvotes,expfs,newpairs,psthatworked

def assignfstopairs(pairs=None,expfs=None,*args,**kwargs):
    varargin = assignfstopairs.varargin
    nargin = assignfstopairs.nargin

    for i in arange(1,size(pairs)).reshape(-1):
        thispair=pairs[i]
# applyfittokit.m:171
        thispair['expf'] = copy(expfs(i))
# applyfittokit.m:172
        pairs[i]=thispair
# applyfittokit.m:173
    return pairs
    
    

def pairlistnearfit(fit=None,*args,**kwargs):

    #calls SPCAT to return a list of pairs in and near the fit
    argsin=fit['info']['argsout']
# applyfittokit.m:178
    jmin=fit['info']['minj'] - 2
# applyfittokit.m:179
    jmax=fit['info']['maxj'] + 4
# applyfittokit.m:180
    argsin['hasa'] = copy(1)
# applyfittokit.m:181
    argsin['hasb'] = copy(1)
# applyfittokit.m:182
    argsin['hasc'] = copy(1)
# applyfittokit.m:183
    pairlist=spcatjrange(argsin,jmin,jmax,0,jmax)
# applyfittokit.m:185
    return pairlist
    
    

def addhits(fit=None,kit=None,expfs=None,*args,**kwargs):

    #goes back to the experimental onedpeakfs, finds them, adds the lines.
#helps with plotting
    hitis=[]
# applyfittokit.m:190
    for ii in arange(1,size(expfs)).reshape(-1):
        f,err,i=closestf(expfs[ii],kit['onedpeakfs'],1)
# applyfittokit.m:192
        hitis[end() + 1]=i
# applyfittokit.m:193
    
    fit['hitis'] = copy(hitis)
# applyfittokit.m:195
    fit['hitfs'] = copy(kit['onedpeakfs'][fit]['hitis'])
# applyfittokit.m:196
    fit['hiths'] = copy(kit['onedpeakhs'][fit]['hitis'])
# applyfittokit.m:197
    return fit
    

def observablelines(fit=None,kit=None,*args,**kwargs):

    expfs=extractonefieldfromcellarray(fit['lines'],'expfreq')
# applyfittokit.m:200
    fit=addhits(fit,kit,expfs)
# applyfittokit.m:201
    fcloseyes=0.06
# applyfittokit.m:203
    explineset['hthresh'] = copy(min(fit['hiths'] / 4))
# applyfittokit.m:204
    #explineset.hthresh = min(fit.pattern.allhs)/4;
    
    usablei=np.where(kit['onedpeakhsunassigned'] > explineset['hthresh'])
# applyfittokit.m:207
    explineset['fs'] = copy(kit['onedpeakfsunassigned'][usablei])
# applyfittokit.m:208
    explineset['hs'] = copy(kit['onedpeakhsunassigned'][usablei])
# applyfittokit.m:209
    explineset['fs'],XI=sort(explineset['fs']), argsort(explineset['fs'])
# applyfittokit.m:211
    explineset['hs'] = copy(explineset['hs'][XI])
# applyfittokit.m:212
    explineset['fmin'] = copy(min(explineset['fs']) + 50)
# applyfittokit.m:214
    explineset['fmax'] = copy(max(explineset['fs']) - 50)
# applyfittokit.m:215
    explineset['meanspacing'] = copy((explineset['fmax'] - explineset['fmin']) / size(explineset['fs']))
# applyfittokit.m:216
    explineset['fthreshold'] = copy(max(fcloseyes,explineset['meanspacing'] / 20))
# applyfittokit.m:217
    return explineset
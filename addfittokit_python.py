# Generated with SMOP  0.41
# from libsmop import *
# addfittokit.m
#status: rewritten (complete)
 import numpy as np   

def addfittokit(kit=None,fit=None):

    if type(fit) is not dict:
        return kit
    
    if (kit=None) and (fit=None):
        n=np.size(kit['fitlist']) + 1
# addfittokit.m:6
    
    if 0 == np.mod(n,6):
        fit['color'] = copy('r')
# addfittokit.m:11
    elif 1 == np.mod(n,6):
        fit['color'] = copy('b')
# addfittokit.m:13
    elif 2 == np.mod(n,6):
        fit['color'] = copy('m')
# addfittokit.m:15
    elif 3 == np.mod(n,6):
        fit['color'] = copy('c')
# addfittokit.m:17
    elif 4 == np.mod(n,6):
        fit['color'] = copy('g')
# addfittokit.m:19
    elif 5 == np.mod(n,6):
        fit['color'] = copy('k')
# addfittokit.m:21
    else:
        fit['color'] = copy('k')
# addfittokit.m:23
    
    kit['fitlist'][n]=fit
# addfittokit.m:25
    kit['numspecies'] = copy(np.size(kit['fitlist']))
# addfittokit.m:26
    kit['latestfit'] = copy(fit)
# addfittokit.m:27
    kit['numvotes'] = copy(fit['yesvotes'])
# addfittokit.m:28
    kit['whichspecies'][fit['hitis']]=n
# addfittokit.m:30
    ulines=np.where(kit['whichspecies'] == 0)
# addfittokit.m:31
    kit['onedpeakfsunassigned'] = copy(kit['onedpeakfs'][ulines])
# addfittokit.m:32
    kit['onedpeakhsunassigned'] = copy(kit['onedpeakhs'][ulines])
# addfittokit.m:33
    kit['fitlistreport'] = copy(makefitlistreport(kit))
# addfittokit.m:34
    kit['finalfit'] = copy(kit['fitlist'][1])
# addfittokit.m:35
    if 'isotopes' in fit:
        for i in np.arange(1,np.size(fit.isotopes)).reshape(-1):
            thisisotope=fit['isotopes'][i]
# addfittokit.m:38
            kit=addfittokit(kit,thisisotope)
# addfittokit.m:39
    return kit
    #displayspfit(finalfit,kit);
#1;
    
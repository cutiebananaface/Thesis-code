# Generated with SMOP  0.41
# from libsmop import *
# findbruteforcefit.m
from numpy import *
from copy import *
import matplotlib.pylab as pylab


def findbruteforcefit(kit=None,*args,**kwargs):
 

    if kit != 1:
        pylab.save('bftfile','kit')
    else:
        pylab.load('bftfile','kit')
        kit['tightnesssettings'] = copy(settingsfromtightness(kit['tightnesssettings']['scalartightness']))
# findbruteforcefit.m:6
    
    random(1)
    ABCexact=array([8572.0553,3640.1063,2790.9666])
# findbruteforcefit.m:9
    ABCguess=array([8572.0,3640.0,2790.0])
# findbruteforcefit.m:10
    
    ABCguess=multiply(ABCguess,array([0.99,1.01,0.99]))
# findbruteforcefit.m:11
    kit=trimkit(kit,kit['tightnesssettings']['bruteforce']['numexperimentlines'])
# findbruteforcefit.m:12
    flimits=array([min(kit['onedpeakfs']),max(kit['onedpeakfs'])])
# findbruteforcefit.m:14
    theoryset=linesforbruteforce2(ABCguess,flimits,kit['tightnesssettings']['bruteforce']['numtheorylines'],max(kit['onedpeakhsunassigned']))
# findbruteforcefit.m:15
    linestouse['lines'] = copy(theoryset)
# findbruteforcefit.m:17
    linestouse['heighttouse'] = copy('sixKweakpulsestrength')
# findbruteforcefit.m:18
    linestouse['fitdescriptor'] = copy('made up brute force fit')
# findbruteforcefit.m:19
    linestouse['ABCxxxxx'] = copy(array([ABCguess,0,0,0,0,0]))
# findbruteforcefit.m:20
    #addC13swithlinelist
    
    ABClist=[ABCguess]
# findbruteforcefit.m:23
    dAdBdC=array([0.01,0.01,0.01])
# findbruteforcefit.m:24
    linestouse['ABClist'] = copy(ABClist)
# findbruteforcefit.m:26
    linestouse['dAdBdC'] = copy(dAdBdC)
# findbruteforcefit.m:27
    kit['findfitsettings'] = copy(kit['tightnesssettings']['bruteforce'])
# findbruteforcefit.m:28
    allfits=findfits(linestouse,kit)
# findbruteforcefit.m:30
    fit=pullbest(allfits,kit)
# findbruteforcefit.m:32
    fit['patternType'] = copy('bruteforce')
# findbruteforcefit.m:33
    kit=addfittokit(kit,fit)
# findbruteforcefit.m:34
    displaykitwithfits(kit)
    1
    return fit
    
@function
def pullbest(fitlist=None,kit=None,*args,**kwargs):

    minScore=0
# findbruteforcefit.m:39
    bestfit=0
# findbruteforcefit.m:40
    for i in arange(1,size(fitlist)).reshape(-1):
        thisfit=applyfittokit(fitlist[i],kit)
# findbruteforcefit.m:42
        thisfit=addscore(thisfit,'pval')
# findbruteforcefit.m:43
        if thisfit['fitScore'] > minScore:
            bestfit=copy(thisfit)
# findbruteforcefit.m:45
            minScore=thisfit['fitScore']
# findbruteforcefit.m:46
    return bestfit
    
    

def trimkit(kit=None,numlines=None,*args,**kwargs):

    exphs=kit['onedpeakhsunassigned']
# findbruteforcefit.m:51
    expfs=kit['onedpeakfsunassigned']
# findbruteforcefit.m:52
    exphs,XI=sort(exphs)[::-1], argsort(exphs)[::-1]
# findbruteforcefit.m:53
    numlines=min(numlines,size(exphs))
# findbruteforcefit.m:54
    kit['onedpeakhsunassigned'] = copy(exphs(arange(1,numlines)))
# findbruteforcefit.m:55
    kit.onedpeakfsunassigned = copy(expfs(XI(arange(1,numlines))))
# findbruteforcefit.m:56
    return kit
    

def linesforbruteforce2(ABC=None,mwbounds=None,numlines=None,scaledh=None,*args,**kwargs):


    pairlist=spcatjrangeABC(array([ABC,0,0,0,0,0]),0,12)
# findbruteforcefit.m:60
    pairlist=trimpairs(pairlist,mwbounds[1],mwbounds[2])
# findbruteforcefit.m:61
    heights=extractonefieldfromcellarray(pairlist,'sixKweakpulsestrength')
# findbruteforcefit.m:62
    numlines=min(numlines,size(heights))
# findbruteforcefit.m:64
    heights,XI=sort(heights)[::-1], argsort(hieghts)[::-1]
# findbruteforcefit.m:65
    scale=scaledh / max(heights)
# findbruteforcefit.m:66
    numlines=min(numlines, size(heights))
# findbruteforcefit.m:68
    outpairs=[]
# findbruteforcefit.m:69
    for i in arange(1,numlines).reshape(-1):
        thispair=pairlist[XI[i]]
# findbruteforcefit.m:72
        thispair['sixKweakpulsestrength'] = copy(dot(thispair['sixKweakpulsestrength'],scale))
# findbruteforcefit.m:73
        outpairs[end() + 1]=thispair
# findbruteforcefit.m:74
    return outpairs
    
    # outpairs;
# theoryf  = extractonefieldfromcellarray(pairlist,'delf');
# figure;
# stickplot(theoryf,heights);
# 1;
    
    
    # 
# function outpairs = linesforbruteforce(ABC,mwbounds,numlines,scaledh)
# pgoargsin.molstats = molstatsfromwhatever(ABC);
#     pgoargsin.maxj = 20;
#     #argsin.usepgo = 0;
#     pgoargsin.reduceset = 0;
#     pgoargsin.maxrf = 0;  #in GHz
#     pgoargsin.minrf = 0;
#     pgoargsin.minmw = mwbounds(1);
#     pgoargsin.maxmw = mwbounds(2);
#     
#     pgoargsin.temp = 6;
#    # pgoargsin.usespcat = 1;
#     [pairlist] = findallpairspgo(pgoargsin);
#     pairlist = trimpairs(pairlist,mwbounds(1)/1000,mwbounds(2)/1000);
#     heights = extractonefieldfromcellarray(pairlist,'sixKweakpulsestrength');
#     [heights XI] = sort(heights,'descend');
#     numlines2 = min(numlines*2,length(heights));
#     firstpairs = {};
# 
#     for i = 1:numlines2
#         thispair = pairlist{XI(i)};
#         thispair.Jupper = thispair.startj;
#         thispair.Jlower = thispair.endj;
#         firstpairs{end+1} = thispair;
#     end
#     
#       
#     thisfit.lines = firstpairs;
#     thisfit.ABCxxxxx = [ABC 0 0 0 0 0];
#     [basefit survivors] = quickspcat(thisfit);
#     firstpairs = survivors;
#     
#     heights = extractonefieldfromcellarray(firstpairs,'sixKweakpulsestrength');
#     scale = scaledh/max(heights);
#     [heights XI] = sort(heights,'descend');
#     numlines = min(numlines,length(heights));
#     outpairs = {};
#     
#     for i = 1:numlines
#         thispair = firstpairs{XI(i)};
#         thispair.sixKweakpulsestrength = thispair.sixKweakpulsestrength*scale;
#         outpairs{end+1} = thispair;
#     end
#     
#     
#     1;
#     
#
    
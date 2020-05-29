# Generated with SMOP  0.41
from libsmop import *
# findallspecies.m
from numpy import *
from copy import *

def findallspecies(kit=None,*args,**kwargs):

    tic
    bestp=1
# findallspecies.m:3
    while kit['numspecies'] < kit['tightnesssettings']['patternfitting']['maxcomponents']:

        if 'scaffold' == kit['method']:
            patternlist=findpatternvariant1(kit)
# findallspecies.m:7
            newfit=trypatterns(kit,patternlist)
# findallspecies.m:8
        elif 'atype' == kit['method']:
            patternlist=findpatternvariant3(kit)
# findallspecies.m:10
            newfit=trypatterns(kit,patternlist)
# findallspecies.m:11
        elif 'bowties' == kit['method']:
            patternlist=findpatternbowties(kit)
# findallspecies.m:13
            newfit=trypatterns(kit,patternlist)
# findallspecies.m:14
        elif 'bruteforce' == kit['method']:
            newfit=findbruteforcefit(kit)
# findallspecies.m:16
        else:
            raise Exception('method %s is unknown\\n'% kit['method'])
        if type(newfit) is dict:
            newfit=improvefit(newfit,kit)
# findallspecies.m:23
            kit=addfittokit(kit,newfit)
# findallspecies.m:24
        else:
            break

    
    kit['allReports'] = copy(makeAllReports(kit))
# findallspecies.m:29
    
    
    if size(patternlist) > 0:
        bestp=patternlist[1]['pval']
# findallspecies.m:32
        kit['latestp'] = copy(bestp)
# findallspecies.m:33
        kit['latestpattern'] = copy(patternlist[1])
# findallspecies.m:34
    return kit
    
    

def makeAllReports(kit=None,*args,**kwargs):

    summary=print('Summary for %s\\n'% kit['reportfilename'])
# findallspecies.m:40
    for i in arange(1,size(kit['fitlist'])).reshape(-1):
        thisFit=kit['fitlist'][i]
# findallspecies.m:42
        s=print('%s\\n%s'% (summary,thisFit['longdescription']))
# findallspecies.m:43
    
    if size(kit['fitlist']) > 0:
        g=open(kit['reportfilename'],'w')
# findallspecies.m:46
        # fprintf(g,s)
        print(g, file=s) # i am not really sure about this 
        close(g)
        fprintf(s) # i am not sure what to do with this line
        1
    else:
        s=array([summary,'NO FIT FOUND'])
# findallspecies.m:53
    
    time_elapsed=copy(toc)
# findallspecies.m:55
    s=print('%s===%3.1f seconds'% (s,time_elapsed))
# findallspecies.m:56
    return s
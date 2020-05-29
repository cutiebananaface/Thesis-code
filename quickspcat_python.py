# Generated with SMOP  0.41
# from libsmop import *
# quickspcat.m
from numpy import *
from copy import *

def quickspcat(lineset=None,delABC=array([0,0,0]),*args,**kwargs):

    #evaluates all the lines in newfit under ABC + delABC
#calls SPCAT to return a list of pairs in and near the fit

# quickspcat.m:5
    
    #argsin = fit.info.argsout;
    argsin['a'] = copy(lineset['ABCxxxxx'][1])
# quickspcat.m:8
    argsin['b'] = copy(lineset['ABCxxxxx'][2])
# quickspcat.m:9
    argsin['c'] = copy(lineset['ABCxxxxx'][3])
# quickspcat.m:10
    argsin['DJ'] = copy(lineset['ABCxxxxx'][4])
# quickspcat.m:11
    argsin['DJK'] = copy(lineset['ABCxxxxx'][5])
# quickspcat.m:12
    argsin['DK'] = copy(lineset['ABCxxxxx'][6])
# quickspcat.m:13
    argsin['deltaJ'] = copy(lineset['ABCxxxxx'][7])
# quickspcat.m:14
    argsin['deltaK'] = copy(lineset['ABCxxxxx'][8])
# quickspcat.m:15
    argsin['a'] = copy(argsin['a'] + delABC[1])
# quickspcat.m:17
    argsin['b'] = copy(argsin['b'] + delABC[2])
# quickspcat.m:18
    argsin['c'] = copy(argsin['c'] + delABC[3])
# quickspcat.m:19
    newABC=array([argsin['a'],argsin['b'],argsin['c']])
# quickspcat.m:20
    jmin=min(extractonefieldfromcellarray(lineset['lines'],'Jlower'))
# quickspcat.m:22
    jmax=max(extractonefieldfromcellarray(lineset['lines'],'Jupper'))
# quickspcat.m:23
    
    argsin['hasa'] = copy(1)
# quickspcat.m:24
    argsin['hasb'] = copy(1)
# quickspcat.m:25
    argsin['hasc'] = copy(1)
# quickspcat.m:26
    pairlist=spcatjrange(argsin,jmin,jmax,0,jmax)
# quickspcat.m:28
    
    1
    hashlist=extractonefieldfromcellarray(lineset.lines,'hash')
# quickspcat.m:30
    newset= []
# quickspcat.m:31
    for i in arange(1,array(pairlist)).reshape(-1):
        thispair=pairlist[i]
# quickspcat.m:33
        if hashlist in thispair['hash']:
            whichi=where(hashlist == thispair['hash'],1)
# quickspcat.m:35
            thisline=lineset['lines'][whichi]
# quickspcat.m:36
            thisline['stretchedf'] = copy(thispair['delf'])
# quickspcat.m:37
            thisline['stretchedABC'] = copy(newABC)
# quickspcat.m:38
            lineset['lines'][whichi]=thisline
# quickspcat.m:40
            1
    return lineset, newset
    
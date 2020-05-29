# Generated with SMOP  0.41
# from libsmop import *
# updatePattern.m
from numpy import *
from copy import *
    

def updatePattern(s=None,kit=None,*args,**kwargs):

    fgrid=s['fgrid']
# updatePattern.m:3
    hgrid=dot(fgrid,0)
# updatePattern.m:4
    allfs=array([])
# updatePattern.m:5
    allhs=array([])
# updatePattern.m:6
    for i in arange(1,size(fgrid(arange(),1))).reshape(-1):
        for j in arange(1,4).reshape(-1):
            thisf=fgrid[i,j]
# updatePattern.m:9
            if thisf > 0:
                thish=findHeight(thisf,kit)
# updatePattern.m:11
                hgrid[i,j]=thish
# updatePattern.m:12
                allfs[end() + 1]=thisf
# updatePattern.m:13
                allhs[end() + 1]=thish
# updatePattern.m:14
    
    allfs,XI=sort(allfs), argsort(allfs)
# updatePattern.m:18
    s['allfs'] = copy(allfs)
# updatePattern.m:19
    s['allhs'] = copy(allhs(XI))
# updatePattern.m:20
    return s
    

def findHeight(f=None,kit=None,*args,**kwargs):


    i=where(kit['onedpeakfs'] == f)[0][0]
# updatePattern.m:24
    h=kit['onedpeakhs'][i]
# updatePattern.m:25
    return h
# Generated with SMOP  0.41
# from libsmop import *
# stringfromfit.m
from numpy import *
from copy import *
    

def stringfromfit(thisfit=None,trueABC=None,*args,**kwargs):


    mol=thisfit['info']['argsout']
# stringfromfit.m:2
    cheatstring=''
# stringfromfit.m:3
    if mol['DJ'] != 0:
        CDstring='CD'
# stringfromfit.m:5
    else:
        CDstring='-'
# stringfromfit.m:7
    
    titlestring=print('A=%3.2f,B=%3.2f,C=%3.2f %s\\n%d lines %f MHz RMS'% (mol['a'],mol['b'],mol['c'],CDstring,size(thisfit['info']['lines']),thisfit['info']['myrms_error']))
# stringfromfit.m:9
    diffs=extractfieldsfromcellarray(thisfit['info']['lines'],['diff'])
# stringfromfit.m:10
    rmsdiff=mean(diffs['diff'] ** 2)
# stringfromfit.m:11
    qnumbers=extractfieldsfromcellarray(thisfit['info']['lines'],['Kaupper','Kalower','Jupper','Jlower'])
# stringfromfit.m:12
    allkas=array([qnumbers['Kaupper'],qnumbers['Kalower']])
# stringfromfit.m:14
    maxka=max(allkas)
# stringfromfit.m:15
    minka=min(allkas)
# stringfromfit.m:16
    alljs=array([qnumbers.Jupper,qnumbers.Jlower])
# stringfromfit.m:18
    maxj=max(alljs)
# stringfromfit.m:19
    minj=min(alljs)
# stringfromfit.m:20
    #fulldescription = sprintf('#s\nJ #d lines, #3.4f MHz RMS\n',titlestring,length(thisfit.info.lines),rmsdiff);
    if 'pval' in thisfit:
        pvalstring=print(' pval = %3.4g'% thisfit['pval'])
# stringfromfit.m:23
    else:
        pvalstring=''
# stringfromfit.m:25
    
    fulldescription=print('=================\\n%s%s\\nJ = %d => %d, Ka = %d=>%d\\n' % (titlestring,pvalstring,minj,maxj,minka,maxka))
# stringfromfit.m:27
    1
    if nargin == 2:
    if (thisfit !=None) and (trueABC !=None):
        fitabc=array([mol['a'],mol['b'],mol['c']])
# stringfromfit.m:31
        cheaterror= linalg.norm(fitabc - trueABC)
# stringfromfit.m:32
        cheatstring=print('ABC off by %3.1f MHz'%cheaterror)
# stringfromfit.m:33
    return titlestring, fulldescription, cheatstring, cheaterror
    
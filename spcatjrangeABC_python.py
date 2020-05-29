# Generated with SMOP  0.41
# from libsmop import *
# spcatjrangeABC.m
from numpy import *
from copy import *
    

def spcatjrangeABC(ABCxxxxx=None,jmin=None,jmax=None,*args,**kwargs):

    kmin=0
# spcatjrangeABC.m:3
    kmax=copy(jmax)
# spcatjrangeABC.m:4
    molstats['a'] = copy(ABCxxxxx[1] / 1000)
# spcatjrangeABC.m:5
    molstats['b'] = copy(ABCxxxxx[2] / 1000)
# spcatjrangeABC.m:6
    molstats['c'] = copy(ABCxxxxx[3] / 1000)
# spcatjrangeABC.m:7
    molstats['DJ'] = copy(- 1e-09 + ABCxxxxx[4] / 1000)
# spcatjrangeABC.m:8
    molstats['DJK'] = copy(- 1e-09 + ABCxxxxx[5] / 1000)
# spcatjrangeABC.m:9
    molstats['DK'] = copy(- 1e-09 + ABCxxxxx[6] / 1000)
# spcatjrangeABC.m:10
    molstats['deltaJ'] = copy(- 1e-09 + ABCxxxxx[7] / 1000)
# spcatjrangeABC.m:11
    molstats['deltaK'] = copy(- 1e-09 + ABCxxxxx[8] / 1000)
# spcatjrangeABC.m:12
    molstats['molname'] = copy('unknown')
# spcatjrangeABC.m:13
    molstats['molid'] = copy(0)
# spcatjrangeABC.m:14
    molstats['mua'] = copy(1)
# spcatjrangeABC.m:15
    molstats['mub'] = copy(1)
# spcatjrangeABC.m:16
    molstats['muc'] = copy(1)
# spcatjrangeABC.m:17
    argsout['vibstates'] = copy(1)
# spcatjrangeABC.m:19
    argsout['spindegeneracy'] = copy(1)
# spcatjrangeABC.m:20
    argsout['temp'] = copy(6)
# spcatjrangeABC.m:22
    argsout['intensethresh'] = copy(- 11)
# spcatjrangeABC.m:23
    
    argsout['maxf'] = copy(30)
# spcatjrangeABC.m:24
    
    argsout['molstats'] = copy(molstats)
# spcatjrangeABC.m:26
    #         fprintf(f, '10000 #f\n', molstats['a * 1000); # A in MHz (all units)
#     fprintf(f, '20000 #f\n', molstats['b * 1000); # B
#     fprintf(f, '30000 #f\n', molstats['c * 1000); # C
#     fprintf(f, '200 #f\n', -molstats['DJ * 1000); # -DeltaJ
#     fprintf(f, '1100 #f\n', -molstats['DJK * 1000); #-DeltaJK
#     fprintf(f, '2000 #f\n', -molstats['DK  * 1000); # -DeltaK
#     fprintf(f, '40100 #f\n', -molstats['deltaJ * 1000); #-deltaJ
#     fprintf(f, '41000 #f\n', -molstats['deltaK * 1000); #-deltaK
    
    #  argsin'] = prepare_sp_argsin();
    argsout['jmin'] = copy(max(jmin,0))
# spcatjrangeABC.m:37
    argsout['jmax'] = copy(jmax)
# spcatjrangeABC.m:38
    argsout['kmin'] = copy(max(kmin,0))
# spcatjrangeABC.m:39
    argsout['kmax'] = copy(kmax)
# spcatjrangeABC.m:40
    argsout['filename'] = copy(array([getspfitpath,'\\spcatfile2']))
# spcatjrangeABC.m:41
    allpairs=runspcat(argsout,1)
# spcatjrangeABC.m:42
    for i in arange(1,size(allpairs)).reshape(-1):
        allpairs[i]=updateline(allpairs[i])
# spcatjrangeABC.m:44
    
    return allpairs

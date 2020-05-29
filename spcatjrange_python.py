# Generated with SMOP  0.41
# from libsmop import *
# spcatjrange.m

    

def spcatjrange(argsin=None,jmin=9,jmax=11,kmin=0,kmax=1,*args,**kwargs):

    
    molstats['a'] = copy(argsin['a'] / 1000)
# spcatjrange.m:8
    molstats['b'] = copy(argsin['b'] / 1000)
# spcatjrange.m:9
    molstats['c'] = copy(argsin['c'] / 1000)
# spcatjrange.m:10
    molstats['DJ'] = copy(- 1e-09 + argsin['DJ'] / 1000)
# spcatjrange.m:11
    molstats['DJK'] = copy(- 1e-09 + argsin['DJK'] / 1000)
# spcatjrange.m:12
    molstats['DK'] = copy(- 1e-09 + argsin['DK'] / 1000)
# spcatjrange.m:13
    molstats['deltaJ'] = copy(- 1e-09 + argsin['deltaJ'] / 1000)
# spcatjrange.m:14
    molstats['deltaK'] = copy(- 1e-09 + argsin['deltaK'] / 1000)
# spcatjrange.m:15
    molstats['molname'] = copy('unknown')
# spcatjrange.m:16
    molstats['molid'] = copy(0)
# spcatjrange.m:17
    molstats['mua'] = copy(argsin['hasa'])
# spcatjrange.m:18
    molstats['mub'] = copy(argsin['hasb'])
# spcatjrange.m:19
    molstats['muc'] = copy(argsin['hasc'])
# spcatjrange.m:20
    argsout['vibstates'] = copy(1)
# spcatjrange.m:21
    argsout['spindegeneracy'] = copy(1)
# spcatjrange.m:22
    argsout['temp'] = copy(6)
# spcatjrange.m:24
    argsout['intensethresh'] = copy(- 11)
# spcatjrange.m:25
    
    argsout['maxf'] = copy(30)
# spcatjrange.m:26
    
    argsout['molstats'] = copy(molstats)
# spcatjrange.m:28
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
# spcatjrange.m:39
    argsout['jmax'] = copy(jmax)
# spcatjrange.m:40
    argsout['kmin'] = copy(max(kmin,0))
# spcatjrange.m:41
    argsout['kmax'] = copy(kmax)
# spcatjrange.m:42
    argsout['filename'] = copy(array([getspfitpath,'\\spcatfile2']))
# spcatjrange.m:43
    allpairs=runspcat(argsout,1)
# spcatjrange.m:44
    for i in arange(1,size(allpairs)).reshape(-1):
        allpairs[i]=updateline(allpairs[i])
# spcatjrange.m:46
    
    return allpairs
    

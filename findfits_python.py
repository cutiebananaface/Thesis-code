# Generated with SMOP  0.41
# from libsmop import *
# findfits.m
#rewritten (complete) but major corrections needed
# okay for this file, the data structures become too complicated for me to imagine without running the code- after line 719 I have stopped making edits to the data structures
import numpy as np
import matplotlib as mpl
import scipy
from copy import *
    

def findfits(linestouse=None,kit=None,*args,**kwargs):

    #originalkit = kit;
    allisotopes=[]
# findfits.m:4
    nummisses=0
# findfits.m:5
    ABClist=linestouse['ABClist']
# findfits.m:6
    linestouse=addABClist(linestouse,ABClist)
# findfits.m:8
    
    
    np.random.seed(6)
    for i in np.arange(1,kit['findfitsettings']['numtrials']).reshape(-1):
        #     sublines = findgoodsub(fit,kit);
#     if (isstruct(sublines) == 1)
#         sublines.targets = findTargets(fit,kit);
#     end
#     if (isstruct(sublines) == 1) && (isstruct(sublines.targets) == 1)
        isotopefit,kit=findIsotopeFit(linestouse,kit,linestouse['ABClist'],linestouse['dAdBdC'])
# findfits.m:17
        if type(isotopefit) is dict:
            #            fprintf('#s YES\n',sublines.descriptor);
            allisotopes.append(isotopefit)
# findfits.m:20
            #             close f
            #         end
            #         f = displaykitwithfits(kit);
            allisotopes=sortcellarraybyfield(allisotopes,'A')
# findfits.m:26
            nummisses=0
# findfits.m:27
            print(f'\\n\\ntotal of {np.size(allisotopes)} isotopologues found {i} trials\\n======\\n')
        else:
            nummisses=nummisses + 1
# findfits.m:32
            print(f'No new isotope found, {nummisses} misses in a row\\n')
        if np.size(allisotopes) >= kit['findfitsettings']['maxspecies']:
            break
        if nummisses > kit['findfitsettings']['maxmisses']:
            break
    return allisotopes
    
    

def addABClist(linestouse=None,ABClist=None,*args,**kwargs):

    stretchlinesets=[]
# findfits.m:49
    linestouse=addDerivatives(linestouse,np.array((0,0,0)))
# findfits.m:50
    linestouse=assesslines(linestouse)
# findfits.m:51
    # testDerivatives(linestouse,[1 1 1]);
# 1;
    
    for i in np.arange(1,np.size(ABClist)).reshape(-1):
        thisABCstretch=ABClist[i]
# findfits.m:57
        if max(abs(thisABCstretch)) > 100:
            thisABCstretch=thisABCstretch - linestouse['ABCxxxxx'][1:3]
# findfits.m:59
        thisABCxxxxxstretch=np.array((thisABCstretch,0,0,0,0,0))
# findfits.m:61
        thislinestouse=addDerivatives(linestouse,thisABCstretch)
# findfits.m:62
        stretchlineset['index'] = copy(i)
# findfits.m:63
        stretchlineset['absABCxxxxx'] = copy,copy(linestouse.ABCxxxxx + thisABCxxxxxstretch)
# findfits.m:65
        stretchlineset['diffABCxxxxx'] = copy(thisABCxxxxxstretch)
# findfits.m:66
        stretchlineset['lineset'] = copy(thislinestouse.lines)
# findfits.m:67
        stretchlinesets[i]=stretchlineset
# findfits.m:68
    
    linestouse['stretchlinesets'] = copy(stretchlinesets)
# findfits.m:70
    return linestouse
    

def getABClist(ABC=None,*args,**kwargs):

    dAdBdC=np.array((0.01,0.01,0.01))
# findfits.m:73
    ABClist[1]= ABC * np.array((0.99,0.99,0.99)))
# findfits.m:74
    #i think this may be an np.array and not a list, but I will treat it as a list for the moment
    ABClist.append(ABC * np.array((0.98,0.99,0.99)))
# findfits.m:75
    ABClist.append(ABC * np.array((0.99,1,1)))
# findfits.m:76
    return ABClist, dAdBdC
    
    

def ijkvals(sublines=None,*args,**kwargs):

    hitcounts=np.zeros((sublines['totaltriads'],1))
# findfits.m:79
    ivals=copy(hitcounts)
# findfits.m:80
    jvals=copy(hitcounts)
# findfits.m:81
    kvals=copy(hitcounts)
# findfits.m:82
    cc=1
# findfits.m:83
    for i in np.arange(1,sublines['line1']['numspurs']).reshape(-1):
        for j in np.arange(1,sublines['line2']['numspurs']).reshape(-1):
            for k in arange(1,sublines['line3']['numspurs']).reshape(-1):
                ivals[cc]=i
# findfits.m:87
                jvals[cc]=j
# findfits.m:88
                kvals[cc]=k
# findfits.m:89
                cc=cc + 1
# findfits.m:90
    return ivals,jvals,kvals,hitcounts
    

def extrappoint(sublines=None,cc=None,ivals=None,jvals=None,kvals=None,kit=None,returnset=None,*args,**kwargs):


    i=ivals[cc]
# findfits.m:96
    j=jvals[cc]
# findfits.m:97
    k=kvals[cc]
# findfits.m:98
    ijk=np.array((i,j,k))
# findfits.m:99
    df1=sublines['line1']['spurfs'][i] - sublines['line1']['theoryf']
# findfits.m:100
    df2=sublines['line2']['spurfs'][j] - sublines['line2']['theoryf']
# findfits.m:101
    df3=sublines['line3']['spurfs'][k] - sublines['line3']['theoryf']
# findfits.m:102
    df=np.array((df1,df2,df3))
# findfits.m:103
    if np.linalg.norm(df) < 10:
        1
    
    dABC=np.dot(sublines['dABCfromdf'],df)
# findfits.m:107
    targetfs=sublines['targets']['fList'] + (np.dot(sublines['targets']['fMatrix'],dABC))
# findfits.m:108
    hashes=np.round(targetfs / kit.findfitsettings.freqpixel)
# findfits.m:109
    
    for ii in np.arange(1,np.size(hashes)).reshape(-1):
        if hashes[ii] in sublines['targets']['kitContainer']:
            inspec= True
# findfits.m:111
    
    numhits=np.size(np.where(inspec == 1))
# findfits.m:113
    if returnset:
        whichhits=np.where(inspec == 1)
# findfits.m:115
    #set is a data type in python so changing it to set1
        set1['numhits'] = copy(numhits)
# findfits.m:117
        set1['df'] = copy(df)
# findfits.m:118
        set1['dABC'] = copy(dABC)
# findfits.m:119
        newlines= []
# findfits.m:120
        triadlines= []
# findfits.m:121
        fulldescriptor=''
# findfits.m:122
        for i in np.arange(1,np.size(inspec)).reshape(-1):
            thisline=sublines['targets']['linelist'][i]
# findfits.m:124
            if inspec[i] == 1:
                foundf=sublines['targets']['kitContainer]']['hashes'][i]
# findfits.m:127
                fulldescriptor=print("%s\\nline %d HIT  linearerror %3.1f %s %3.1f %3.1f h target %3.1f %d dupes found %3.1f" %(fulldescriptor,i,thisline['linearerror'],thisline['descriptor'],thisline['theoryf'],thisline['sixKweakpulsestrength'],targetfs[i],thisline['dupelevel'],foundf))
# findfits.m:128
            else:
                fulldescriptor=print('%s\\nline %d MISS linearerror %3.1f %s %3.1f %3.1f h target %3.1f %d dupes' % fulldescriptor,i,thisline['linearerror'],thisline['descriptor'],thisline['theoryf'],thisline['sixKweakpulsestrength'],targetfs[i],thisline['dupelevel'])
# findfits.m:130
            if numpy.in1d(thisline['hash'],sublines['hashes']):
                fulldescriptor=print('%s*'%fulldescriptor)
# findfits.m:133
        for i in np.arange(1,numhits).reshape(-1):
            thisi=whichhits[i]
# findfits.m:137
            foundf=sublines['targets']['kitContainer']['hashes'][thisi]
# findfits.m:138
            thisline=sublines['targets']['linelist'][thisi]
# findfits.m:139
            if 'expf' in thisline:
                thisline['orginalexpf'] = copy(thisline['expf'])
# findfits.m:141
            else:
                thisline['orginalexpf'] = copy(0)
# findfits.m:143
            thisline['orginalexph'] = copy(thisline['sublines']['heighttouse'])
# findfits.m:145
            ferrors=abs(foundf - kit['onedpeakfsunassigned'])
# findfits.m:147
            besti=np.where(ferrors == min(ferrors))[0]
# findfits.m:148
            thisline['exph'] = copy(kit['onedpeakhsunassigned'][besti])
# findfits.m:149
            thisline['expf'] = copy(foundf)
# findfits.m:151
            thisline['expfreq'] = copy(foundf)
# findfits.m:152
            newlines.append(thisline)
# findfits.m:153
            if numpy.in1d(thisline['hash'],sublines['hashes']):
                triadlines.append(thisline)
# findfits.m:155
        set1['c13lines'] = copy(newlines)
# findfits.m:158
        set1['triadlines'] = copy(triadlines)
# findfits.m:159
        set1['hitdescriptor'] = copy(fulldescriptor)
# findfits.m:160
    return numhits,ijk,df,dABC,set1
    
    
    

def addAllSpurs(sublines=None,kit=None,dAdBdC=None,*args,**kwargs):

    dAdBdC=dAdBdC*sublines['ABCxxxxx'][1:3]
# findfits.m:165
    sublines['line1'] = copy(addSpurs( sublines['line1'], sublines['heighttouse'],kit, sublines['dffromdABC'][1,:],dAdBdC))
# findfits.m:166
    sublines['line2'] = copy(addSpurs( sublines['line2'], sublines['heighttouse'],kit, sublines['dffromdABC'][2,:],dAdBdC))
# findfits.m:167
    sublines['line3'] = copy(addSpurs( sublines['line3'], sublines['heighttouse'],kit, sublines['dffromdABC'][3,:],dAdBdC))
# findfits.m:168
    sublines['totaltriads'] = oopy.copy(np.dot(np.dot( sublines['line1']['numspurs'], sublines['line2']['numspurs'], sublines['line3']['numspurs'])))
# findfits.m:169
    sublines['fulldescriptor'] = copy(print('3 lines, dscore %3.1f,hscore %3.1f, linearscore %3.1f,%d total triads'% sublines['dscore'], sublines['hscore'], sublines['linearscore'], sublines['totaltriads']))
    return sublines

# findfits.m:170
    

def findIsotopeFit(fit=None,kit=None,ABClist=None,dAdBdC=None):

    
    c13fit=0
# findfits.m:175
    sublines=findgoodsub(fit,kit)
# findfits.m:176
    if type(sublines) is not dict:
        return c13fit,kit
    
    sublines['targets'] = copy(findTargets(fit,kit))
# findfits.m:180
    if type(sublines['targets']) is not dict:
        return c13fit,kit
    
    print(sublines['targets']['hashreport'])
    for i in np.arange(1,np.size(ABClist)).reshape(-1):
        sublines['stretchindex'] = copy(i)
# findfits.m:186
        sublines=updatesublines(sublines,fit)
# findfits.m:187
        1
        sublines=addAllSpurs(sublines,kit,dAdBdC)
# findfits.m:190
        sublines['targets'] = copy(updatetargets(sublines.targets,fit,i))
# findfits.m:192
        sublines['targets'] = copy(addmaps(sublines.targets,kit))
# findfits.m:193
        c13fit=sweepSpurs(sublines,kit,1)
# findfits.m:195
        mpl.pyplot.subplot(1,1,1)
        mpl.pyplot.title('ABC {i}, [{str(ABClist[i])}]')
        sleep(0.001)
        if type(c13fit) is dict:
            kit=addfittokit(kit,c13fit)
# findfits.m:200
            break
    return c13fit, kit
    
    

def sweepSpurs(sublines=None,kit=None,verbose=None):

    if verbose=None:
        verbose=0
# findfits.m:207
    
    ivals,jvals,kvals,hitcounts=ijkvals(sublines)
# findfits.m:209
    bestyet=0
# findfits.m:210
    c13fit=0
# findfits.m:211
    iFitList= []
# findfits.m:212
    for cc in np.arange(1,np.size(ivals)).reshape(-1):
        numhits,ijk,df,dABC=extrappoint(sublines,cc,ivals,jvals,kvals,kit,0)
# findfits.m:214
        hitcounts[cc]=numhits
# findfits.m:215
        if numhits > bestyet:
            bestijk=copy(ijk)
# findfits.m:217
            bestf1f2f3=copy(df)
# findfits.m:218
            bestyet=copy(numhits)
# findfits.m:219
        if np.mod(cc,40000) == 0:
            print(f'finished %d of %d triads, bestyet %d\\n'% (cc,np.size(ivals),bestyet))
    
    whichi=significanthits(hitcounts,verbose)
# findfits.m:226
    if np.size(whichi) == 0:
        return c13fit
    
    besti=whichi(1)
# findfits.m:230
    print('mean hit count %3.1f, inspecting hit count of %d\\n'% (mean(hitcounts),hitcounts(besti)))
    numhits,ijk,df,dABC,thisset=extrappoint(sublines,besti,ivals,jvals,kvals,kit,1)
# findfits.m:233
    print(' frequency pixel size is %3.1f\\n' % kit['findfitsettings']['freqpixel'])
    print(sublines['fulldescriptor'])
    print(thisset['hitdescriptor'])
    1
    
    #thisfit = quickspfit(thistrial.lineset,thistrial.ABC);
#newfit = myquickspfit(thisset.triadlines,sublines.ABCxxxxx,0);
#  newfit = quickspfit(thisset.triadlines,sublines.ABCxxxxx,0);
    print('Parent fit:  %s\\n'% sublines['parentfitdescriptor'])
    newfit=quickspfit(thisset['c13lines'],sublines['ABCxxxxx'],0)
# findfits.m:242
    newfit['patterntype'] = copy('C13extension')
# findfits.m:243
    newfit=testfitonkit(newfit,kit)
# findfits.m:244
    #    newfit.C13frac = fitfrac(parentfit,childfit);
#newerfit2 = evolveFitSave(newfit,kit,'broadpval',[4 4]); #seems to never help, explore.
#     dABC2 = sublines.ABCxxxxx - newerfit2.ABCxxxxx;
#     dABC
#     dABC2
    
    if newfit['pval'] < kit['findfitsettings']['c13pval']:
        c13fit=copy(newfit)
# findfits.m:252
    
    # figure;
# plot(hitcounts);
    return c13fit
    
    
    

def significanthits(hitcounts=None,verbose=None):

    hitcounts=hitcounts - 3
# findfits.m:263
    
    lambda_=mean(hitcounts)
# findfits.m:264
    pvals=scipy.stats.poisson(hitcounts,lambda_,'upper')
# findfits.m:265
    thresh=0.1 / np.size(hitcounts)
# findfits.m:266
    whichi=np.where(pvals < thresh)
# findfits.m:267
    ipvals=pvals(whichi)
# findfits.m:268
    ipvals,XI=np.sort(ipvals,nargout=2), np.argsort(ipvals)
# findfits.m:269
    whichi=whichi[XI]
# findfits.m:270
    if verbose:
        #figure;
        mpl.pyplot.subplot(311)
        mpl.pyplot.plot(0,0)
        mpl.pyplot.subplot(1,1,1)
        mpl.pyplot.plot(hitcounts)
        # hold('all') hold is on automatically for mpl
        mpl.pyplot.stem(whichi,hitcounts(whichi),'r')
        mpl.pyplot.title(f'{np.size(whichi)} significant hits found bestp = {min(pvals)}\\n')
        mpl.pyplot.xlabel('attempt')
        mpl.pyplot.ylabel('hit count')
        #     subplot(3,1,2);
#     x = 0:max(hitcounts) + 5;
#     y = poisspdf(x,lambda);
#     y2 = y*0;
#     for i = 1:length(x)
#         y2(i) = length(find(hitcounts == x(i)))/length(hitcounts);
#     end
#     plot(x,y,'bs');
#     hold all;
#     plot(x,y2,'rs');
#     legend(sprintf('possion, lambda = #3.2f',lambda),'hitcount');
#     subplot(3,1,3);
#     x = 0:max(hitcounts) + 5;
#     y = poisspdf(x,lambda);
#     for i = 1:length(x)
#         y2(i) = length(find(hitcounts == x(i)))/length(hitcounts);
#     end
#     plot(x,y,'bs');
#     hold all;
#     plot(x,y2,'rs');
#     legend(sprintf('possion, lambda = #3.2f',lambda),'hitcount');
#     ylim([0 .01]);
    return whichi
    
    

def dfmax(dfdABC=None,dABC=None):

    vvals= [np.array([1,1,1]).T, np.array([1, 1, -1]).T, np.array([1, -1, 1]).T, np.array([1, -1, -1]).T]
# findfits.m:307
    for i in np.arange(1,4).reshape(-1):
        dfs[i]=dfdABC @ (dABC.T * vvals[i])
# findfits.m:309
    
    df=max(abs(dfs))
# findfits.m:311
    return df
    

def addSpurs(line=None,heighttouse=None,kit=None,dfdABC=None,dABC=None,*args,**kwargs):

    1
    df=dfmax(dfdABC,dABC)
# findfits.m:316
    line['spurhthresh'] = line['heighttouse'] / kit['findfitsettings']['heightratiomax']
# findfits.m:318
    # line.spurfmin = line.expf * kit.findfitsettings.freqmin;
# line.spurfmax = line.expf * kit.findfitsettings.freqmax;
    line['spurfmin'] = copy(line.theoryf - df)
# findfits.m:321
    line['spurfmax'] = copy(line.theoryf + df)
# findfits.m:322
    spurhs=np.array([])
# findfits.m:323
    spurfs=np.array([])
# findfits.m:324
    for i in np.arange(1,np.size(kit['onedpeakfsunassigned'])).reshape(-1):
        thisf=kit['onedpeakfsunassigned'][i]
# findfits.m:326
        thish=kit['onedpeakhsunassigned'][i]
# findfits.m:327
        if (thisf > line['spurfmin']) and (thisf < line['spurfmax']) and (thish > line['spurhthresh']):
            spurfs= np.append(spurfs, thisf)
# findfits.m:329
            spurhs= np.append(spurhs, thish)
# findfits.m:330
    
    line['numspurs'] = copy(length(spurfs))
# findfits.m:333
    line['spurfs'] = copy(spurfs)
# findfits.m:334
    line['spurhs'] = copy(spurhs)
# findfits.m:335
    line['spurdescription'] = copy(print(f'{line['numspurs']} spurs from {line['descriptor']}'))
# findfits.m:336
    return line


def findgoodsub(fit=None,kit=None,*args,**kwargs):


    #first task is pick lines to use for the search.  For now, pick just 3?
#Maybe I can use ALL for confirmation
    bestlines=0
# findfits.m:341
    exphs=extractonefieldfromcellarray(fit['lines'],fit['heighttouse'])
# findfits.m:342
    hthresh=min(kit['onedpeakhsunassigned'])
# findfits.m:343
    maxscore=0
# findfits.m:344
    for i in np.arange(1,kit['findfitsettings']['dicerolls']).reshape(-1):
        sublines=findasub(fit,exphs,hthresh,kit['findfitsettings']['minSNR'])
# findfits.m:346
        if sublines['healthy']:
            if sublines['netscore'] > maxscore:
                bestlines=copy(sublines)
# findfits.m:350
                maxscore=bestlines['netscore']
# findfits.m:351
    
    if maxscore == 0:
        print('No healthy triad found')
    else:
        print('picking sublines %s\\n' % bestlines['descriptor'])
    return bestlines
    
    

def findTargets(fit=None,kit=None):
 

    targets=0
# findfits.m:362
    exphs=extractonefieldfromcellarray(fit.lines,fit.heighttouse)
# findfits.m:363
    exphs,XI=np.sort(exphs)[::-1], np.argsort(exphs)[::-1]
# findfits.m:364
    hthresh=min(kit['onedpeakhsunassigned'])@ kit['findfitsettings']['targetminheight']
# findfits.m:365
    possibles=np.where(exphs > hthresh)
# findfits.m:366
    if np.size(possibles) < min(kit['findfitsettings']['numtargetmax']):
        print('Not enough strong targets')
        return targets
    else:
        targets.clear()
        numTargets=np.size(possibles)
# findfits.m:372
        exphs=exphs[np.arange(1,numTargets)]
# findfits.m:373
        XI=XI[np.arange(1,numTargets)]
# findfits.m:374
    
    
    #numTargets = min(kit.findfitsettings.numtargetmax,length(exphs));
    
    targets['indices'] = copy(XI)
# findfits.m:380
    targets['useheights'] = copy(exphs)
# findfits.m:381
    targets=updatetargets(targets,fit,0)
# findfits.m:384
    targets=addmaps(targets,kit)
# findfits.m:385
    return targets
    

def addmaps(targets=None,kit=None,*args,**kwargs):

    for i in np.arange(1,np.size(targets['linelist'])).reshape(-1):
        thisline=targets['linelist'][i]
# findfits.m:389
        thisline['useheight'] = copy(targets['useheights'][i])
# findfits.m:390
        c={[0]:[0]}# i do not think this line will work
# findfits.m:391
        remove(c,0)
        thisline['lineContainer'] = copy(c)
# findfits.m:393
        targets['linelist'][i]=thisline
# findfits.m:394
    
    
    frange=max(kit['onedpeakfsunassigned']) - min(kit['onedpeakfsunassigned'])
# findfits.m:397
    numblips=np.size(kit['onedpeakfsunassigned'])
# findfits.m:398
    freqpixel=kit['findfitsettings']['freqpixel']
# findfits.m:399
    autofreqpixel= 0.1 @ frange / numblips
# findfits.m:400
    targets['hashreport']= copy(print('%d blips are %3.1f wide, auto recommends %3.1f\\n' % (numblips,freqpixel,autofreqpixel)))
# findfits.m:401
    c=containers.Map(cellarray([0]),cellarray([0]))
    c= {np.array([0]): np.array([0])}
# findfits.m:402
    remove(c,0)
    for ii in np.arange(1,np.size(kit['onedpeakfsunassigned'])).reshape(-1):
        i=1 + length(kit.onedpeakfsunassigned) - ii
# findfits.m:405
        thisf=kit['onedpeakfsunassigned'][i]
# findfits.m:406
        thish=kit['onedpeakhsunassigned'][i]
# findfits.m:407
        thishash=np.floor(thisf / kit['findfitsettings']['freqpixel'])
# findfits.m:408
        c[thishash]=thisf
# findfits.m:409
        c[thishash + 1]=thisf
# findfits.m:410
        for j in np.arange(1,np.size(targets['linelist'])).reshape(-1):
            thisline=targets['linelist'][j]
# findfits.m:412
            thisbasef=thisline['theoryf']
# findfits.m:413
            thisbaseh=thisline['useheight']
# findfits.m:414
            if (abs(thisbasef - thisf) / thisbasef) < kit['findfitsettings']['fdriftmax']:
                if thish > (np.dot(thisbaseh,kit['findfitsettings']['spurratiomin'])):
                    targets['linelist'][j]['lineContainer'][thishash]=thisf
# findfits.m:417
                    targets['linelist'][j]['lineContainer'][thishash + 1]=thisf
# findfits.m:418
    
    for i in np.arange(1,np.size(targets['linelist'])).reshape(-1):
        thisline=targets['linelist'][i]
# findfits.m:424
        targetspurs=stripcellarray(thisline['lineContainer'].values())
# findfits.m:425
        targetkeys=stripcellarray(thisline['lineContainer'].keys())
# findfits.m:426
        thisline['numtargetspurs'] = copy(np.size(targetspurs))
# findfits.m:428
        thisline['targetspurrange'] = copy(np.array((min(targetspurs),max(targetspurs))))
# findfits.m:429
        thisline['targetfpixel'] = copy((max(targetspurs) - min(targetspurs)) / thisline['numtargetspurs'])
# findfits.m:430
        thisline['dupelevel'] = copy(np.floor(np.dot(kit['findfitsettings']['targetoccupancy'],((max(targetkeys) - min(targetkeys)) / thisline['numtargetspurs'])) / 2))
# findfits.m:431
        c2= {thisline['lineContainer']['keys']: thisline['lineContainer']['values']}
# findfits.m:433
        for j in targetkeys.reshape(-1):
            for kk in np.arange(j - thisline['dupelevel'],j + thisline['dupelevel']).reshape(-1):
                c2[kk]=c2[j]
# findfits.m:436
        thisline['broadlineContainer'] = copy(c2)
# findfits.m:439
        targets['linelist'][i]=thisline
# findfits.m:440
    
    targets['kitContainer'] = copy(c)
# findfits.m:443
    1
    return targets
    

def updatetargets(targets=None,fit=None,ABCindex=None,*args,**kwargs):

    targets['numtargets'] = copy(np.size(targets['indices']))
# findfits.m:451
    fMatrix=np.zeros((targets['numtargets'],3))
# findfits.m:452
    flist=np.zeros((targets['numtargets'],1))
# findfits.m:453
    linearerrorlist=np.zeros((targets['numtargets'],1))
# findfits.m:454
    linelist= []
# findfits.m:455
    for i in np.arange(1,targets['numtargets']).reshape(-1):
        j=targets['indices'][i]
# findfits.m:458
        if ABCindex == 0:
            thisline=fit['lines'][j]
# findfits.m:460
        else:
            thisline=fit['stretchlinesets'][ABCindex][lineset][j]
# findfits.m:462
        #thisline = fit.lines{j};
        flist[i]=thisline['theoryf']
# findfits.m:465
        linearerrorlist[i]=thisline['linearerror']
# findfits.m:466
        fMatrix[i,:]=thisline['dfdABC']
# findfits.m:467
        linelist[i]=thisline
# findfits.m:468
    
    targets['fList'] = copy(flist)
# findfits.m:471
    targets['fMatrix'] = copy(fMatrix)
# findfits.m:472
    targets['linearerrorlist'] = copy(linearerrorlist)
# findfits.m:473
    targets['numtargets'] = copy(np.size(flist))
# findfits.m:474
    targets['linelist'] = copy(linelist)
# findfits.m:475
    targets['descriptor'] = copy(print('%d targets found'% (targets.numtargets)))
# findfits.m:476
    1
    #at this point, fpredicts = flist + fMatrix * dABC.
    return targets
    

def updatesublines(sublines=None,fit=None,*args,**kwargs):


    #fit is only needed if stetchindex ~= 0
    sublines['hs']= np.array((sublines['lines1'][sublines]['heightouse'], sublines['line2'][sublines]['heighttouse'], sublines['line3'][sublines]['heighttouse']))
# findfits.m:482
    sublines['hashes'] = copy(np.array((sublines['line1']['hash'],sublines['line2']['hash'],sublines['line3']['hash'])))
# findfits.m:483
    sublines['minh'] = copy(min(sublines['hs']))
# findfits.m:484
    sublines['dffromdABC'] = copy(np.zeros((3)))
# findfits.m:487
    if sublines['stretchindex'] == 0:
        line1=sublines['line1']
# findfits.m:490
        line2=sublines['line2']
# findfits.m:491
        line3=sublines['line3']
# findfits.m:492
    else: #honestly I dont know how to format these lines because 
        line1=fit['stretchlinesets'][sublines]['stretchindex'][lineset][sublines.ivals(1)]
# findfits.m:494  $you are here
        line2=fit.stretchlinesets[sublines.stretchindex].lineset[sublines.ivals(2)]
# findfits.m:495
        line3=fit.stretchlinesets[sublines.stretchindex].lineset[sublines.ivals(3)]
# findfits.m:496
        sublines.ABCxxxxx = copy(fit.stretchlinesets[sublines.stretchindex].absABCxxxxx)
# findfits.m:497

    
    sublines.line1.theoryf = copy(line1.theoryf)
# findfits.m:499
    sublines.line2.theoryf = copy(line2.theoryf)
# findfits.m:500
    sublines.line3.theoryf = copy(line3.theoryf)
# findfits.m:501
    if 'expf' in sublines.line1:
        sublines.rawfs = copy(np.array((sublines.line1.expf,sublines.line2.expf,sublines.line3.expf)))
# findfits.m:503
    else:
        sublines.rawfs = copy(np.array((0,0,0)))
# findfits.m:505
    
    sublines.linearerrors = copy(np.array((line1.linearerror,line2.linearerror,line3.linearerror)))
# findfits.m:507
    sublines.stretchedfs = copy(np.array((line1.theoryf,line2.theoryf,line3.theoryf)))
# findfits.m:508
    sublines.dffromdABC[1,:]=line1.dfdABC
# findfits.m:509
    sublines.dffromdABC[2,:]=line2.dfdABC
# findfits.m:510
    sublines.dffromdABC[3,:]=line3.dfdABC
# findfits.m:511
    sublines.dABCfromdf = copy(sublines.dffromdABC ** - 1)
# findfits.m:513
    sublines.eigs = copy(np.linalg.eig(sublines.dffromdABC))
# findfits.m:514
    sublines.det = copy(np.linalg.det(sublines.dffromdABC))
# findfits.m:515
    sublines.hscore = copy(sublines.minh / sublines.hthresh)
# findfits.m:516
    sublines.dscore = copy(min(abs(sublines.eigs)))
# findfits.m:517
    sublines.linearscore = copy(1 / max(sublines.linearerrors))
# findfits.m:518
    sublines.types = copy(np.array((sublines.line1.transitiontype,sublines.line2.transitiontype,sublines.line3.transitiontype)))
# findfits.m:520
    sublines.numtypes = copy(np.size(np.unique(sublines.types)))
# findfits.m:521
    sublines.netscore = copy(max(sublines.numtypes,2))
# findfits.m:522
    
    if (sublines.hscore > sublines.minSNR):
        sublines.healthy = copy(1)
# findfits.m:525
        sublines.descriptor = copy(print('good lineset, hscore %3.1f,dscore %3.1f, netscore %3.2f' % (sublines.hscore,sublines.dscore,sublines.netscore)))
# findfits.m:526
    else:
        sublines.healthy = copy(0)
# findfits.m:528
        sublines.descriptor = copy(sprintf('sick lineset, hscore %3.1f,dscore %3.1f' % (sublines.hscore,sublines.dscore)))
# findfits.m:529
    return sublines
    
    
def findasub(fit=None,exphs=None,hthresh=None,minSNR=None,*args,**kwargs):

    sublines.hthresh = copy(hthresh)
# findfits.m:533
    ivals=pickn(exphs,3)
# findfits.m:534
    sublines.ivals = copy(ivals)
# findfits.m:535
    sublines.minSNR = copy(minSNR)
# findfits.m:536
    sublines.line1 = copy(fit.lines[ivals(1)])
# findfits.m:537
    sublines.line2 = copy(fit.lines[ivals(2)])
# findfits.m:538
    sublines.line3 = copy(fit.lines[ivals(3)])
# findfits.m:539

    if 'fitdescriptor' in fit:
        sublines.parentfitdescriptor = copy(fit.fitdescriptor)
# findfits.m:541
    else:
        sublines.parentfitdescriptor = copy('No parent')
# findfits.m:543
    
    sublines.ABCxxxxx = copy(fit.ABCxxxxx)
# findfits.m:545
    sublines.stretchindex = copy(0)
# findfits.m:546
    sublines.heighttouse = copy(fit.heighttouse)
# findfits.m:547
    sublines=updatesublines(sublines)
# findfits.m:548
    return sublines
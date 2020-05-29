# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:15:30 2020

@author: rodri
"""
#status: rewritten(complete)
# Generated with SMOP  0.41
#from libsmop import *
import numpy as np
#from np.size_py import np.size, findnonzeros
from sortcellarraybyfield_python import sortcellarraybyfield
from extractfieldsfromcellarray_python import extractfieldsfromcellarray
from updateseries_python import updateseries
from predictnext_python import predictnext
from countfrommcounttool_python import countfrommcounttool
from loadmatlab_workspace import load_mat
from updateseriessquare_python_temp import updateseriessquare
# extendseriessquarealltheway.m
from loadmatlab_workspace import load_mat
from copy import *
    
before= load_mat('input-extendseriessquarealltheway-nopinone')
fs= before['fs']
hs= before['hs']
squarelist= before['squarelist']
###look at this arianna, it ran without error but u still need to look over the output

def extendseriessquarealltheway(squarelist,fs,hs):


    census= np.zeros(20)
# extendseriessquarealltheway.m:4
    boggeddown=0
# extendseriessquarealltheway.m:5
    newsquarelist= copy(squarelist)
# extendseriessquarealltheway.m:6
    if np.size(squarelist) == 0:
        return newsquarelist,boggeddown,census
    
    extendingup=1
# extendseriessquarealltheway.m:10
    #in these nearly degenerate series, I'm crossing threads.  That is, I'm
#finding transitions that should be in one series and assigning them to the
#other.  More dangerous, in real spectra these lines might be unresolved.
#Having the same line in more than one spectrum is not necessarily wrong!
    ts=squarelist[0]['tightnesssettings']
# extendseriessquarealltheway.m:16
    numrounds=0
# extendseriessquarealltheway.m:17
    while extendingup:

        newlist= []
# extendseriessquarealltheway.m:19
        # thissquare = squarelist{i};
        for i in np.arange(0, np.size(squarelist)):
            s=copy(squarelist[i])
# extendseriessquarealltheway.m:23
            newguys=extendseriessquare(s,fs,hs,1)
# extendseriessquarealltheway.m:24
            newlist= np.concatenate((copy(newlist),newguys))
# extendseriessquarealltheway.m:25
        squarelist= sortcellarraybyfield(newlist,'netpval')
# extendseriessquarealltheway.m:27
        updowns= extractfieldsfromcellarray(squarelist,np.array(['upterminated','downterminated','degree','netpval']))
# extendseriessquarealltheway.m:29
        numrounds=numrounds + 1
# extendseriessquarealltheway.m:31
        qualities= np.sort(updowns['netpval'])
# extendseriessquarealltheway.m:32
        numquality= np.size(np.where(qualities< ts['minpval']))
        numquality= np.size(np.where(qualities< ts['minpval']))
# extendseriessquarealltheway.m:33
        print('after %d rounds, %d total,%d candidates with p < %.1e\\n' % (numrounds,np.size(squarelist),numquality,ts['minpval']))
        if numquality > ts['maxscaffolds']:
            boggeddown=1
# extendseriessquarealltheway.m:37
            squarelist=[]
# extendseriessquarealltheway.m:38
            break
        ups=updowns['upterminated']
# extendseriessquarealltheway.m:41
        #https://www.geeksforgeeks.org/python-index-of-non-zero-elements-in-python-list/
        stilllive=[idx for idx, val in enumerate(ups) if val == 0]
# extendseriessquarealltheway.m:42
        # fprintf('#d series remain, degree #d => #d going up\n',length(updowns.degree),min(updowns.degree),max(updowns.degree));
        if len(stilllive) == 0:
            break

    
    degrees=updowns['degree']
# extendseriessquarealltheway.m:51
    for i in np.arange(0,15):
        census[i]= np.size(np.where(degrees ==1))
# extendseriessquarealltheway.m:53
    
    newsquarelist=copy(squarelist)
    return newsquarelist, boggeddown, census
# extendseriessquarealltheway.m:55
    

def extendseriessquare(s, allfs, allhs, upordown):

    #if the squares can be extended, newsquares is a list of those extensions.
#currently assumes series 1 is complete.
    newsquares=[] #newsquares is a list
# extendseriessquarealltheway.m:64
    c1=s['nextcolumn']
# extendseriessquarealltheway.m:65
    r1=s['nextrow']
# extendseriessquarealltheway.m:66
    c2=s['nextnextcolumn']
# extendseriessquarealltheway.m:68
    r2=s['nextnextrow']
# extendseriessquarealltheway.m:69
    if c1 == 0:
        s['upterminated'] = copy(1)
# extendseriessquarealltheway.m:71
    
    if (s['upterminated'] == 1) and (upordown == 1):
        newsquares.insert(0,s)
# extendseriessquarealltheway.m:74
        return newsquares
    
    newsquares=[]
# extendseriessquarealltheway.m:77
    if (s['downterminated'] == 1) and (upordown == 0):
        newsquares.insert(0,s)
# extendseriessquarealltheway.m:79
        return newsquares
    
    #bpluscold = s['series1.fs(2) - s['series1.fs(1);
#bplusc = s['bpluscguess;
#fprintf('old guess #3.1f new guess #3.1f\n',bpluscold,bplusc);
    newsquares=[]
# extendseriessquarealltheway.m:86
    rup=min(np.size(s['column1']['fs']),r1 + 1)
# extendseriessquarealltheway.m:88
    rdown=max(1,r1 - 1)
# extendseriessquarealltheway.m:89
    otherfs=np.concatenate((s['fgrid'][r1-1,:],s['fgrid'][rup-1,:],s['fgrid'][rdown-1,:])) #brings index down
# extendseriessquarealltheway.m:90
    otherfs=otherfs[otherfs != 0]
# extendseriessquarealltheway.m:91
    energydiff=s['nextenergydiff']
# extendseriessquarealltheway.m:92
    # if ((c1 == 4)  && (c2 == 2)) || ((c1 == 1)  && (c2 == 3)) 
#     energydiff = s['energies(r1,1) - s['energies(r1,2);
#     if (s['energies(r1,1) == 0) || (s['energies(r1,2) == 0)
#         1;
#         error('energies below are not known');
#     end
# end
# if ((c1 == 4)  && (c2 == 3)) || ((c1 == 1)  && (c2 == 2)) 
#     energydiff = s['energies(r1+1,2) - s['energies(r1+1,1);
#     if (s['energies(r1+1,1) == 0) || (s['energies(r1+1,2) == 0)
#         1;
#         error('energies above are not known');
#     end
# end
# if c1 == 1
#     energydiff = -1 * energydiff;
# end
#this next line can be easily modified if there's a known ladder; it simply
#pulls known ladder(c1,r1).  
#it also should perhaps be moved.  It would be more elegant to at least
#predict in updateseriessquare.
    
    #[nextseries1f nextseries1h ferr1 series1frange] = extendseriesbyone(s,c1,r1,allfs,allhs); #this is new f2
    if s['laddermode'] == 0:
        allowedf= np.nonzero((allfs<s['nextmaxf']) & (allfs>s['nextminf']))
# extendseriessquarealltheway.m:117
        nextseries1f= allfs[allowedf]
# extendseriessquarealltheway.m:118
        nextseries1h=allhs[allowedf]
# extendseriessquarealltheway.m:119
    else:
        nextseries1f=s['ladderf'][r1-1,c1-1]
# extendseriessquarealltheway.m:121
        nextseries1h=1
# extendseriessquarealltheway.m:122
    
    # oldf = mean(series1frange);
# newf = s['nextpredictf;
# if abs(newf - oldf) > 0.01;
#     
#     newf
#     oldf
#     1;
# end
#[nextseries2f nextseries2h ferr2 series2frange] = extendseriesbyone(s,c2,nextj,allfs,allhs); #this is new f2
    
    # [nextseries2f nextseries2h ferr2 series2frange] = extendseriesbyone(s['series2,allfs,allhs,upordown,s); #this is new f3
# 
# [nextseries3f nextseries3h ferr series3frange] = extendseriesbyone(s['series3,allfs,allhs,upordown,s); #this is new f3
#n = length(s['column1.fs);
# if length(s['series1.realfs) < n
#     error('series 1 seems incomplete');
# end
# if upordown == 0
#     1;
# end
#targetnextj = nextj;
    for ii in np.arange(0,np.size(nextseries1f)):
        nextj=copy(r1)
# extendseriessquarealltheway.m:146
        #    for jj = 1:length(nextseries2f)
#    highenough = 0;
        f1=nextseries1f[ii]
# extendseriessquarealltheway.m:150
        #      f2 = nextseries2f(ii);
        fneeded=f1 - energydiff
# extendseriessquarealltheway.m:152
        h1=nextseries1h[ii]
# extendseriessquarealltheway.m:156
        if (h1 > s['aheight'] / s['tightnesssettings']['seriesaratio']):
            if s['laddermode'] == 0:
                minval,ival=closest(fneeded,allfs)
# extendseriessquarealltheway.m:161
                h2=allhs[ival]
# extendseriessquarealltheway.m:162
                f2=allfs[ival]
# extendseriessquarealltheway.m:163
            else:
                f2=s['ladderfs'][r2,c2]
# extendseriessquarealltheway.m:165
                h2=1
# extendseriessquarealltheway.m:166
            ferror=abs(f2 - fneeded)
# extendseriessquarealltheway.m:168
            if (ferror < s['tightnesssettings']['seriessquarefthresh']) and (h2 > s['bheight'] / s['tightnesssettings']['seriesbratio']) and (min(np.diff(np.sort(np.concatenate((np.array((f1,f2)),otherfs)) ))) > 0.1):
                1
                news= copy(s)
# extendseriessquarealltheway.m:171
                #             if addrowbelow
#                 nextj = targetnextj+1;
#                 1;
#             end
                #somewhere along the line this becomes an int? this definietly shouldnt be! lets change to float
                news['column1']['fs']= news['column1']['fs'].astype(np.float32)
                news['column2']['fs']= news['column2']['fs'].astype(np.float32)
                news['column3']['fs']= news['column3']['fs'].astype(np.float32)
                news['column4']['fs']= news['column4']['fs'].astype(np.float32)

                news['column1']['hs']= news['column1']['hs'].astype(np.float32)
                news['column2']['hs']= news['column2']['hs'].astype(np.float32)
                news['column3']['hs']= news['column3']['hs'].astype(np.float32)
                news['column4']['hs']= news['column4']['hs'].astype(np.float32)
                if 1 == c1:
                    news['column1']['fs'][r1-1]=f1
# extendseriessquarealltheway.m:178
                    news['column1']['hs'][r1-1]=h1
# extendseriessquarealltheway.m:179
                else:
                    if 4 == c1:
                        news['column4']['fs'][r1-1]=f1
# extendseriessquarealltheway.m:181
                        news['column4']['hs'][r1-1]=h1
# extendseriessquarealltheway.m:182
                if 2 == c2:
                    news['column2']['fs'][r2-1]=f2
# extendseriessquarealltheway.m:187
                    news['column2']['hs'][r2-1]=h2
# extendseriessquarealltheway.m:188
                else:
                    if 3 == c2:
                        news['column3']['fs'][r2-1]=f2
# extendseriessquarealltheway.m:190
                        news['column3']['hs'][r2-1]=h2
# extendseriessquarealltheway.m:191
                news['allpredicts'][r2-1,c2-1]=fneeded
# extendseriessquarealltheway.m:193
                try:
                    news['listpredicts']=np.insert(news['listpredicts'],s['nextline']-1,fneeded,axis=0)
                except:
                    print('error at 259 in extendseriessquarealltheway>extendseriessquare')
# extendseriessquarealltheway.m:194
                # news['listpredicts'][0][int(s['nextline']-1)]=fneeded
                news=updateseriessquare(news)
# extendseriessquarealltheway.m:195
                #             if containsf(news,3000) == 0
#                 1;
#             end
                if news['isoutlawed'] == 0:
                    #check to see if its legal?
                    newsquares.append(news)
# extendseriessquarealltheway.m:201
                else:
                    #   news.fgrid
                    1
    
    #if length(newsquares) == 0  #no extensions.  mark original as terminal and hand back
    if upordown == 1:
        s['upterminated'] = copy(1)
# extendseriessquarealltheway.m:212
    
    if upordown == 0:
        s['downterminated'] = copy(1)
# extendseriessquarealltheway.m:215
    
    s=updateseriessquare(s)
# extendseriessquarealltheway.m:217
    newsquares.append(s)
# extendseriessquarealltheway.m:218
    return newsquares
    

def closest(f,allfs):

    allfs=abs(allfs - f)
# extendseriessquarealltheway.m:222
    minval=min(allfs)
    ival = np.argmin(allfs)
# extendseriessquarealltheway.m:223
    return minval, ival


newsquarelist, boggeddown, census = extendseriessquarealltheway(squarelist,fs,hs)
print('oh my god almost there')
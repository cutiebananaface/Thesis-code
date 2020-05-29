# Generated with SMOP  0.41
# from libsmop import *
# findbowties.m
#status: rewrtten()
    # Usage: findbowties(kit, fit_params, cont(optional))
# - kit: kitfromcsvfile
# - fit_params: an object with variables (dot referenced); -1 for defaults
# - cont: if cont=0, return 1st grid found; else return all grids found in
#         < cont seconds
# - an octet is formatted [series1high, series2high, series3high, series4high,
#   series1low, series2low, series3low, series4low]
import numpy as np

def findbowties(kit=None,cont=None):

    # tic  not sure what to do with tic
    if cont= None:
        cont=copy(false)
# findbowties.m:11
    
    fit_params=kit['tightnesssettings']['bowties']
# findbowties.m:13
    fgrids,times=findquads(kit,fit_params,cont)
# findbowties.m:14
    return fgrids,times



def findquads(kit=None,fit_params=None,cont=None):

    fgrids=[]
# findbowties.m:18
    times=np.array([])
# findbowties.m:19
    divthresh=fit_params['divthresh']
# findbowties.m:20
    divthresh2=fit_params['divthresh']
# findbowties.m:21
    divthreshs=fit_params['divthreshs']
# findbowties.m:22
    weakAorB=fit_params['weakAorB']
# findbowties.m:23
    

    def getFsAndHs(*args,**kwargs):

        fs=kit['onedpeakfsunassigned']
    # findbowties.m:26
        hs=kit['onedpeakhsunassigned']
    # findbowties.m:27
        hthresh=max(hs) / fit_params['hsdivthresh']
    # findbowties.m:28
        fs=fs[hs > hthresh]
    # findbowties.m:29
        hs=hs[hs > hthresh]
    # findbowties.m:30
        sorted_hs= np.sort(hs)[::-1]
        XJ= np.argsort(hs)[::-1]
    # findbowties.m:31
        sorted_fs_by_hs=fs[XJ]
    # findbowties.m:32
        n=np.size(sorted_fs_by_hs)
    # findbowties.m:33
        return sorted_fs_by_hs,sorted_hs,n
        
    sorted_fs_by_hs,sorted_hs,n=getFsAndHs(nargout=3)
# findbowties.m:35
    

    def storeAndSortByDiffs(*args,**kwargs):

        alldiffs,allhighlines,alllowlines,allstrongNtsts,allweakNtsts=np.zeros((n,n))
    # findbowties.m:38
        for i in np.arange(1,n).reshape(-1):
            for j in np.arange(i + 1,n).reshape(-1):
                alldiffs[i,j]=sorted_fs_by_hs[i] - sorted_fs_by_hs[j]
    # findbowties.m:41
                alldiffs[j,i]=dot(- 1,alldiffs[i,j])
    # findbowties.m:42
                if sorted_fs_by_hs[i] > sorted_fs_by_hs[j]:
                    allhighlines[i,j]=sorted_fs_by_hs[i]
    # findbowties.m:44
                    allhighlines[j,i]=sorted_fs_by_hs[i]
    # findbowties.m:45
                    alllowlines[i,j]=sorted_fs_by_hs[j]
    # findbowties.m:46
                    alllowlines[j,i]=sorted_fs_by_hs[j]
    # findbowties.m:47
                else:
                    allhighlines[i,j]=sorted_fs_by_hs[j]
    # findbowties.m:49
                    allhighlines[j,i]=sorted_fs_by_hs[j]
    # findbowties.m:50
                    alllowlines[i,j]=sorted_fs_by_hs[i]
    # findbowties.m:51
                    alllowlines[j,i]=sorted_fs_by_hs[i]
    # findbowties.m:52
                if sorted_hs[i] > sorted_hs[j]:
                    allstrongNtsts[i,j]=sorted_hs[i]
    # findbowties.m:55
                    allstrongNtsts[j,i]=sorted_hs[i]
    # findbowties.m:56
                    allweakNtsts[i,j]=sorted_hs[j]
    # findbowties.m:57
                    allweakNtsts[j,i]=sorted_hs[j]
    # findbowties.m:58
                else:
                    allstrongNtsts[i,j]=sorted_hs[j]
    # findbowties.m:60
                    allstrongNtsts[j,i]=sorted_hs[j]
    # findbowties.m:61
                    allweakNtsts[i,j]=sorted_hs[i]
    # findbowties.m:62
                    allweakNtsts[j,i]=sorted_hs[i]
    # findbowties.m:63
        
        sorted_diffs_by_diffs=np.sort(alldiffs[1,n ** 2])
        XDIFF= np.argsort(alldiffs[1,n ** 2])
    # findbowties.m:67
        
        # XDIFF[i] = presort index for a given postsort index i; usage: alldiffs([XDIFF[i]])
        XHS =np.argsort(XDIFF)
    # findbowties.m:69
        
        allhighlines=allhighlines[XDIFF]
    # findbowties.m:70
        alllowlines=alllowlines[XDIFF]
    # findbowties.m:71
        allstrongNtsts=allstrongNtsts[XDIFF]
    # findbowties.m:72
        allweakNtsts=allweakNtsts[XDIFF]
    # findbowties.m:73
        return allhighlines,alllowlines,allstrongNtsts,allweakNtsts,sorted_diffs_by_diffs,XHS
        

    allhighlines,alllowlines,allstrongNtsts,allweakNtsts,sorted_diffs_by_diffs,XHS=storeAndSortByDiffs()
# findbowties.m:75
    

    def searchOneDiff(*args,**kwargs):
        

        for hI in np.arange(1,fit_params.rank).reshape(-1):
            ranges,rangesSorted=np.empty(1,n)
    # findbowties.m:79
            for i in np.arange(hI + 1,n).reshape(-1):
                if sorted_hs[i] < sorted_hs[hI] / divthreshs:
                    break
                if (cont and toc > cont) or (not cont and converged is dict):
                    return
                dI=XHS[np.dot((hI - 1),n) + i]
    # findbowties.m:87
                lowerIndex,upperIndex=searchRangeWithTolerance(sorted_diffs_by_diffs,dI,fit_params['dthresh'])
    # findbowties.m:88
                rangeLength=upperIndex - lowerIndex + 1
    # findbowties.m:89
                if (rangeLength < 3):
                    continue
                highLinesRange=allhighlines(np.arange(lowerIndex,upperIndex))
    # findbowties.m:91
                lowLinesRange=alllowlines(np.arange(lowerIndex,upperIndex))
    # findbowties.m:92
                strongNtstsRange=allstrongNtsts(np.arange(lowerIndex,upperIndex))
    # findbowties.m:93
                weakNtstsRange=allweakNtsts(np.arange(lowerIndex,upperIndex))
    # findbowties.m:94
                j1=dI - lowerIndex + 1
    # findbowties.m:95
                rangeLength,Idxs=searchRange2(strongNtstsRange,weakNtstsRange,divthresh,divthresh2,weakAorB,j1)
    # findbowties.m:97
                if (rangeLength < 3):
                    continue
                highLinesRange=highLinesRange(Idxs)
    # findbowties.m:99
                lowLinesRange=lowLinesRange(Idxs)
    # findbowties.m:100
                ranges[i]=np.concatenate(([highLinesRange],[lowLinesRange]))
    # findbowties.m:101
                rangesSorted[i]=np.sort(ranges[i][:]) # may need ravel
    # findbowties.m:102
                octet=np.zeros((1,8))
    # findbowties.m:103
                for j in np.arange(hI + 1,i - 1).reshape(-1):
                    if (np.size(ranges[i]) >= 4 or np.size(ranges[j]) >= 4) and np.sum(np.isin(rangesSorted[i],rangesSorted[j])) >= 4:
                        kis=otherInPair[np.where(ranges[i] == sorted_fs_by_hs[j])]
    # findbowties.m:106
                        if (kis == 0):
                            continue
                        kjs=otherInPair[np.where(ranges[j] == sorted_fs_by_hs[i])]
    # findbowties.m:108
                        if (kjs == 0):
                            continue
                        fs_k=np.intersect1d(ranges[i][kis],ranges[j][kjs])
    # findbowties.m:110
                        if np.size(fs_k)== 0:
                            continue
                        if np.size(ranges[j]) >= 8:
                            highLinesRangej=ranges[j][1,:]
    # findbowties.m:113
                            lowLinesRangej=ranges[j][2,:]
    # findbowties.m:114
                            dJ=XHS(np.dot((hI - 1),n) + j)
    # findbowties.m:115
                            octet[1,1:4]=np.concatenate((allhighlines[dJ],alllowlines[dJ],max(fs_k[1],sorted_fs_by_hs[i]),min(fs_k[1],sorted_fs_by_hs[i])))
    # findbowties.m:116
                            fgrid=rangeChoose2(highLinesRangej,lowLinesRangej,np.size(highLinesRangej),octet,fit_params)
    # findbowties.m:118
                            if np.size(fgrid) > 1:
                                fgrids.append(fgrid)
    # findbowties.m:120
                                times.append(toc)
    # findbowties.m:121
                                if not cont or toc > cont:
                                    return
                        if np.size(ranges[i]) >= 8:
                            octet[1,1]=allhighlines(dI)
    # findbowties.m:129
                            octet[1,2]=alllowlines(dI)
    # findbowties.m:130
                            octet[1,3]=max(fs_k[1],sorted_fs_by_hs[j])
    # findbowties.m:131
                            octet[1,4]=min(fs_k[1],sorted_fs_by_hs[j])
    # findbowties.m:132
                            fgrid=rangeChoose2(highLinesRange,lowLinesRange,rangeLength,octet,fit_params)
    # findbowties.m:134
                            if np.size(fgrid) > 1:
                                fgrids.append(fgrid)
    # findbowties.m:136
                                times.append(toc)
    # findbowties.m:137
                                if not cont or toc > cont:
                                    return
        
        return
        
    searchOneDiff()
    return
    
    
    

def searchRange2(strongNtstsRange=None,weakNtstsRange=None,divthresh=None,divthresh2=None,weakAorB=None,j1=None):

    high1val=strongNtstsRange[j1]
# findbowties.m:153
    
    low1val=weakNtstsRange[j1]
# findbowties.m:154
    
    strongNtst=max(np.concatenate((high1val,low1val)))
# findbowties.m:155
    weakNtst=min(np.concatenate((high1val,low1val)))
# findbowties.m:156
    strongIdxs=np.where(strongNtstsRange > strongNtst / divthresh)
# findbowties.m:157
    if not weakAorB:
        weakIdxs=np.where(weakNtstsRange > strongNtst / divthresh)
# findbowties.m:159
    else:
        weakIdxs=np.where(weakNtstsRange > weakNtst / divthresh2 and weakNtstsRange < dot(weakNtst,divthresh2))
# findbowties.m:161
    
    Idxs=np.intersect1d(strongIdxs,weakIdxs)
# findbowties.m:163
    rangeLength=np.size(Idxs)
# findbowties.m:164
    return rangeLength,Idxs

    
    

def rangeChoose2(highLinesRange=None,lowLinesRange=None,m=None,octet=None,fit_params=None):

    fgrid=0
# findbowties.m:168
    for j3 in np.arange(1,m).reshape(-1):
        if highLinesRange[j3] == octet[1,1] or highLinesRange[j3] == octet[1,3]:
            continue
        octet[1,np.arange(5,6)]=np.concatenate((highLinesRange[j3],lowLinesRange[j3]))
# findbowties.m:173
        for j4 in np.arange(j3 + 1,m).reshape(-1):
            if highLinesRange[j4] == octet[1,1] or highLinesRange[j4] == octet[1,3]:
                continue
            octet[1,np.arange(7,8)]=np.concatenate((highLinesRange[j4],lowLinesRange[j4]))
# findbowties.m:179
            if np.size(np.unique1d(octet[np.arange(1,8)])) == np.size(octet[np.arange(1,8)]):
                octet128=perm128(octet[arange(1,8)],fit_params['containsOblate'])
# findbowties.m:182
                lenoct128=np.size(octet128) / 8
# findbowties.m:183
                for j in np.arange(1,lenoct128).reshape(-1):
                    if isGoodOctet(octet128[j,np.arange()],fit_params):
                        fgrid=np.vstack((np.zeros((2,4)),octet128[j,np.arange(5,8)],octet128[j,arange(1,4)],np.zeros(4,4)))
# findbowties.m:186
                        return fgrid
    
    return fgrid



def searchRangeWithTolerance(arr=None,idx=None,dthresh=None):

    lowerIdx,upperIdx=idx
# findbowties.m:196
    for i in np.arange(idx,1,- 1).reshape(-1):
        if arr[i] < arr[idx] - dthresh:
            lowerIdx=i + 1
# findbowties.m:199
            break
    
    for i in np.arange(idx,np.size(arr)).reshape(-1):
        if arr[i] > arr[idx] + dthresh:
            upperIdx=i - 1
# findbowties.m:205
            break
    
    return lowerIdx,upperIdx
    

def otherInPair(its=None):

    if its == 0:
        ks=0
# findbowties.m:213
    else:
        itseven=its[np.mod(its,2) == 0] - 1
# findbowties.m:215
        itsodd=its[np.mod(its,2) == 1] + 1
# findbowties.m:216
        try:
            ks=np.vstack((itseven[:],itsodd[:]))
# findbowties.m:218
        except:
            its
            1
    
    return ks
    
# Generated with SMOP  0.41
# from libsmop import *
# perm128.m
#status: rewritten(complete) this one will need work!
import numpy as np
import copy    

def perm128(octet=None,isOblate=None):

    if isOblate= None:
        isOblate=copy.copy(true)
# perm128.m:3
    
    octet128=np.zeros((0,8))
# perm128.m:5
    pairs=np.reshape(octet,np.concatenate((2,4)))
# perm128.m:6
    # pairs=np.sort(pairs,2,'descend')
    pairs= np.sort(pairs)[::-1]
# perm128.m:7
    if not isOblate:
    	pairs1= [5,1,6,2,4,3,8,7]
    	pairs2=[3,1,4,2,6,5,8,7]
        octet128=np.vstack(pairs[pairs1],pairs[pairs2])
# perm128.m:9
    else:
        for jt in np.arange(0,7).reshape(-1):
            pairsj=copy.copy(pairs)
# perm128.m:12
            j=copy.copy(jt)
# perm128.m:13
            if j >= 4:
                pairsj[np.concatenate([3,4,5,6])]=pairsj(np.concatenate([5,6,3,4]))
# perm128.m:15
                j=j - 4
# perm128.m:16
            if j >= 2:
                pairsj[np.concatenate([1,2,3,4])]=pairsj(np.concatenate([3,4,1,2]))
# perm128.m:19
                j=j - 2
# perm128.m:20
            if j == 1:
                pairsj[np.concatenate([5,6,7,8])]=pairsj(np.concatenate([7,8,5,6]))
# perm128.m:23
            for it in np.arange(0,15).reshape(-1):
                pairsi=copy.copy(pairsj)
# perm128.m:26
                i=copy.copy(it)
# perm128.m:27
                if i >= 8:
                    pairsi[np.arange(),1]=swap(pairsi[:,1]) # not sure what swap is (variable or function?)
# perm128.m:29
                    i=i - 8
# perm128.m:30
                if i >= 4:
                    pairsi[np.arange(),2]=swap(pairsi[:,2])
# perm128.m:33
                    i=i - 4
# perm128.m:34
                if i >= 2:
                    pairsi[np.arange(),3]=swap(pairsi[:,3])
# perm128.m:37
                    i=i - 2
# perm128.m:38
                if i == 1:
                    pairsi[np.arange(),4]=swap(pairsi[:,4])
# perm128.m:41
                # octet128[end() + 1,arange()]=pairsi(concat([1,3,2,4,5,6,7,8]))
                octet128.append(pairsi[np.concatenate([1,3,2,4,5,6,7,8])])
# perm128.m:43
    
    return octet128
    

    

def swap(pair=None):
	pairindex1= [1,2]
	pairindex2=[2,1]
    pair[pairindex1]=pair[pairindex2]
# perm128.m:50
    return pair
    


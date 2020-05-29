# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:38:00 2020

@author: rodri
"""
#status: ported (complete) debugging(not working at column 2 line ~89 in guessquality)


import numpy as np
import copy as copy
from loadmatlab_workspace import load_mat

# before=load_mat("before-updateseries-nopinone")
# after=load_mat("after-updateseries-nopinone")
# s=before['s']
# output=after['ans']
def updateseries(s):

    s = seriesbasics(s) #call local function
    try:
        s['firsti']= np.where(s['fs']>0)[0][0] 
    except:
        s['firsti']= []
    try:
#    s['firsti']= np.where(s['fs']>0)[0][0] #calling fiindnonzeros, one of my functions , find the first index of the nonzero elements
        s['lasti']= np.where(s['fs']>0)[0][-1]
    except:
        s['lasti']=[]
    try:
        s['realfs']= s['fs'][np.where(s['fs']>0)]
    except:
        s['realfs']=[]#for some reason these are ints i am confused
    try:
        s['realhs']= s['hs'][np.where(s['fs']>0)]
    except:
        s['realhs']=[]#for some reason these are ints i am confused
    ## updateseries.m:9
    s=settolerance(s)
    # updateseries.m:11
    s=updatepval(s)
    # updateseries.m:12
    s=updatepredictions(s)
    # updateseries.m:13
    return s


def seriesbasics(s): #good
# function s = seriesbasics(s)
    s['predictstring'] = 'empty series'
    s['poly'] = 0
    s['nextf'] = 0
    s['prevf'] = 0
    s['predicts'] = np.array([])
    s['predecterrs'] = np.array([])
    s['outlawed'] = 0
    s['outlawchar'] = 'O'
    s['predicts'] = np.array([0, 0])
    s['predicterrs'] = np.array([0, 0])
    s['maxdegree'] = 3
    s['pval'] = 1
    if np.size(s['fs'], axis=None) == 2: #new series
#        array_temp= np.array([0, 0, 0, 0, 0, 0]) #may need to use dtype=Float
#        s['fs']= np.insert(array_temp, 2, s['fs'][((s['fs']>0).nonzero())]) 
#        s['hs'] = np.insert(array_temp, 2, s['hs'][ ((s['hs']>0).nonzero())]);
        s['fs']= np.array([0,0,s['fs'][0],s['fs'][1],0,0,0,0])
        s['hs']= np.array([0,0,s['hs'][0],s['hs'][1],0,0,0,0])
        #these are ints are the command is run
    return s

def settolerance(s):
# function s = settolerance(s)
    if s['whichcolumn'] == 1:
       s['tolerance'] = s['lowsidetolerance'].copy()
    elif s['whichcolumn'] == 2:
       s['tolerance'] = np.array([0, 0, 0, 0, 0])
    elif s['whichcolumn']== 3:
       s['tolerance'] = np.array([0, 0, 0, 0, 0])
    elif s['whichcolumn']== 4:
       s['tolerance'] = s['highsidetolerance'].copy()
    return s

def updatepredictions(s):
# function s = updatepredictions(s)
    if np.size(s['realfs'], axis=None) >= 2:
       n = min((np.size(s['realfs'],axis=None)),s['maxdegree']+1)

       x = np.arange(1,n+1)
       y = s['realfs'][0:n]  #!!!
       s['poly'] = np.polyfit(x,y,n-1).copy() #this one is not returning the numbers after the decimal
       s['prevf'] = np.polyval(s['poly'],0).copy()
       s['prevfspread'] = guessquality(y,s,0).copy()
       
       
       y = s['realfs'][-1-n:]
       s['poly'] = np.polyfit(x,y,n-1)
       s['nextf'] = np.polyval(s['poly'],n+1) #dtype and check index again
       s['nextfspread'] = guessquality(y,s,1) #dtype and check index again
       s['predictstring'] = ('%s next %.1f prev %.1f\n' % (str(s['predicterrs']),s['nextf'],s['prevf']))
    return s
   
def guessquality(fs,s,upordown):
# function fspread = guessquality(fs,s,upordown)
    degree = min(s['maxdegree'], np.size(fs))
    fspread = s['tolerance'][degree-1]
    minj = fs[0] / (fs[1] - fs[0]) #this is not working at column 2
    # print(f" fs[0], {fs[0]}, and fs[1] - fs[0] {fs[1] - fs[0]}")
    maxj = fs[-1] / (fs[-1] - fs[-2])
    # print(f" fs[-1], {fs[-1]}, and fs[-1] - fs[-2] {fs[-1] - fs[-2]}")
    if upordown == 1:
       jtouse = copy.copy(maxj)
    else:
       jtouse = copy.copy(minj)

    if jtouse < s['lowjthresh']:
       fspread = fspread * 2
    1
    return fspread

   
def updatepval(s):
# function s = updatepval(s)
   s['pval'] = 1
   for n in range(1, (np.size(s['realfs'], axis=None)-2)):
       # %   n = min(length(s['realfs']),maxdegree+1);
       numabove = np.size(s['realfs'],axis=None) - n
       numtouse = min(s['maxdegree'],numabove)
       x = np.arange(1,numtouse)
       y = s['realfs'][n+1:n+numtouse]
       [p] = np.polyfit(x,y,numtouse-1)
       predictf = np.polyval(p,0)
       ferr = s['realfs'][n] - predictf
       s['predicts'][-1+1] = predictf ###!!! not sure what type so i am unsure how to index
       s['predicterrs'][-1+1] = abs(ferr)
       thisp = abs(ferr) / s['frange']
       if thisp < 1:
           s['pval'] = copy.copy(s['pval'] * thisp)
   return s
   
# def test_answer():
#     assert updateseries(s) == output

# output= updateseries(s)
# print('cool u are done')
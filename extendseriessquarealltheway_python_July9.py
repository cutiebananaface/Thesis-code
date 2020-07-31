# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:15:30 2020

@author: rodri
"""
#status: rewritten(complete)
# Generated with SMOP  0.41
#from libsmop import *
# import unittest

import numpy as np
#from np.size_py import np.size, findnonzeros
from sortcellarraybyfield_python import sortcellarraybyfield
from extractfieldsfromcellarray_python import extractfieldsfromcellarray
# from updateseries_python import updateseries
# from predictnext_python import predictnext
# from countfrommcounttool_python import countfrommcounttool
from loadmatlab_workspace import load_mat
from updateseriessquare_python_July9 import updateseriessquare
# extendseriessquarealltheway.m
# from loadmatlab_workspace import load_mat
from copy import *
from datetime import datetime
from comparefileoutputs import unpackingstruct
    
# before= load_mat('input-extendseriessquarealltheway-nopinone')
# fs= before['fs']
# hs= before['hs']
# squarelist= before['squarelist']
# # ###look at this arianna, it ran without error but u still need to look over the output
# # middle=load_mat('inthemiddle-extendseriesalltheway-squarelist')
# # squarelist_m=middle['squarelist']
# # newlist_m=middle['newlist']
# # before_m=load_mat('squarelist-beforesorting-essatw')
# squarelist_beforesortm= load_mat('squarelist-beforesorting-essatw')['newlist']
# # after_m= load_mat('squarelist-aftersorting-essatw')
# squarelist_aftersortm= load_mat('squarelist-aftersorting-essatw')['squarelist']

def extendseriessquarealltheway(squarelist,fs,hs):


    census= np.zeros(20)
# extendseriessquarealltheway.m:4
    boggeddown=0
# extendseriessquarealltheway.m:5
    newsquarelist= deepcopy(squarelist)
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
            # print(f"this is the index: {i} ~~~~~~~ \n")
            s = deepcopy(squarelist[i])
# extendseriessquarealltheway.m:23
            newguys=extendseriessquare(s,fs,hs,1) #local function
# extendseriessquarealltheway.m:24
            newlist= np.concatenate((deepcopy(newlist),deepcopy(newguys)))
# extendseriessquarealltheway.m:25
#         squarelist=newlist
        squarelist= sortcellarraybyfield(newlist,'netpval') 
        #line for testing
        # return squarelist
# extendseriessquarealltheway.m:27
        updowns= extractfieldsfromcellarray(squarelist,np.array(['upterminated','downterminated','degree','netpval']))
# extendseriessquarealltheway.m:29
        numrounds=numrounds + 1
# extendseriessquarealltheway.m:31
        qualities= np.sort(updowns['netpval'])
# extendseriessquarealltheway.m:32
#         numquality= np.size(np.where(qualities< ts['minpval']))
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
    
    newsquarelist= deepcopy(squarelist)
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
        # newsquares.insert(0,s)
        # newsquares[0]=s
        newsquares.append(s)
# extendseriessquarealltheway.m:79
        return newsquares
    
    #bpluscold = s['series1.fs(2) - s['series1.fs(1);
#bplusc = s['bpluscguess;
#fprintf('old guess #3.1f new guess #3.1f\n',bpluscold,bplusc);
    newsquares=[]
# extendseriessquarealltheway.m:86
    rup=min(np.size(s['column1']['fs'])-1,r1 + 1)
# extendseriessquarealltheway.m:88
    rdown=max(0,r1 - 1)
# extendseriessquarealltheway.m:89
    otherfs=np.concatenate((s['fgrid'][r1,:],s['fgrid'][rup,:],s['fgrid'][rdown,:])) #brings index down
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
            if ((ferror < s['tightnesssettings']['seriessquarefthresh']) and
                    (h2 > s['bheight'] / s['tightnesssettings']['seriesbratio']) and
                    (min(np.diff(np.sort(np.concatenate((np.array((f1, f2)), otherfs))))) > 0.1)):
                news = deepcopy(s)
# extendseriessquarealltheway.m:171
                #             if addrowbelow
#                 nextj = targetnextj+1;
#                 1;
#             end
                #somewhere along the line this becomes an int? this definietly shouldnt be! lets change to float
                #changing to float64 to possibly fix #106 round 1
                news['column1']['fs']= news['column1']['fs'].astype(np.float64)
                news['column2']['fs']= news['column2']['fs'].astype(np.float64)
                news['column3']['fs']= news['column3']['fs'].astype(np.float64)
                news['column4']['fs']= news['column4']['fs'].astype(np.float64)

                news['column1']['hs']= news['column1']['hs'].astype(np.float64)
                news['column2']['hs']= news['column2']['hs'].astype(np.float64)
                news['column3']['hs']= news['column3']['hs'].astype(np.float64)
                news['column4']['hs']= news['column4']['hs'].astype(np.float64)
                if 1 == c1:
                    news['column1']['fs'][r1]=f1
# extendseriessquarealltheway.m:178
                    news['column1']['hs'][r1]=h1
# extendseriessquarealltheway.m:179
                else:
                    if 4 == c1:
                        news['column4']['fs'][r1]=f1
# extendseriessquarealltheway.m:181
                        news['column4']['hs'][r1]=h1
# extendseriessquarealltheway.m:182
                if 2 == c2:
                    news['column2']['fs'][r2]=f2
# extendseriessquarealltheway.m:187
                    news['column2']['hs'][r2]=h2
# extendseriessquarealltheway.m:188
                else:
                    if 3 == c2:
                        news['column3']['fs'][r2]=f2
# extendseriessquarealltheway.m:190
                        news['column3']['hs'][r2]=h2
# extendseriessquarealltheway.m:191
                news['allpredicts'][r2,c2-1]=fneeded
# extendseriessquarealltheway.m:193
                try:
                    news['listpredicts']=np.insert(news['listpredicts'],s['nextline']-1,fneeded,axis=0)
                except:
                    # print('error at 259 in extendseriessquarealltheway>extendseriessquare')
                    news['listpredicts'].resize((1, s['nextline']), refcheck=False)
                    news['listpredicts']= news['listpredicts'][0]
                    news['listpredicts'][s['nextline'] - 1] = fneeded
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
    
    s=updateseriessquare(s) #during this int column3.fs is wrong
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

# def checkkeys(generaldict1, generaldict2): #alt: make a list of the key values which are the same
#     #checks if keys in the dictionary are the same
#     missingkeys=[]
#     for x in generaldict1.keys():
#         if x not in generaldict2.keys(): 
#             missingkeys.append(x)
#     return missingkeys

# def unpack(generaldict1, generaldict2):
#     missingkeys= checkkeys(generaldict1, generaldict2)
#     with open('unpackoutput.txt', 'a') as f:
#         print(f"these keys are missing from generaldict2 {missingkeys}", file=f)
#     for key, val in generaldict1.items():
#         if key not in missingkeys:
#             if type(generaldict1[key]) is dict:
#                 unpack(generaldict1[key], generaldict2[key])
#             else:
#                 with open('unpackoutput.txt', 'a') as f:
#                     print(f" generaldict[{key}],\n {generaldict1[key]} and {generaldict2[key]},\n {generaldict1[key] == generaldict2[key]} \n", file=f) # i think i could just print the val but whatever

# def unpackingstruct(struct, struct2):
#     # now = datetime.now() #time to include in the file
#     with open('unpackoutput.txt', 'a') as f: #during a newrun, add a new line with the date and time
#         print(f"----~newrun: date/time={datetime.now()} ~-----~newrun~-----~newrun~-----~newrun~----\n", file=f)
#     #block for actually unpacking and comparing elements    
#     for ind, j in enumerate(struct): #unpacking the list, ind is the index, j is the val

#         missingkeys=checkkeys(struct[ind], struct2[ind]) #check for missing keys in the two structs
#         with open('unpackoutput.txt', 'a') as f:
#             print(f"these keys are missing from struct2[{ind}] {missingkeys}", file=f) #print missingkeys to file
        
#         for x, y in j.items(): #iterates through j (a dict), x is the key and y is the val
#             if x not in missingkeys: #dont run this block unless the key actually exists
#                 if type(j[x]) is dict:
#                     with open('unpackoutput.txt', 'a') as f:
#                         print(f"squarelist[{ind}][{x}] is a dict, unpack further \n", file=f)
#                     unpack(struct[ind][x], struct2[ind][x])
#                 else:
#                     with open('unpackoutput.txt', 'a') as f:
#                         print(f"squarelist[{ind}][{x}], \n {struct[ind][x]} and {struct2[ind][x]},\n {struct[ind][x]==struct2[ind][x]} \n", file=f)


# squarelist = extendseriessquarealltheway(squarelist,fs,hs)
# # unpackingstruct(squarelist, squarelist_beforesortm, "unpackingbefore-2.txt")
# # unpackingstruct(squarelist, squarelist_beforesortm)
# print('oh my god almost there')


# class Mytest(unittest.TestCase):
#     def setUp(self):
#         before= load_mat('input-extendseriessquarealltheway-nopinone')
#         fs= before['fs']
#         hs= before['hs']
#         squarelist= before['squarelist']
#         ###look at this arianna, it ran without error but u still need to look over the output
#         middle=load_mat('inthemiddle-extendseriesalltheway-squarelist')
#         self.squarelist_m=middle['squarelist']
#         # newlist_m=middle['newlist']
#         self.squarelist= extendseriessquarealltheway(squarelist,fs,hs)
#         # print(type(self.squarelist), type(self.squarelist_m))

#     def test(self):
#         # self.assertDictEqual(self.squarelist, self.squarelist_m)
#         # pass
#         for ind,j in enumerate(self.squarelist): #ind is the index in the cell array squarelist, j is the element in that array, 
#             print(ind)
#             print(type(self.squarelist[ind]))
#             self.assertEqual(self.squarelist[ind], self.squarelist_m[ind])
#             for x,y in j.items(): # j is a dict, and x is a key and y is the value
#                 if type(j[x]) is dict: #if a specific key in j is a dict, do this
#                     for xj, yj in j[x].items(): # iterate through this dict, xj is the key and yj the value
#                         #so j <outer dict> [x] <key in outer dict> [xj] <key of x, the nested dict>
#                         if not (xj =="tightnesssettings" or xj =="counttool" or x =="tightnesssettings"): 
#                             print(ind, x, xj)
#                             try:
#                                 self.assertEqual(self.squarelist[ind][x][xj], self.squarelist_m[ind][x][xj])
#                                 print(self.squarelist[ind][x][xj] == self.squarelist_m[ind][x][xj])
#                             except ValueError:
#                                 print("value error! \n")
#                                 # print(self.squarelist[ind], self.squarelist_m[ind])
#                             except KeyError:
#                                 print("key error! \n")
#                                 # print(self.squarelist[ind], self.squarelist_m[ind])
#                             except:
#                                 print("error occurred")
#                                 # try:
#                                 #     print(self.squarelist[ind][x][xj]==self.squarelist_m[ind][x][xj])
#                                 # except ValueError:
#                                 #     print('value error', self.squarelist[ind][x][xj], self.squarelist_m[ind][x][xj])
#                                 # except KeyError:
#                                 #     raise Exception("encountered KeyError!!")
#                                 #     print(self.squarelist[ind][x], self.squarelist_m[ind][x] )
#                 try:
#                     self.assertEqual(self.squarelist[ind][x], self.squarelist_m[ind][x])
#                 except: 
#                     print('bottom',ind,x)
#                 try:
#                     print(self.squarelist[ind][x]==self.squarelist_m[ind][x])
#                 except ValueError:
#                     print('bottom value error', self.squarelist[ind][x], self.squarelist_m[ind][x])
#                 if type(j[x])

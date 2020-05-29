# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:51:48 2020

@author: rodri
"""
import numpy as np
from copy import *
from loadmatlab_workspace import loadmat
from updateseries_python import updateseries
before=loadmat('updateseriessquare_before')
s=before['s']
s['column1'] = updateseries(s['column1'])
s['column2'] = updateseries(s['column2'])
s['column3'] = updateseries(s['column3'])
s['column4'] = updateseries(s['column4'])
s['numjs'] = np.size(s['column1']['fs'], axis=None)

s['fgrid'] = np.zeros((s['numjs'],4))

# if s['dtype == 1
s['fgrid'][:,0]=s['column1']['fs']

s['fgrid'][:,1]=s['column2']['fs']

s['fgrid'][:,2]=s['column3']['fs']

s['fgrid'][:,3]=s['column4']['fs']

if not 'originalfgrid' in s: 
    s['originalfgrid']= s['fgrid']

if not 'allpredicts' in s == 0:
    s['lineorder'] = np.dot(s['fgrid'],0)
# updateseriessquare.m:27
    if s['flattype']== 'D':
        if s['fgrid'][2,0] != 0:
            s['lineorder'][2]=np.array([1,3,0,0])
            s['lineorder'][3]=np.array([2,0,4,0])
        else:
            s['lineorder'][2]=np.array([0,0,3,1])
            s['lineorder'][3]=np.array([0,4,0,2])
    elif s['flattype']=='/':
        s['lineorder'][2]=np.array([3,1,0,0])
        s['lineorder'][3]=np.array([0,2,0,4])
    elif s['flattype']== '\\':
        s['lineorder'][2]=np.array([0,0,1,3])
        s['lineorder'][3]=np.array([4,0,2,0])
#         s['lineorder(6,:) = [13 16  14  15];
#         s['lineorder(7,:) = [17 20  18  19]; 
#         s['lineorder(8,:) = [21 24  22  23];

    s['allpredicts'] = s['fgrid']* 0
    s['alineorder'] = s['lineorder']
    s['corners'] = np.zeros((1,8))

s['maxnumlines'] = np.amax(s['lineorder'])
s['maxnumlines']= int(s['maxnumlines'])
s['columnorder'] = np.zeros((1,s['maxnumlines']))
s['roworder'] = deepcopy(s['columnorder'])
a=np.where(s['lineorder']) #index where lineorder is nonzero
c=np.argsort(s['lineorder'][a]) #lineorder[a]-> only where lineorder is nonzero, and the indices for the sorting of it
ro=a[0][c] #now sort the nonzero indices
co=a[1][c] #now sort the nonzero indices
#n=1
#for i in np.arange(0,s['numjs']).reshape(-1):
#    for j in np.arange(0,3).reshape(-1):
#        #             if s['originalfgrid(i,j) ~= 0
##                 s['alineorder(i,j) = n;
##                 n = n+1;
##             end
#        thiso=s['lineorder'][i,j]
#        thiso=int(thiso)
#        print(f"this is i,{i}, and j,{j}, and this is thiso, {thiso}\n")
#        print(f"this is columnorder, {s['columnorder']} and this is roworder {s['roworder']}\n")
#        if thiso > 0:
#            thiso_c= deepcopy(thiso)-1
#            s['columnorder'][0][thiso_c]= deepcopy(j)
#            s['roworder'][0][thiso_c]= deepcopy(i)
#            print(f"4loop. this is i,{i}, and j,{j}, and this is thiso, {thiso}, this is thiso_c, {thiso_c}\n")
#            print(f"4loop.this is columnorder, {s['columnorder']} and this is roworder {s['roworder']}\n")
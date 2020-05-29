# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:06:22 2020

@author: rodri
"""
import numpy as np
from mylength_py import mylength
orange= np.random.random((10,))
apple=[]
for i in range(1, np.size(orange, axis=None)):
    print(i)
    apple.append(orange[i])
    
###will print i from 1 to 9
## fills apple with orange from 1 to 9
apple=[]
for i in range(0, np.size(orange, axis=None)):
    print(i)
    apple.append(orange[i])
    
    
#after changes i will go from 1 to 9 
# and apple will be a copy of orange 
    
 #--------------------
cake={}
cake['icing']='vanilla'

try:
    if cake['icing']== 'vanilla':
        print('yum')
except:
        cake['icing']='chocolate'

mango=[]
for mm in range(1,4):
    print(mm)
    mango=orange[mm]


baby={}
baby['pacifier']='yes'
baby['crib']='of course'
if 'toys' in baby:
    pass
else:
    baby['toys']='brandnew'
    
cats= np.arange(1,20)
#np.reshape(-1):
    
    
    
    
    
    
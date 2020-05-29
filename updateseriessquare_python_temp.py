# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:06:32 2020

@author: rodri
"""
#status: rewritten (complete) need to correct index while porting

# Generated with SMOP  0.41
#from libsmop import *
from updateseries_python import updateseries
import numpy as np
import math as math
from copy import *
from scipy import interpolate
#import operator as op
from predictnext_python import predictnext
from countfrommcounttool_python import countfrommcounttool
from loadmatlab_workspace import load_mat

# updateseriessquare.m

before=load_mat('before-updateseriessquare-nopinone')
s_i=before['s']

def updateseriessquare(s, slowmode=1): #fgrid is made here!

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
    
    if 'allpredicts' not in s:
        s['lineorder'] = s['fgrid'] * 0
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
        s['alineorder'] = deepcopy(s['lineorder']) #alineorder is same as MATLAB here
        s['corners'] = np.zeros((1,8))
    
    s['maxnumlines'] = np.amax(s['lineorder'])
    s['maxnumlines']= int(s['maxnumlines'])
    s['columnorder'] = np.zeros((1,s['maxnumlines']))
    s['roworder'] = copy(s['columnorder'])
    
    
    n=1
    nonzero_lineorder=np.where(s['lineorder']) #index where lineorder is nonzero
    indice_nz_lineorder=np.argsort(s['lineorder'][nonzero_lineorder]) #lineorder[a]-> only where lineorder is nonzero, and returns the indices for the sorting of it
    s['roworder']=nonzero_lineorder[0][indice_nz_lineorder] #now apply the sorting to the nonzero indices
    s['columnorder']=nonzero_lineorder[1][indice_nz_lineorder] 
#    for i in np.arange(0,s['numjs']).reshape(-1):
#        for j in np.arange(0,3).reshape(-1):
#            #             if s['originalfgrid(i,j) ~= 0
##                 s['alineorder(i,j) = n;
##                 n = n+1;
##             end
#            thiso=s['lineorder'][i,j]
#            thiso=int(thiso)
#            print(f"this is i,{i}, and j,{j}, and this is thiso, {thiso}\n")
#            print(f"this is columnorder, {s['columnorder']} and this is roworder {s['roworder']}\n")
#            if thiso > 0:
#                thiso_c= deepcopy(thiso)
#                s['columnorder'][0][thiso_c]= deepcopy(j)
#                s['roworder'][0][thiso_c]= deepcopy(i)
#                print(f"4loop. this is i,{i}, and j,{j}, and this is thiso, {thiso}, this is thiso_c, {thiso_c}\n")
#                print(f"4loop.this is columnorder, {s['columnorder']} and this is roworder {s['roworder']}\n")
    s.update({'listpredicts': []})
    for i in np.arange(0,4):
        r=s['roworder'][i]
        c=s['columnorder'][i]
        s['listpredicts'].append(s['fgrid'][r][c] - s['flatsquare']['flaterrors'][i])
        s['allpredicts'][r,c]=s['listpredicts'][i]
    
    s['allerrors'] = s['fgrid'] - s['allpredicts']
    
    
    fdiffs=np.array([])
    if np.size(s['column1']['realfs']) >= 2:
        fdiffs=np.diff(s['column1']['realfs'])
    
    if np.size(s['column4']['realfs']) >= 2:
        fdiffs=np.concatenate((fdiffs, np.diff(s['column4']['realfs'])))
    
    if np.size(fdiffs) > 0:
        s['bpluscguess'] = np.mean(fdiffs)
        s['bpluscerror'] = s['lowsidetolerance'][1]
    else:
        if np.size(s['column2']['realfs']) >= 2:
            fdiffs= np.diff(s['column2']['realfs'])
            
        if np.size(s['column3']['realfs']) >= 2:
            fdiffs= np.concatenate((fdiffs, np.diff(s['column3']['realfs'])))
            
        if np.size(fdiffs) > 0:
            s['bpluscguess'] = np.mean(fdiffs)
            s['bpluscerror'] = s['lowsidetolerance'][1]
        else:
            s['bpluscguess'] = 3000
            s['bpluscerror'] = s['bpluscguess']*0.9

    
    s['highestfullrow'] = 0
    s['lowestfullrow'] = 0
    
    n= np.size(s['column1']['fs']) 
    i=np.size(s['column1']['fs'])-1
    if (s['column1']['fs'][i] != 0) and (s['column2']['fs'][i] != 0) and (s['column3']['fs'](i) != 0) and (s['column4']['fs'][i] != 0):
        s['highestfullrow'] = i
# updateseriessquare.m:119
    if (s['column1']['fs'][n - i] != 0) and (s['column2']['fs'][n - i] != 0) and (s['column3']['fs'][n - i] != 0) and (s['column4']['fs'][n - i] != 0):
        s['lowestfullrow'] = n - i
# updateseriessquare.m:122
    if (s['column1']['fs'][i] != 0) or (s['column2']['fs'][i] != 0) or (s['column3']['fs'][i] != 0) or (s['column4']['fs'][i] != 0):
        s['highestpartialrow'] = i
# updateseriessquare.m:125
    if (s['column1']['fs'][n - i] != 0) or (s['column2']['fs'][n - i] != 0) or (s['column3']['fs'][n - i] != 0) or (s['column4']['fs'][n - i] != 0):
        s['lowestpartialrow'] = n - i
# updateseriessquare.m:128
    
    #s['degree = length(s['column1']['fs']) - 1;
    quadsums=np.array([])
# updateseriessquare.m:132
    for i in np.arange(1, np.size(s['column1']['fs']) - 1):
        if (s['fgrid'][i,0] != 0) and (s['fgrid'][i + 1,0] != 0) and (s['fgrid'][i,1] != 0) and (s['fgrid'][i + 1,2] != 0):
            quadsums=np.append(quadsums,s['fgrid'][i,0] + s['fgrid'][i + 1,0] - s['fgrid'][i,1] - s['fgrid'][i + 1,2])
# updateseriessquare.m:135
        if (s['fgrid'][i,3] != 0) and (s['fgrid'][i + 1,3] != 0) and (s['fgrid'][i,2] != 0) and (s['fgrid'][i + 1,1] != 0):
            quadsums=np.append(quadsums,s['fgrid'][i,3] + s['fgrid'][i + 1,3] - s['fgrid'][i,2] - s['fgrid'][i + 1,1])
# updateseriessquare.m:138
        if (s['fgrid'][i,0] != 0) and (s['fgrid'][i,1] != 0) and (s['fgrid'][i + 1,1] != 0) and (s['fgrid'][i + 1,3] != 0):
            quadsums=np.append(quadsums,s['fgrid'][i,0] - s['fgrid'][i + 1,3] - s['fgrid'][i,1] + s['fgrid'][i + 1,1])
# updateseriessquare.m:141
        if (s['fgrid'][i + 1,0] != 0) and (s['fgrid'][i,2] != 0) and (s['fgrid'][i + 1,2] != 0) and (s['fgrid'][i,3] != 0):
            quadsums=np.append(quadsums,s['fgrid'][i + 1,0] - s['fgrid'][i,3] + s['fgrid'][i,2] - s['fgrid'][i + 1,2])
# updateseriessquare.m:144
        if (s['fgrid'][i,0] != 0) and (s['fgrid'][i,1] != 0) and (s['fgrid'][i,2] != 0) and (s['fgrid'][i,3] != 0):
            quadsums=np.append(quadsums,s['fgrid'][i,0] + s['fgrid'][i,3] - s['fgrid'][i,2] - s['fgrid'][i,1])
# updateseriessquare.m:147
    
    s['healthy'] = checkhealth(s)
# updateseriessquare.m:150
    s['aheight'] = np.mean(np.concatenate((s['column1']['realhs'],s['column4']['realhs'])))
# updateseriessquare.m:151
    s['bheight'] = np.mean(np.concatenate((s['column2']['realhs'],s['column3']['realhs'])))
# updateseriessquare.m:152
    #     if length(s['column1']realhs) > 0
#         s['aheight = mean(s['column1']realhs);
#     else
#         s['aheight = s['column4['realhs'](end);
#     end
#     if (length(s['column1']realhs) > 0) && (length(s['column4['realhs']) > 0)
#         aheight = (s['column1']realhs(end) + s['column1']realhs(end))/2;
#     end
#     if length(s['column2['realhs']) > 0
#         bheight = s['column2['realhs'](end);
#     else
#         bheight = s['column3['realhs'](end);
#     end
#     if (length(s['column2['realhs']) > 0) && (length(s['column3['realhs']) > 0)
#         bheight = (s['column2['realhs'](end) + s['column3['realhs'](end))/2;
#     end
    s['longquadstring'] = ('Quad sums:')
# updateseriessquare.m:169
    for i in np.arange(0,np.size(quadsums)).reshape(-1):
        s['longquadstring'] = f"{s['longquadstring']} \n {quadsums[i]: .4f}"
# updateseriessquare.m:171
    
    s['medianquadsum'] = np.median(abs(quadsums))
# updateseriessquare.m:173
    s['maxquadsum'] = max(abs(quadsums))
# updateseriessquare.m:174
    s['quadstring'] = f"{np.size(quadsums)} quads, median {np.dot(s['medianquadsum'],1000): .1f},max {np.dot(s['maxquadsum'],1000): 0.1f} Khz"
# updateseriessquare.m:175
    meanquadsum= math.sqrt(np.mean(quadsums ** 2))
# updateseriessquare.m:176
    s['meanquadsum'] = max(meanquadsum, 0.001)
# updateseriessquare.m:177
    if s['meanquadsum'] > 0.1:
        #     if containsf(s,3000) == 0
#         fprintf('doesnt have 3000');
#     end
        quadsums
        s['fgrid']
        #  error('quads dont work!');
    
    s['quadsums'] = quadsums
# updateseriessquare.m:186
    s['onequadpval'] = s['meanquadsum'] / s['frange']
# updateseriessquare.m:187
    sums=np.array([])
# updateseriessquare.m:188
    csums=np.array([])
# updateseriessquare.m:189
    s['allfs'] = np.concatenate((s['column1']['realfs'],s['column2']['realfs'],s['column3']['realfs'],s['column4']['realfs']))
# updateseriessquare.m:192
    s['allhs'] = np.concatenate((s['column1']['realhs'],s['column2']['realhs'],s['column3']['realhs'],s['column4']['realhs']))
# updateseriessquare.m:193
    s['listerrors'] = np.zeros((1,np.size(s['allfs'])))
# updateseriessquare.m:195
    s['f1'] = s['fgrid'][s['roworder'][0]][s['columnorder'][0]]
# updateseriessquare.m:196
    for i in np.arange(0,4).reshape(-1):
        for j in np.arange(0,np.size(s['column1']['fs'])).reshape(-1):
            thiso=s['alineorder'][j,i]
# updateseriessquare.m:199
            thisf=s['fgrid'][j,i]
# updateseriessquare.m:200
            if thisf != 0:
                if thiso == 0:
                    1
                thiso=int(thiso)
                s['listerrors'][0][thiso-1]=s['allerrors'][j,i]
# updateseriessquare.m:205
#    a=np.where(s['alineorder']) #index where lineorder is nonzero
#    kk=np.argsort(s['alineorder'][a]) #lineorder[a]-> only where lineorder is nonzero, and returns the indices for the sorting of it
#    s['roworder']=a[0][kk] #now apply the sorting to the nonzero indices
#    s['columnorder']=a[1][kk] 
    
    s['allnormerrors'] = s['allerrors'] / s['f1']
# updateseriessquare.m:209
    s['listnormerrors'] = s['listerrors'] / s['f1']
# updateseriessquare.m:210
    s['errorstring'] = ('prediction\\n errors\\n')
# updateseriessquare.m:211
    s['searchspace'] = 1
# updateseriessquare.m:212
    for i in np.arange(0, np.size(s['listerrors'])).reshape(-1):
        if (i <= 11) and ((i == 1) or np.mod(i,2) == 0): ##this needs to validated
            s['searchspace'] = s['searchspace']*s['listerrors'][0][i] ##stopped here
# updateseriessquare.m:216
        s['errorstring'] = f"{s['errorstring']} {s['listerrors'][0][i]: 0.2f}\\n"
# updateseriessquare.m:218
    
    s['errorstring'] = f"{s['errorstring']} NET \n {s['searchspace']} \n"
# updateseriessquare.m:220
    s['nextline'] = np.size(s['allfs']) + 1
# updateseriessquare.m:221
    s['aamaxerror'] = 0
# updateseriessquare.m:224
    s['abmaxerror'] = 0
# updateseriessquare.m:225
    aaerrors=np.array([])
# updateseriessquare.m:226
    aberrors=np.array([])
# updateseriessquare.m:227
    for i in np.arange(0,np.size(s['column1']['fs'])).reshape(-1):
        if (s['column1']['fs'][i] != 0) and (s['column4']['fs'][i] != 0):
            aaerrors= np.append(aaerrors, s['column1']['fs'][i] - s['column4']['fs'][i])
# updateseriessquare.m:230
        if (s['column1']['fs'][i] != 0) and (s['column2']['fs'][i] != 0):
            aberrors= np.append(aberrors,s['column1']['fs'][i] - s['column2']['fs'][i])
# updateseriessquare.m:233
        if (s['column1']['fs'][i] != 0) and (s['column3']['fs'][i] != 0):
            aberrors= np.append(aberrors,s['column1']['fs'][i] - s['column3']['fs'][i])
# updateseriessquare.m:236
    
    if np.size(aaerrors) > 0:
        s['aamaxerror'] = max(abs(aaerrors))
# updateseriessquare.m:240
    
    if np.size(aberrors) > 0:
        s['abmaxerror'] = max(abs(aberrors))
# updateseriessquare.m:243
    
    s['numlines'] = np.size(s['allfs'])
# updateseriessquare.m:245
    s['numconstraints'] = (s['numlines'] / 2) - 1
# updateseriessquare.m:246
    
    s['degree'] = s['numconstraints']
# updateseriessquare.m:247
    #if s['dtype == 1
    s['allafs'] = np.concatenate((s['column1']['realfs'],s['column4']['realfs']))
# updateseriessquare.m:249'
    s['allahs'] = np.concatenate((s['column1']['realhs'],s['column4']['realhs']))
# updateseriessquare.m:250
    s['allbfs'] = np.concatenate((s['column2']['realfs'],s['column3']['realfs']))
# updateseriessquare.m:251
    s['allbhs'] = np.concatenate((s['column2']['realhs'],s['column3']['realhs']))
# updateseriessquare.m:252
    # else
#     s['allafs = [s['series2.realfs s['series3.realfs];
#     s['allahs = [s['series2['realhs'] s['series3['realhs']];
#     s['allbfs = [s['series1.realfs s['series4.realfs];
#     s['allbhs = [s['series1['realhs'] s['series4['realhs']];
# end
    s['heightstring'] = f"A heights {np.array2string(s['allahs'],3)}, B heights {np.array2string(s['allbhs'],3)}"
# updateseriessquare.m:259
    #s['series4string = print('Series 4 predictions: #s',num2np.array2string(s['series4.fs,6));
    
    s['minf'] = min(s['allfs'])
# updateseriessquare.m:262
    s['minh'] = min(s['allhs'])
# updateseriessquare.m:263
    s['allbestfs'] = copy(s['allfs'])
# updateseriessquare.m:264
    s['allbesths'] = copy(s['allhs'])
# updateseriessquare.m:265
    
    s['bestfstring'] = np.array2string(s['allfs'],6)
# updateseriessquare.m:266
    s['series4string'] = 'no series 4 yet'
# updateseriessquare.m:267
    s['allfstring'] = np.array2string(s['allfs'],6)
# updateseriessquare.m:268
    s['bendstring'] = '2 points, no bend'
# updateseriessquare.m:269
    s['sortfs'] = np.sort(s['allfs'])
# updateseriessquare.m:270
    s['usablefgrid'] = usablefgrid(s)
# updateseriessquare.m:271
    s['gridhash'] = hashfromsquare(s)
# updateseriessquare.m:272
    s['mindiff'] = min(np.diff(s['sortfs']))
# updateseriessquare.m:273
    s['isoutlawed'] = s['column1']['outlawed'] or s['column2']['outlawed'] or s['column3']['outlawed'] or s['column4']['outlawed'] or (s['mindiff'] < 0.01)
# updateseriessquare.m:274
    s['seriesstring'] = ("%s%s%s%s" % (s['column1']['outlawchar'],s['column2']['outlawchar'],s['column3']['outlawchar'],s['column4']['outlawchar']))
# updateseriessquare.m:275
    s['a1diff'] = 0
# updateseriessquare.m:279
    s['a2diff'] = 0
# updateseriessquare.m:280
    s['a1bend'] = 0
# updateseriessquare.m:281
    s['a2bend'] = 0
# updateseriessquare.m:282
    s['b1diff'] = 0
# updateseriessquare.m:283
    s['b2diff'] = 0
# updateseriessquare.m:284
    s['b1bend'] = 0
# updateseriessquare.m:285
    s['b2bend'] = 0
# updateseriessquare.m:286
    if np.size(s['column1']['realfs']) >= 2:
        s['a1diff'] = np.mean(np.diff(s['column1']['realfs']))
# updateseriessquare.m:288
    
    if np.size(s['column1']['realfs']) >= 3:
        s['a1bend'] = np.mean(np.diff(np.diff(s['column1']['realfs'])))
# updateseriessquare.m:292
    
    s['a1bendstring'] = f"a1diff' {s['a1diff']: 0.3f}, a1bend {s['a1bend']: 0.3f}"
# updateseriessquare.m:294
    if np.size(s['column2']['realfs']) >= 2:
        s['b1diff'] = np.mean(np.diff(s['column2']['realfs']))
# updateseriessquare.m:297
    
    if np.size(s['column2']['realfs']) >= 3:
        s['b1bend'] = np.mean(np.diff(np.diff(s['column2']['realfs'])))
# updateseriessquare.m:301
    
    s['b1bendstring'] = f"b1diff {s['b1diff']: 0.3f}, b1bend {s['b1bend']: 0.3f}"
# updateseriessquare.m:304
    if np.size(s['column4']['realfs']) >= 2:
        s['a2diff'] = np.mean(np.diff(s['column4']['realfs']))
# updateseriessquare.m:307
    
    if np.size(s['column4']['realfs']) >= 3:
        s['a2bend'] = np.mean(np.diff(np.diff(s['column4']['realfs'])))
# updateseriessquare.m:311
    
    s['a2bendstring'] = f"a2diff {s['a2diff']: 0.3f}, a2bend {s['a2bend']: 0.3f}"
# updateseriessquare.m:313
    if np.size(s['column3']['realfs']) >= 2:
        s['b2diff'] = np.mean(np.diff(s['column3']['realfs']))
# updateseriessquare.m:316
    
    if np.size(s['column3']['realfs']) >= 3:
        s['b2bend'] = np.mean(np.diff(np.diff(s['column3']['realfs'])))
# updateseriessquare.m:320
    
    s['b2bendstring'] = f"b2diff {s['b2diff']: 0.3f}, b2bend {s['b2bend']: 0.3f}"
# updateseriessquare.m:322
    s['tightdescriptor'] = ('%s\\n%s\\n%s\\n%s\\n%s\\naa tolerance %f, abtolerance %f\\n' % (s['a1bendstring'],s['a2bendstring'],s['b1bendstring'],s['b2bendstring'],s['quadstring'],s['aamaxerror'],s['abmaxerror']))
# updateseriessquare.m:325
    s['columnp'] = 1
# updateseriessquare.m:326
    s['columndiffs'] = np.array([s['a1diff'],s['b1diff'],s['b2diff'],s['a2diff']])
# updateseriessquare.m:327
    s['realcolumndiffs'] = s['columndiffs'][s['columndiffs'] < float('inf')]
# updateseriessquare.m:328
    s['columndiffspread'] = max(s['realcolumndiffs'] - min(s['realcolumndiffs']))
# updateseriessquare.m:329
    s['numcolumnconstraints'] = np.size(s['realcolumndiffs']) - 1
# updateseriessquare.m:330
    #reward for columns agreeing with each other.
    if s['numcolumnconstraints'] >= 1:
        s['columnp'] = (s['columndiffspread'] / s['frange']) ** s['numcolumnconstraints']
# updateseriessquare.m:333
    
    s['termstring'] = 'ud'
# updateseriessquare.m:336
    if s['upterminated'] == 1:
        s['termstring']='Ud'
# updateseriessquare.m:338
    
    if s['downterminated'] == 1:
        s['termstring']='uD'
# updateseriessquare.m:341
    
    #now do pvalues
    s=addlevels(s)
# updateseriessquare.m:344
    #choose which row to do next
    allcoords=[]
    allcoords.append(predictnext(s,'ur'))
# updateseriessquare.m:346
    allcoords.append(predictnext(s,'ul'))
# updateseriessquare.m:347
    allcoords.append(predictnext(s,'dr'))
# updateseriessquare.m:348
    allcoords.append(predictnext(s,'dl'))
# updateseriessquare.m:349
    if s['forcecorners'] == 0:
        dists= np.array((allcoords[0]['fdist'],allcoords[1]['fdist'],allcoords[2]['fdist'],allcoords[3]['fdist']))
# updateseriessquare.m:351
        #recn = find(recommended == 1);
    #dists = dists(recn);
        bestcorner= np.nonzero(dists==min(dists))[0][0]
# updateseriessquare.m:357
        reccoords=allcoords[bestcorner]
# updateseriessquare.m:358
        if min(dists) > 1000000000.0:
            s['closedout'] = 1
# updateseriessquare.m:360
    else:
        if (s['numlines'] + 1) > np.size(s['cornermap']):
            s['closedout'] = 1
# updateseriessquare.m:364
        else:
            reccoords=allcoords[s['cornermap'][s['numlines'] + 1]]
# updateseriessquare.m:367
            bestcorner=s['cornermap'][s['numlines'] + 1]
# updateseriessquare.m:368
    
    if s['closedout'] == 0:
        s['corners'][int(s['numlines'])-1]=bestcorner
# updateseriessquare.m:374
        s['nextcolumn'] = reccoords['c1']
# updateseriessquare.m:376
        s['nextrow'] = reccoords['r1']
# updateseriessquare.m:377
        s['nextnextcolumn'] = reccoords['c2']
# updateseriessquare.m:379
        s['nextnextrow'] = reccoords['r2']
# updateseriessquare.m:380
        s['alineorder'][s['nextrow'],s['nextcolumn']-1]=s['numlines'] + 1
# updateseriessquare.m:381
        s['alineorder'][s['nextnextrow'],s['nextnextcolumn']-1]=s['numlines'] + 2
# updateseriessquare.m:382
        s['nextpredictf'] = reccoords['f1']
# updateseriessquare.m:384
        s['nextnextpredictf'] = reccoords['f2']
# updateseriessquare.m:385
        s['nextenergydiff'] = reccoords['energydiff']
# updateseriessquare.m:386
        s['nextminf'] = reccoords['minf']
# updateseriessquare.m:387
        s['nextmaxf'] = reccoords['maxf']
# updateseriessquare.m:388
        s['allpredicts'][s['nextrow'],s['nextcolumn']-1]=s['nextpredictf']
# updateseriessquare.m:389
    else:
        s['nextcolumn'] = 0
# updateseriessquare.m:391
        s['nextrow'] = 0
# updateseriessquare.m:392
        s['nextnextcolumn'] = 0
# updateseriessquare.m:393
        s['nextnextrow'] = 0
# updateseriessquare.m:394
    
    if (s['prolate'] == 1) and (s['oblate'] == 1):
        s['isoutlawed'] = 1
# updateseriessquare.m:398
    
    if s['prolate'] == 0:
        1
        sold=s
# updateseriessquare.m:403
        s=flipseriessquare(s)
# updateseriessquare.m:404
        1
    
    s['pvalprefactor'] = 1
# updateseriessquare.m:408
    for h in s['allhs']:
        linecount=countfrommcounttool(s['counttool'],h)
# updateseriessquare.m:410
        s['pvalprefactor'] = s['pvalprefactor']*(linecount*1.5)
# updateseriessquare.m:411
    
    s['linecount'] = countfrommcounttool(s['counttool'],min(s['allhs']))
# updateseriessquare.m:413
    s['oldpvalprefactor'] = s['linecount'] ** np.size(s['allfs'])
# updateseriessquare.m:415
    s['seriespval'] = s['column1']['pval'] * s['column2']['pval'] * s['column3']['pval'] * s['column4']['pval']
# updateseriessquare.m:417
    s['quadpval'] = s['onequadpval'] ** s['numconstraints']
# updateseriessquare.m:418
    s['netpval'] = s['pvalprefactor'] * s['seriespval'] * s['quadpval'] * s['columnp']
# updateseriessquare.m:420
    if np.isnan(s['netpval']):
        1
    
    if not 'originalpval' in s:
        s['originalpval'] = s['netpval']
# updateseriessquare.m:425
    
    f2f1=s['column1']['fs'][1] - s['column1']['fs'][0]
# updateseriessquare.m:428
    if s['column1']['fs'][2] > 0:
        s['predictoffset'] = s['column1']['fs'][2] / s['bpluscguess']
# updateseriessquare.m:430
    else:
        s['predictoffset'] = (s['column1']['fs'][3] / s['bpluscguess']) - 1
# updateseriessquare.m:432
    
    s['pvalstring'] = ('net pval %.1e [%.1e original], %d constraints, [%.1e %.1e]' % (s['netpval'],s['originalpval'],s['numconstraints'],s['seriespval'],s['quadpval']))
# updateseriessquare.m:434
    s['shortpvalstring'] = ('net pval %.1e, %d constraints'% (s['netpval'],s['numconstraints']))
# updateseriessquare.m:435
    s['verbosebend'] = ('%s\\n %s\\n %s'% (s['column1']['predictstring'],s['column2']['predictstring'],s['column3']['predictstring']))
# updateseriessquare.m:436
    s['descriptor'] = ('%s square of degree %d, %d lines'% (s['termstring'],s['degree'],s['numlines']))
# updateseriessquare.m:437
    if (s['degree'] >= s['tightnesssettings']['mindegree']) and (s['netpval'] < s['tightnesssettings']['checkablepval']):
        s['testable'] = 1
# updateseriessquare.m:439
    else:
        s['testable'] = 0
# updateseriessquare.m:441
    return s
    
def usablefgrid(s):
   
    fatgrid=0
# updateseriessquare.m:445
    numrows= np.size(s['fgrid'][:,1])
# updateseriessquare.m:446
    numentries= np.size(s['allfs'])
# updateseriessquare.m:447
    if numentries <= s['tightnesssettings']['smallestscaffold']:
        shortfgrid=s['fgrid']
# updateseriessquare.m:449
        return shortfgrid
    
    # if numentries > 16
#     fatgrid = 1;
# end
    shortfgrid= np.dot(s['fgrid'],0)
# updateseriessquare.m:455
    numfilled=0
# updateseriessquare.m:456
    for i in np.arange(1,numrows).reshape(-1):
        thisrow=s['fgrid'][1,:]
# updateseriessquare.m:458
        if min(thisrow) > 0:
            #fullrows(i) = 1;
            if (fatgrid == 0):
                shortfgrid[i,:]=thisrow
# updateseriessquare.m:462
                numfilled=numfilled + 1
# updateseriessquare.m:463
            else:
                fatgrid=0
# updateseriessquare.m:465
            if numfilled >= s['tightnesssettings']['minrungs']:
                return shortfgrid
    return shortfgrid

def hashfromsquare(s):
    fgrid=s['usablefgrid']
    # updateseriessquare.m:474
    gridhash=0
    # updateseriessquare.m:475
    numrows=np.size(fgrid[:,1])
    # updateseriessquare.m:476
    for i in np.arange(0,numrows):
        thisrow=fgrid[i,:]
    # updateseriessquare.m:478
        if max(thisrow) > 0:
            firstentry=i+1
            break
    # updateseriessquare.m:480

    for i in np.arange(0,numrows):
        for j in np.arange(0,4):
                gridhash=gridhash + (fgrid[i,j]*((1 + (i+1) - firstentry) + (12345 * (j+1))))
    return gridhash

def addlevels(s):

    #strings together transitions to find levels['  not particularly fast. by
#the end, levels['maxe and levels['mine should reflect the spread of
#calculated values[' overcontraints simply ignored - work it out later
#levels['isknown = zeros(s['numjs+1,2); #how many constr
    
    #also labels items in fgrid which are searchable or overconstrained.
#s['fstatus can be: 
#s['fstatus(i,j) == 0 # untouched
#s['fstatus(i,j) == 1 # known
#s['fstatus(i,j) == 2 # worth searching - connects to two. set flimits?
#maybe not
#s['fstates(i,j) == 3 # MUST search - overconstrained. s['flimits set tight
#fstatus = s['
    levels={}
    levels['energy'] = np.zeros((s['numjs'] + 1,2))
# updateseriessquare.m:504
    #levels['energy(2,1) = 1;
    if s['fgrid'][2,0] != 0:
        levels['energy'][2,0]= -1
# updateseriessquare.m:507
    else:
        if s['fgrid'][2,3] != 0:
            levels['energy'][2,1]= -1
# updateseriessquare.m:510
        else:
            raise Exception('grid is a blank-o')
    
    growing=1
# updateseriessquare.m:515
    while growing == 1:

        growing=0
# updateseriessquare.m:517
        for j in np.arange(0,s['numjs']).reshape(-1):
            for i in np.arange(0,4).reshape(-1):
                if s['fgrid'][j,i] != 0:
                    levels,added=addlinetolevels(levels,j,i,s['fgrid'][j,i]) #levels is the one that is wrong
# updateseriessquare.m:521
                    if added:
                        growing=1
# updateseriessquare.m:523

    
    minenergy=min(np.ndarray.flatten(levels['energy']))
# updateseriessquare.m:529
    newenergies=1e-08 + copy(levels['energy']) - minenergy
# updateseriessquare.m:531
    
    for i in np.arange(0,s['numjs'] + 1):
        for j in np.arange(0,2):
            if levels['energy'][i,j] == 0:
                newenergies[i,j]=0
# updateseriessquare.m:535
    
    s['prolate'] = 0
# updateseriessquare.m:539
    s['oblate'] = 0
# updateseriessquare.m:540
    for i in np.arange(0,s['numjs'] + 1).reshape(-1):
        if (newenergies[i,0] != 0) and (newenergies[i,1] != 0):
            if (newenergies[i,0] < newenergies[i,1]):
                s['prolate'] = 1
# updateseriessquare.m:544
            else:
                s['oblate'] = 1
# updateseriessquare.m:546
    
    #     end
#     if (newenergies(i,1) ~= 0) && (newenergies(i,2) ~= 0) && (newenergies(i,1) < newenergies(i,2))
#         s['oblate = 1;
#     end
# end
    s['energies'] = newenergies
# updateseriessquare.m:555
    #strings together transitions to find the levels, which are nominally
#needed just for plotting, but also are a good thing to keep in mind.ab
    return s

def checkhealth(s):
    healthy=1
# updateseriessquare.m:560
    numrows= np.size(s['fgrid'][:,1])
# updateseriessquare.m:561
    for i in np.arange(0,numrows - 1).reshape(-1):
        ivalue=s['fgrid'][i,1]
# updateseriessquare.m:563
        jvalue=s['fgrid'][i + 1,1]
# updateseriessquare.m:564
        if tooclose(s['fgrid'][i,1],s['fgrid'][i + 1,2],3.0):
            healthy=0
# updateseriessquare.m:567
        if tooclose(s['fgrid'][i,2],s['fgrid'][i + 1,1],3.0):
            healthy=0
# updateseriessquare.m:570
        if healthy == 0:
            1
    return healthy

def tooclose(i,j,thresh):
    if (i > 0) and (j > 0) and abs(i - j) < thresh:
        t=1
# updateseriessquare.m:579
    else:
        t=0
# updateseriessquare.m:581
    return t

def addlinetolevels(levels,j,whichseries,f):

    level1i=j
# updateseriessquare.m:585
    level2i=j + 1
# updateseriessquare.m:586
    
    added=0
# updateseriessquare.m:587
    if 0 == whichseries:
        level1j=0
# updateseriessquare.m:590
        level2j=0
# updateseriessquare.m:591
    else:
        if 1 == whichseries:
            level1j=0
# updateseriessquare.m:593
            level2j=1
# updateseriessquare.m:594
        else:
            if 2 == whichseries:
                level1j=1
# updateseriessquare.m:596
                level2j=0
# updateseriessquare.m:597
            else:
                if 3 == whichseries:
                    level1j=1
# updateseriessquare.m:599
                    level2j=1
# updateseriessquare.m:600
    
    # known1 = levels['isknown(level1j,level1i);
# known2 = levels['isknown(level2j,level2i);
    e1=levels['energy'][level1i,level1j]
# updateseriessquare.m:604
    e2=levels['energy'][level2i,level2j]
# updateseriessquare.m:605
    if abs(f - 12016) < 1:
        1
    
    if ((e1 == 0) and (e2 == 0)) or ((e1 != 0) and (e2 != 0)):
        #cowcow theres something here.. this is overconstrained.
        return levels, added
     
    if (e1 != 0):
        newe2=e1 + f
# updateseriessquare.m:614
        if (e2 == 0):
            added=1
# updateseriessquare.m:616
            levels['energy'][level2i,level2j]=newe2
# updateseriessquare.m:617
    
    if (e2 != 0):
        newe1=e2 - f
# updateseriessquare.m:621
        if (e1 == 0):
            added=1
# updateseriessquare.m:623
            levels['energy'][level1i,level1j]=newe1
# updateseriessquare.m:624
    return levels, added

def flipseriessquare(s):
    s2=deepcopy(s) #is column 3 and 4 bad?
# updateseriessquare.m:629
    s2['column1'] = deepcopy(s['column4'])  #this is where fs goes wrong
# updateseriessquare.m:630
    s2['column2'] = deepcopy(s['column3'])
# updateseriessquare.m:631
    s2['column3'] = deepcopy(s['column2'])
# updateseriessquare.m:632
    s2['column4'] = deepcopy(s['column1'])
# updateseriessquare.m:633
    s2['column1']['whichcolumn'] = 1
# updateseriessquare.m:634
    s2['column2']['whichcolumn'] = 2
# updateseriessquare.m:635
    s2['column3']['whichcolumn'] = 3
# updateseriessquare.m:636
    s2['column4']['whichcolumn'] = 4
# updateseriessquare.m:637
    s2['flipped'] = s['flipped'] + 1
# updateseriessquare.m:639
    s2['fgrid'] = flipmatrix(s['fgrid'])
# updateseriessquare.m:640
    s2['originalfgrid'] = flipmatrix(s['originalfgrid'])
# updateseriessquare.m:641
    s2['alineorder'] = flipmatrix(s['alineorder'])
# updateseriessquare.m:642
    s2['lineorder'] = flipmatrix(s['lineorder'])
# updateseriessquare.m:643
    s2['allerrors'] = flipmatrix(s['allerrors'])
# updateseriessquare.m:644
    if s['flattype'] == '/':
        s2['flattype'] = '\\'
# updateseriessquare.m:646
    
    if s['flattype'] == '\\':
        s2['flattype'] = '/'
# updateseriessquare.m:649
    
    #s2 = rmfield(s2,'lineorder');
    s2=updateseriessquare(s2)
    return s2

def flipmatrix(g):

    g2=np.dot(g,0)
# updateseriessquare.m:655
    g2[:,0]=g[:,3]
# updateseriessquare.m:656
    g2[:,1]=g[:,2]
# updateseriessquare.m:657
    g2[:,2]=g[:,1]
# updateseriessquare.m:658
    g2[:,3]=g[:,0]
    return g2

output=updateseriessquare(s_i)
print("done!!! :))) ")
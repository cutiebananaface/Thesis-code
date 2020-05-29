# Generated with SMOP  0.41
# from libsmop import *
# updateSeriesPair.m
#status: rewritten(complete)
import numpy as np

def updateSeriesPair(s=None):
    # varargin = updateSeriesPair.varargin
    # nargin = updateSeriesPair.nargin

    if not 'fgrid' in s:
        s=seriesBasics(s)
# updateSeriesPair.m:5
    
    s=updateColumns(s)
# updateSeriesPair.m:8
    s=updateDisplays(s)
# updateSeriesPair.m:9
    s=updatePredictions(s)
# updateSeriesPair.m:10
    s=updatePvals(s)
# updateSeriesPair.m:11
    s=updateHealths(s)
# updateSeriesPair.m:12
    1
    return s
    

def seriesBasics(s=None):
   
    s['f0Freqs'] = np.array([])
# updateSeriesPair.m:19
    s['f0Heights'] = np.array([])
# updateSeriesPair.m:20
    startingJ=predictJ(s['f1Freqs'][1],s['f1Freqs'][2])
# updateSeriesPair.m:21
    if startingJ <= 0:
        1
    
    maxJ=3 + np.floor(np.dot(np.dot(1.5,startingJ),(s['maxf'] / s['f1Freqs'][1])))
# updateSeriesPair.m:25
    s['Jvalues'] = copy.copy(np.arange(1,maxJ))
# updateSeriesPair.m:26
    if 'originalFreqs' not in s :
        s['originalFreqs'] = copy.copy(s['f1Freqs'])
# updateSeriesPair.m:28
    
    s['fgrid'] = copy.copy(np.zeros((maxJ,2)))
# updateSeriesPair.m:30
    s['hgrid'] = copy.copy(s['fgrid'])
# updateSeriesPair.m:31
    s['fgrid'][np.arange(startingJ,startingJ + 1),2]=s['f1Freqs']
# updateSeriesPair.m:32
    s['hgrid'][np.arange(startingJ,startingJ + 1),2]=s['f1Heights']
# updateSeriesPair.m:33
    s['numf'] = copy.copy(2)
# updateSeriesPair.m:34
    s['closedf0'] = copy.copy(0)
# updateSeriesPair.m:35
    s['closedAbove'] = copy.copy(0)
# updateSeriesPair.m:36
    s['closedBelow'] = copy.copy(0)
# updateSeriesPair.m:37
    s['closedAbovef0'] = copy.copy(0)
# updateSeriesPair.m:38
    s['closedBelowf0'] = copy.copy(0)
# updateSeriesPair.m:39
    s['closedOut'] = copy.copy(0)
# updateSeriesPair.m:40
    s['seenBefore'] = copy.copy(0)
# updateSeriesPair.m:41
    s['outlawed'] = copy.copy(0)
# updateSeriesPair.m:42
    s['outlawChar'] = copy.copy('O')
# updateSeriesPair.m:43
    s['predicts'] = copy.copy(np.array([0,0]))
# updateSeriesPair.m:44
    s['predictErrs'] = copy.copy(np.array([0,0]))
# updateSeriesPair.m:45
    s['allResiduals'] = np.array([])
# updateSeriesPair.m:46
    s['maxDegree'] = copy.copy(2)
# updateSeriesPair.m:47
    s['k'] = np.array([])
# updateSeriesPair.m:48
    s['midp'] = copy.copy((s['maxf'] + s['minf']) / 2)
# updateSeriesPair.m:49
    s['pval'] = copy.copy(1)
# updateSeriesPair.m:50
    return s
    

def updateDisplays(s=None):

    s['blockString'] = copy.copy(np.concatenate([blockCharFromFlag(s['closedBelow']),blockCharFromFlag(s['closedAbove']),blockCharFromFlag(s['closedf0']),blockCharFromFlag(s['closedBelowf0']),blockCharFromFlag(s['closedAbovef0'])]))
# updateSeriesPair.m:53
    s['blockInt'] = copy.copy((np.dot(s['searchf0'],100000)) + (np.dot(s['closedBelow'],10000)) + (np.dot(s['closedAbove'],1000)) + (np.dot(s['closedf0'],100)) + (np.dot(s['closedBelowf0'],10)) + (np.dot(s['closedAbovef0'],1)))
# updateSeriesPair.m:54
    s['hashInt'] = copy.copy(np.round(np.sum(np.dot(s['f1vals'],1000)) + np.sum(np.dot(s['f0vals'],10000))) + s['blockInt'])
# updateSeriesPair.m:55
    s['originString'] = copy.copy(sprintf('Born from %3.2f/%3.2f',s['originalFreqs'][1],s['originalFreqs'][2]))
# updateSeriesPair.m:56
    s['gridString'] = copy.copy('')
# updateSeriesPair.m:57
    for j in np.arange(1,np.size(s['fgrid'](np.arange(),1))).reshape(-1):
        i=1 + (np.size(s['fgrid'](np.arange(),1)) - j)
# updateSeriesPair.m:59
        if (s['fgrid'][i,1] > 0) or (s['fgrid'][i,2] > 0):
            if (s['fgrid'][i,1] == 0):
                s['gridString'] = copy.copy(sprintf('%s\\nJ = %d, f0 = 00000.0, f1 = %3.1f',s['gridString'],s['Jvalues'][i],s['fgrid'][i,2]))
# updateSeriesPair.m:62
            else:
                s['gridString'] = copy.copy(sprintf('%s\\nJ = %d, f0 = %3.1f, f1 = %3.1f',s['gridString'],s['Jvalues'][i],s['fgrid'][i,1],s['fgrid'](i,2)))
# updateSeriesPair.m:64
    
    s['fullString'] = sprintf('#d lines,#d pval = #3.2e\n#s',s['totalLines'],s['blockInt'],s['pval'],s['gridString']);
    return s
    
    

def blockCharFromFlag(f=None):

    if 0 == f:
        c='-'
# updateSeriesPair.m:73
    else:
        if 1 == f:
            c='X'
# updateSeriesPair.m:75
        else:
            c='?'
# updateSeriesPair.m:77
    return c 
    
    
 
def updateColumns(s=None):

    s['f1vals'] = copy.copy(s['fgrid'](np.arange(),2))
# updateSeriesPair.m:81
    s['f0vals'] = copy.copy(s['fgrid'](np.arange(),1))
# updateSeriesPair.m:82
    s['f1HighestJ'] = copy.copy(np.where(s['f1vals']>0)[-1])
# updateSeriesPair.m:85
    s['f1LowestJ'] = copy.copy(np.where(s['f1vals']>0)[0])
# updateSeriesPair.m:86
    s['f1RealFreqs'] = copy.copy(s['f1vals'][s['f1LowestJ']:s['f1HighestJ']])
# updateSeriesPair.m:88
    s['f1RealHeights'] = copy.copy(s['hgrid'][s['f1LowestJ']:s['f1HighestJ'],2])
# updateSeriesPair.m:89
    s['f0HighestJ'] = copy.copy(np.where(s['f0vals']>0)[-1])
# updateSeriesPair.m:90
    if np.size(s['f0HighestJ']) > 0:
        s['f0LowestJ'] = copy.copy(np.where(s['f0vals']>0)[0])
# updateSeriesPair.m:92
        s['f0RealFreqs'] = copy.copy(s['f0vals'][s['f0LowestJ']:s['f0HighestJ']])
# updateSeriesPair.m:93
        s['f0RealHeights'] = copy.copy(s['hgrid'][s['f0LowestJ']:s['f0HighestJ'],1])
# updateSeriesPair.m:94
        s['nextf0J'] = copy.copy(s['f0HighestJ'] + 1)
# updateSeriesPair.m:95
        s['prevf0J'] = copy.copy(s['f0LowestJ'] - 1)
# updateSeriesPair.m:96
    else:
        s['f0RealFreqs'] = np.array([])
# updateSeriesPair.m:99
        s['f0RealHeights'] = np.array([])
# updateSeriesPair.m:100
    
    if np.size(s['f0RealFreqs']) > 0:
        s['closedf0'] = copy.copy(1)
# updateSeriesPair.m:103
    
    s['numf1'] = copy.copy(np.size(s['f1RealFreqs']))
# updateSeriesPair.m:105
    s['numf0'] = copy.copy(np.size(s['f0RealFreqs']))
# updateSeriesPair.m:106
    s['allfs'] = copy.copy(np.concatenate((s['f1RealFreqs'],s['f0RealFreqs'])))
# updateSeriesPair.m:107
    s['allhs'] = copy.copy(np.concatenate((s['f1RealHeights'],s['f0RealHeights'])))
# updateSeriesPair.m:108
    s['heightThresh'] = copy.copy(np.mean(s['f1RealHeights']) / s['ts']['meantolerance'])
# updateSeriesPair.m:110
    s['totalLines'] = copy.copy(np.size(s['f1RealFreqs']) + np.size(s['f0RealFreqs']))
# updateSeriesPair.m:112
    if s['f1HighestJ'] > np.size(s['Jvalues']):
        1
    
    s['f1RealJs'] = copy.copy(s['Jvalues'][s['f1LowestJ']:s['f1HighestJ']])
# updateSeriesPair.m:116
    s['nextf1J'] = copy.copy(s['f1HighestJ'] + 1)
# updateSeriesPair.m:117
    s['prevf1J'] = copy.copy(s['f1LowestJ'] - 1)
# updateSeriesPair.m:118
    return s

def updateHealths(s=None):

    s['frequencyHealth'] = copy.copy(1)
# updateSeriesPair.m:121
    s['totalSick'] = copy.copy(0)
# updateSeriesPair.m:122
    s['kindaSick'] = copy.copy(0)
# updateSeriesPair.m:123
    # variant3.heightHealthRatio = 10;  #higher is more tolerance
# variant3.freqHealthLimit = - 0.1;
    if s['numf1'] >= 4:
        s['frequencyHealth'] = copy.copy(s['ts']['freqHealthLimit'] / s['meanResidual'])
# updateSeriesPair.m:127
    
    s['heightHealth'] = copy.copy(np.dot(s['ts']['heightHealthRatio'],np.min(s['allhs'])) / np.mean(s['allhs']))
# updateSeriesPair.m:129
    s['totalHealth'] = copy.copy(np.dot(s['heightHealth'],s['frequencyHealth']))
# updateSeriesPair.m:130
    s['healthString'] = copy.copy(sprintf('healthy, f = %3.1f, h = %3.1f',s['frequencyHealth'],s['heightHealth']))
# updateSeriesPair.m:131
    if (s['heightHealth'] < 1) or (s['frequencyHealth'] < 1):
        s['kindaSick'] = copy.copy(1)
# updateSeriesPair.m:134
        s['healthString'] = copy.copy(sprintf('declared kinda sick, f = %3.1f, h = %3.1f',s['frequencyHealth'],s['heightHealth']))
# updateSeriesPair.m:135
    
    if s['totalHealth'] < s['ts']['totalHealthLimit']:
        s['totalSick'] = copy.copy(1)
# updateSeriesPair.m:139
        s['healthString'] = copy.copy(sprintf('declared totally sick, f = %3.1f, h = %3.1f',s['frequencyHealth'],s['heightHealth']))
# updateSeriesPair.m:140
    return s
    

def updatePvals(s=None):

    #each line falls within a residual of perfect.  pvalprefactor is ``how 
#num
    s['pvalprefactor'] = copy.copy(1)
# updateSeriesPair.m:146
    
    for h in s['allhs'].reshape(-1):
        linecount=countfrommcounttool(s['countTool'],h)
# updateSeriesPair.m:148
        s['pvalprefactor'] = copy.copy(dot(s['pvalprefactor'],(np.dot(linecount,1.5))))
# updateSeriesPair.m:149
    
    
    if np.size(s['allResiduals'] >= 4):
        s['meanResidual'] = copy.copy(np.mean(abs(s['allResiduals'])))
# updateSeriesPair.m:153
        s['numConstraints'] = copy.copy(np.size(s['allResiduals']) - np.size(s['k']))
# updateSeriesPair.m:154
        s['rawP'] = copy.copy((s['meanResidual'] / (s['maxf'] - s['minf'])) ** s['numConstraints'])
# updateSeriesPair.m:155
        s['pval'] = copy.copy(np.dot(s['rawP'],s['pvalprefactor']))
# updateSeriesPair.m:157
        s['residualString'] = copy.copy(sprintf('%d lines,%d constraints, %3.1f kHz residuals,p=%3.1g',s['totalLines'],s['numConstraints'],np.dot(s['meanResidual'],1000),s['pval']))
# updateSeriesPair.m:158
        s['fullString'] = copy.copy(sprintf('%s\\n%d blocked\\n%s',s['residualString'],s['blockInt'],s['gridString']))
# updateSeriesPair.m:159
    else:
        s['pval'] = copy.copy(np.dot(100,s['pvalprefactor']))
# updateSeriesPair.m:161
        s['residualString'] = copy.copy(sprintf('%d lines, no residuals'))
# updateSeriesPair.m:162
        s['fullString'] = copy.copy(sprintf('%d lines,%d no residuals\\n%s',s['totalLines'],s['blockInt'],s['gridString']))
# updateSeriesPair.m:163
    return s
  
def updatePredictions(s=None):
    #first do a polynomial prediction - either linear or quadratic using
    #last few points
    s['nextf0'] = copy.copy(0)
# updateSeriesPair.m:169
    s['prevf0'] = copy.copy(0)
# updateSeriesPair.m:170
    s=updatePolyPredictions(s)
# updateSeriesPair.m:171
    s=updateFancyPredictions(s)
# updateSeriesPair.m:172
    s=chooseCorner(s)
# updateSeriesPair.m:173
    s['predictString'] = copy.copy(sprintf('next ftoseek %s,%3.1f-%3.1f\\n',s['nextCorner'],s['minftoseek'],s['maxftoseek']))
# updateSeriesPair.m:174
    return s

def updateFancyPredictions(s=None):

    exitFlag=0
# updateSeriesPair.m:177
    if np.size(s['f1RealFreqs']) > 2:
        if np.size(s['f0RealFreqs']) == 0:
            s,exitFlag=addfitf1(s)
# updateSeriesPair.m:180
        else:
            s,exitFlag=addfitf1f0(s)
# updateSeriesPair.m:182
    
    if exitFlag <= 0:
        s['nextf1'] = copy.copy(s['polyNextf1'])
# updateSeriesPair.m:186
        s['prevf1'] = copy.copy(s['polyPrevf1'])
# updateSeriesPair.m:187
        #  s['f1Spread = s['ts['bendTolerance(degree);
        s['f1Spread'] = copy.copy(guessQuality(s))
# updateSeriesPair.m:190
        s['fittype'] = copy.copy('polynomial')
# updateSeriesPair.m:191
    
    
    

def addfitf1f0(s=None):
    

    k,residuals,f1predicts,f0predicts,J1,J0,exitFlag=fitf1f0(s['f1RealFreqs'],s['f0RealFreqs'],s['ka'],s['k'])
# updateSeriesPair.m:195
    
    #STUFF HERE FOR RESIDUALS, TO BE EATEN BY PVALs[' PVALS AND H
    if exitFlag < 0:
        s['f1RealFreqs']
        s['f1Failed'] = copy.copy(1)
# updateSeriesPair.m:200
        s['closedOut'] = copy.copy(1)
# updateSeriesPair.m:201
        s['closeOutReason'] = copy.copy('fitf1f0 failed')
# updateSeriesPair.m:202
        fprintf('fitf1f0 failed..not sure what to do. f0 = %3.1f',s['f0RealFreqs'][1])
        s['fgrid']
    
    s['f0predicts'] = copy.copy(f0predicts)
# updateSeriesPair.m:206
    
    s['allResiduals'] = copy.copy(residuals)
# updateSeriesPair.m:208
    
    s['k'] = copy.copy(k)
# updateSeriesPair.m:210
    
    #    1;
    #end
  #  s['fancyPredicts = predicts;
    if abs(s['f0RealFreqs'][1] - 13481) < 1:
        1
    
    s['nextf1'] = copy.copy(f1predicts[2])
# updateSeriesPair.m:218
    s['prevf1'] = copy.copy(f1predicts[1])
# updateSeriesPair.m:219
    s['nextf0'] = copy.copy(f0predicts[2])
# updateSeriesPair.m:220
    s['prevf0'] = copy.copy(f0predicts[1])
# updateSeriesPair.m:221
    s['f0Spread'] = copy.copy(s['ts']['fancytolerancef0'])
# updateSeriesPair.m:222
    if np.size(s['f0RealFreqs']) == 1:
        s['f0Spread'] = copy.copy(s['ts']['fancytolerancef0first'])
# updateSeriesPair.m:224
    
    if np.mean(s['f1RealJs']) < s['ts']['lowj']:
        s['f0Spread'] = copy.copy(s['ts']['fancytolerancef0lowJ'])
# updateSeriesPair.m:227
    
    s['fittype'] = copy.copy('fitf1f0')
# updateSeriesPair.m:229
    return s, exitFlag


def addfitf1(s=None):

    k,residuals,predicts,J,exitFlag,f0predicts=fitf1(s['f1RealFreqs'],s['f1RealJs'],s['ka'],s['k'])
# updateSeriesPair.m:233
    
    if exitFlag < 0:
        # s['f1RealFreqs;
        #fprintf('diff is #s, bend is #s\n',num2str(diff(s['f1RealFreqs)),num2str(diff(diff(s['f1RealFreqs))));
        s['f1Failed'] = copy.copy(1)
# updateSeriesPair.m:238
        s['closedOut'] = copy.copy(1)
# updateSeriesPair.m:239
        s['closedOutReason'] = copy.copy('f1 failed')
# updateSeriesPair.m:240
    
    
    s['k'] = copy.copy(k)
# updateSeriesPair.m:244
    s['f0predicts'] = copy.copy(f0predicts)
# updateSeriesPair.m:245
    s['allResiduals'] = copy.copy(residuals)
# updateSeriesPair.m:246
    
    s['nextf1'] = copy.copy(predicts[2])
# updateSeriesPair.m:248
    s['prevf1'] = copy.copy(predicts[1])
# updateSeriesPair.m:249
    s['f1Spread'] = copy.copy(s['ts']['fancytolerance'])
# updateSeriesPair.m:250
    if (np.mean(s['f1RealJs']) < s['ts']['lowj']) and (np.size(s['f1RealJs']) <= 4):
        s['f1Spread'] = copy.copy(s['ts']['fancytolerancef1lowJ'])
# updateSeriesPair.m:252
    
    
    s['fittype'] = copy.copy('fitf1')
# updateSeriesPair.m:256
    return s, exitFlag


def updatePolyPredictions(s=None):

    n=np.min(np.size(s['f1RealFreqs']),s['maxDegree'] + 1)
# updateSeriesPair.m:259
    x=np.arange(1,n)
# updateSeriesPair.m:260
    y=s['f1RealFreqs'][1:n]
# updateSeriesPair.m:261
    s['poly'] = copy.copy(np.polyfit(x,y,n - 1))
# updateSeriesPair.m:262
    s['polyPrevf1'] = copy.copy(np.polyval(s['poly'],0))
# updateSeriesPair.m:263
    s['f1Spread'] = copy.copy(guessQuality(s))
# updateSeriesPair.m:264
    y=s['f1RealFreqs'][np.arange(-1 + 1 - n,-1)]
# updateSeriesPair.m:266
    s['poly'] = copy.copy(np.polyfit(x,y,n - 1))
# updateSeriesPair.m:267
    s['polyNextf1'] = copy.copy(np.polyval(s['poly'],n + 1))
# updateSeriesPair.m:268
    return s
    

def assignCorner(s=None):

    if 'f0up' == s['nextCorner']:
        s['ftoseek'] = copy.copy(s['nextf0'])
# updateSeriesPair.m:273
        s['nextcolumn'] = copy.copy(1)
# updateSeriesPair.m:274
        s['nextrow'] = copy.copy(s['nextf0J'])
# updateSeriesPair.m:275
        s['maxftoseek'] = copy.copy(s['ftoseek'] + s['f0Spread'])
# updateSeriesPair.m:276
        s['minftoseek'] = copy.copy(s['ftoseek'] - s['f0Spread'])
# updateSeriesPair.m:277
    elif 'f0down' == s['nextCorner']:
        s['ftoseek'] = copy.copy(s['prevf0'])
# updateSeriesPair.m:279
        s['nextcolumn'] = copy.copy(1)
# updateSeriesPair.m:280
        s['nextrow'] = copy.copy(s['prevf0J'])
# updateSeriesPair.m:281
        s['maxftoseek'] = copy.copy(s['ftoseek'] + s['f0Spread'])
# updateSeriesPair.m:282
        s['minftoseek'] = copy.copy(s['ftoseek'] - s['f0Spread'])
# updateSeriesPair.m:283
    elif 'f0first' == s['nextCorner']:
        bestJ,bestf=pickOneF(s['f0predicts'],s['f1RealJs'])
# updateSeriesPair.m:285
        s['ftoseek'] = copy.copy(bestf)
# updateSeriesPair.m:286
        if s['pval'] > s['ts']['f1tof0toleranceThresh']:
            s['maxftoseek'] = copy.copy(s['ftoseek'] + s['ts']['f1tof0tolerance'])
# updateSeriesPair.m:288
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['ts']['f1tof0tolerance'])
# updateSeriesPair.m:289
        else:
            s['maxftoseek'] = copy.copy(s['ftoseek'] + s['ts']['f1tof0toleranceSure'])
# updateSeriesPair.m:291
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['ts']['f1tof0toleranceSure'])
# updateSeriesPair.m:292
        s['nextcolumn'] = copy.copy(1)
# updateSeriesPair.m:294
        s['nextrow'] = copy.copy(bestJ)
# updateSeriesPair.m:295
    elif 'f1up' == s['nextCorner']:
        s['ftoseek'] = copy.copy(s['nextf1'])
# updateSeriesPair.m:297
        s['nextcolumn'] = copy.copy(2)
# updateSeriesPair.m:298
        s['nextrow'] = copy.copy(s['nextf1J'])
# updateSeriesPair.m:299
        if (np.size(s['f1RealFreqs']) == 2):
            s['maxftoseek'] = copy.copy(s['ftoseek'])
# updateSeriesPair.m:301
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['f1Spread'])
# updateSeriesPair.m:302
        else:
            s['maxftoseek'] = copy.copy(s['ftoseek'] + s['f1Spread'])
# updateSeriesPair.m:304
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['f1Spread'])
# updateSeriesPair.m:305

    elif 'f1down' == s['nextCorner']:
        s['ftoseek'] = copy.copy(s['prevf1'])
# updateSeriesPair.m:308
        s['nextcolumn'] = copy.copy(2)
# updateSeriesPair.m:309
        s['nextrow'] = copy.copy(s['prevf1J'])
# updateSeriesPair.m:310
        if (np.size(s['f1RealFreqs']) == 2):
            s['maxftoseek'] = copy.copy(s['ftoseek'])
# updateSeriesPair.m:312
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['f1Spread'])
# updateSeriesPair.m:313
        else:
            s['maxftoseek'] = copy.copy(s['ftoseek'] + s['f1Spread'])
# updateSeriesPair.m:315
            s['minftoseek'] = copy.copy(s['ftoseek'] - s['f1Spread'])
# updateSeriesPair.m:316

    elif 'closedOut' == s['nextCorner']:
        s['closedOut'] = copy.copy(1)
# updateSeriesPair.m:319
        s['closedOutReason'] = copy.copy('self assigned')
# updateSeriesPair.m:320
        s['ftoseek'] = copy.copy(0)
# updateSeriesPair.m:321
        s['maxftoseek'] = copy.copy(0)
# updateSeriesPair.m:322
        s['minftoseek'] = copy.copy(0)
# updateSeriesPair.m:323
    return s
    
    

def choosef1Corner(s=None):

    if abs(s['nextf1'] - s['midp']) < abs(s['prevf1'] - s['midp']):
        preferUp=1
# updateSeriesPair.m:329
    else:
        preferUp=0
# updateSeriesPair.m:331
    
    s['nextCorner'] = copy.copy('closedOut')
# updateSeriesPair.m:333
    if (s['closedAbove'] == 0) and (s['closedBelow'] == 0):
        if preferUp:
            s['nextCorner'] = copy.copy('f1up')
# updateSeriesPair.m:336
        else:
            s['nextCorner'] = copy.copy('f1down')
# updateSeriesPair.m:338
    
    if (s['closedAbove'] == 0) and (s['closedBelow'] == 1):
        s['nextCorner'] = copy.copy('f1up')
# updateSeriesPair.m:342
    
    if (s['closedAbove'] == 1) and (s['closedBelow'] == 0):
        s['nextCorner'] = copy.copy('f1down')
# updateSeriesPair.m:345
    return s
    
    

def choosef0Corner(s=None):

    if (s['closedf0']) and (np.size(s['f0RealFreqs']) == 0):
        s['nextCorner'] = copy.copy('closedOut')
# updateSeriesPair.m:351
        return s
    
    if (s['closedf0'] == 0):
        if (np.size(s['f0RealFreqs']) == 0) and (np.size(s['f1RealFreqs']) >= s['ts']['minf1length']):
            s['nextCorner'] = copy.copy('f0first')
# updateSeriesPair.m:356
        else:
            s['closedf0'] = copy.copy(1)
# updateSeriesPair.m:358
            s['nextCorner'] = copy.copy('closedOut')
# updateSeriesPair.m:359
        return s
    
    
    if abs(s['nextf0'] - s['midp']) < abs(s['prevf0'] - s['midp']):
        preferUp=1
# updateSeriesPair.m:365
    else:
        preferUp=0
# updateSeriesPair.m:367
    
    if (s['closedAbovef0'] == 0) and (s['closedBelowf0'] == 0):
        if preferUp:
            s['nextCorner'] = copy.copy('f0up')
# updateSeriesPair.m:371
        else:
            s['nextCorner'] = copy.copy('f0down')
# updateSeriesPair.m:373
    
    if (s['closedAbovef0'] == 0) and (s['closedBelowf0'] == 1):
        s['nextCorner'] = copy.copy('f0up')
# updateSeriesPair.m:377
    
    if (s['closedAbovef0'] == 1) and (s['closedBelowf0'] == 0):
        s['nextCorner'] = copy.copy('f0down')
# updateSeriesPair.m:380
    return s
    
    
    

def updateCloseouts(s=None):


    if s['nextf1'] > s['maxf']:
        s['closedAbove'] = copy.copy(1)
# updateSeriesPair.m:385
    
    if s['prevf1'] < s['minf']:
        s['closedBelow'] = copy.copy(1)
# updateSeriesPair.m:388
    
    if (s['nextf0'] > s['maxf']) and (s['nextf0'] > 0):
        s['closedAbovef0'] = copy.copy(1)
# updateSeriesPair.m:391
    
    if (s['prevf0'] < s['minf']) and (s['prevf0'] > 0):
        s['closedBelowf0'] = copy.copy(1)
# updateSeriesPair.m:394
    return s
    
    

def chooseCorner(s=None):

    #selects which row and column to try and predict next.
    s=updateCloseouts(s)
# updateSeriesPair.m:399
    s['nextCorner'] = copy.copy('closedOut')
# updateSeriesPair.m:400
    if (s['closedAbove'] == 0) or (s['closedBelow'] == 0):
        s=choosef1Corner(s)
# updateSeriesPair.m:402
    else:
        s=choosef0Corner(s)
# updateSeriesPair.m:404
    
    s=assignCorner(s)
# updateSeriesPair.m:406
    return s
    

def pickOneF(f0predicts=None,J=None):
 
    besti=np.around(np.size(J) / 2)
# updateSeriesPair.m:410
    bestJ=J[besti]
# updateSeriesPair.m:411
    bestf=f0predicts[besti]
# updateSeriesPair.m:412
    return bestJ, bestf
    

def guessQuality(s=None):

    fs=s['f1RealFreqs']
# updateSeriesPair.m:415
    if np.size(fs) == 2:
        tolerance1=s['ts']['bendTolerance'][1]
# updateSeriesPair.m:417
        maxgap=np.max(np.diff(s['f1RealFreqs']))
# updateSeriesPair.m:418
        tolerance2=maxgap / s['ts']['gapoverbendmax']
# updateSeriesPair.m:419
    else:
        tolerance1=s['ts']['bendTolerance'][np.size(fs) - 1]
# updateSeriesPair.m:421
        tolerance2=np.dot(3,np.mean(abs(np.diff(np.diff(fs)))))
# updateSeriesPair.m:422
    
    fspread=np.min(tolerance1,tolerance2)
# updateSeriesPair.m:424
    if mean(s['f1RealJs']) < s['ts']['lowj']:
        fspread=np.dot(fspread,2)
# updateSeriesPair.m:427
    return fspread
    
    
    

def updatepval(s=None):

    s['pval'] = copy.copy(1)
# updateSeriesPair.m:432
    for n in np.arange(1,(np.size(s['realfs']) - 2)).reshape(-1):
        #   n = min(length(s['realfs),maxdegree+1);
        numabove=np.size(s['realfs']) - n
# updateSeriesPair.m:435
        numtouse=np.min(s['maxdegree'],numabove)
# updateSeriesPair.m:436
        x=np.arange(1,numtouse)
# updateSeriesPair.m:437
        y=s['realfs'](np.arange(n + 1,n + numtouse))
# updateSeriesPair.m:438
        p=np.polyfit(x,y,numtouse - 1)
# updateSeriesPair.m:439
        predictf=np.polyval(p,0)
# updateSeriesPair.m:440
        ferr=s['realfs'][n] - predictf
# updateSeriesPair.m:441
        s['predicts'].append(predictf)
# updateSeriesPair.m:442
        s['predicterrs'].append(abs(ferr))
# updateSeriesPair.m:443
        thisp=abs(ferr) / s['frange']
# updateSeriesPair.m:446
        if thisp < 1:
            s['pval'] = copy.copy(np.dot(s['pval'],thisp))
    return s
# updateSeriesPair.m:448
    
    
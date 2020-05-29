# Generated with SMOP  0.41
# from libsmop import *
# extendAllf1Series.m
#status: rewritten (complete)
    

def extendAllf1Series(thisSeriesList=None,babyKit=None):

    global ALLEVERTRIED
    thisSeriesList=findUniqueSeriesPairs(thisSeriesList)
# extendAllf1Series.m:4
    #[thisSeriesList] = findNewSeriesPairs(thisSeriesList,alltried);
    alltriedthistime={0:0}
# extendAllf1Series.m:6
    if np.size(thisSeriesList) > 0:
        if thisSeriesList[1]['searchf0'] == 0:
            fprintf('Extending %d baby series 4s\\n',length(thisSeriesList))
        else:
            fprintf('Extending %d series 4s into series 1-4s\\n',length(thisSeriesList))
    
    if babyKit['ts']['verbose'] == 1:
        displaySeries(thisSeriesList,babyKit.cheatCodes)
    
    
    stillGrowing=1
# extendAllf1Series.m:19
    numrounds=0
# extendAllf1Series.m:20
    finalSeriesList=[]
# extendAllf1Series.m:21
    while stillGrowing:

        numrounds=numrounds + 1
# extendAllf1Series.m:23
        thisSeriesList=findNewSeriesPairs(thisSeriesList,ALLEVERTRIED)
# extendAllf1Series.m:24
        listhashes=extractonefieldfromcellarray(thisSeriesList,'hashInt')
# extendAllf1Series.m:27
        for i in listhashes.reshape(-1):
            alltriedthistime[i]=1
# extendAllf1Series.m:29
        thisSeriesList,stillGrowing=extendf1SeriesListByOne(thisSeriesList,babyKit)
# extendAllf1Series.m:31
        thisSeriesList=findUniqueSeriesPairs(thisSeriesList)
# extendAllf1Series.m:33
        #now, find items which have never been tried
#    [thisSeriesList, alltried] = markKnownSeriesPairs(thisSeriesList,alltried);
        if np.size(thisSeriesList) == 0:
            fprintf('after %d rounds, none left\\n')
            break
        #  thisSeriesList = sortcellarraybyfield(thisSeriesList,'pval');
        a=extractfieldsfromcellarray(thisSeriesList,np.array(['closedOut','pval','totalLines']))
# extendAllf1Series.m:42
        closeouts=a['closedOut']
# extendAllf1Series.m:43
        lengths=a['totalLines']
# extendAllf1Series.m:44
        pvals=a['pval']
# extendAllf1Series.m:45
        if np.size(np.where(closeouts == 0)) == 0:
            stillGrowing=0
# extendAllf1Series.m:47
        fprintf('after %d rounds, %d survivors,length %d-%d, best p %3.1e\\n',numrounds,length(thisSeriesList),min(lengths),max(lengths),min(pvals))
        if babyKit['ts']['verbose'] == 1:
            displaySeries(thisSeriesList,babyKit['cheatCodes'])

    
    for i in np.arange(1,np.size(thisSeriesList)).reshape(-1):
        if thisSeriesList[i].pval < babyKit.ts.maxPval:
            finalSeriesList.append(thisSeriesList[i])
# extendAllf1Series.m:56
    return finalSeriesList, alltriedthistime
    

def displaySeries(sl=None,cheatcode=None):

    format('short') ## not sure about this line
    for i in np.arange(1,np.size(sl)).reshape(-1):
        thisseries=sl[i]
# extendAllf1Series.m:64
        f1s=thisseries['f1RealFreqs']
# extendAllf1Series.m:65
        color=1
# extendAllf1Series.m:66
        if nearlycontains(f1s,cheatcode['correctf1']) and nearlycontains(f1s,cheatcode['correctf2']):
            goodstart=1
# extendAllf1Series.m:68
            color=2
# extendAllf1Series.m:69
        fprintf(color,'series %d f1 freqs: %s p = %3.1e\\n',i,num2str(thisseries.f1RealFreqs),thisseries.pval)
        1
    
    
    

def nearlycontains(series=None,value=None,tolerance=None):

    if tolerance== None:
        tolerance=1
# extendAllf1Series.m:78
    
    minerror=np.min(abs(series - value))
# extendAllf1Series.m:80
    if minerror < tolerance:
        yesorno=1
# extendAllf1Series.m:82
    else:
        yesorno=0
# extendAllf1Series.m:84
    
    #tentative rule: if your series is length 2, you HAVE to extend it, and in
#the given direction. return a list of series, each of length 3.
    
    #if your series is 3 or longer, [3 is an adjustment], the returned list
#incl
    return yesorno
    

def extendf1SeriesListByOne(thisSeriesList=None,babyKit=None):

    #if doOrDie is 1, then don't add yourself - extend or perish. if 0, add
#self with a closeout.
    foundNewOne=0
# extendAllf1Series.m:94
    newSeriesList=[]
# extendAllf1Series.m:95
    for i in np.arange(1,np.size(thisSeriesList)).reshape(-1):
        s=thisSeriesList[i]
# extendAllf1Series.m:97
        if (s['seenBefore'] == 1) or (s['closedOut'] == 1) or (s['nextCorner']=='f0first'==True) and (s['searchf0'] == 0)):
            #is it a keeper? this one will never grow old. use minlines.
        #fredos need not apply
            newSeriesList.append(s)
# extendAllf1Series.m:102
        else:
            #         heightThresh = mean(s.f1RealHeights) / s.ts.meantolerance;
#         startf = s.minftoseek;
#         stopf = s.maxftoseek;
            if s['nextcolumn'] == 1:
                1
            fs,hs=findcandidates(s,babyKit)
# extendAllf1Series.m:113
            for i in np.arange(1,np.size(fs)).reshape(-1):
                newSeriesList.append(addCandidate(s,fs[i],hs[i]))
# extendAllf1Series.m:115
                foundNewOne=1
# extendAllf1Series.m:116
            if (np.size(fs) == 0) and (s['totalLines'] >= s['ts']['minforcloseout']):
                newSeriesList.append(closeOut(s))
# extendAllf1Series.m:119
                foundNewOne=1
# extendAllf1Series.m:120
    return newSeriesList, foundNewOne
    

def closeOut(s=None):

    if 'f1down' == s['nextCorner']:
        s['closedBelow'] = copy(1)
    elif 'f1up' == s['nextCorner']:
        s['closedAbove'] = copy(1)
    elif 'f0first' == s['nextCorner']:
        s['closedf0'] = copy(1)
    elif 'f0down' == s['nextCorner']:
        s['closedBelowf0'] = copy(1)
    elif 'f0up' == s.nextCorner:
        s['closedAbovef0'] = copy(1)
# extendAllf1Series.m:136
    
    if (np.size(s['f0RealFreqs']) == 0) and s['closedf0'] and s['closedAbove'] and s['closedBelow']:
        s['closedOut'] = copy(1)
# extendAllf1Series.m:139
    
    if s.closedBelowf0 and s.closedAbovef0 and s.closedAbove and s.closedBelow:
        s['closedOut'] = copy(1)
# extendAllf1Series.m:142
    
    s=updateSeriesPair(s)
# extendAllf1Series.m:144
    return s
    

def addCandidate(s=None,f=None,h=None):

    try:
        s['fgrid'][s['nextrow'],s['nextcolumn']]=f
# extendAllf1Series.m:148
        s['hgrid'][s['nextrow'],s['nextcolumn']]=h
# extendAllf1Series.m:149
    except:
        s['nextrow'] = 1;
        s['fgrid'][s['nextrow'],s['nextcolumn']] = f;
        s['hgrid'][s['nextrow'],s['nextcolumn']] = h;
    
    s['seenBefore'] = copy(0)
# extendAllf1Series.m:155
    if s['nextcolumn'] == 1:
        1
    
    s=updateSeriesPair(s)
    return s
# extendAllf1Series.m:159
    

def findcandidates(s=None,babyKit=None):

    #heightThresh = mean(s.f1RealHeights) / s.ts.meantolerance;
    
    startf=s['minftoseek']
# extendAllf1Series.m:164
    stopf=s['maxftoseek']
# extendAllf1Series.m:165
    firsti=np.where(babyKit['fs']>startf)[0]
# extendAllf1Series.m:166
    lasti=np.where(babyKit['fs']<stopf)[-1]
# extendAllf1Series.m:167
    
    fs=np.array([])
# extendAllf1Series.m:169
    hs=np.array([])
# extendAllf1Series.m:170
    for i in np.arange(firsti,lasti).reshape(-1):
        if babyKit['hs'][i] > s['heightThresh']:
            fs.append(babyKit['fs'][i])
# extendAllf1Series.m:173
            hs.append(babyKit['hs'][i])
# extendAllf1Series.m:174
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:40:09 2020

@author: rodri
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:00:30 2020

@author: rodri
"""
#status: ported (complete)
import numpy as np
from makecounttool_python import makecounttool
from pickfirstf_python import pickfirstf
# from settingsfromtightness_python import settingsfromtightness
import copy 
# from loadmatlab_workspace import load_mat

# before= load_mat('before-getflatsquares-in-getflatsquares')
# kit= before['kit']
# linetouse= before['linetouse']
# ts= before['ts']

def getflatsquares(kit, linetouse, ts):
#function [allsquares,kit,f1] = getflatsquares(kit,linetouse,ts)
    s={}
    if linetouse ==0:
        laddermode = 1
    else:
        laddermode = 0
    #%loads flatsquares EITHER from a csvkitfile, or from a kit containing a
    #%theoryladder for a dry run
     
    #%     gapmax = 2250;
    #%     gapmin = 2240; %menthone is 1164
    #    % gapmax = 3000; %about 2500
    #    % gapmin = 200; %about 600
    #    
    #    % gapmax = frange / 4; %about 2500
    #    % gapmin = gapmax / 4; %about 600
    #    
    #    %pick a good first frequency. strong line a bit short of the middle
    numchecked = 0
    numfound = 0
    allsquares = []
    
    if laddermode == 0:
        try:
            if kit['onedpeakfsvis']: ## i think this is fine
                fs = kit['onedpeakfsvis']
                hs = kit['onedpeakhsvis']
        except:
            fs = kit['onedpeakfsunassigned']  #first instance
            hs = kit['onedpeakhsunassigned']
            
        counttool = makecounttool(hs)
    ##    %maxheight = max(hs);
    ##    %   hthresh = maxheight/50;
        
        frange = max(fs) - min(fs)
    #    
    ##%     gapmax = 1667; %% 3000; %frange / 4; %about 2500
    ##%     gapmin = 1665; %frange / 15; %about 600
        
        
            
        gapmax = ts['gapmax']
        gapmin = ts['gapmin'] #%menthone is 1164
        
    #   wary about istart & rank
        f1, h1, istart, rank = pickfirstf(kit,linetouse)
        f1error = f1 - linetouse
    #%    f1cheat = makecheats(f1,kit,linetouse,ts);
        # print('%s: jumping in, rank %d, height %3.1f f = %3.1f\n', kit['molname'], rank, h1, f1);
        print('%s: jumping in, rank %d, height %.1f f = %.1f\n'%(kit['molname'], rank, h1, f1))
    #%     newhs = [];
    #%     
    #%     f = 6;
    #%     hthresh = 1e10;  
        minlines = ts['minlines']
     
    #%    possh = hs(imin:imax);
        sorth=np.sort(hs)[::-1]
        ##minlines should be 599 not 600 for python 
        # if np.size(sorth, axis=None) < minlines:
        #     minlines =np.size(sorth, axis=None)
        
        tightthresh = h1/ts['firstcutheightratio']
        hthresh = min(tightthresh, sorth[minlines-1])
    ##%    tightthresh
    ##%    hthresh
    ##%     while (length(newhs) < 1000) && (hthresh > min(hs))
    ##%         hthresh = h1/(f * tightness);
    ##% 
    ##%         newfs = fs(find(hs > hthresh));
    ##%         newhs = hs(find(hs > hthresh));
    ##%         f = f * 1.5;
    ##%      %   f
    ##%      %   length(newhs)
    ##%     end
    
        fs= fs[np.where(hs>hthresh)]
        hs= hs[np.where(hs>hthresh)]
        kit['usefs']=fs
        kit['usehs']=hs
        try:
            if kit['forcefs'] > 0:
                ferrs= abs(fs-kit['forcef2'])
                minjj= np.where(ferrs==min(ferrs))[0][0]
                maxjj= minjj
        except:
            minjj= np.where(fs>(f1+gapmin))[0][0]  #returns a tuple, then [0] grabs the first element, then [0] grabs the first value of that element
            maxjj= np.where(fs>(f1+gapmax))[0][0]
            if np.size(maxjj, axis=None) == 0:
                maxjj = np.size(fs, axis=None)
    ##    %code here to deal with f2correction if exists.
        
    ##%     numf2s = 1 + maxjj - minjj;
    ##%     
    ##%     totalnum = (maxjj - minjj) * length(fs);
        
        f2list = fs
        f3list = fs
        f4list = fs
        
        h2list = hs
        h3list = hs
        h4list = hs
        #ported correctly!
        
    ##    %f3f1 is one of the numbers scouted by plotprimary series. for menthone
    ##    %it is 300 MHz. So this bound is actually not that conservative.
    ##%    f3f1thresh = 2000 * (tightness^2);
    ##%cowcow take out f2 and f3 assigned as well..
        
    # else:
    #     counttool=0
    #     frange= 100000
    #     ts=settingsfromtightness(10) ## make sure this index is right
    #     f1= kit['firstsquare'][0]
    #     h1=1
    #     f1error = f1 - kit['templateabsolute'][0];  
        
    #     f2list = kit['firstsquare'][1]
    #     f3list = kit['firstsquare'][2]
    #     f4list = kit['firstsquare'][3]
    
    #     h2list = 1
    #     h3list = 1
    #     h4list = 1
    #     minjj = 1
    #     maxjj = 1

      
    for jj in range(minjj,maxjj): ## for some reason minjj and maxjj are a gigantic array filled with ZEROS
        f2= f2list[jj]
        h2= h2list[jj]
        f2error= f2-f1- (kit['templatenorm'][1]*f1)
        if (h2 >(h1/ts['flatsquareheightratio'])):
            for kk in np.arange(0, np.size(f3list, axis=None)):
                f3= f3list[kk] #kk will start 0, 1, 2,)
                h3= h3list[kk]
                f3f1= abs(f3-f1)
                f3error = f3 - f1 - (kit['templatenorm'][2]*f1)
    #                %code here to deal with f3 correction if it exists..
                if ((min(np.diff(np.sort(np.array([f1, f2, f3])))) > 0.1) and (f3f1 < ts['f3f1thresh'])): ##need to fix syntax!!!
                    f4s = abs(np.array([f1 + f2 - f3, f1 - f2 + f3,f1 - f2 - f3]))
                    numchecked = numchecked+1
                    for mm in np.arange(0,3):
                        f4 = f4s[mm]
                        if f4 > f3  or laddermode: #avoids double finding does this mean laddermode true?
    #                     %       [minval ival] = closest(f4,fs);
                            ferrs = abs(f4list-f4) #f4list fine, f4 not right
                            [minval,ival] = np.min(ferrs), np.argmin(ferrs) ##!!
                            if minval < ts['flatsquarefthresh']: ### this loop is not running
                                oldf4 = f4;
                                f4 = f4list[ival];
                                f4error = f4 - oldf4;
                                s['fs'] = np.array([f1, f2, f3, f4]);
                                s['hs'] = np.array([h1, h2, h3, h4list[ival]])
                                if mm == 0:
                                    s['signs'] = np.array([1, 1, -1, -1]);
                                elif mm ==1:
                                    s['signs'] = np.array([1, -1, 1, -1]);
                                elif mm== 2:
                                    s['signs'] = np.array([1, -1, -1, 1]);
    #                             
                                s['usecorrection'] = 1;
                                s['laddermode'] = laddermode;
                                s['originalf1'] = f1;
                                s['originallinetouse'] = linetouse;
                                s['counttool'] = counttool;
                                s['frange'] = frange;
                                # if laddermode == 1:
                                #     if kit['visiblewindow'] in kit.keys():
                                #         s['frecommendedmin'] = kit['visiblewindow'][0]; ###!!!!
                                #         s['frecommendedmax'] = kit['visiblewindow'][1];
                                #     else:
                                #         s['frecommendedmin'] = 10000;
                                #         s['frecommendedmax'] = 18500;
    
                                # else:
                                s['frecommendedmin'] = min(fs) + 0.05 * frange;
                                s['frecommendedmax'] = min(fs)  + 0.95*frange;
                                s['templateabsolute'] =  kit['templateabsolute'];
                                s['templatenorm'] =  kit['templatenorm']
                                s['forcecorners'] = kit['forcecorners'];
                                s['cornermap'] = kit['cornermap'];
                                s['flaterrors'] =np.array([f1error, f2error, f3error, f4error]); 
                                s['tightnesssettings'] = ts;
                                s['signedfs'] = s['signs'] * s['fs'];  #so we know which ones are in a series yet? Maybe not.   !!!!
                                s['ferror'] = sum(s['signedfs']);
                                s['ferror2'] = minval;
#                                s['originstring'] = print('%s %3.1f line %d',kit.kitfilename,f1,linetouse);  #!!!!!
#                                s['descriptor'] = print('unconfirmed square %3.2f %3.2f %3.2f %3.2f',s.signedfs(1),s.signedfs(2),s.signedfs(3),s.signedfs(4));
#                %                disp(s);
                                numfound = numfound+1
                                allsquares.append(s.copy());  ###!!!! need to figure out indexing for here
#    return allsquares, kit, f1
    allsquares = uniquesquares(allsquares)
    
    if np.size(allsquares, axis=None) == 0: 
        print('no squares found :(\n') #!!!
    return allsquares, kit, f1

def uniquesquares(allsquares):
#function newsquares = uniquesquares(allsquares)
    newsquares = []; ### be sure if that needs a list or a dictionary
    for i in range(0, np.size(allsquares, axis=None)):
        
        seemsnew = 1;
        thissquare = allsquares[i];
        for k in range(0, np.size(newsquares, axis=None)):
            thatsquare = newsquares[k];
            sortfs =  np.sort(thissquare['fs'][0:2]);
            sortfs2 = np.sort(thatsquare['fs'][0:2]);
            maxdiff12 = max(abs(sortfs - sortfs2));
            sortfs = np.sort(thissquare['fs'][2:4]);
            sortfs2 = np.sort(thatsquare['fs'][2:4]);
            maxdiff34 = max(abs(sortfs - sortfs2));
            
            if (maxdiff12 < 0.1) and (maxdiff34 < 0.1):
                seemsnew = 0;
                
        if seemsnew:
            mindiff = min(np.diff(np.sort(thissquare['fs'])))
            
            if mindiff > 1:
                newsquares.append(thissquare.copy())
                
                
    return newsquares
    
# allsquares, kit, f1= getflatsquares(kit, linetouse, ts)
# print('done!')
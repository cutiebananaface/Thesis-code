# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:52:22 2020

@author: rodri
"""
#from easygui import*
import numpy as np
import copy
import subprocess
import os
import sys
import multiprocessing
from multiprocessing import Process, Queue
import psutil
import re

import string
import math
import time
from scipy.interpolate import *
#import matplotlib
#matplotlib.use('TkAgg')
#import pylab
#from matplotlib import pyplot as pp
#from pylab import*
#from scipy import*
#from matplotlib import*

#from settingsfromtightness import settingtightness
from steves_peak_cube import peakpicker, cubic_spline
#def main():
    
# function [kit] = autofit(molname,method,cheatLevel,numSpecies,ts)
#if nargin == 0
    #molname = 'myrtenal';
molname = 'nopinone'
numSpecies=1
cheatLevel = 0;
csvfilename="Nopinone.csv"

 #   molname = 'angelica';
   # molname = 'hexanal';  #hexanal is having trouble with the f1->f0 jump
  #  molname = 'BenzOD';
# end
#  if nargin < 2
    # method = 'scaffold';
#    method = 'bowties';
#     method = 'atype';
#  end
#  if nargin < 3
    
# end
# csvfilename = completeFilename(molname);


# =============================================================================
# in this section RAARR is getting the CSV file name but isnt actually anazlyzing it
# =============================================================================
#function csvfilename = completeFilename(molname)
#    if strcmp(molname(end-3:end),'.csv') == 1
#        csvfilename = molname;
#        return
#    end
#    csvfilename = sprintf('Molecules/%s/%s.csv',molname,molname);
#    %csvfilename = sprintf('../squareassign/Molecules/%s/%s.csv',molname,molname);
#    if length(dir(csvfilename)) == 0
#        if molname(1) ~= upper(molname(1))
#            molname(1) = upper(molname(1));
#            csvfilename = completeFilename(molname);
#        else
#            
#            fprintf('file %s not found\n',csvfilename);
#            csvfilename = [];
#        end
#    end
list1=[]
t=1
ts={}
    #%first settings which are common to methods
    #%ts has various components: variant settings, spfit settings
ts['scalartightness'] = t;
ts['f3f1thresh'] =  4000 * (t) ;
ts[' flatsquareheightratio'] = 12 * t;
ts['firstcutheightratio'] =  12 * t;

ts['mindegree'] = 2;

ts['lowjthresh'] = 7;

isotopefitting={}
isotopefitting['heightratiomax'] = 250;
isotopefitting['freqmin'] = .98;
isotopefitting['freqmax'] = 1.01;
isotopefitting['numtargetmax'] = 15;
#ts.update(isotopefitting)

list1.append(ts)
list1.append(isotopefitting)
success= True

#freqs=[]
#amps=[]
#try:
#    data_input_file = open(csvfilename)
#except:
#    error_message = "%s couldn't be opened. Try again with a different one."%(csvfilename)
#    print(error_message)
#    success= False
#    
#if success==True:
#    try:
#        for row in data_input_file:
#            temp=row.split(",")
#            freqs.append(float(temp[0]))
#            amps.append(float(temp[1].rstrip('\n')))
#    except:
#        error_message = "Data from a file (%s) couldn't be properly processed; try again with a different file."%(csvfilename)
#        print(error_message)
#        
#print(amps[12], amps[13])
#print(freqs[12], freqs[13])
#print(temp)


#### this runs- dont edit arianna---------------
data_file=csvfilename

try:
    fh = np.loadtxt(data_file,delimiter=',') #loads full experimental data file, not just list of peaks. Should be in directory this script is run from (same as input file).
except:
    try:
        fh = np.loadtxt(data_file) #fh contains entire spectrum
    except:
        error_message = "%s couldn't be properly loaded. Try again with a different file or check the file for issues."%(data_file) # will probably want to try a whole bunch of things and then only raise an error if none of them work.
        print(error_message)

xdata = copy.copy(fh[:,0]) # Need to handle both of these, just in case it's like an empty file (or has wrong number of columns or something)
ydata = copy.copy(fh[:,1]) #x gets freqs and y gets amps

low_intensity = np.mean(ydata)*2 # does this work? seems too easy. Probably not bad for semi-sparse spectra
high_intensity = max(ydata)*1.05 # finds the max of tbe spectra
inten_high = high_intensity
inten_low = low_intensity
resolution=2 #i put in 2 because it felt right
splined_spectrum = cubic_spline(xdata, ydata, 2) # Interpolates experimental spectrum to a 2 kHz resolution with a cubic spline.  Gives better peak-pick values.
(peaklist, freq_low, freq_high) = peakpicker(splined_spectrum,inten_low,inten_high) # Calls slightly modified version of Cristobal's routine to pick 
#####-----------------

# if nargin < 5
#tightnesssettings = settingtightness(1);
#save('tightnesssetting_data', 'tightnesssettings')

#if __name__ ==  "__main__":
#    main()
# =============================================================================
# This is the function for settingsfromtightness
# =============================================================================
#function ts = settingsfromtightness(t)
#%tightnesssettings contains all thresholds.  some are fixed, some vary with
#%tightness. high tightness is TOLERANT
#t=1
##%first settings which are common to methods
##%ts has various components: variant settings, spfit settings
#scalartightness = t;
#f3f1thresh =  4000 * (t) ;
#
#flatsquareheightratio =  12 * t;
#firstcutheightratio =  12 * t;
#
#mindegree = 2;
#
##% patternfitting.maxcomponents = 1;
##% patternfitting.maxpatterns = 20;
##% patternfitting.maxka = 1;
##% ts.patternfitting = patternfitting;
##% 
##% ts.maxcomponents = 1;
##% ts.maxpatterns = 20;
##% ts.maxka = 1;
#highsidetolerance =   t * 0.5 * [50 50 10];  #how well can we predict the next f? lactone had to lower
#lowsidetolerance =   t * [300 70 25];
#lowjthresh = 7;
#
##%ts.btolerance =   0 * t *  [300 90 40 20 4 2 2 2];
#
#
#
#aatolerance = t *  800;  #series1 - series4, about. angelica is about 700
#abtolerance = t * 4000;
#
#
#ladderSearchtimes = {[5,1e-40],[20, 1e-40],[100,1e-40],[500,1e-8],[4000,100]}; #these are time,pval pairs. last one means "just quit after 1000".
#seriesaratio = 15;
#seriesbratio = 15;
#gapmax = 4000; #flat square b+c
#gapmin = 400;
#minlines = 600;  #number of lines in the spectrum after first cut
#flatsquarefthresh = .050;
#seriessquarefthresh = .050;
#flatsquarelimit = 6000;
#minpval = 1e-6;
#checkablepval = 1e-8;
##%ts.numABCs = 3;
#
#
#smallestscaffold = 12;  %usually 12
#minrungs = 3; %usually 3
#numjguess = 3;
#if t >= 1
#    checkablepval = 1e-8;
#end
#if t >= 2
#    checkablepval = 1e-5;
#end
#maxka = 2;
#okhitvotecount = 10;
#maxscaffolds = 80; %when do things bog down?
#evolveFit = 0;
#addisotopes = 0;
#foundfitvotecount = 20;
#greathitvotecount = 80;
#maxsquaresfromline = 3;
##ts.totaltime = totaltime;
#trimends = 0;  %cut off ends of long series - they might be wrong and we have enough..
#
##%ts.lines = [1:40]; %[1:40];
#ts.lines = [1:50];
#if t > 1
#    ts.lines = [1:60];
#end
#if t > 2
#    ts.lines = [1:80];
#end
#
#isotopefitting.heightratiomax = 250;
#isotopefitting.freqmin = .98;
#isotopefitting.freqmax = 1.01;
#isotopefitting.numtargetmax = 15;
#isotopefitting.targetminheight = 100;
#isotopefitting.freqpixel = .10;
#isotopefitting.minSNR = 200;
#isotopefitting.c13pval = 1e-10;
#isotopefitting.numtrials = 100;
#isotopefitting.maxspecies = 1;   %number of isotopologues you can find..
#isotopefitting.fdriftmax = 0.05;
#isotopefitting.targetoccupancy = 0.05;
#isotopefitting.maxmisses = 125;
#isotopefitting.dicerolls = 4;  %lower is more random, more stupid triad choices
#isotopefitting.spurratiomin = 0.001;
#ts.isotopefitting = isotopefitting;
#
#patternfitting.numABCs = 3;
#patternfitting.maxcomponents = 1;
#patternfitting.maxpatterns = 20;
#patternfitting.actypes = [0];  %try both ab and ac
##%patternfitting.actypes = [1];  %try just ac
#patternfitting.maxka = 2;
#patternfitting.numjguess = 3;
#ts.patternfitting = patternfitting;
### block for bruteforce
##bruteforce.numtheorylines = 50;
##bruteforce.numexperimentlines = 500;
##bruteforce.heightratiomax = 500;
##% bruteforce.freqmin = .98;
##% bruteforce.freqmax = 1.01;
##bruteforce.numtargetmax = 15;
##bruteforce.targetminheight = 0;
##bruteforce.freqpixel = 2.00;
##bruteforce.minSNR = 1;
##bruteforce.c13pval = 1e-10;
##bruteforce.numtrials = 3;
##bruteforce.maxspecies = 1;
##bruteforce.fdriftmax = 0.05;
##bruteforce.targetoccupancy = 0.05;
##bruteforce.spurratiomin = 0.05;  %spurs must be this tall
##bruteforce.maxmisses = 125;
##bruteforce.dicerolls = 4;  %lower is more random, more stupid triad choices
##ts.bruteforce = bruteforce;
##-----------
#
#variant3.babytolerance = 5;  %height ratio for first pair
#variant3.atolerance = 30;  %height ratio for ANY line in an a-series
#variant3.babyatolerance = 10;  %height ratio for first two line in an a-series
#variant3.meantolerance = 20;  %height new line from a-series mean
#variant3.fancytolerance = 0.5; %in MHz.  on fake data seem to hit more like 0.1 MHz.
#variant3.fancytolerancef1lowJ = 5; 
#  
#variant3.fancytolerancef0 = 0.5; %in MHz.  on fake data seem to hit more like 0.1 MHz.
#variant3.fancytolerancef0first = 10; %in MHz.  on fake data seem to hit more like 0.1 MHz.
#variant3.fancytolerancef0lowJ = 10; %5 MHz was too little, missed 1/9
#variant3.f1tof0tolerance = 50; %in MHz
#variant3.f1tof0toleranceSure = 300;  %accept MANY jumps if f1 series is iron clad
#variant3.f1tof0toleranceThresh = 1e2;
#variant3.minf1length = 3; %how long does an f1 streak need to be befoe jumping to f0
#variant3.minlines = 4;
#variant3.gapmax = 4000; %flat square b+c
#variant3.gapmin = 400; 
#variant3.maxPatterns = 2;
#variant3.heightHealthRatio = 15;  %higher is more tolerance
#variant3.freqHealthLimit = 0.2;  %higher is more tolerance. in MHz.
#variant3.maxPval = 10;  %think about this. sliding scale?
#variant3.minforcloseout = 2;
#variant3.maxtof0 = 20;
#variant3.totalHealthLimit = 1; %larger is LESS tolerant. 
#%variant3.maxfromoneline = 2;
#variant3.gapoverbendmax = 100; %never seen this violated
#%cowcow make bendtolerance higher at higher j. if j < 6, double it maybe? 
#variant3.bendTolerance = [50 20 10 10 10 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]; %third line in f1 a series can be how far out of straight
#variant3.lowj = 5;  %all tolerances looser down here
#variant3.lines = [1:30];
#variant3.kaguesses = [0];
#variant3.verbose = 0;
##%settings for variant 3
#ts.variant3 = variant3;
#
##
#bowties.rank = 200;
#bowties.containsOblate = false;
#bowties.weakAorB = 0;
#bowties.divthresh = 8;
#bowties.divthresh2 = 8;
#bowties.divthreshs = 105;
#bowties.dthresh = 0.05;
#bowties.hsdivthresh = 3500;
#bowties.rmsthresh = 0.005;
#bowties.percentmaxdiff = 0.08;
#bowties.percenth14diff = 0.04;
#bowties.leftsq = 0.02;
#bowties.rightsq = 0.02;
#bowties.prll1 = 0.02;
#bowties.prll2 = 0.02;
#bowties.inttest = 0;
#bowties.ratiovar = 0.045;
#ts.bowties = bowties;




# else
#     tightnesssettings = ts;
# end
# 
#kit = kitfromcsvfile(csvfilename,tightnesssettings);
# kit.cheatLevel = cheatLevel;
# kit.cheatCodes = getCheatCodes(molname,cheatLevel);
# 
# kit.method = method;
# kit.tightnesssettings = tightnesssettings;
# 
# if (nargin >= 4) || (nargin == 0)
#     kit.tightnesssettings.patternfitting.maxcomponents = numSpecies;
# end
# displaybarekit(kit);




# #[kit] = findfitd(kit);
# [kit] = findallspecies(kit);
# savekit(kit);
# 
# #hexanal f1s: 11632.55 13293.32 14953.67 16613.57 18272.99
# #hexanal f0s: 11799.56 13480.96 15160.66 16838.49 18514.24
# #these lead to A being rather wrong, but the fit should converge.
# 
# 
# 
# function makepgos(kit)
#     
#     for i = 1:length(kit.fitlist)
#         thisfit = kit.fitlist{i};
#         pgofilename = sprintf('#s#s_comp#d.pgo',kit.directoryname,kit.molname,i);
#         makepgofile(thisfit.molstats,pgofilename,6,'abc');
#        # pgofilename =
#     end
#     
# 
# function savekit(kit)
#     
#     save(kit.kitfilename,'kit');
#     displaykitwithfits(kit);
#     
#     if length(kit.fitlist) > 0
#         makepgos(kit);
#         try
#             if (kit.cheatLevel <= 1)
#                 launchpgopher(kit.molname);
#             end
#         end
#         try
#             saveas(gcf,kit.figfilename);
#             saveas(gcf,kit.pdffilename);
#         catch
#             fprintf('cannot save pdf, probably open in narcissistic adobe');
#         end
#     end
#     disp(kit.fitlistreport);
#     pause(0.001);
# 
# 
# 
# 

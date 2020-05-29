from settingsfromtightness_python import settingsfromtightness
from kitfromcsvfile_python import kitfromcsvfile
# from peakpicking import cubic_spline, peakpicker
import numpy as np
import copy 
import matplotlib
import matplotlib.pyplot as plt
import math
class Molecule:  #trying out some ideas for building classes!
    def __init__(self, molname, numSpecies, filename, method, cheatLevel): #initialize with the arguments from autofit.m
        self.molname= molname  
        self.numSpecies= numSpecies
        self.filename= filename
        self.method= method
        self.cheatLevel= cheatLevel
    
    def tightness(self, setting):  #get the tightnesssettings- many of the values are hardcoded in the original m-file
        if setting == 1:
            self.tightnesssettings= settingsfromtightness(1)
        else:
            self.tightnesssettings= setting
        return

class Kit(Molecule): #Child class- gets the attributes from molecule
    def rawspec(self): #get the raw spec from the spectrum file
        try:
            fh = np.loadtxt(self.filename,delimiter=',') #loads full experimental data file, not just list of peaks. Should be in directory this script is run from (same as input file).
        except:
            try:
                fh = np.loadtxt(self.filename) #fh contains entire spectrum
            except:
                error_message = "%s couldn't be properly loaded. Try again with a different file or check the file for issues."%(self.filename) # will probably want to try a whole bunch of things and then only raise an error if none of them work.
                print(error_message)
        # getting the freq and amps, x is freqs and y is amps 
        self.xdata = copy.copy(fh[:,0]) # Need to handle both of these, just in case it's like an empty file (or has wrong number of columns or something)
        self.ydata = copy.copy(fh[:,1]) 
        return self.xdata, self.ydata

    def smooth(self, a, WSZ): #a smoothing function meant to replicate MATLAB's smooth function (https://www.mathworks.com/help/curvefit/smooth.html)
        #https://stackoverflow.com/questions/40443020/matlabs-smooth-implementation-n-point-moving-average-in-numpy-python
        # a: NumPy 1-D array containing the data to be smoothed
        # WSZ: smoothing window size needs, which must be odd number,
        # as in the original MATLAB implementation
        WSZ= int(WSZ)
        out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ    
        r = np.arange(1,WSZ-1,2)
        start = np.cumsum(a[:WSZ-1])[::2]/r
        stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
        return np.concatenate((  start , out0, stop  ))

    def peakpicker(self, spectrum):#Code taken from Cristobal's peak-picking script; assumes spectrum is in increasing frequency order
        #altering peakpicker to just use the amps input
        peaks=[]
        # self.inten_low=1.6894 #hard coded for nopinone but will use the code from RAARR to find this value
        for i in range(1, len(spectrum)-1):
            #pick the peak if it is greater than the lowest (inten_low) intensity, less than the greatest (inten_high), and if it is greater than to the two surrounding peaks
            # if (spectrum[i,1] > self.inten_low and 
            #     spectrum[i,1] < self.inten_high and 
            #     spectrum[i,1] > spectrum[(i-1),1] and  
            #     spectrum[i,1] > spectrum[(i+1),1]):
            #altered from original peakfinder, removed inten_high and inten_low uses RAARR's code for finding the minimum hieght
            if (spectrum[i,1] > self.inten_low and spectrum[i,1] > spectrum[(i-1),1] and spectrum[i,1] > spectrum[(i+1),1]):  
                peaks.append(spectrum[i])

        peakpicks=np.zeros((len(peaks),2))
        for i,row in enumerate(peaks):
            peakpicks[i,0]=row[0] #freqs values
            peakpicks[i,1]=row[1] #amp values
        locs= peakpicks[:,0] #freq values (not indices!)
        pks= peakpicks[:,1] #amp values
        return pks, locs

    def before_peakfinding(self, newf, finalspec ,threshsigma=7,specr=0.05e6):
        freqs = [] 
        sigheights = [] 

        livepoints = np.where(finalspec != 0) 
        finalspec = finalspec[livepoints] 
        newf = newf[livepoints]
        nsmooth = np.floor(1 + (specr / (newf[1] - newf[0]))) 

        # self.splined_spectrum = cubic_spline(newf, finalspec, 2)
        smoothspec = self.smooth(finalspec,nsmooth) 


        rawdata = smoothspec[np.where(smoothspec > 0)] 
        rawmedian = np.median(rawdata) 
        zeropoints = rawdata[np.where(rawdata < rawmedian*2)] 

        newstd = np.std(zeropoints) 
        flatspec = smoothspec - rawmedian 

        newthresh = newstd *  threshsigma
        # low_intensity = np.mean(self.ydata)*2 # does this work? seems too easy. Probably not bad for semi-sparse spectra
        # high_intensity = max(self.ydata)*1.05 # finds the max of tbe spectra
        # self.inten_high = high_intensity
        # self.inten_low = low_intensity
        self.inten_low= newthresh
        spectrum=np.zeros((np.size(flatspec),2))
        spectrum[:,0]=copy.copy(newf)  ##freqs
        spectrum[:,1]=copy.copy(flatspec)  ##amps

        # index_amps= np.argsort(flatspec)[::-1]
        # sorted_freqs= newf[index_amps] #sort freq values in descending amps order

        pks, peak_freqs = self.peakpicker(spectrum) ## findpeaks.m, pks is the amps and peak_freqs is the frequencies of the peaks (not indices!!)
        
        #https://stackoverflow.com/questions/33678543/finding-indices-of-matches-of-one-array-in-another-array
        sorted_amp = np.argsort(flatspec)
        locs = sorted_amp[np.searchsorted(flatspec,pks, sorter = sorted_amp)]
        
        pks, pki= np.sort(pks)[::-1], np.argsort(pks)[::-1] ## sort pks in decending order, return the indices for the descending sort as pki
        locs= locs[pki] #sort peak indices by decreasing peak order
        freqs= peak_freqs[pki] ##sort peak_freqs in descending order

        peakresults= {}
        thispeak={}
        peakresults['excluded'] = 0 * newf
        peakresults['residuals'] = copy.copy(flatspec)
        delf = newf[1]-newf[0]
        allpeaks = []
        exactfs = np.array([]) 
        exacths = np.array([]) 
        for i in range(0, np.size(freqs)):
            thispeak['f'] = copy.copy(freqs[i])
            thispeak['specrs'] = copy.copy(specr)
            thispeak['height'] = copy.copy(pks[i])
            thispeak['centeri'] = copy.copy(locs[i])
            zonesize = nsmooth * 20
            thispeak['minzone'] = int(max(1,thispeak['centeri']-zonesize))
            thispeak['maxzone'] = int(min(np.size(newf),thispeak['centeri']+zonesize))
            thispeak['zonei'] = np.arange(thispeak['minzone'],thispeak['maxzone']+1).astype(int)
            thispeak['zonef'] = copy.copy(newf[thispeak['zonei']])
            thispeak['zonesig'] = copy.copy(flatspec[thispeak['zonei']].conj().T)
            thispeak['assigned'] = 0
            thispeak['threshhold'] = copy.copy(newthresh)
            errsig = math.inf
            guessi_a= np.linspace(-1,1,201)
            for i in range(0,np.size(guessi_a)):
                guessi= copy.copy(guessi_a[i])
                guessf = thispeak['f'] + (delf*guessi) 
                localdetune = (thispeak['zonef'] - guessf) / (2.4*specr) 
                gaussenv = (1.0 * thispeak['height'] * np.exp(-localdetune**2)).conj().T
                sizegauss = np.shape([gaussenv]) 
                sizeresults = np.shape([peakresults['residuals'][thispeak['zonei']]]) 
                if (sizegauss[0] == sizeresults[0]):
                    gaussenv = copy.copy(gaussenv.conj().T)
                
                thiserror = sum((peakresults['residuals'][thispeak['zonei']] - gaussenv.conj().T)**2)
                if thiserror < errsig:
                    errsig = copy.copy(thiserror) 
                    bestguessf = copy.copy(guessf)
                    bestenv = copy.copy(gaussenv) 
            
            peakresults['residuals'][thispeak['zonei']] = peakresults['residuals'][thispeak['zonei']] - bestenv.conj().T
            thispeak['exactf'] = copy.copy(bestguessf) 
            localdetune = (thispeak['zonef'] - bestguessf) / (2.6*specr) 
            thispeak['gaussenv'] = 1.0 * thispeak['height'] * np.exp(-localdetune**2) 
            localdetune = (thispeak['zonef'] - bestguessf) / (1.8*specr) 
            thispeak['exclusionenv'] = 0.9 * thispeak['height'] * (1./(1+abs(localdetune)**3.00)) 
            allpeaks.append(copy.copy(thispeak))
            for j, j_val in enumerate(thispeak['zonei']):
                peakresults['excluded'][j_val] = max(peakresults['excluded'][j_val],thispeak['exclusionenv'][1+(j_val)-thispeak['minzone']-1]) 
    
        
        for i in range(0,np.size(allpeaks)):
            thispeak = allpeaks[i] 
            if thispeak['height'] > peakresults['excluded'][thispeak['centeri']]:
                exactfs= np.append(exactfs, thispeak['exactf'])
                exacths= np.append(exacths, thispeak['height'])
                
                thispeak['verified'] = 1 
            else:
                thispeak['verified'] = 0 

            
        # %[prunedfreqs prunedheights] = prunepeaks(freqs,heights,specr) 
        # %plot(freqs,pks,'bs') 
        sigheights = pks 
        peakresults['allpeaks'] = allpeaks 
        peakresults['freqs'] = freqs 
        peakresults['exactfs'] = exactfs 
        peakresults['exacths'] = exacths 
        peakresults['sigheights'] = sigheights 
        peakresults['stddev'] = newstd 
        peakresults['thresh'] = newthresh 
        peakresults['threshsigma'] = threshsigma 
        peakresults['flatspec'] = flatspec 
        peakresults['newf'] = newf
        return peakresults



trialKit = Kit("nopinone", 1, "Nopinone.csv", 'scaffold', 0)
trialKit.tightness(1)
xdata, ydata= trialKit.rawspec() ##raw spect from csv file
peakresults =trialKit.before_peakfinding(xdata, ydata,7, 0.050) ##preparing variables specific to RAARR that are created before peakfinding, also smoothing

# print('hewwo')
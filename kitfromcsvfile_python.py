import copy
import csv
import numpy as np
def kitfromcsvfile(csvfilename, ts):
#function kit = kitfromcsvfile(csvfilename,ts)
    #python has interesting nargin read more here https://stackoverflow.com/q/51407329
    # if csvfilename='fake' or csvfilename='propanediol':  
        # #if csvfilename='propanediol':
        # correctheights = 0;
    # else
        # correctheights = 1;

    
    # if (nargin >= 2) && isfield(ts,'correctheights') == 1
        # correctheights = ts.correctheights;
        
    #for the moment we will say correctheights=1
    correctheights=1

    # try
        # M = csvread(csvfilename);
        # freqs = M(:,1);
        # amps = M(:,2);
    # catch
        
        # M = dlmread(csvfilename,' ');
        # freqs = M(:,1);
        # amps = M(:,2) * 1000;
    # end


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
    (peaklist, freq_low, freq_high) = peakpicker(splined_spectrum,inten_low,inten_high)

    

    # peakresults = findpeaksd(freqs,amps,7,.050);
    # %peakresults = findpeaksd(freqs,amps,7,.050);
    # fs = peakresults.exactfs;
    # hs = peakresults.exacths;
    # [fs XI] = sort(fs);
    # hs = hs(XI);

    # if correctheights
        # [fs hs] = redrigspectralcorrection(fs,hs);
    # end

    # # % lastslash = find(csvfilename == '/',1,'last') + 1;
    # # % lastdot = find(csvfilename == '.',1,'last') - 1;
    # # % molname = filenames(lastslash:lastdot);
    # # % lastslash = find(filenames == '/',1,'last') + 1;
    # # % lastdot = find(filenames == '.',1,'last') - 1;
    # kit['kitfilename'] =  kitfilename(csvfilename); ## havent converted
    # # function s = kitfilename(csvfilename)
    # # s = [csvfilename(1:end-4) 'kit'];
    # kit['figfilename'] = figfilename(csvfilename);
    # # function s = figfilename(csvfilename)
    # # s = [csvfilename(1:end-4) 'fig.fig'];
    # kit['pdffilename'] = pdffilename(csvfilename);
    # # function s = pdffilename(csvfilename)
    # # s = [csvfilename(1:end-4) 'pdf.pdf'];
    # kit['reportfilename'] = reportfilename(csvfilename);
    # # function s = reportfilename(csvfilename)
    # # s = [csvfilename(1:end-4) '_report.txt'];
    # [kit['molname'], directoryname] = molnamefromfilename(csvfilename);
    # # function [molname,directoryname] = molnamefromfilename(filename)
    # # lastslash = find(filename == '/',1,'last') + 1;
    # # lastdot = find(filename == '.',1,'last') - 1;
    # # molname = filename(lastslash:lastdot);
    # # directoryname = filename(1:lastslash-1);
    
    # ##havent converted anything after = , Jan 21 2020
    # kit['directoryname'] = directoryname;
    # kit['freqs1d'] = xdata;
    # kit['amps1d'] = amps;
    # kit['searchedf1s'] =[];
    # kit['candidateScaffolds'] = {};

    # kit['latestpattern'] = 0;
    # kit['numvotes'] = 0;
    # kit['skipspfit'] = 0;
    # kit['onedpeakfs'] = fs;
    # kit['onedpeakhs'] = hs;
    # kit['onedpeakfsunassigned'] = fs;
    # kit['onedpeakhsunassigned'] = hs;
    # kit['minf'] = min(kit['onedpeakfs']);
    # kit['maxf'] = max(kit['onedpeakfs']);
    # kit['frange'] = kit['maxf'] - kit['minf'];
    # kit['numpeaks'] = length(kit['onedpeakfs']);
    
    # kit['SNR'] = 0.5 * max(hs)/peakresults['stddev'];
    # # kit['barekitdescriptor'] = sprintf('Spectrum %3.1f->%3.1f MHz\n %d peaks, SNR'] = %3.1f',min(fs),max(fs),kit['numpeaks'],kit['SNR'];
    # kit['barekitedescriptor']= f"Spectrum %3.1f->%3.1f MHz\n %d peaks, SNR'] = %3.1f',min(fs),max(fs),kit['numpeaks'],kit['SNR']"
    # kit['numspecies'] = 0;
    # kit['numtries'] = 0;
    
    # kit['fitlist'] = {};
    # kit['Dinverted'] = 1;
    # kit['bogged'] = 0;
    # kit['experimental'] = 1;
    # kit['fitlistreport'] = '';
    
    # kit['totalflatsquares'] = 0;
    # kit['totalCensus'] = zeros(1,20);
    # kit['bestScaffoldp'] = 1;
    # kit['csvfilename'] = csvfilename;
    # kit['whichspecies'] = zeros(1,length(kit['onedpeakfs));
    # kit['templateabsolute'] = zeros(1,50);
    # kit['templatenorm'] = zeros(1,50);
    # kit['forcecorners'] = 0;
    # kit['cornermap'] = 0;
    # # %kit['tightmode = tightmode;
    # kit['breakmode'] = 1;
    # # %kit['maxka'] = 4;
    # kit['flexibletightness'] = 1;
    # kit['flextights'] = 0;
    # # %kit['skipfit = 0;
    # kit['foundfit'] = 0;
    return kit

def peakpicker(spectrum,thresh_l,thresh_h):#Code taken from Cristobal's peak-picking script; assumes spectrum is in increasing frequency order
    peaks=[]
    for i in range(1, len(spectrum)-1):
        if spectrum[i,1] > thresh_l and spectrum[i,1] < thresh_h and spectrum[i,1] > spectrum[(i-1),1] and spectrum[i,1] > spectrum[(i+1),1]:
            peaks.append(spectrum[i])

    peakpicks=numpy.zeros((len(peaks),2))
    for i,row in enumerate(peaks):
        peakpicks[i,0]=row[0]
        peakpicks[i,1]=row[1]
    freq_low = spectrum[0,0]
    freq_high = spectrum[-1,0]
    return peakpicks, freq_low, freq_high

def cubic_spline(spectrum,new_resolution): # Cubic spline of spectrum to new_resolution; used pre-peak-picking.  Assumes spectrum is already in order of increasing frequency.

    x = spectrum[:,0]
    y = spectrum[:,1]

    old_resolution = (x[-1]-x[0]) / len(spectrum)
    scale_factor = old_resolution / new_resolution

    new_length = int(math.floor(scale_factor*len(spectrum)))

    tck = splrep(x,y,s=0)
    xnew = numpy.arange(x[0],x[-1],new_resolution)
    ynew = splev(xnew,tck,der=0)

    output_spectrum = numpy.column_stack((xnew,ynew))

    return output_spectrum


from numpy import *
from copy import *
from stickplot_python import *
import matplotlib.pyplot as mpl

def plotpairs(pairlist=findallpairs(),whichplot='scaledsixKweakpulsestrength',plotstyle='b',scalefactor=1,inMHZ=0):

    flipit = 1
    if whichplot[-1] == '-':
        whichplot = whichplot[1:-2]
        flipit = -1
    numpairs = size(pairlist)
    if size(numpairs) == 0:
        return
    freqs = array([])
    amps = array([])
    pols = array([])
    ytoplot = array([])
    for i in range(1, numpairs):
        thispair = pairlist[i]
        if inMHZ:
            freqs[end+1] = thispair['delfMHZ']
        elif 'localf' in thispair:
            freqs[end+1] = thispair['localf']
        else
            freqs[end+1] = thispair['delf']

        amps[end+1] = thispair['transmoment']
        pols[end+1] = thispair['polarizability']
        ytoplot[end+1] = scalefactor @ flipit @ thispair['whichplot']
    f, xi = sort(freqs), argsort(freqs)
    newp = pols[xi]
    for i in range(1,numpairs):
        thispair = pairlist[xi][i]
    if plotstyle == 'q':
        p = stickplot(freqs,ytoplot)
    else:
        p = stickplot(freqs,ytoplot,plotstyle)
    a['datatype'] = 'Pairlist'
    a['pairlist'] = pairlist
    set(p,'UserData',a) ## basically set the property for the plot- not sure what to replace with
    mpl.ylabel(whichplot)
    return
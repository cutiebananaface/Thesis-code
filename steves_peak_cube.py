# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:07:17 2020

@author: rodri
"""
import subprocess
import os
import sys
import multiprocessing
from multiprocessing import Process, Queue
import psutil
import re
import numpy
import string
import math
import time
from scipy.interpolate import *
import copy

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
	
def cubic_spline(xdata, ydata, new_resolution_kHz): # Cubic spline of spectrum to new_resolution; used pre-peak-picking.  Assumes spectrum is already in order of increasing frequency.

    x = copy.copy(xdata)
    y = copy.copy(ydata)

    new_resolution = new_resolution_kHz / 1000.0

    old_resolution = (x[-1]-x[0]) / len(x) #last in x- first in x/lenght of x
    scale_factor = old_resolution / new_resolution #create scale factor

    new_length = int(math.floor(scale_factor*len(x))) #times the scale factor by the length and use the largest value 

    tck = splrep(x,y,s=0) #find B-spline representation-smooths spectra- the core of this function
    xnew = numpy.arange(x[0],x[-1],new_resolution)
    ynew = splev(xnew,tck,der=0)

    output_spectrum = numpy.column_stack((xnew,ynew))
    print(new_resolution)
    print( old_resolution)
    print(scale_factor)
    print(new_length)
    print(tck)
    output_spectrum = numpy.column_stack((xnew,ynew))
    return output_spectrum
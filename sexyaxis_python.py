from numpy import *
import matplotlib.pyplot as mpl
def sexyaxis(*args,**kwargs):
	a = xlim

	minf = a[1]
	maxf = a[2]
	possibles = arange(1,50) * 2000
	if (maxf - minf) < 8000:
	    possibles = possibles/2
	ticks = array([])
	labels = []
	for i in range(1, size(possibles)):
	    if (possibles[i] >= minf) and (possibles[i] <= maxf):
	        ticks[end+1] = possibles[i];
	        labels[end+1] = print('%d'% possibles[i])

	mpl.xticks(ticks)
	mpl.xticklabels(labels)
	return a

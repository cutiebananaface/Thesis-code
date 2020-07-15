from evalf_python import evalf
from scipy import interpolate
from loadmatlab_workspace import load_mat
import numpy as np
from custommpl import customplot


from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

before= load_mat('input-saveAshape-plotting')
kit= before['kit']
def saveAshape(kit,verbose=1):
	# Omitting stuff about loading and saving files
	# if nargin < 1
	# load('ttfile','kit')
	# else
	# save('ttfile','kit')

	f0J = kit['series1']['fs']
	f1J = kit['series4']['fs']
	J = range(len(f1J))
	Jforf1 = kit['series4']['jvalues']
	Jforf0 = kit['series1']['jvalues']

	#commenting out call to otherwise unused function, also commented out below
	#exploreBC(Jforf0,f0J,kit.cheat.molstats);

	maxJ = max(J)
	firstk1 = f1J[-1] - f1J[-2]
	secondk1 = f0J[-1] - f0J[-2]

	k1 = 0.5*(firstk1 + secondk1)
	k2 = 1
	x1vals = [0]
	x0vals = [0]
	f1vals = [0]
	f0vals = [0]

	for i in range(maxJ):
		x1vals.append(Jforf1[i]+1)
		x0vals.append(Jforf0[i]+1)

		f1vals.append((f1J[i] - (k1*(Jforf1[i]+1)))/k2) # line flexes with above
		f0vals.append((f0J[i] - (k1*(Jforf0[i]+1)))/k2) # line flexes with above

	k2 = (f1vals[-1] + f0vals[-1])/2

	for i in range(len(f1vals)):
		f1vals[i] = f1vals[i]/k2
		f0vals[i] = f0vals[i]/k2

	bigx1vals = np.linspace(0,max(x1vals),400)
	bigx0vals = np.linspace(0,max(x0vals),400)
	print('max x0vals %s, max x1vals %s'%(str(max(x0vals)),str(max(x1vals))))

	f_x1 = interpolate.interp1d(x1vals,f1vals,kind='slinear',fill_value='extrapolate')
	f_x0 = interpolate.interp1d(x0vals,f0vals,kind='slinear',fill_value='extrapolate')

	bigf1vals = f_x1(bigx1vals)
	bigf0vals = f_x0(bigx0vals)

	smallx = 0.1
	k3 = np.interp(smallx,bigf1vals,bigx1vals) # check this
	k3 = k3/smallx
	print('k3 %s, smallx %s'%(str(k3),str(smallx)))

	f1table = {}
	f0table = {}

	f1table['xvals'] = bigx1vals / k3
	f1table['yvals'] = bigf1vals

	f0table['xvals'] = bigx0vals / k3 # Matlab has this as bigx1vals, but that can't be intended
	f0table['yvals'] = bigf0vals

	f0slope = f0table['yvals'][1] / f0table['xvals'][1]
	f1slope = f1table['yvals'][1] / f1table['xvals'][1]
	print('f0 slope is %3.3f, f1 slope is %3.3f\n'%(f0slope,f1slope))

	kit['f1table'] = f1table
	kit['f0table'] = f0table
	kit['k1'] = k1
	kit['k2'] = k2
	kit['k3'] = k3
	bigJvalues = np.linspace(0,max(Jforf1),500)

	f1outputs = evalf(bigJvalues,k1,k2,k3,1)
	f0outputs = evalf(bigJvalues,k1,k2,k3,0)
	tempy=[]
	for i in range(len(f0vals)):
		tempy.append(f0vals[i]*k2)
	xydatas={"xdata": [], "ydata": []}
	xydatas["xdata"].append(x0vals)
	xydatas["ydata"].append(tempy)
	
	fig3 = Figure() #figure instance
	ax1f3 = fig3.add_subplot(111)
	ax1f3.pcolormesh(np.random.rand(20,40))

# 	customplot(x0vals, tempy)
	customplot("testfig from func", fig3) #wow it worked probably should make a loop for the list
	
	#removed a bunch of plotting stuff that only showed if verbose == 1
	return kit

output=saveAshape(kit)
# Commented out this function from Matlab that didn't seem to net do anything:    
#    function exploreBC(J,f,molstats)
#        A = molstats.a;
#        B = molstats.b;
#        C = molstats.c;
#        
#        bcguess = ((A+B) * (J+1)) + ((2*C - A - B)*(J+0.5));
#        dpguess = 2*C*J + (A+B);
#        
#        dperrors = f-dpguess;
#        bcerrors = f-bcguess;
#        
#        dperrors;
#        bcerrors;
#        1;

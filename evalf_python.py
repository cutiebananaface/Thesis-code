import numpy as np
from scipy import interpolate

def evalf(J,k1,k2,k3,ftable):
	if type(ftable) is not dict:
		loaded_table = np.load('ftablefile.npz',allow_pickle=True)
		if ftable == 0:
			table = loaded_table['f0table'].item()
		elif ftable == 1:
			table = loaded_table['f1table'].item()
		else:
			print('unknown function')
			return False

	else:
		table = ftable

	x = (J+1)/k3 # not sure about data types here...

	extrap_func = interpolate.interp1d(table['xvals'],table['yvals'],kind='linear',fill_value='extrapolate')

	y1 = k2*extrap_func(x)
	freq = ((J+1) * k1) + y1

	return freq

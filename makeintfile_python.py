from numpy import  *
def makeintfile(argsin=prepare_sp_argsin):
	molstats= argsin['molstats']
	for types = array(['a', 'b','c']):
		filename=array([argsin['filename'], '.int'])
		partitionfn= (5.3311 * 10**6) * sqrt(argsin['temp']**3/(molstats['a'] * molstats['b'] * molstats['c']))
		f= open(filename, 'w')
		print('%s\n'% molstats['molname'], file=f)
		print( '114 %i %f %i %i %f ,, %f %f\n' % (-molstats['molid'], partitionfn, argsin['jmin'], argsin['jmax'], argsin['intensethresh'], argsin['maxf'], argsin['temp']), file=f)
		if types=='a':
			print('001 %f\n' % molstats['mua'], file=f)
		elif types=='b':
        	print('002 %f\n' % molstats['mub'], file=f)
	    else
	        print('003 %f\n' % molstats['muc'], file=f)
        fclose(f)
    return filename
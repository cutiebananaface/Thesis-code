
def litestringfromfit(thisfit):
	mol = thisfit['info']['argsout']
	cheatstring = ''
	if mol['DJ'] != 0:
	    CDstring = 'CD'
	else:
	    CDstring = '-'
	titlestring = print('A=%3.2f,B=%3.2f,C=%3.2f %s %d hits'% (mol['a'],mol['b'],mol['c'],CDstring,thisfit['yesvotes']))
	if 'C13frac' in thisfit:
	    titlestring = print('%s %3.3f ^{13}C'% (titlestring,thisfit['C13frac']))
    return titlestring



#rewritten (complete)
def updateline(thisline):
	if ('Jlower' not in thisline) and ('endj' in thisline):
	    thisline['Jlower'] = thisline['endj']
	    thisline['Kalower'] = thisline['endka']
	    thisline['Kclower'] = thisline['endkc']
	    thisline['Jupper'] = thisline['startj']
	    thisline['Kaupper'] = thisline['startka']
	    thisline['Kcupper'] = thisline['startkc']
	# i think an element wise multiplcation (*) will be fine, rather than a matrix multiplcation (@)
	thisline['lowerhash'] = (thisline['Jlower'] * 1e4) + (thisline['Kalower'] * 1e2) + (thisline['Kclower'])
	thisline['upperhash'] = (thisline['Jupper'] * 1e4) + (thisline['Kaupper'] * 1e2) + (thisline['Kcupper'])
	thisline['hash'] = thisline['lowerhash'] + (1e6 * thisline['upperhash'])
	
	if 'expfreq' in thisline
	    thisline['descriptor'] = print(f"{thisline['upperhash']}->{thisline['lowerhash']} {thisline['expfreq']}")
	else
	    thisline['descriptor'] = print(f"{thisline['upperhash']}->{thisline['lowerhash']} no experiment")
	s
	return thisline
    

from pickfirstf_python import pickfirstf
from getflatsquares_python import getflatsquares
from seriessquarefromflatsquare_python import seriessquarefromflatsquare
from extendseriessquarealltheway_python_July9 import extendseriessquarealltheway
from extractfieldsfromcellarray_python import extractfieldsfromcellarray
from sortcellarraybyfield_python import sortcellarraybyfield
# from trimends_python import trimends
from loadmatlab_workspace import load_mat
from comparefileoutputs import unpackingstruct
# from removeidentical_python import removeidentical

before = load_mat('input-addsquaresfromlines-s')
kit = before['kit']
linetouse = before['linetouse']
import numpy as np

def squaresfromline(kit,linetouse):
	searchReport = {}

	ts = kit['tightnesssettings']
	# Ignoring timing stuff. Original line: ts.starttime = now;
	searchReport['bogged'] = 0
	searchReport['numflatsquares'] = 0

	finalsquares = []
	(allsquares,kit, f1) = getflatsquares(kit,linetouse,ts) #adding in f1 to solve the value error
	fs = kit['usefs']
	hs = kit['usehs']
	seriessquares = []

	searchReport['numflatsquares'] = len(allsquares)

	for i in range(len(allsquares)):
		seriessquares.append(seriessquarefromflatsquare(allsquares[i],0))
		if seriessquares[-1]['dtype'] and kit['Dinverted']:
			seriessquares.append(seriessquarefromflatsquare(allsquares[i],1))

	if len(seriessquares) > ts['flatsquarelimit']:
		print('%d is far too many flatsquares\n'%(len(seriessquares)))
		searchReport['bogged'] = 1
		return finalsquares,searchReport

	if linetouse > 5000:
		if len(seriessquares) < 3:
			for i in range(len(seriessquares)):
				print(seriessquares[i]['bestfstring'])
				# Removing line that plotted things. Original was: showseriessquare(seriessquares{i},kit);

	(seriessquares,bogged,census) = extendseriessquarealltheway(seriessquares,fs,hs)
	searchReport['census'] = census

	if bogged == 1:
		searchReport['bogged'] = 1
		return finalsquares,searchReport

	allps = extractfieldsfromcellarray(seriessquares,['netpval','testable']) # not sure of argument input format, check
	alltests = allps['testable']
	allps = allps['netpval']

	for i in range(len(seriessquares)):
		s = seriessquares[i]

		if s['testable'] == 1:
			numps = len(np.where(alltests == 1))
			if s['netpval'] == min(allps):
				print('adding %d squares from %3.1f of degree %d, pval %3.2e\n'%(numps,s['originalf1'],s['degree'],s['netpval']))
			finalsquares.append(s)

	finalsquares = sortcellarraybyfield(finalsquares,'netpval','ascend')
	if ts['trimends']:
		finalsquares = trimends(finalsquares)

	finalsquares = removeidentical(finalsquares)

	return finalsquares,searchReport


def removeidentical(slist):
	newlist = []
	for i in range(len(slist)):
		isindy = 1
		for j in range(len(newlist)):
			if identicalseries(slist[i],newlist[j]):
				isindy = 0

		if isindy:
			sortfs = np.sort(slist[i]['allfs'])
			if min(np.diff(sortfs)) > 0.01:
				newlist= np.append(newlist, slist[i])

	return newlist


def identicalseries(s1,s2):
	yesorno = 1

	if len(s1['fgrid'][:,0]) != len(s2['fgrid'][:,0]): # not sure of datatype of s['fgrid'], hopefully this works
		yesorno = 0

	return yesorno


def addtrialsquarestokit(kit,newsquares):
	if len(newsquares) > 0:
		newsquares = sortcellarraybyfield(newsquares,'netpval','ascend')
		numsquares = min(kit['tightnesssettings']['maxsquaresfromline'],np.size(newsquares))
		for i in range(numsquares):
			thissquare = newsquares[i]
			kit['candidateScaffolds']= np.append(kit['candidateScaffolds'], thissquare)

		kit['candidateScaffolds'] = sortScaffolds(kit['candidateScaffolds'])

	if len(kit['candidateScaffolds']) == 0:
		kit['bestScaffoldp'] = 1
	else:
		kit['bestScaffoldp'] = kit['candidateScaffolds'][0]['netpval']

	return kit


def sortScaffolds(candidateScaffolds):
	newScoffoldList = []
	hashesUsed = []
	candidateScaffolds = sortcellarraybyfield(candidateScaffolds,'netpval','ascend')

	for i in range(len(candidateScaffolds)):
		thisScaffold = candidateScaffolds[i]
		thisHash = thisScaffold['gridhash']
		thisHash= thisHash.item()
		if thisHash not in hashesUsed: # check this- this still needs to be checked july 27
			newScoffoldList= np.append(newScoffoldList, thisScaffold)
			hashesUsed.append(thisHash)

	return newScoffoldList


def addsquaresfromline(kit,linetouse):

	f1 = pickfirstf(kit,linetouse)
	(newsquares,searchreport) = squaresfromline(kit,linetouse)
	kit['searchedf1s']= np.append(kit['searchedf1s'], f1)
	print("woohoo")

	if searchreport['bogged'] == 0:
		kit = addtrialsquarestokit(kit,newsquares)
		kit['totalflatsquares'] += searchreport['numflatsquares']
		kit['totalCensus'] = kit['totalCensus'] + searchreport['census']

	return kit


output = addsquaresfromline(kit, linetouse)

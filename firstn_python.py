#status: rewritten (complete)
def firstn(cellarray, n):
	newarray=[]
	for i in np.arange(1, np.min(np.size(cellarray))):
		newarray.append(cellarray[i])
	return newarray
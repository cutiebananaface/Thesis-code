#status: rewritten (complete)
import numpy as np
import math
def showPairList(pairList=None, n=None):
	if pairList != None:
		n= math.inf
	n=min(np.size(pairList), n)
	for i in range(1,n):
		print(f"grid {i / np.size(pairList)}:==================\n{pairList[i]['fullstring']}\n")
		

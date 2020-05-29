import numpy as np
#status: rewritten (complete)
def predictJ(f1,f2):
	#predicts the lower j of an f1 type series
	jguess = f1 / (f2-f1);
    jguess = np.floor(jguess)-1;
	#code below added because RAARR crashes in at least 3 places when jguess = 0
    if jguess == 0:
        jguess = 1
    return jguess

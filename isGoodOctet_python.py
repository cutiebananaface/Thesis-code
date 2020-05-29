# Generated with SMOP  0.41
# from libsmop import *
# isGoodOctet.m
#status: rewritten(complete)
    

def isGoodOctet(octet=None,fit_params=None):

    score=0
# isGoodOctet.m:2
    if (not fit_params['containsOblate']) or (octet[1] > octet[4] and octet[5] > octet[8]):
        return score
    
    if (not fit_params['containsOblate']) or (octet[1] > octet[3] and octet[2] > octet[4]):
        return score
    
    r12=(octet(1) - octet(2)) / (octet(5) - octet(6))
# isGoodOctet.m:9
    if r12 < 0:
        return score
    
    r13=(octet[1] - octet[3]) / (octet[5] - octet[7])
# isGoodOctet.m:13
    r23=(octet[2] - octet[3]) / (octet[6] - octet[7])
# isGoodOctet.m:14
    r24=(octet[2] - octet[4]) / (octet[6] - octet[8])
# isGoodOctet.m:15
    r34=(octet[3] - octet[4]) / (octet[7] - octet[8])
# isGoodOctet.m:16
    ratio5=np.concatenate((r12,r13,r23,r24,r34))
# isGoodOctet.m:17
    percentmaxdiff=(max(ratio5) - min(ratio5)) / mean(ratio5)
# isGoodOctet.m:18
    h1=octet[1] + octet[5]
# isGoodOctet.m:19
    h4=octet[4] + octet[8]
# isGoodOctet.m:20
    percenth14diff=abs((h1 - h4) / mean(np.concatenate((h1,h4))))
# isGoodOctet.m:21
    leftsq=abs(octet[1] - octet[3] - octet[6] + octet[5])
# isGoodOctet.m:22
    rightsq=abs(octet[4] - octet[2] - octet[7] + octet[8])
# isGoodOctet.m:23
    prll1=abs(octet[1] - octet[3] - octet[8] + octet[7])
# isGoodOctet.m:24
    prll2=abs(octet[2] - octet[4] - octet[6] + octet[5])
# isGoodOctet.m:25
    ratiovar=max(abs(ratio5 - r12))
# isGoodOctet.m:26
    if abs(percentmaxdiff) < fit_params['percentmaxdiff']:
        score=score + 1
# isGoodOctet.m:28
    
    if abs(percenth14diff) < fit_params['percenth14diff']:
        score=score + 1
# isGoodOctet.m:31
    
    if leftsq < fit_params['leftsq']:
        score=score + 1
# isGoodOctet.m:34
    
    if rightsq < fit_params['rightsq']:
        score=score + 1
# isGoodOctet.m:37
    
    if prll1 < fit_params['prll1']:
        score=score + 1
# isGoodOctet.m:40
    
    if prll2 < fit_params['prll2']:
        score=score + 1
# isGoodOctet.m:43
    
    if ratiovar < fit_params['ratiovar']:
        score=score + 1
# isGoodOctet.m:46
    
    if score <= 5:
        if score == 5:
            1
        score=0
# isGoodOctet.m:52
    else:
        1
    
    return score
    

    
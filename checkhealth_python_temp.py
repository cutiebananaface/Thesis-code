import numpy as np
from updateseriessquare_python import tooclose
def checkhealth(s):
    healthy=1
# updateseriessquare.m:560
    numrows= np.size(s['fgrid'][:,1])
# updateseriessquare.m:561
    for i in np.arange(0,numrows - 1).reshape(-1):
        ivalue=s['fgrid'][i,1]
# updateseriessquare.m:563
        jvalue=s['fgrid'][i + 1,1]
# updateseriessquare.m:564
        if tooclose(s['fgrid'][i,1],s['fgrid'][i + 1,2],3.0):
            healthy=0
# updateseriessquare.m:567
        if tooclose(s['fgrid'][i,2],s['fgrid'][i + 1,1],3.0):
            healthy=0
# updateseriessquare.m:570
        if healthy == 0:
            1
    return healthy
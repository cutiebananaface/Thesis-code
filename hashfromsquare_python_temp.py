import numpy as np
def hashfromsquare(s):
    fgrid=s['usablefgrid']
    # updateseriessquare.m:474
    gridhash=0
    # updateseriessquare.m:475
    numrows=np.size(fgrid[:,1])
    # updateseriessquare.m:476
    for i in np.arange(0,numrows):
        thisrow=fgrid[i,:]
    # updateseriessquare.m:478
        if max(thisrow) > 0:
            firstentry=i+1
            break
    # updateseriessquare.m:480

    for i in np.arange(0,numrows):
        for j in np.arange(0,4):
                gridhash=gridhash + (fgrid[i,j]*((1 + (i+1) - firstentry) + (12345 * (j+1))))
    return gridhash
# updateseriessquare.m:486
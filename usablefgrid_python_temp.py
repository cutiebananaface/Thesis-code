import numpy as np
def usablefgrid(s):
   
    fatgrid=0
# updateseriessquare.m:445
    numrows= np.size(s['fgrid'][:,1])
# updateseriessquare.m:446
    numentries= np.size(s['allfs'])
# updateseriessquare.m:447
    if numentries <= s['tightnesssettings']['smallestscaffold']:
        shortfgrid=s['fgrid']
# updateseriessquare.m:449
        return shortfgrid
    
    # if numentries > 16
#     fatgrid = 1;
# end
    shortfgrid= np.dot(s['fgrid'],0)
# updateseriessquare.m:455
    numfilled=0
# updateseriessquare.m:456
    for i in np.arange(1,numrows).reshape(-1):
        thisrow=s['fgrid'][1,:]
# updateseriessquare.m:458
        if min(thisrow) > 0:
            #fullrows(i) = 1;
            if (fatgrid == 0):
                shortfgrid[i,:]=thisrow
# updateseriessquare.m:462
                numfilled=numfilled + 1
# updateseriessquare.m:463
            else:
                fatgrid=0
# updateseriessquare.m:465
            if numfilled >= s['tightnesssettings']['minrungs']:
                return shortfgrid
    return shortfgrid
import numpy as np
def flipmatrix(g):

    g2=np.dot(g,0)
# updateseriessquare.m:655
    g2[:,0]=g[:,3]
# updateseriessquare.m:656
    g2[:,1]=g[:,2]
# updateseriessquare.m:657
    g2[:,2]=g[:,1]
# updateseriessquare.m:658
    g2[:,3]=g[:,0]
    return g2
# updateseriessquare.m:659
import numpy as np
def addlinetolevels(levels,j,whichseries,f):

    level1i=j
# updateseriessquare.m:585
    level2i=j + 1
# updateseriessquare.m:586
    
    added=0
# updateseriessquare.m:587
    if 0 == whichseries:
        level1j=0
# updateseriessquare.m:590
        level2j=0
# updateseriessquare.m:591
    else:
        if 1 == whichseries:
            level1j=0
# updateseriessquare.m:593
            level2j=1
# updateseriessquare.m:594
        else:
            if 2 == whichseries:
                level1j=1
# updateseriessquare.m:596
                level2j=0
# updateseriessquare.m:597
            else:
                if 3 == whichseries:
                    level1j=1
# updateseriessquare.m:599
                    level2j=1
# updateseriessquare.m:600
    
    # known1 = levels['isknown(level1j,level1i);
# known2 = levels['isknown(level2j,level2i);
    e1=levels['energy'][level1i,level1j]
# updateseriessquare.m:604
    e2=levels['energy'][level2i,level2j]
# updateseriessquare.m:605
    if abs(f - 12016) < 1:
        1
    
    if ((e1 == 0) and (e2 == 0)) or ((e1 != 0) and (e2 != 0)):
        #cowcow theres something here.. this is overconstrained.
        return levels, added
     
    if (e1 != 0):
        newe2=e1 + f
# updateseriessquare.m:614
        if (e2 == 0):
            added=1
# updateseriessquare.m:616
            levels['energy'][level2i,level2j]=newe2
# updateseriessquare.m:617
    
    if (e2 != 0):
        newe1=e2 - f
# updateseriessquare.m:621
        if (e1 == 0):
            added=1
# updateseriessquare.m:623
            levels['energy'][level1i,level1j]=newe1
# updateseriessquare.m:624
    return levels, added
import numpy as np
from addlinetolevels_python_temp import addlinetolevels
def addlevels(s):

    #strings together transitions to find levels['  not particularly fast. by
#the end, levels['maxe and levels['mine should reflect the spread of
#calculated values[' overcontraints simply ignored - work it out later
#levels['isknown = zeros(s['numjs+1,2); #how many constr
    
    #also labels items in fgrid which are searchable or overconstrained.
#s['fstatus can be: 
#s['fstatus(i,j) == 0 # untouched
#s['fstatus(i,j) == 1 # known
#s['fstatus(i,j) == 2 # worth searching - connects to two. set flimits?
#maybe not
#s['fstates(i,j) == 3 # MUST search - overconstrained. s['flimits set tight
#fstatus = s['
    levels={}
    levels['energy'] = np.zeros((s['numjs'] + 1,2))
# updateseriessquare.m:504
    #levels['energy(2,1) = 1;
    if s['fgrid'][2,0] != 0:
        levels['energy'][2,0]=- 1
# updateseriessquare.m:507
    else:
        if s['fgrid'][2,3] != 0:
            levels['energy'][2,1]=- 1
# updateseriessquare.m:510
        else:
            raise Exception('grid is a blank-o')
    
    growing=1
# updateseriessquare.m:515
    while growing == 1:

        growing=0
# updateseriessquare.m:517
        for j in np.arange(0,s['numjs']).reshape(-1):
            for i in np.arange(0,4).reshape(-1):
                if s['fgrid'][j,i] != 0:
                    levels,added=addlinetolevels(levels,j,i,s['fgrid'][j,i])
# updateseriessquare.m:521
                    if added:
                        growing=1
# updateseriessquare.m:523

    
    minenergy=min(np.ndarray.flatten(levels['energy']))
# updateseriessquare.m:529
    newenergies=1e-08 + levels['energy'] - minenergy
# updateseriessquare.m:531
    
    for i in np.arange(0,s['numjs'] + 1).reshape(-1):
        for j in np.arange(0,2).reshape(-1):
            if levels['energy'][i,j] == 0:
                newenergies[i,j]=0
# updateseriessquare.m:535
    
    s['prolate'] = 0
# updateseriessquare.m:539
    s['oblate'] = 0
# updateseriessquare.m:540
    for i in np.arange(0,s['numjs'] + 1).reshape(-1):
        if (newenergies[i,0] != 0) and (newenergies[i,1] != 0):
            if (newenergies[i,0] < newenergies[i,1]):
                s['prolate'] = 1
# updateseriessquare.m:544
            else:
                s['oblate'] = 1
# updateseriessquare.m:546
    
    #     end
#     if (newenergies(i,1) ~= 0) && (newenergies(i,2) ~= 0) && (newenergies(i,1) < newenergies(i,2))
#         s['oblate = 1;
#     end
# end
    s['energies'] = newenergies
# updateseriessquare.m:555
    #strings together transitions to find the levels, which are nominally
#needed just for plotting, but also are a good thing to keep in mind.ab
    return s
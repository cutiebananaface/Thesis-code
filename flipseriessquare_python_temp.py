import numpy as np
from flipmatrix_python_temp import flipmatrix
from updateseriessquare_python_temp import updateseriessquare
def flipseriessquare(s):
    s2=s
# updateseriessquare.m:629
    s2['column1'] = s['column4']
# updateseriessquare.m:630
    s2['column2'] = s['column3']
# updateseriessquare.m:631
    s2['column3'] = s['column2']
# updateseriessquare.m:632
    s2['column4'] = s['column1']
# updateseriessquare.m:633
    s2['column1']['whichcolumn'] = 1
# updateseriessquare.m:634
    s2['column2']['whichcolumn'] = 2
# updateseriessquare.m:635
    s2['column3']['whichcolumn'] = 3
# updateseriessquare.m:636
    s2['column4']['whichcolumn'] = 4
# updateseriessquare.m:637
    s2['flipped'] = s['flipped'] + 1
# updateseriessquare.m:639
    s2['fgrid'] = flipmatrix(s['fgrid'])
# updateseriessquare.m:640
    s2['originalfgrid'] = flipmatrix(s['originalfgrid'])
# updateseriessquare.m:641
    s2['alineorder'] = flipmatrix(s['alineorder'])
# updateseriessquare.m:642
    s2['lineorder'] = flipmatrix(s['lineorder'])
# updateseriessquare.m:643
    s2['allerrors'] = flipmatrix(s['allerrors'])
# updateseriessquare.m:644
    if s['flattype'] == '/':
        s2['flattype'] = '\\'
# updateseriessquare.m:646
    
    if s['flattype'] == '\\':
        s2['flattype'] = '/'
# updateseriessquare.m:649
    
    #s2 = rmfield(s2,'lineorder');
    s2=updateseriessquare(s2)
    return s2
# updateseriessquare.m:652
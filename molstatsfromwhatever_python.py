def molstatsfromwhatever(molname):

    if type(molname) is dict:
        thismol = molname
        return thismol
    if type(molname) is str:
        thismol = loadmol(molname);
        thismol['molname'] =  print ('%s [%3.1f %3.1f %3.1f]'% (molname,thismol['a'],thismol['b'],thismol['c']))
        return thismol
    thismol = loadmol('menthone1');
    thismol['a'] = molname[1]
    thismol['b'] = molname[2]
    thismol['c'] = molname[3]
    thismol['fakemolname'] = print ('fiction [%3.1f %3.1f %3.1f]'% (molname[1],molname[2],molname[3]))
        
    if (size(molname) >= 8) and (molname[4] ~= 0):
        thismol['fakemolname'] = print ('fiction [%3.1f %3.1f %3.1f] CD'% (molname[1],molname[2],molname[3]))
        thismol['DJ'] = molname[4]
        thismol['DJK'] = molname[5]
        thismol['DK'] = molname[6]
        thismol['deltaJ'] = molname[7]
        thismol['deltaK'] = molname[8]
    thismol['molname'] = thismol['fakemolname']
    1
    return thismol




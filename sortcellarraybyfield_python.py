# Generated with SMOP  0.41
# from libsmop import *
# sortcellarraybyfield.m
import numpy as np

 
def sortcellarraybyfield(database,fieldname,upordown="ascend"):

    if upordown == "ascend":
        upordown= 1 #'ascend'
# sortcellarraybyfield.m:3
    if upordown=='descend':
        upordown= -1
    
    if (upordown != 1) and (upordown != -1):
        raise Exception('have to ascend or descend')
    
    output=[]
# sortcellarraybyfield.m:8
    fields=np.zeros((1, np.size(database, axis=None)))
# sortcellarraybyfield.m:9
    for i in range(0, np.size(database,axis=None)):
        fields[0][i]= database[i][fieldname]
# sortcellarraybyfield.m:11
    
    sorted1 = np.sort(fields)[::upordown]
    Xi= np.argsort(fields)[::upordown]
# sortcellarraybyfield.m:14
    output= []
    for i in range(0,np.size(database, axis=None)):
        output.append(database[Xi[0][i]])
        # try:
        #     output.insert(i,database[XI][0][i])
        # # except:
        # #     print(i)
    
    return output
# sortcellarraybyfield.m:16
    
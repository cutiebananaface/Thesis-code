# Generated with SMOP  0.41
# from libsmop import *
# extractfieldsfromcellarray.m
# import numpy as np
#status: rewritten (complete but needs alot of debugging)
import numpy as np
from loadmatlab_workspace import load_mat

# before= load_mat('input-extractsfieldsfromcellarray')
# database= before['database']
# fieldname = before['fieldname']
def extractfieldsfromcellarray(database,fieldname):
    output={}
    for i in fieldname:
        output.update({i: []})
    
    for i in range(0,np.size(database)):
        for j in output:
            output[j].append(database[i][j])
    return output

# output=extractfieldsfromcellarray(database,fieldname)
# print('wowowowowo')

#     output={}
#     if type(database) is str:
#         #using fromfile() from numpy, but load() from matplotlib can also be used
#         b=np.fromfile(database)
# # extractfieldsfromcellarray.m:4
#         name=np.array(b.keys()) #i am a bit iffy about this port
# # extractfieldsfromcellarray.m:5
#         database=b[name][0]
# # extractfieldsfromcellarray.m:6
    
#     if not (np.size(database) >= 1):
#         output={}
# # extractfieldsfromcellarray.m:10
#         for i in np.arange(1,np.size(fieldname)).reshape(-1):
#             output[fieldname[i]]=np.array([])  #initializing the placement of each field in output
# # extractfieldsfromcellarray.m:12
#     else:
#         if type(fieldname) is str:
#             if 'all' in fieldname:
#                 fieldname=database[0].keys()
# # extractfieldsfromcellarray.m:17
#                 fieldname=np.transpose(fieldname)
# # extractfieldsfromcellarray.m:18
#             else:
#                 raise Exception('Enter a different specification string or a cell array of fieldnames')
#         cellmarker=np.array([])
# # extractfieldsfromcellarray.m:24
#         for i in np.arange(0,np.size(fieldname)).reshape(-1):
#             thisfieldname=fieldname[i]
# # extractfieldsfromcellarray.m:26
#             if not (thisfieldname in database[0]):
#                 raise Exception(print(f"{thisfieldname} field not found"))
#             else:
#                 if (type(database[1][thisfieldname]) is str) or (type(database[1][thisfieldname]) is dict) or (type(database[1][thisfieldname]) is list):
#                     output[thisfieldname]=[]#not sure if this item already exists in output
# # extractfieldsfromcellarray.m:31
#                     cellmarker=np.append(cellmarker,1)
# # extractfieldsfromcellarray.m:32
#                 else:
#                     output[thisfieldname]=np.array([])
# # extractfieldsfromcellarray.m:34
#                     cellmarker=np.append(cellmarker,0)
# # extractfieldsfromcellarray.m:35
#         for i in np.arange(0,np.size(database)).reshape(-1):
#             for j in np.arange(0,np.size(cellmarker)).reshape(-1):
#                 thisfield=fieldname[j]
# # extractfieldsfromcellarray.m:44
#                 if cellmarker[j]:
#                     if thisfield in database[1]:
#                         # output.update({thisfield:database[i][thisfield]})
#                         output[thisfield]=np.append(output[thisfield],database[i][thisfield])
# # extractfieldsfromcellarray.m:47
#                     else:
#                         # output.update({thisfield:'NA'})
#                         output[thisfield]=np.append(output[thisfield],database[i][thisfield])
# # extractfieldsfromcellarray.m:49
#                 else:
#                     if thisfield in database[i]:
#                         # output.update({thisfield:database[i][thisfield]}) #not sure about this line
#                         output[thisfield]=np.append(output[thisfield],database[i][thisfield])
# # extractfieldsfromcellarray.m:53
#                     else:
#                         # output.update({thisfield:-1}) #may want to use np.insert
#                         output[thisfield]=np.append(output[thisfield],-1)
# # extractfieldsfromcellarray.m:55
    # return output
    
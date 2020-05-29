from loadmatlab_workspace import load_mat
import copy
import numpy as np
from pickfirstf_python import pickfirstf
before= load_mat('nopinone-kit')
kit=before['kit']
fs_original = kit['onedpeakfsunassigned']
hs_original = kit['onedpeakhsunassigned']
fs= copy.copy(fs_original)
hs= copy.copy(hs_original)
fstart, hstart, istart, rank = pickfirstf(kit,1)

fs = fs[np.where(hs > 12.8685)] #within this treshold
hs = hs[np.where(hs > 12.8685)]
print("wow")


# database= before['database']
# fieldname = before['fieldname']
# # database=[]
# # dict1= {'a' :'k', 'netpval': 2, 'dog':'woof'}
# # dict2= {'a' :'c', 'netpval': 1, 'dog':'bork'}
# # dict3= {'a' :'b', 'netpval': 5, 'dog':'bark'}
# # database.append(dict1)
# # database.append(dict2)
# # database.append(dict3)
# output={}
# for i in fieldname:
#    output.update({i: []})
# # dog_sounds= []
# # letters=[]
# # netpval= []
# # for i in range(0,len(database)):
# #     print(database[i]['dog'])
# #     dog_sounds.append(database[i]['dog'])
# #     letters.append(database[i]['a'])
# #     netpval.append(database[i]['netpval'])
# for i in range(0,np.size(database)):
#     for j in output:
#         output[j].append(database[i][j])

# print('wow!')

import numpy as np
from loadmatlab_workspace import load_mat
# before= load_mat('makecounttool-workspace-before')
# after= load_mat('makecounttool-workspace-end')
# hs=before['hs']
# hs1=after['hs']
def makecounttool(hs):
    '''
    Tool for counting the elements in counttool
    
    '''
    hs1= np.sort(hs)[::-1] #sort hs into descending order
    counttool1={} #initalize the counttool dict
    counttool1['minh'] = min(hs1) #add the minimum of hs1
    counttool1['maxh'] = max(hs1) #add the maximum of hs1
    counttool1['hvalues'] = np.linspace(counttool1['minh'],counttool1['maxh'],50) #create an evenly spaced vector from minh to maxh of 50 values
    counttool1['countvalues'] = counttool1['hvalues'] * 0 #initialize an key in counttool that is an array the size of hvalues and fill it with zeros
    
    #for this part it is important to remember that python indices start at 0 and matlab indices start at 1
    countvalues_list=[] #initialize the a list called countvalues_list
    for x in np.nditer(counttool1['hvalues']): #a for loop special to np. Iterate through counttool1['hvalues']
        #if counttool['hvalues'] was a dict and not a np.array then x=counttool['hvalues'].items(i)
        a_temp=np.array((hs1>=x).nonzero()) #find the indices of the nonzero elements where hs>=x and make an array, a_temp, from that
        countvalues_list.append(a_temp[0,-1]) #append to the list the last element of the np.array, a_temp
    
    counttool1['countvalues']=np.asarray(countvalues_list) #after the for loop is done, turn the countvalues_list into an array and append to counttool1
    return counttool1
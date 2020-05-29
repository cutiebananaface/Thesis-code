# Generated with SMOP  0.41
# from libsmop import *
# sortstructcellarraybyfield.m

    

def sortstructcellarraybyfield(cellarray=None,fieldname=None,*args,**kwargs):

    if size(cellarray) == 0:
        sortedcellarray=[]
# sortstructcellarraybyfield.m:3
        return sortedcellarray
    
    to_sort=array([])
# sortstructcellarraybyfield.m:6
    for i in arange(1,size(cellarray)).reshape(-1):
        to_sort[i]=getfield(cellarray[i],fieldname)
# sortstructcellarraybyfield.m:9
    
    sorted,indices=sort(to_sort), argsort(to_sort)
# sortstructcellarraybyfield.m:12
    sortedcellarray=array([indices])
# sortstructcellarraybyfield.m:13
    if size(sortedcellarray) !=0:
        if 'source' in sortedcellarray[1]:
            for i in arange(1,size(sortedcellarray)).reshape(-1):
                sortedcellarray[i]['databaseID'] = copy(i)
# sortstructcellarraybyfield.m:18
    return sortedcellarray
    
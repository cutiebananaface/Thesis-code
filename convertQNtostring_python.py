# Generated with SMOP  0.41
# from libsmop import *
# convertQNtostring.m
from numpy import *

def convertQNtostring(QN=None,*args,**kwargs):

    # converts a quantum number in int format to a string ready for SPFIT/SPCAT
    
    QN_string=[]
# convertQNtostring.m:4
    for i in arange(1,size(QN)).reshape(-1):
        if QN[i] >= 100:
            QN_string[i]=str(QN[i])
# convertQNtostring.m:8
        else:
            if QN[i] >= 10:
                QN_string[i]=array([' ',str(QN[i])])
# convertQNtostring.m:10
            else:
                QN_string[i]=array(['  ',str(QN[i])])
# convertQNtostring.m:12
    
    if size(QN_string) == 1:
        QN_string=QN_string[1]
# convertQNtostring.m:17
    
    return QN_string

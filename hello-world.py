import numpy as np
import pandas as pd
from doctest import testmod 

def hellow_fx(arr):
    '''
    This function writes hello world
    Input and output:
    >>> hellow_fx(np.array(['hello', 'world']))
    2
    '''
    # arr = np.array(['hello', 'world'])
    series = pd.Series(arr)
    # print(series)
    # a=np.size(arr)
    return np.size(arr)

if __name__ == '__main__': 
    testmod(name ='hellow_fx', verbose = True) 
# def adding(a,b):
#     '''
#     adding
#     >>> adding(2,3)
#     5
#     '''
#     return a+b

# if __name__ == '__main__': 
#     testmod(name ='adding', verbose = True) 
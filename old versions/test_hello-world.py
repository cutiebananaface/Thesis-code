import numpy as np
import pandas as pd
from doctest import testmod 

# def helloworld(arr):
#     # '''
#     # This function writes hello world
#     # Input and output:
#     # >>> hellow_fx(np.array(['hello', 'world']))
#     # 2
#     # '''
#     # arr = np.array(['hello', 'world'])
#     # series = pd.Series(arr)
#     # print(series)
#     # a=np.size(arr)

#     arr['red']='apples'
#     other= {'orange': 'oranges', 'yellow': 'banana'}
#     arr.update(other)
#     arr['other']=other
#     return arr, arr['red']

# # fruit={}
# # output=helloworld(fruit)
# # print(output)

# def test_answer():
#     fruit={}
#     output={}
#     output['red']='apples'
#     other= {'orange': 'oranges', 'yellow': 'banana'}
#     output.update(other)
#     output['other']=other
#     assert helloworld(fruit) == output, output['red']

# # if __name__ == '__main__': 
# #     testmod(name ='hellow_fx', verbose = True) 

def adding(a,b):
    '''
    adding
    >>> adding(2,3)
    5
    '''
    return a+b

if __name__ == '__main__': 
    testmod(name ='adding', verbose = True) 
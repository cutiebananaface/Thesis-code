# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:39:01 2020

@author: rodri
"""
import numpy as np
import operator as op

def mylength(v, axis1=None):
    length= np.size(v, axis=None)
    if type(v) is dict:
        length=len(v)
    return length

def findnonzeros(v, comparing_val=0, operator_fx= op.gt , options= 'all'): # for finding elements 
    """ v= array, comparing val= the value you want to compare the array to, operator_fx= function from the operator module 
    options= all (returns the indices, nonzero elements, the first nonzero index and last nonzero index), indices (returns nonzero indices)
    nonzero_elements (returns the nonzero elements of the array), firsti (returns the first nonzero index), lasti (returns the last nonzero index) """
    # this assumes you have an array with only one column
    # v is your numpy array
    #first we will find all of the indices of nonzero elements
    v_indices= np.array([(operator_fx(v, comparing_val)).nonzero()])
    #next we will extract the elements of v which are nonzero
    v_nonzero_elements= v[(v>comparing_val).nonzero()] ###BAd i left in a hardcoded thing
    # now we will use v_indices to find the first index of a nonzero element
    v_firsti= v_indices[0,0]
    # and now the last index
    v_lasti= v_indices[0,-1]
    if options == 'all':
        return v_indices, v_nonzero_elements, v_firsti, v_lasti
    
    elif options== 'indices':
        return v_indices
    
    elif options== 'nonzero_elements':
        return v_nonzero_elements
    
    elif options== 'firsti':
        return v_firsti
    
    elif options == 'lasti':
        return v_lasti
        
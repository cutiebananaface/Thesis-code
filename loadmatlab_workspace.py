# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:29:46 2020

@author: rodri
"""
# import numpy
# import scipy.io as spio

# #the following functions are from https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries
# #they are used for loading matlab structures as dicts!
# def loadmat(filename):
#     '''
#     this function should be called instead of direct spio.loadmat
#     as it cures the problem of not properly recovering python dictionaries
#     from mat files. It calls the function check keys to cure all entries
#     which are still mat-objects
#     '''
#     data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True, mat_dtype=True)
#     return _check_keys(data)

# def _check_keys(dict):
#     '''
#     checks if entries in dictionary are mat-objects. If yes
#     todict is called to change them to nested dictionaries
#     '''
#     for key in dict:
#         if isinstance(dict[key], spio.matlab.mio5_params.mat_struct):
#             dict[key] = _todict(dict[key])
#     return dict   

# def _todict(matobj):
#     '''
#     A recursive function which constructs from matobjects nested dictionaries
#     '''
#     dict = {}
#     for strg in matobj._fieldnames:
#         elem = matobj.__dict__[strg]
#         if isinstance(elem, spio.matlab.mio5_params.mat_struct):
#             dict[strg] = _todict(elem)
#         else:
#             dict[strg] = elem
#     return dict

# import scipy
# import numpy as np
# import scipy.io as spio


# def loadmat(filename):
#     '''
    # https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries
#     this function should be called instead of direct spio.loadmat
#     as it cures the problem of not properly recovering python dictionaries
#     from mat files. It calls the function check keys to cure all entries
#     which are still mat-objects
#     '''
#     def _check_keys(d):
#         '''
#         checks if entries in dictionary are mat-objects. If yes
#         todict is called to change them to nested dictionaries
#         '''
#         for key in d:
#             if isinstance(d[key], spio.matlab.mio5_params.mat_struct):
#                 d[key] = _todict(d[key])
#         return d

#     def _has_struct(elem):
#         """Determine if elem is an array and if any array item is a struct"""
#         return isinstance(elem, np.ndarray) and any(isinstance(
#                     e, scipy.io.matlab.mio5_params.mat_struct) for e in elem)

#     def _todict(matobj):
#         '''
#         A recursive function which constructs from matobjects nested dictionaries
#         '''
#         d = {}
#         for strg in matobj._fieldnames:
#             elem = matobj.__dict__[strg]
#             if isinstance(elem, spio.matlab.mio5_params.mat_struct):
#                 d[strg] = _todict(elem)
#             elif _has_struct(elem):
#                 d[strg] = _tolist(elem)
#             else:
#                 d[strg] = elem
#         return d

#     def _tolist(ndarray):
#         '''
#         A recursive function which constructs lists from cellarrays
#         (which are loaded as numpy ndarrays), recursing into the elements
#         if they contain matobjects.
#         '''
#         elem_list = []
#         for sub_elem in ndarray:
#             if isinstance(sub_elem, spio.matlab.mio5_params.mat_struct):
#                 elem_list.append(_todict(sub_elem))
#             elif _has_struct(sub_elem):
#                 elem_list.append(_tolist(sub_elem))
#             else:
#                 elem_list.append(sub_elem)
#         return elem_list
#     data = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True, mat_dtype=True)
#     return _check_keys(data)

from scipy.io import loadmat, matlab
import numpy as np
def load_mat(filename):
    """
    https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries
    This function should be called instead of direct scipy.io.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    """

    def _check_vars(d):
        """
        Checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        """
        for key in d:
            if isinstance(d[key], matlab.mio5_params.mat_struct):
                d[key] = _todict(d[key])
            elif isinstance(d[key], np.ndarray):
                d[key] = _toarray(d[key])
        return d

    def _todict(matobj):
        """
        A recursive function which constructs from matobjects nested dictionaries
        """
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, matlab.mio5_params.mat_struct):
                d[strg] = _todict(elem)
            elif isinstance(elem, np.ndarray):
                d[strg] = _toarray(elem)
            else:
                d[strg] = elem
        return d

    def _toarray(ndarray):
        """
        A recursive function which constructs ndarray from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        """
        if ndarray.dtype != 'float64':
            elem_list = []
            for sub_elem in ndarray:
                if isinstance(sub_elem, matlab.mio5_params.mat_struct):
                    elem_list.append(_todict(sub_elem))
                elif isinstance(sub_elem, np.ndarray):
                    elem_list.append(_toarray(sub_elem))
                else:
                    elem_list.append(sub_elem)
            return np.array(elem_list)
        else:
            return ndarray

    data = loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_vars(data)

# before= load_mat('makecounttool-workspace-before')
# fs= before['fs']
# hs= before['hs']
# squarelist= before['squarelist']

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:00:30 2020

@author: rodri
"""

import numpy as np
from makecounttool_python import makecounttool
from pickfirstf_python import pickfirstf
from settingsfromtightness_python import settingsfromtightness
from loadmatlab_workspace import loadmat
from updateseries_python import updateseries


before=loadmat('updateseries_before')
after=loadmat('s-column1-updateseries-after')
s=before['s']

#kit=before['kit']
#linetouse=before['linetouse']
#ts=before['ts']
#s_col1=updateseries(s)

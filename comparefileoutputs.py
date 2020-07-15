# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:50:30 2020

@author: rodri
"""
# from comparefileoutputs import unpackingstruct
from datetime import datetime

def checkkeys(generaldict1, generaldict2): #alt: make a list of the key values which are the same
    #checks if keys in the dictionary are the same
    missingkeys=[]
    for x in generaldict1.keys():
        if x not in generaldict2.keys(): 
            missingkeys.append(x)
            
    return missingkeys

def unpack(generaldict1, generaldict2,nameoffile):
    missingkeys= checkkeys(generaldict1, generaldict2)
    with open(nameoffile, 'a') as f:
        print(f"these keys are missing from generaldict2 {missingkeys}", file=f)
        
    for key, val in generaldict1.items():
        if key not in missingkeys:
            if type(generaldict1[key]) is dict:
                with open(nameoffile, 'a') as f:
                        print(f"generaldict[{key}] is a dict, unpack further \n", file=f)
                unpack(generaldict1[key], generaldict2[key], nameoffile)
                
            else:
                with open(nameoffile, 'a') as f:
                    print(f" generaldict[{key}],\n {generaldict1[key]} and {generaldict2[key]},\n {generaldict1[key] == generaldict2[key]} \n", file=f) # i think i could just print the val but whatever

def unpackingstruct(struct, struct2, nameoffile):
    # now = datetime.now() #time to include in the file
    with open(nameoffile, 'a') as f: #during a newrun, add a new line with the date and time
        print(f"----~newrun: date/time={datetime.now()} ~-----~newrun~-----~newrun~-----~newrun~----\n", file=f)
    #block for actually unpacking and comparing elements    
    
    for ind, j in enumerate(struct): #unpacking the list, ind is the index, j is the val
        missingkeys=checkkeys(struct[ind], struct2[ind]) #check for missing keys in the two structs
        with open(nameoffile, 'a') as f:
            print(f"these keys are missing from struct2[{ind}] {missingkeys}", file=f) #print missingkeys to file
        
        for x, y in j.items(): #iterates through j (a dict), x is the key and y is the val
            if x not in missingkeys: #dont run this block unless the key actually exists
                if type(j[x]) is dict:
                    with open(nameoffile, 'a') as f:
                        print(f"struct[{ind}][{x}] is a dict, unpack further \n", file=f)
                    unpack(struct[ind][x], struct2[ind][x], nameoffile)
                    
                else:
                # elif (struct[ind][x] != struct2[ind][x]).all():
                    with open(nameoffile, 'a') as f:
                        print(f"struct[{ind}][{x}], \n {struct[ind][x]} and {struct2[ind][x]},\n {struct[ind][x]==struct2[ind][x]} \n", file=f)

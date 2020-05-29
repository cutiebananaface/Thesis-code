def extractonefieldfromcellarray(cellarray,fieldname):
	#so i dont think these will be neccessary in python? because of how dictionaries are set up
    f = extractfieldsfromcellarray(cellarray,[fieldname]);
    f=f[fieldname];
    return f
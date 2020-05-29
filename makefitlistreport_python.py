# status: rewritten(complete)
def makefitlistreport(kit):
s = print(f'{kit['molename']}: {kit['numspecies']} components found\n')
for i in range(1,np.size(kit['fitlist'])):
    thisfit = kit['fitlist'][i]
    s = print(f'{s} component {i}: {thisfit['fitdescriptor']}\n')
	return s

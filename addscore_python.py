from numpy import *
def addscore(thisFit, scoretype):
	if scoretype='pval':
		thisFit['fitScore']=thisFit[pval]**(-1)
	elif scoretype= 'pvaledge'
	 	thisFit['fitScore'] = thisFit['pval']**(-1)  * 2**size(thisFit['lines']);
    elif scoretype='pvaledgeJ':
        Jvals = extractonefieldfromcellarray(thisFit['lines'],'Jupper');
    	stdJ = std(Jvals);
        thisFit['fitScore'] = thisFit['pval']**(-1)  * 2**size(thisFit['lines']) * 10**stdJ * 10^thisFit['numtypes'];
    elif scoretype= 'broadpval';
        thisFit.fitScore = thisFit.pval^(-0.5) * 10^length(thisFit.lines);
  
    thisFit['scoretype'] = scoretype;
    thisFit['scorefitdescriptor'] = print('p = %3.1e, score %s = %3.1e, %d lines, %d hits' % (thisFit['pval'],scoretype,thisFit['fitScore'],size(thisFit['lines']),thisFit['yesvotes']));
    return thisFit

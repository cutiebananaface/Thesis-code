# Generated with SMOP  0.41
# from libsmop import *
# improvefit.m
#status: rewritten (complete)
import numpy as np 
import copy

def improvefit(fit=None,kit=None):

    #    broadfit = addDerivatives(broadfit);
#     broadfit = addHeights(broadfit,kit);
    if kit['tightnesssettings']['evolveFit'] == 1:
        print('Evolving fit and CD\\n')
        fit=evolveFit(fit,kit,'pvaledge',np.concatenate((10,5)))
# improvefit.m:6
        1
        print(f"\\n==HiFi fit {fit['scorefitdescriptor']} {fit['scorefitdescriptor']}====\\n",) 
        fit=evolveFit(fit,kit,'broadpval',np.concatenate((8,4)))
# improvefit.m:9
        print(f"\\n+++DeepFi fit {fit['scorefitdescriptor']}+++n")
    
    #newfit = addtemptofit(fit,kit);
    if kit['tightnesssettings']['addisotopes'] == 1:
        newfit=addC13s(fit,kit)
# improvefit.m:14
        newfit['quality'] = copy.copy(newfit['yesvotes'])
# improvefit.m:15
        newfit['longdescription'] = copy.copy(print(f"FIT: {newfit['shortdescriptor']} {np.size(newfit['isotopes'])} C13s"))
# improvefit.m:16
    else:
        newfit=copy.copy(fit)
# improvefit.m:18
        newfit['quality'] = copy.copy(newfit.yesvotes)
# improvefit.m:19
        newfit['longdescription'] = copy.copy(print(f"FIT: {newfit['shortdescriptor']}"))
# improvefit.m:20
    return newfit

    
    
    
    
# Generated with SMOP  0.41
from libsmop import *
# settingsfromtightness.m

    
@function
def settingsfromtightness(t=None,*args,**kwargs):
    varargin = settingsfromtightness.varargin
    nargin = settingsfromtightness.nargin

    #tightnesssettings contains all thresholds.  some are fixed, some vary with
#tightness. high tightness is TOLERANT
    
    #first settings which are common to methods
#ts has various components: variant settings, spfit settings
    
    ts.scalartightness = copy(t)
# settingsfromtightness.m:8
    ts.f3f1thresh = copy(dot(4000,(t)))
# settingsfromtightness.m:9
    ts.flatsquareheightratio = copy(dot(12,t))
# settingsfromtightness.m:11
    ts.firstcutheightratio = copy(dot(12,t))
# settingsfromtightness.m:12
    ts.mindegree = copy(2)
# settingsfromtightness.m:14
    # patternfitting.maxcomponents = 1;
# patternfitting.maxpatterns = 20;
# patternfitting.maxka = 1;
# ts.patternfitting = patternfitting;
# 
# ts.maxcomponents = 1;
# ts.maxpatterns = 20;
# ts.maxka = 1;
    
    ts.highsidetolerance = copy(dot(dot(t,0.5),concat([50,50,10])))
# settingsfromtightness.m:25
    
    ts.lowsidetolerance = copy(dot(t,concat([300,70,25])))
# settingsfromtightness.m:26
    ts.lowjthresh = copy(7)
# settingsfromtightness.m:27
    #ts.btolerance =   0 * t *  [300 90 40 20 4 2 2 2];
    
    ts.aatolerance = copy(dot(t,800))
# settingsfromtightness.m:33
    
    ts.abtolerance = copy(dot(t,4000))
# settingsfromtightness.m:34
    ts.ladderSearchtimes = copy(cellarray([concat([5,1e-40]),concat([20,1e-40]),concat([100,1e-40]),concat([500,1e-08]),concat([4000,100])]))
# settingsfromtightness.m:37
    
    ts.seriesaratio = copy(15)
# settingsfromtightness.m:38
    ts.seriesbratio = copy(15)
# settingsfromtightness.m:39
    ts.gapmax = copy(4000)
# settingsfromtightness.m:40
    
    ts.gapmin = copy(400)
# settingsfromtightness.m:41
    ts.minlines = copy(600)
# settingsfromtightness.m:42
    
    ts.flatsquarefthresh = copy(0.05)
# settingsfromtightness.m:43
    ts.seriessquarefthresh = copy(0.05)
# settingsfromtightness.m:44
    ts.flatsquarelimit = copy(6000)
# settingsfromtightness.m:45
    ts.minpval = copy(1e-06)
# settingsfromtightness.m:46
    ts.checkablepval = copy(1e-08)
# settingsfromtightness.m:47
    #ts.numABCs = 3;
    
    ts.smallestscaffold = copy(12)
# settingsfromtightness.m:51
    
    ts.minrungs = copy(3)
# settingsfromtightness.m:52
    
    ts.numjguess = copy(3)
# settingsfromtightness.m:53
    if t >= 1:
        ts.checkablepval = copy(1e-08)
# settingsfromtightness.m:55
    
    if t >= 2:
        ts.checkablepval = copy(1e-05)
# settingsfromtightness.m:58
    
    ts.maxka = copy(2)
# settingsfromtightness.m:60
    ts.okhitvotecount = copy(10)
# settingsfromtightness.m:61
    ts.maxscaffolds = copy(80)
# settingsfromtightness.m:62
    
    ts.evolveFit = copy(0)
# settingsfromtightness.m:63
    ts.addisotopes = copy(0)
# settingsfromtightness.m:64
    ts.foundfitvotecount = copy(20)
# settingsfromtightness.m:65
    ts.greathitvotecount = copy(80)
# settingsfromtightness.m:66
    ts.maxsquaresfromline = copy(3)
# settingsfromtightness.m:67
    #ts.totaltime = totaltime;
    ts.trimends = copy(0)
# settingsfromtightness.m:69
    
    #ts.lines = [1:40]; #[1:40];
    ts.lines = copy(concat([arange(1,50)]))
# settingsfromtightness.m:72
    if t > 1:
        ts.lines = copy(concat([arange(1,60)]))
# settingsfromtightness.m:74
    
    if t > 2:
        ts.lines = copy(concat([arange(1,80)]))
# settingsfromtightness.m:77
    
    ##
    isotopefitting.heightratiomax = copy(250)
# settingsfromtightness.m:80
    isotopefitting.freqmin = copy(0.98)
# settingsfromtightness.m:81
    isotopefitting.freqmax = copy(1.01)
# settingsfromtightness.m:82
    isotopefitting.numtargetmax = copy(15)
# settingsfromtightness.m:83
    isotopefitting.targetminheight = copy(100)
# settingsfromtightness.m:84
    isotopefitting.freqpixel = copy(0.1)
# settingsfromtightness.m:85
    isotopefitting.minSNR = copy(200)
# settingsfromtightness.m:86
    isotopefitting.c13pval = copy(1e-10)
# settingsfromtightness.m:87
    isotopefitting.numtrials = copy(100)
# settingsfromtightness.m:88
    isotopefitting.maxspecies = copy(1)
# settingsfromtightness.m:89
    
    isotopefitting.fdriftmax = copy(0.05)
# settingsfromtightness.m:90
    isotopefitting.targetoccupancy = copy(0.05)
# settingsfromtightness.m:91
    isotopefitting.maxmisses = copy(125)
# settingsfromtightness.m:92
    isotopefitting.dicerolls = copy(4)
# settingsfromtightness.m:93
    
    isotopefitting.spurratiomin = copy(0.001)
# settingsfromtightness.m:94
    ts.isotopefitting = copy(isotopefitting)
# settingsfromtightness.m:95
    patternfitting.numABCs = copy(3)
# settingsfromtightness.m:97
    patternfitting.maxcomponents = copy(1)
# settingsfromtightness.m:98
    patternfitting.maxpatterns = copy(20)
# settingsfromtightness.m:99
    patternfitting.actypes = copy(concat([0]))
# settingsfromtightness.m:100
    
    #patternfitting.actypes = [1];  #try just ac
    patternfitting.maxka = copy(2)
# settingsfromtightness.m:102
    patternfitting.numjguess = copy(3)
# settingsfromtightness.m:103
    ts.patternfitting = copy(patternfitting)
# settingsfromtightness.m:104
    ## block for bruteforce
    bruteforce.numtheorylines = copy(50)
# settingsfromtightness.m:106
    bruteforce.numexperimentlines = copy(500)
# settingsfromtightness.m:107
    bruteforce.heightratiomax = copy(500)
# settingsfromtightness.m:108
    # bruteforce.freqmin = .98;
# bruteforce.freqmax = 1.01;
    bruteforce.numtargetmax = copy(15)
# settingsfromtightness.m:111
    bruteforce.targetminheight = copy(0)
# settingsfromtightness.m:112
    bruteforce.freqpixel = copy(2.0)
# settingsfromtightness.m:113
    bruteforce.minSNR = copy(1)
# settingsfromtightness.m:114
    bruteforce.c13pval = copy(1e-10)
# settingsfromtightness.m:115
    bruteforce.numtrials = copy(3)
# settingsfromtightness.m:116
    bruteforce.maxspecies = copy(1)
# settingsfromtightness.m:117
    bruteforce.fdriftmax = copy(0.05)
# settingsfromtightness.m:118
    bruteforce.targetoccupancy = copy(0.05)
# settingsfromtightness.m:119
    bruteforce.spurratiomin = copy(0.05)
# settingsfromtightness.m:120
    
    bruteforce.maxmisses = copy(125)
# settingsfromtightness.m:121
    bruteforce.dicerolls = copy(4)
# settingsfromtightness.m:122
    
    ts.bruteforce = copy(bruteforce)
# settingsfromtightness.m:123
    ##
    variant3.babytolerance = copy(5)
# settingsfromtightness.m:126
    
    variant3.atolerance = copy(30)
# settingsfromtightness.m:127
    
    variant3.babyatolerance = copy(10)
# settingsfromtightness.m:128
    
    variant3.meantolerance = copy(20)
# settingsfromtightness.m:129
    
    variant3.fancytolerance = copy(0.5)
# settingsfromtightness.m:130
    
    variant3.fancytolerancef1lowJ = copy(5)
# settingsfromtightness.m:131
    variant3.fancytolerancef0 = copy(0.5)
# settingsfromtightness.m:133
    
    variant3.fancytolerancef0first = copy(10)
# settingsfromtightness.m:134
    
    variant3.fancytolerancef0lowJ = copy(10)
# settingsfromtightness.m:135
    
    variant3.f1tof0tolerance = copy(50)
# settingsfromtightness.m:136
    
    variant3.f1tof0toleranceSure = copy(300)
# settingsfromtightness.m:137
    
    variant3.f1tof0toleranceThresh = copy(100.0)
# settingsfromtightness.m:138
    variant3.minf1length = copy(3)
# settingsfromtightness.m:139
    
    variant3.minlines = copy(4)
# settingsfromtightness.m:140
    variant3.gapmax = copy(4000)
# settingsfromtightness.m:141
    
    variant3.gapmin = copy(400)
# settingsfromtightness.m:142
    variant3.maxPatterns = copy(2)
# settingsfromtightness.m:143
    variant3.heightHealthRatio = copy(15)
# settingsfromtightness.m:144
    
    variant3.freqHealthLimit = copy(0.2)
# settingsfromtightness.m:145
    
    variant3.maxPval = copy(10)
# settingsfromtightness.m:146
    
    variant3.minforcloseout = copy(2)
# settingsfromtightness.m:147
    variant3.maxtof0 = copy(20)
# settingsfromtightness.m:148
    variant3.totalHealthLimit = copy(1)
# settingsfromtightness.m:149
    
    #variant3.maxfromoneline = 2;
    variant3.gapoverbendmax = copy(100)
# settingsfromtightness.m:151
    
    #cowcow make bendtolerance higher at higher j. if j < 6, double it maybe?
    variant3.bendTolerance = copy(concat([50,20,10,10,10,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
# settingsfromtightness.m:153
    
    variant3.lowj = copy(5)
# settingsfromtightness.m:154
    
    variant3.lines = copy(concat([arange(1,30)]))
# settingsfromtightness.m:155
    variant3.kaguesses = copy(concat([0]))
# settingsfromtightness.m:156
    variant3.verbose = copy(0)
# settingsfromtightness.m:157
    #settings for variant 3
    ts.variant3 = copy(variant3)
# settingsfromtightness.m:159
    ##
    bowties.rank = copy(200)
# settingsfromtightness.m:162
    bowties.containsOblate = copy(false)
# settingsfromtightness.m:163
    bowties.weakAorB = copy(0)
# settingsfromtightness.m:164
    bowties.divthresh = copy(8)
# settingsfromtightness.m:165
    bowties.divthresh2 = copy(8)
# settingsfromtightness.m:166
    bowties.divthreshs = copy(105)
# settingsfromtightness.m:167
    bowties.dthresh = copy(0.05)
# settingsfromtightness.m:168
    bowties.hsdivthresh = copy(3500)
# settingsfromtightness.m:169
    bowties.rmsthresh = copy(0.005)
# settingsfromtightness.m:170
    bowties.percentmaxdiff = copy(0.08)
# settingsfromtightness.m:171
    bowties.percenth14diff = copy(0.04)
# settingsfromtightness.m:172
    bowties.leftsq = copy(0.02)
# settingsfromtightness.m:173
    bowties.rightsq = copy(0.02)
# settingsfromtightness.m:174
    bowties.prll1 = copy(0.02)
# settingsfromtightness.m:175
    bowties.prll2 = copy(0.02)
# settingsfromtightness.m:176
    bowties.inttest = copy(0)
# settingsfromtightness.m:177
    bowties.ratiovar = copy(0.045)
# settingsfromtightness.m:178
    ts.bowties = copy(bowties)
# settingsfromtightness.m:179
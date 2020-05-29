# Generated with SMOP  0.41
# from libsmop import *
# displaykitwithfits.m
import matplotlib.pyplot as plt
    

def displaykitwithfits(kit=None,nada=None,*args,**kwargs):


    # if isstruct(thisfit) == 0
#     return;
# end
    
    #figure('Name',kit.molname,'Position',[36   239   965   525]);
    
    numfits=size(kit.fitlist)
# displaykitwithfits.m:9
    figname=print('%s with %d fits' % (kit['molname'],numfits))
# displaykitwithfits.m:10
    # for this line im honestly not sure
    f=figure('Name',figname,'Position',concat([36,239,965,525]))
# displaykitwithfits.m:11
    if ('finalfit' in kit) and (type(kit['finalfit']) is dict):
        #    kit.fitlist{end+1} = kit.finalfit;
        if kit['finalfit']['patternType']= scaffold
            plt.subplot(1,3,3)
            s=kit['finalfit']['pattern']['archive']
# displaykitwithfits.m:19
            showseriesladder(s,kit['finalfit']['trial']['lineset'])
            plt.subplot(3,3,np.array([7,8]))
            p1=stickplot(s['column1']['realfs'],s['column1']['realhs'],'b')
# displaykitwithfits.m:23
            p2=stickplot(s['column2']['realfs'],s['column2']['realhs'],'r')
# displaykitwithfits.m:24
            p3=stickplot(s['column3']['realfs'],s['column3']['realhs'],'m')
# displaykitwithfits.m:25
            p4=stickplot(s['column4']['realfs'],s['column4']['realhs'],'k')
# displaykitwithfits.m:26
            #     p1 = stickplot(s.series1.realfs,s.series1.realhs,'r');
            #     p2 = stickplot(s.series2.realfs,s.series2.realhs,'b');
            #     p3 = stickplot(s.series3.realfs,s.series3.realhs,'k');
            #     p4 = stickplot(s.series4.realfs,s.series3.realhs,'m');
            # end
            #not sure what set is suppose to be will leave for later
            set(p1,'LineWidth',1)
            set(p2,'LineWidth',1)
            set(p3,'LineWidth',1)
            set(p4,'LineWidth',1)
            plt.plot(s['flatsquare']['fs'][1],s['flatsquare']['hs'][1],'X','MarkerSize',6)
            plt.title('scaffold fit')
        elif kit['finalfit']['patternType']= 'aTypes'
            plt.subplot(3,3,np.array([7,8]))
            s=kit['finalfit']['pattern']['archive']
# displaykitwithfits.m:43
            p1=stickplot(s['f0RealFreqs'],s['f0RealHeights'],'b')
# displaykitwithfits.m:45
            p4=stickplot(s['f1RealFreqs'],s['f1RealHeights'],'k')
# displaykitwithfits.m:47
    #not sure about set
            set(p1,'LineWidth',1)
            set(p4,'LineWidth',1)
            plt.text(s['originString'],1)
            plt.title('a-series fit')
    
    plt.subplot(3,3,concat([1,2,4,5]))
    if 'freqs1d' in kit:
        #  stickplot(kit.onedpeakfs,kit.onedpeakhs,'c');
        plt.plot(kit['freqs1d'],kit['amps1d'],'k')
    else:
        stickplot(kit['onedpeakfs'],kit['onedpeakhs'],'c')
    
    legs[1]=np.array([kit['molname'],'all lines'])
# displaykitwithfits.m:66
    for n in arange(1,size(kit.fitlist)).reshape(-1):
        thisfit=kit['fitlist'][n]
# displaykitwithfits.m:70
        if 'allpairs' not in thisfit:
            thisfit=add_amplitudes_to_fit(thisfit,kit,0)
# displaykitwithfits.m:72
        a=copy(xlim)
# displaykitwithfits.m:77
        plotpairs(thisfit['allpairs'],'scaledstrength-',thisfit['color'])
        plt.ylabel('')
        plt.yticks([])
        plt.xlim(a)
        if 'molfilename' in kit:
            plt.text(kit['molfilename'],- 2)
        legs[end() + 1]=litestringfromfit(thisfit)
# displaykitwithfits.m:85
        if n == 1:
            plt.title(print('%s - %d species found'% (kit['molname'],kit['numspecies'])))
        #addtext(thisfit.branchtypestring);
    
    for n in arange(1,size(kit['fitlist'])).reshape(-1):
        thisfit=kit['fitlist'][n]
# displaykitwithfits.m:95
        stickplot(thisfit['hitfs'],thisfit['hiths'],thisfit['color'])
    
    if kit['numspecies'] >= 1:
        plt.legend(legs)
    
    fancystickies()
    a=copy(xlim)
# displaykitwithfits.m:104
    sexyaxis()
    plt.subplot(3,3,np.array([7,8]))
    plt.xlim(a)
    b=copy(ylim)
# displaykitwithfits.m:108
    b[1]=1e-05
# displaykitwithfits.m:109
    plt.yticks([])
    plt.ylim(b)
    if 'finalfit' in kit:
        if 'trial' in kit['finalfit']:
            plt.text(print('%s\\n%s\\n%s'% (kit['csvfilename'],date,kit['finalfit']['trial']['lineset'][1]['descriptor'])))
        else:
            plt.text(sprintf('%s\\n%s\\n%s'% (kit['csvfilename'],date,kit['finalfit']['fitdescriptor'])))
    else:
        plt.text(print('%s\\n%s\\nNONE FOUND'% (kit['csvfilename'],date)))
    
    sexyaxis()
    # 
# ulines = find(kit.whichspecies == 0);
# stickplot(kit.onedpeakfs(ulines),kit.onedpeakhs(ulines),'k');
# title('unassigned lines');
    return f
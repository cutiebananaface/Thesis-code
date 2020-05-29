from numpy import *
import matplotlib.pyplot as plt
def stickplot(xvals=None,yvals=None,linespec1=None, linespec2=None):
xv = array([]);
yv = array([]);

for i in arange(1,size(xvals)):
    xv[(3*i) - 2] = xvals[i];
    xv[(3*i) - 1]= xvals[i];   
    xv[3*i] = xvals[i];
    yv[(3*i)-2] = 0;
    yv[(3*i)-1] = yvals(i);
    yv[3*i] = 0;
end

if (linespec1=None) & (linespec1='q') == 0:
    p = plt.plot(xv,yv,linespec1);
elif linespec2=None:
    p = plt.plot(xv,yv,linespec1,linespec2);
else
    p = plt.plot(xv,yv);

	return p


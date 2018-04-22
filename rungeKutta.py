from math import sin, pi
from numpy import array, arange
import matplotlib.pyplot as plt
#from pylab import plot, xlabel, show
#import pdb

#pdb.set_trace()



g = 9.81
l = .1
thetaO = 179.0*pi/180

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta, fomega], float)

a = 0
b = 20
N = 100
h = (b-a) / N

tp = arange(a, b, h)
thetapt = []
ypt = []

#Here i Set the initial angle and time Now we start our for loop to
r = array([thetaO, 0.0], float)
for t in tp:
    thetapt.append(r[0])
#    ypt.append(r[1])
    #The next part is the standard equations for our 4th order runge-kutta method
    k1 = h * f(r,t)
    k2 = h * f(r + 0.5*k1, t + 0.5*h)
    k3 = h * f(r + 0.5*k2, t + 0.5*h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6


plt.plot(tp, thetapt)
plt.xlabel('Time')
plt.show()

#print(xpt)
#print(ypt)

'''
if n <= 100:
     xpt.append(r[0])
     ypt.append(r[1])
     k1 = h * f(r,t)
     k2 = h * f(r + 0.5*k1, t + 0.5*h)
     k3 = h * f(r + 0.5*k2, t + 0.5*h)
     k4 = h * f(r + k3, t + h)
     r += (k1 + 2 * k2 + 2 * k3 + k4)/6

plot(tp , xpt)
plot(tp , ypt)
xlabel('Time')
show()
'''

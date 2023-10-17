# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:08:30 2023

@author: agocu
"""

import numpy as np
import matplotlib.pyplot as plt

a = 5999 # semi major axis

mu = 42828 # gravitational parameter of mars

cd = 2.2

asp = 1.2

aspf = 2*asp

marm = 2.95

spf = 7.82*10**-6 * marm

alpha = 0

alpha2 = np.radians(90)

tsp =   0.0161

yawspt = 2.54*10**-5


# func

def densitysm(x):
    ans = 0.001*np.e**(-x/11.1)
    return ans


def drag(z):
    #ans1 =  np.e**( 2.65472E-11*(z - 3399)**5 - 2.45558E-08*(z - 3399)**4 + 6.31410E-06*(z - 3399)**3 + 4.73359E-04*(z - 3399)**2 - 0.443712*(z - 3399) + 23.79408)
    ans2 = 1000* (np.sqrt( mu * (2/(z+3399) - 1/a)))
    ans1 = 0.001*np.e**(-(z)/11.1)
    ans3 = ans1*(ans2**2)*0.5*cd*asp*marm
    return ans3

def dragspeedper(z):
    ans1 = 0.001*np.e**(-(200)/11.1)
    ans = ans1*(z**2)*0.5*cd*asp*marm
    return ans

def dragalt(z):
    ans1 =  np.e**( 2.65472E-11*(z - 3399)**5 - 2.45558E-08*(z - 3399)**4 + 6.31410E-06*(z - 3399)**3 + 4.73359E-04*(z - 3399)**2 - 0.443712*(z - 3399) + 23.79408)
    ans2 = 1000* (np.sqrt( mu * (2/z - 1/a)))
    ans3 = ans1*(ans2**2)*0.5*cd*asp*marm
    return ans3
rmwforcelist = []

def yawdrag(z):
    ans1 = 0.001*np.e**(-(z)/11.1)
    ans2 = 1000* (np.sqrt( mu * (2/(z+3399) - 1/a)))
    ans3 = 0.5*ans1*(ans2**2)*cd*(aspf)
    ans4 = 0.5*ans1*(ans2**2)*cd*(tsp*aspf)
    ans5 = (ans3 - ans4)*marm
    return ans5


def yawdragspeed(z):
    ans1 = 0.001*np.e**(-(200)/11.1)
    ans3 = 0.5*ans1*(z**2)*cd*(aspf)
    ans4 = 0.5*ans1*(z**2)*cd*(tsp*aspf)
    ans5 = (ans3 - ans4)*marm
    return ans5
    
yawrmwforcelist = []


alt2 = np.arange(200,300,0.1 )

rmwisspf = False

for z in alt2:
    rmwforce = drag(z)
    if rmwforce > spf :
        rmwforcelist.append(rmwforce)
        rmwisspf = True
    else:
        if rmwisspf: 
            rmwforcelist.append(spf)
    
rmwforcearray = np.array(rmwforcelist)


yawrmwisspf = False

for z in alt2:
    yawrmwforce = yawdrag(z)
    if yawrmwforce > yawspt :
        yawrmwforcelist.append(yawrmwforce)
        yawrmwisspf = True
    else:
        if yawrmwisspf: 
            yawrmwforcelist.append(yawspt)
    
yawrmwforcearray = np.array(yawrmwforcelist)


dragarray = np.vectorize(drag)(alt2)
yawdragarray = np.vectorize(yawdrag)(alt2)


crossint = np.where(dragarray < spf)[0]

crossalt = alt2[crossint]

crossaltlim = crossalt[0]
    
print(crossaltlim)

yawcrossint = np.where(yawdragarray < yawspt)[0]

yawcrossalt = alt2[yawcrossint]

yawcrossaltlim = yawcrossalt[0]

print(yawcrossaltlim)

def rolldragmomentum(c,t,z):
    ans1 = 0.001*np.e**(-(z)/11.1)
    ans2 = 1000* (np.sqrt( mu * (2/(z+3399) - 1/c)))
    ans3 = ans1*(ans2**2)*0.5*cd*asp*marm
    ans4 = ans3*2*t*0.25*0.707
    return ans4
    





plt.yscale('log')
plt.plot(alt2, rmwforcearray, label= 'Roll RW torque ')
plt.plot(alt2, yawrmwforcearray, label = 'Yaw RW torque')
leg= plt.legend(loc='upper center')
plt.show()

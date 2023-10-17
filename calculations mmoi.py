import numpy as np
import matplotlib.pyplot as plt

#variables 

Vbegin = 0.769

rho = 1296

vexhaust = 2865

thrust = 150

tburn =  19026.141

steps = 10000

R = 0.5683456978

mtank = 31.7

mbig = 461.3 #mass without propellant and tank

mdot = Vbegin * rho / tburn

mdry = mbig + mtank

mwet = mdry + rho * Vbegin


Isc_roll_initial=494.193 #kg m^2

#functions

def Dvtoburntime(Dv):
    ans1 = mwet / (np.e**(Dv/vexhaust))
    ans2 = mwet - ans1
    ans = ans2/mdot
    return ans

#def DvtoMass(Dv):
    ans1 = mwet / (np.e**(Dv/vexhaust))
    ans2 = mwet - ans1
    ans = ans2/mdot
    return ans


def Isc_Roll(h):
    ans = Isc_roll_initial-(Iroll(2*R)-Iroll(h))
    return ans

def Iroll(h):
    Ir = 0.5 * rho * np.pi * ((h**5)/5 - R * h**4 + ((4 * R**2)/3) * h**3)
    return Ir

def h(v):
    h = np.roots([(-np.pi/3),np.pi*R,0,-v])
    return h[1]

def Vol(t):
    Volume = Vbegin - ((mdot * t) / rho)
    return Volume

def FunnyFunc_Roll(t):
    ans = Isc_Roll(h(Vol(t)))
    return ans


def com_roll(h):
    ans1 = (rho * np.pi / 12 * h**3 *(8*R-3*h)) + R * mtank + 1.5 * mbig
    ans2 = (rho * np.pi/3 * (3 * R * h**2 - h**3) + mtank + mbig)
    ans = ans1 / ans2
    return ans

def FunnyFunc_com_Roll(t):
    ans = com_roll(h(Vol(t)))
    return ans
#do the arrays 

time = np.arange(0,tburn, tburn/steps)
plt.plot(time, [FunnyFunc_com_Roll(t) for t in time])
plt.show()
#minimal = np.min(time)



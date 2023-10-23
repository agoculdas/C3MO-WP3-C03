# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:11:41 2023

@author: agocu
"""

import numpy as np

import matplotlib.pyplot as plt 


def gravytorque(z):
    ans = (4.28*(10**13))
    ans2 = (((3399+z)*(10**3))**3)
    ans3 = (ans/ans2)*300*1.5
    return ans3

def gravymoment():
    ans = gravytorque(200)*(1/2**0.5)*((235*60)/8)
    return ans

alt = np.arange(200,5000, 0.1)


plt.plot(alt, [gravytorque(z) for z in alt])
plt.xlabel('Spacecraft Altitude')
plt.ylabel('Gravity gradient torque')
plt.savefig('Gravytorque', dpi=400, bbox_inches = "tight")


plt.show()
"""
Created on Tue Oct 17 19:32:44 2023

@author: agocu
"""

import matplotlib.pyplot as plt
#lists
missionstage = ['Insertion', 'Parking', 'Final']

dragtorque = [3.54*10**-3, 2.65*10**-3, 1.91*10**-3]


#graph
plt.step(missionstage, dragtorque, where='mid', label='Max Torque')
plt.xlabel('Orbit type')
plt.ylabel('Peak RW Torque, Nm')
plt.legend()

plt.show()
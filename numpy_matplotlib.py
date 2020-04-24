# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:02:27 2019

@author: Andile XeroxZen
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)

#separate the figure object and axes object
#from the plotting object
fig, ax1 = plt.subplots()

#Duplicate the axes with a different y axis
#and the same x-axis
ax2 = ax1.twinx()

curve1, = ax1.plot(x ,y, label='sin', color='r')
curve2, = ax2.plot(x ,z, label='sinh', color='b')

#Make a curves list to access the parameters in the curves
curves = [curve1, curve2]

#add legend via axis 1 or axis 2
#one command is usually suffiecient
#ax1.legend() #will not display the legend of ax2
#ax2.legend() #will not display the legend of ax1

ax1.legend(curves, [curve.get_label() for curve in curves])
#ax2.legend(curves, [curve.get_label() for curve in curves])

#global figure properties
plt.title('Plot of sine and hyperbolic sine.')
plt.show()


#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

#generate 20 datapoints between 0 and 10
x = np.linspace(0,10,20) 
y= x**2 
z = x**3
 
fig = plt.figure()

ax1 = fig.add_axes([0.1,0.2,0.8,0.7])
# [%left, %bottom, %width, %height]
# If you make it .5 from the left, but set width at 1.0, it will cut off part of the graph

#Plot the x2 line
# x and y are NOT points but arrays of points

ax1.plot(x,y,linewidth=3,  linestyle='dashed',  color='rebeccapurple')

#You plot the x3 line on your own
#Change the color and the linestyle
ax1.plot(x, z, linewidth=3, linestyle="dashed", color="hotpink")

ax1.set_title('Johns Plot')
ax1.set_xlabel('Xs to be squared')
ax1.set_ylabel('function values')
# Go ahead and create a title, xlabel and
#y_label for ax2

#create a new figure object
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])# [left, bottom, width, height]
ax2 = fig.add_axes([0.2,0.5,0.4,0.3])# [left, bottom, width, height]
#Where do you think figure ax1 is going and where is ax2 going in the window?
ax1.plot(x,y,linewidth=3,  linestyle='dashed',  color='rebeccapurple')
ax1.plot(y,x,linewidth=3,  linestyle='dashed',  color='rebeccapurple')

plt.savefig("graphs/output.png")

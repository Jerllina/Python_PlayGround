# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:28:58 2018

@author: lijie
"""
'''☆☆☆☆☆☆'''

import numpy as np
import matplotlib.pyplot as plt

#set the labels
labels=np.array(list('abcdefghij'))

#create data
data=np.array([11,4]*5)
dataLength=len(labels)

#divide the circle into dataLength pieces, excluding the end point
angles=np.linspace(0,2*np.pi,dataLength,endpoint=False)

#complete the circle
data=np.append(data,data[0])
angles=np.append(angles,angles[0])

#plot & set the picture
plt.polar(angles,data,'bv--',linewidth=3)

#set the grid labels
plt.thetagrids(angles*180/np.pi,labels)

#fill the ☆
plt.fill(angles,data,facecolor='b',alpha=0.6)

#set the coordinate of ☆
plt.ylim(0,12)

plt.show()




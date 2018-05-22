# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:00:53 2018

@author: lijie
"""
import numpy as np
import matplotlib.pyplot as plt

#create a piece of data
x=np.linspace(0,10,11)
y=11-x

#plot the bar gragh
plt.bar(x,y,color='orange',width=0.8,alpha=0.6,edgecolor='red',
        linestyle='--',linewidth=0.9,hatch='*')
#plot the edge of the bar:yellow,fill the bar with '*' ,alpha:transparency透明度

#text label
for xx,yy in zip(x,y):
    plt.text(xx-0.2,yy+0.1,'%2d'%yy)
    
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:37:57 2023

@author: icon
"""
import pandas as pd
songs_66=pd.Series([3,None,11,9],
                   index=["george","ringo","john","paul"],
                   name="counts")
songs_69=pd.Series([7,16,21,39],
                   index=["ram","sham","ghamsahm","krishra"],
                   name="counts")
import matplotlib.pyplot as plt

fig = plt.figure()  # open canvas
songs_69.plot()
plt.legend()

################################

fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

################################

import numpy as np
data = pd.Series(np.random.randn(500),name="500 random number")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

############################################################

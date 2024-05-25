# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:32:45 2023

@author: icon
"""


 
import pandas as pd
songs2=pd.Series([145,142,38,9],name="count")
songs2.index
print(songs2)
#the index can be string

import pandas as pd
songs3=pd.Series([145,142,38,9],name="counts",
                 index=["paul","john","justin","ringo"])
songs3.index
songs3

# null value is ignored in arithmatic opertaion

### series and arrays ###

import numpy as np
numpy_ser=np.array([145,141,38,9])
print(songs3[1] )       # accessing series
print(numpy_ser[1])

print(songs3.mean())
print(numpy_ser.mean())

###############  pandas series ##################

george=pd.Series([10,7,1,22],
                 index=[1968,1982,1945,1933],
                 name='george songs')
print(george)

#to read or select item from series
george[1968]

# iterating over series
for item in george:
    print(item)

#updating values in series
george[1968]=68

#deleting values in series
import pandas as pd
s=pd.Series([1,2,3],index=[0,1,2])
print(s)
del s[1]

############################################################

# convert types
#string use.astype(str),.apply(str)
#numeric use pd.to_numeric
#integer use .astype(int),
#note that this will fall with nan
#datetime use pd.to_datatime

songs_66=pd.Series([3,None,11,9],
                   index=["george","ringo","john","paul"],
                   name="counts")


songs_66.dtypes
#dtype("float64")

pd.to_numeric(songs_66.apply(str))
#there will be error

pd.to_numeric(songs_66.astype(str),errors='coerce')
#this will pass errors='coerce'
#we can see that it supports many formates
#data type will not be change but statements will be executed
songs_66.dtypes

#dealing with none
#the .fillna method will replace them with a given value
songs_66.fillna(0)

# nan values can be dropped from the series using .dropna
songs_66.dropna()

#################################################################

#Append ,combining, and joining two series

songs_69=pd.Series([7,16,21,39],
                   index=["ram","sham","ghamsahm","krishra"],
                   name="counts")

# to concatenate two series together

songs=songs_66.append(songs_69)

#################################################################













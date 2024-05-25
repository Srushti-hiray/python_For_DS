# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:40:40 2023

@author: icon
"""

######################  pandas dataframe ####################

# two dimentional data structure , immutable ,heterogeneous 
#tabular 

import pandas as pd
pd.__version__

### DF using list of list

technologies=[["sparks",20000,"30days"],#list of list
              ["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)#data frame
print(df)
# add row and colume to dataframe
colume_name=["courses","fee","duration"]
row_label=["a","b"]
#df=pd.DataFrame(technologies,row_label)
df=pd.DataFrame(technologies,columns=colume_name,index=row_label)
print(df)


###################
df.dtypes
###################

###DF using dictionary

import pandas as pd
technologies ={
    "courses":["sparks","pysparks","hadoop","python"],
    "fee":[2000,25000,3000,4200],
    "duration":["30days","40days","25days","50days"],
    "discount":[11.2,55.3,9.1,44]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)  ### To check data types

# convert all types to best posssible types
#convert object to string
df2=df.convert_dtypes()
print(df2.dtypes)

# change all colume to same type
#convert into object
df=df.astype(str)
print(df.dtypes)

#change specific column
df=df.astype({"fee":int,"discount":float})
print(df.dtypes)

#convert data type for all columns in list
df=pd.DataFrame(technologies)
cols=["fee","discount"]
df[cols]=df[cols].astype("float")
df.dtypes

#ignore errors
df=df.astype({"courses":int},errors="ignore")
df.dtypes

# generate error
df=df.astype({"courses":int},errors="raise")
df.dtypes

##############################
#create dataframe from dictionary

import pandas as pd
technologies ={
    "courses":["sparks","pysparks","hadoop","python"],
    "fee":[2000,25000,3000,4200],
    "duration":["30days","40days","25days","50days"],
    "discount":[1000,2000,999,440]
    }
df=pd.DataFrame(technologies)
df        # prints output

###############################################

# convert dataframe to csv 
df.to_csv('data_file.csv')

#convert csv file to dataframe
df=pd.read_csv('data_file.csv')
df=pd.read_csv("C:/1-python/age.csv.xls")

################################################

#pandas basic operation

import pandas as pd
import numpy as np
technologies ={
    "courses":["sparks","pysparks","hadoop","python","pandas",None,"sparks","cpp"],
    "fee":[2000,25000,3000,4200,np.nan,2500,700,3000],
    "duration":["30days","40days","25days","50days","30days","40days","25days","50days"],
    "discount":[1000,2000,999,440,777,344,223,500]
    }

row_lable=["r0","r1","r2","r3","r4","r5","r6","r7"]
df=pd.DataFrame(technologies,index=row_lable)
print(df)

df.to_csv('technologies.csv.xls') # converted to csv file

#data properties
df.shape
#rows and columes

df.size
#rows * columes

df.columns
#displays columes

df.columns.values
#displays columes

df.index
#displays index

df.dtypes

### accessing one column contents
df['fee']

### accessing two column contents
df[['fee','discount']]
df[['fee','discount','courses']]

#accessing specific rows and columns

df2=df[6:]
df3=df[2:3]
df2=df[:3]

# individul cell value
df['duration'][3]

#substracting specific number from column
df['fee']=df['fee']-500
df['fee']


#pandas to manipulate dataframe
#describe dataFrame
#Describe dataframe for all numeric column

df.describe()
#it will show 5 no. summary

#changing column names

df.columns=['A',"B","C","D"]
df

# rename column using rename()
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})

# droping rows using row label

df=df.drop(["r1"])
df=df.drop(df.index[1]) # index 1st row deleted
df=df.drop(df.index[[2,5]])  # it will delete 2,5th row
df=df.drop(df.index[4:]) # it will remove all rows from 4th
df=df.drop(df.index[2:5]) # it will remove row from 2 to 4

df=pd.DataFrame(technologies)
df
df=df.drop(0) #it will delete 0Th index
df=df.drop([1,4]) # it will delete 1,4th index
df=df.drop(range(2,5)) # it will delete row from 2 to 4th row

# droping columns

df=df.drop(["courses","fee"],axis='columns')
df=df.drop(labels=["courses","fee"],axis=1)
df=df.drop(columns=["fee"],axis=1)
df=df.drop(df.columns[1],axis=1) # will delete column of 1st index
df=df.drop(df.columns[[1,2]],axis=1)# will delete multiple colulmns
#to make changes in same dataframe

df.drop(df.columns[2],axis=1,inplace=True)

litcol=["courses","fee"]
df=df.drop(litcol,axis=1)

#df.iloc[startrow:endrow,startcolumn:endcolumn] ##SYNTAX

df=pd.DataFrame(technologies)
df=df.iloc[1:3,0:2] #1st,2nd row and 0th,1st column
df
df=df.iloc[:,0:2]# all rows and oth,1st column
df
df=df.iloc[0:2,:]# all column and oth,1st row

df=df.iloc[2]
print(df) # it will give series of single column

df=df.iloc[[2,3,6]] 

#it will select 2nd,3rd and 6th column

df=df.iloc[1:5]
print(df) # it will select 1 to 4 rows

df=df.iloc[:2]#it will select 0th,1st row

df=df.iloc[-2:] # it will select all rows from -2 onwards

df=df.iloc[:-3]#it will select all rows till -3 leaving -3

df=df.iloc[::3]# it will select all rows which are multiple of 3

#### loc  ###

df=pd.DataFrame(technologies,index=row_lable)
df=df.loc['r1']

df=df.loc[['r1','r2']]

df=df.loc['r1':'r4']  #it will select r1 to r4 including r4

df=df.loc['r0':'r7':2] #it will select in step of 2

#df.loc[:,start:stop:step] #SYNTAX

df=df.loc["r0":"r5",["courses","fee","duration"]]  # it will have courses fee and duration column
                                                  #from r0 to r5
df=df.loc["r0",'fee':'discount'] # it will select column from fee to discount
                                 #only row r0 , series 
df=df.loc[:,"duration":] # it will select all column frim duration

df=df.loc[:,:"discount"] # it will select all columns including discount

#####################################





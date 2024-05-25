# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:56:28 2023

@author: icon
"""

import pandas as pd
df=pd.read_csv("C:/2-python/Iris.csv")
print(df)

#data type
print(df.dtypes)


#convert object into string
df2=df.convert_dtypes()
df2
print(df2.dtypes)

#convert all column to object
df2=df.astype(str)
print(df2.dtypes)

df.columns
#change data type of specific column
df2=df.astype({"SepalLengthCm":int,"SepalWidthCm":int})
df2
print(df2.dtypes)


#convert all datatypes of columns using string
cols=["SepalLengthCm","SepalWidthCm"]
df[cols]=df[cols].astype(int)
print(df.dtypes)


#ignore error
df2=df.astype({'Species':int},errors="ignore")
print(df2.dtypes)


#raise error
df2=df.astype({"Species":int},errors="raise")
print(df2.dtypes)

df.shape

df.index

df.columns

df.size

df.columns.values

df.describe()


#accessing columns

      #single column
df["Species"]      
      #multiple columns
df[["Id","Species"]]      


#accessing individual cell
df["Id"][4]


#substracting value from perticular column
df2=df["SepalLengthCm"]-4
print(df2)


#changing columns name
df.columns=["A","B","C","D","E","F"]
df

df2=df.rename({"Id":"A","SepalLengthCm":"B"},axis=1)
df2=df.rename({"PetalLengthCm":"A","Species":"B"},axis="columns")
df2=df.rename(columns={"Id":"A","SepalLengthCm":"B"})


#dropping rows using index
df=df.drop(df.index[1])
df=df.drop(df.index[[2,3]])
df=df.drop(df.index[:7])
df=df.drop(df.index[10:15])
df.drop(4)
df=df.drop(range(2,5))


#to drop columns
df=df.drop(df.columns[2],axis=1)
df=df.drop(df.columns[[1,2]],axis=1)
    #drop multiple column
col=['Id', 'SepalLengthCm']
df=df.drop(col,axis=1)


#Iloc

df2=df.iloc[1:3,0:2]
print(df2)
df2=df.iloc[2]
df2=df.iloc[[2,3,5]]
df2=df.iloc[1:4]
df2=df.iloc[:-2]
df2=df.iloc[::2]


#loc

df2=df.loc[:,"Id":"SepalWidthCm"]
df2=df.loc[1:4,"Id":"SepalWidthCm"]
df2=df.loc[:,"PetalLengthCm":]
df2=df.loc[2:7,["PetalLengthCm","Id"]]


#add columns
import random
eye_no=[]
for x in range(150):
    eye_no.append(random.randrange(-3,3))
df["eye_number"]=eye_no


#add multiple column
import random
spec_width=[]
for x in range(150):
    spec_width.append(random.randrange(1,5))
df=df.assign(Eye_no=eye_no,Spec_width=spec_width)


#derive new column from existing column
df2=df.assign(add=lambda x:x.Id + x.SepalWidthCm)


#add column to specific position
df.insert(0,"eye_no",eye_no)


#add rows
df.loc[151]=[1,23,45,3,5,67,"ksefuhwi",54]


#to find no of row and column
rows_count=len(df.index)
rows_count=len(df.axes[0])
column_count=len(df.axes[1])

df.columns


#print where eye_no>1
a=df[df.eye_no>1]
print(a)
b=df.loc[df["eye_no"]>1]
print(b)


#select PetalWidthCm between 0.5 to 1

df2=df[df.PetalWidthCm.between(0.5,1)]
df2=df.loc[df.PetalWidthCm.between(0.5,1)]


#change specific value in dataframe

df.loc[2,"SepalLengthCm"]=1
df


#sum(),mean()
print(df.SepalLengthCm.sum())
print(df.SepalLengthCm.mean())


#sort in ascending or descending way
df=df.sort_values(by=["SepalWidthCm"],ascending=True)
df=df.sort_values(by=["SepalWidthCm"],ascending=False)


#replace value
df['Species']=df['Species'].map({"Iris-setosa":"iris"})


#iterate over rows
for index,row in df.iterrows():
   # print(row["SepalLengthCm"],row["PetalWidthCm"])
    print(index,row)


#apply() - using def functions
def add_2(x):
    return x+2

df2=df.apply(add_2) # error because there is one string column
df2=df.SepalLengthCm.apply(add_2)
df[["SepalWidthCm","Id"]]=df[["SepalWidthCm","Id"]].apply(add_2)


#lambda function 
df[["SepalWidthCm","Id"]]=df[["SepalWidthCm","Id"]].apply(lambda x:x+2)


#transform()
df=df.Id.transform(add_2)


#map()
df=df.Id.map(add_2)


#using numpy function
import numpy as np
df2=df.Id.apply(np.square)


#groupby()
df2=df.groupby(["SepalWidthCm"]).sum()
df2=df.groupby(["SepalWidthCm"]).sum().reset_index()
df2=df.groupby(["SepalWidthCm","SepalLengthCm"]).sum().reset_index()


#shuffle()
df2=df.sample(frac=1)
df2=df.sample(frac=0.5)


















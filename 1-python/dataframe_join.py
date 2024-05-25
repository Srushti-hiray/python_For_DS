# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:03:46 2023

@author: icon
"""

############# using dataframe.apply() to apply function to columns
import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

df2=((df.A).apply(add_3))

#using apply function single column

def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

#apply to multiple columns
df[["A","B"]]=df[["A","B"]].apply(add_4)
df

#apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2

#using lamda fun for multiple columns
df[["A","B"]]=df[["A","B"]].apply(lambda x:x+10)
df

#transform() function instead of apply on all column
def add_5(x):
    return x+5
df=df.transform(add_5)
df

#####map() on single column
df["A"]=df["A"].map(lambda x:x+5)
df["A"]

#using numpy function on single columns
#using dataframe.apply $ [] operator
import numpy as np
df["A"]=df["A"].apply(np.square)
print(df)

df["A"]=np.square(df["A"])

########groupby()#if repeated entry are present than they are grp by single using groupby()
df=pd.read_csv("C:/1-python/technologies.csv")
df
df2=df.groupby(["courses"]).sum()# not have index
print(df2)

df2=df.groupby(["courses"]).sum().reset_index()# have index
print(df2)

#on multiple column
df2=df.groupby(["courses","duration"]).sum()
print(df2)

#get list of columns from header
column_header=list(df.columns.values)
print("the column header:",column_header)

##########pandas shuffle dataframe rows############
#shuffle the dataframe row and return all rows
df1=df.sample(frac=1)#100% shuffle
print(df1)

df1=df.sample(frac=0.5)#50% shuffle
print(df1)

#create new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

####drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)#reset index will delete the index instead of inserting back into column


########## joining the dataframe (inner,left,right)  ############
# one column must me common

technologies2={
    "courses":["cpp","python","java","c++","c","html","php","css"],
    "fee":[100,200,300,400,500,600,700,800],
    "duration":["30days","20days","10days","50days","40days","60days","80days","70days"]
    }
indexl=["r100","r2","r3","r4","r5","r6","r7","r8"]
df2=pd.DataFrame(technologies2,indexl)
df2

technologies3={
    "courses":["cpp","python","hindi","mar","c","dsf","dbms","css"],
    
    "discount":[150,250,350,450,550,650,750,850],
    
    }
indexl=["r9","r2","r11","r12","r5","r14","r15","r8"]
df3=pd.DataFrame(technologies3,indexl)
df3

#index , courses must be same for 2 DF

#joining horizontally,concatinating vertically joining
#left join
df4=df2.join(df3,lsuffix="left",rsuffix="right")
print(df4)
df4=df2.join(df3,lsuffix="left",rsuffix="right",how="left")
print(df4)

#inner join

df4=df2.join(df3,lsuffix="left",rsuffix="right",how="inner")
print(df4)

# right join
df4=df2.join(df3,lsuffix="left",rsuffix="right",how="right")
print(df4)


#pandas join on columns
df4=df2.set_index("courses").join(df3.set_index("courses"),how="right")
print(df4)
#here index doesn't matter it depends on column name 

df4=df2.set_index("courses").join(df3.set_index("courses"),how="inner")
print(df4)

####################   merge   #######################
#horizontal join
#using pandas.merge() for inner join
df4=pd.merge(df,df1)
print(df4)
df4=df2.merge(df3)

df=pd.DataFrame({
    "course":["sparks","pysparks","python","cpp"],
    "fee":[100,200,400,400]})
df1=pd.DataFrame({
    "course":["pandas","numppy","hadop","java"],
    "fee":[500,300,600,900]})


print()
############   concat()    ################
#vertical join
data=(df,df1)
df2=pd.concat(data)
df2

data=(df2,df3)
df4=pd.concat(data)
df4

#concatinate multiple DF
data=(df2,df3,df1)
df4=pd.concat(data)
df4






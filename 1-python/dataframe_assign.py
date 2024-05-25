# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:42:51 2023

@author: icon
"""

#assignment

#write python program to craete series

import pandas as pd
ds=pd.Series([2,4,6,10])
print(ds)

#####################################


# write a panda program to convert a panda module series to 
#python list and its type
import pandas as pd
ds=pd.Series([2,4,6,10])
print("panda series and its type:")
print(ds)
print(ds.tolist())
print(type(ds.tolist()))

######################################


# write python program to add,sub,mul,2 series
import pandas as pd
ds1=pd.Series([1,2,3,4])
ds2=pd.Series([9,8,7,6])
ds=ds1*ds2
print(ds)
ds=ds1/ds2
print(ds)
ds=ds1-ds2
print(ds)


########################################

#write python program to compare 2 series
import pandas as pd
ds1=pd.Series([1,7,3,8])
ds2=pd.Series([9,5,7,6])
print(f"series first\n{ds1} series second \n{ds2}")
print("equals:\n")
print(ds1==ds2)
print("ds1<ds2:\n")
print(ds1<ds2)
print("ds1>ds2:\n")
print(ds1>ds2)

#########################################

#write pandas program to convert dictionary to pandas series
import pandas as pd
dict={2:"trups",6:"sass",4:"guddhi",8:"anuu"}
ds=pd.Series(dict)
print(ds)

lst=(1,2,3,4)
print(type(lst))
ds=pd.Series(lst)
print(ds)

###########################################

#convert numpy array into series

import numpy as np
arr=np.array([1,4,7,9])
print("array",arr)
print("series:\n")
ds1=pd.Series(arr)
print(ds)
print(type(ds))

############################################

#write pandas program to change datatype of given column of sereies

ds=pd.Series(["1","4"])
print("change to numeric data type")
ds1=pd.to_numeric(ds,errors="coerce")
print(ds1)

############################################

# write pandas program to convert first colume of dataframe as seies

import pandas as pd
d={"col":[1,2,3,4,5],
   "col2":[6,7,8,9,10],
   "col3":[11,12,13,14,15]
   }
df=pd.DataFrame(d)

print("orignal data frame:")
print(df)
print(type(df))
ds1=df.iloc[:,0]#all row and 0th column
print("dataframe as series (only 1 column)")
print(ds1)
print(type(ds1))

#############################################

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###

import pandas as pd
s=pd.Series([
    ["red","yellow"],
    ["blue","green"],
    ["purple","white","black"]])
print("orignal series of list:\n")
print(s)
print("one series")
s=s.apply(pd.Series).stack().reset_index(drop=True)
print(s)


import pandas as pd
s=pd.Series([
    ["red","yellow"],
    ["blue","green"],
    ["purple","white","black"]])
print("orignal series of list:\n")
print(s)
print("one series")
s=s.apply(pd.Series)
s=s.stack()
s=s.reset_index(drop=True)
print(s)

#####################################

#write pandas program to add some data to existing series
s1=pd.Series([1,5,77,8])
print(s1)
news1=pd.concat([s1, pd.Series(["hello",33]),pd.Series([45])],ignore_index=True)
print(news1)

#####################################

#write pandas program to sort given series
s1=pd.Series(["1","5","python","77","8"])
print(s1)
ss1=pd.Series(s1).sort_values()
print(ss1)

######################################

#to change order of index

import pandas as pd
s1=pd.Series(data=[1,3,5,8],
             index=["A","B",'C',"D"])
print(s1)
s1=s1.reindex(index=["B","A","D","C"])
print("after reindexing:")
print(s1)

########################################################

################### Assignments  ########################

# csv to dataframe operations
import pandas as pd
df=pd.read_csv("C:/2-python/loan.csv.xls")

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

#accessing one column

df["member_id"]

# accessing more than 2 columns
df[["member_id","num_bc_sats"]]

df.describe()

df["member_id"][6]

d2=df[2:4]
d3=df.iloc[2:4,1:6]
d4=df.iloc[3:8,8]

df["loan_amnt"]=df["loan_amnt"]-500
df["loan_amnt"]

df=df.rename({"id":"ID","member_id":"MEMBER_ID"},axis=1)
df=df.rename({"loan_amnt":"LOAN_AMOUNT"},axis="columns")
df=df.rename(columns={"term":"TERM"})

ds1=df.iloc[:,0]#converting data frame into series of 0Th column
lst=ds1.tolist()#converting series into list
print(lst)

df=df.drop(["id","member_id"])

df=df.drop(df.index[1])
df=df.drop(range(2,5))

df=df.iloc[0:2,:]# all column and oth,1st row

df=df.iloc[3]# it will give series of single column

df=df.iloc[[2,6]] #it will select 2nd and 6th column

df=df.loc[:,["id","member_id","loan_amnt"]]  

df=df.loc[:,'id':'term'] 

#                   ********************                        #

import pandas as pd
df1=pd.read_csv("C:/2-python/crime_data.csv.xls")

df1.shape   #(50,5)

df1.size    # 250

df1.columns

df1.columns.values

df1.index

df1.dtypes

df1.info
df1['Unnamed: 0']
df1["Murder"][5]
df1[['Unnamed: 0',"Murder",'Assault']]

df1.iloc[2:3,0:4] # 2nd row and 0th to 3rd column
df1[2:6]# 2nd to 5Th row

df1["Assault"]=df1["Assault"]-36
df1

df1.describe()

df1.rename({"Murder":"killed"},axis=1)
df1=df1.rename({"Assault":"ASSAULT"},axis="columns")

df1=df1.drop(["Unnamed: 0","Murder"])
df=df.drop(df.index[1])
df1=df1.drop(range(2,5))

df1=df1.iloc[0:2,:]# all column and oth,1st row

df1=df1.iloc[3]# it will give series of single column

df1=df1.iloc[[2,6]] #it will select 2nd and 6th column

df1=df1.loc[:,["Murder","Assault"]]  

df1=df1.loc[:,'Murder':'Rape'] 

#                         @@@@@@@@@@                            #

import pandas as pd
df2=pd.read_csv("C:/2-python/bank_data.csv.xls")

df2.shape   #(50,5)

df2.size    # 250

df2.columns

df2.columns.values

df2.index

df2.dtypes

df2.info
df2['age']
df2["default"][5]
df2[['default',"previous",'con_cellular']]

df2.iloc[2:3,0:4] # 2nd row and 0th to 3rd column
df2[2:6]# 2nd to 5Th row

df2["duration"]=df1["duration"]-36
df2

df2.describe()

df2.rename({"age":"AGE"},axis=1)
df2=df2.rename({"balance":"BALANCE"},axis="columns")

df2=df2.drop(["campaign","housing"])
df2=df2.drop(df.index[7])
df2=df2.drop(range(2,19))

df2=df2.iloc[0:99,:]

df2=df2.iloc[7]

df2=df2.iloc[[17,6]] 
df2=df2.loc[:,["age","balance","loan"]]  

df2=df2.loc[:,'pdays':'duration'] 

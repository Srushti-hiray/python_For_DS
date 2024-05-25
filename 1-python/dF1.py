# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:21:12 2023

@author: icon
"""

#display all columns till that column
import pandas as pd
technologies ={
    "courses":["sparks","pysparks","hadoop","python"],
    "fee":[2000,25000,3000,4200],
    "duration":["30days","40days","25days","50days"],
    "discount":[11.2,55.3,9.1,44]
    }
df=pd.DataFrame(technologies)

df2=df.loc[:,:'duration']
df2

#all rows
#pandas add column to dataframe
#add new column to dataframe
tutors=['ram','sham','radhesham','dhansham',]
df2=df.assign(Tutor_Assigned=tutors)
print(df2)

#add multiple columns to DF
mnccompany=['tata','infosysy','amazon','google']
tutors=['ram','sham','radhesham','dhansham',]
df2=df.assign(Tutor_Assigned=tutors,mnccompany=mnccompany)
print(df2)

#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(dis_percentage=lambda x: x.fee * x.discount/100)
print(df2)

#add  new column to existing dataframe
df=pd.DataFrame(technologies)
df['mnccompany'] =mnccompany
print(df)

#add new column to specific position

df=pd.DataFrame(technologies)
df.insert(0,'tutors',tutors)
print(df)

#to find how many no. of rows and columns are there in dataframe

rows_count=len(df.index)
print(rows_count)
#                   or
rows_count=len(df.axes[0])
print(rows_count)

column_count=len(df.axes[1])
print(column_count)

#another way to find row as well as column count
#for row

row_count=df.shape[0]
print(row_count)
#for column

column_count=df.shape[1]
print(column_count)

################          assignments           ################

#write programe to craete dataframe from dictionary and create it


dict1={"1":"siddhi","2":"trupti","3":"sakshi","4":"anushri"}
names=pd.DataFrame(dict1)
print(names)       ###errorr

a={'A':[78,85,96,80,86],'B':[11,23,75,65,43],'C':[2,43,44,67,3]}
name=pd.DataFrame(a)
print(name)


#write pandas program to display summary of basic info about dataframe

a={'A':[78,85,96,80,86],'B':[11,23,75,65,43],'C':[2,43,44,67,3]}
name=pd.DataFrame(a)
print(name)
name.info()
name.describe()


#write pandas programe to get 1st 3 rows of DF

import numpy as np
exam_data={'name':["ram","sham","ghansham","bahubali","bhalaldev"],
           "score":[12.5,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)
df
print("to select specific columns")
print(df[['name','score']])
print(df.iloc[[1,3],[1,2]])## row ,column


#write python program to select rows where the number of attempts in
#examination is greater than 2

import pandas as pd
import numpy as np
exam_data={'name':["ram","sham","ghansham","bahubali","bhalaldev"],
           "score":[12.5,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)#df=pd.DataFrame(exam_data,index=labels)
df
print("no of attempt")
print(df[df['attempts']>2])
df2=df.loc[df.attempts>2]
print(df2)


#to count no of rows and column
row=len(df.axes[0])#shape[0]
column=len(df.axes[1])#shape[1]
row1=str(row)
print(type(row1))
print("no. of rows:"+str(row))
print(row,column)


#write pandas program to select the row where score is missing i.e nan

import pandas as pd
import numpy as np
exam_data={'name':["ram","sham","ghansham","bahubali","bhalaldev"],
           "score":[16,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)#df=pd.DataFrame(exam_data,index=labels)
df
print(df[df["score"].isnull()])
print(df.loc[df.score.isnull()])


#write pandas program to select score between 15 and 20

print("score between 15 and 20")
df2=df[df['score'].between(15,20)]
df2=df.loc[df["score"].between(15,20)]
print(df2)


#no.of attempts is less than 2 and score greater then 15

import pandas as pd
import numpy as np
exam_data={'name':["ram","sham","ghansham","bahubali","bhalaldev"],
           "score":[16,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)#df=pd.DataFrame(exam_data,index=labels)
df
print(df[(df['attempts']<2) & (df['score']>15)])
print(df.loc[(df.attempts<2) & (df.score>15)])


#write pandas program to change the score 

print("change the score in b row")
df.loc["d","score"]=11.5   #important
print(df)


#write pandas program to calculate the sum of examination of attempts
#by students

import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev"],
           "score":[16,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)#df=pd.DataFrame(exam_data,index=labels)
print(df["attempts"].sum())


#write pandas program to calculate mean of all the students scores

import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev"],
           "score":[16,34,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)
print(df["score"].mean())


#write a program to append new row

print("append new row")
df.loc["f"]=["avantika",20,3,"no"]
print("print all the recordes after insertion:")
print(df)


#write pandas program to sort DF in descending order and then ascending 
#order
 
import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev"],
           "score":[16,3,67,55.6,np.nan],
           "attempts":[1,3,2,5,3],
           "qualify":["yes","no","no","yes","no"]}

labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,labels)
df=df.sort_values(by=["name"],ascending=[False])
df=df.sort_values(by=["score"],ascending=[True])
#here name will be false (descending), score will be true(ascending)
print("sorted\n",df)


#write pandas program to replace qualify column with the values "yes"
#"no" with true and false

import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev","avantika"],
           "score":[16,3,67,55.6,np.nan,3],
           "attempts":[1,3,2,5,.33,],
           "qualify":["yes","no","no","yes","no","yes"]
           }
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,labels)
df["qualify"]=df["qualify"].map({"yes":True,"no":False})
print(df)


#change name avantika to kalkera 

import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev","avantika"],
           "score":[16,3,67,55.6,np.nan,3],
           "attempts":[1,3,2,5,.33,4],
           "qualify":["yes","no","no","yes","no","yes"]
           }
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,labels)
df["name"]=df["name"].replace("avantika","kalkera")
print(df)


#add new column

import pandas as pd
import numpy as np
exam_data={'name':["shivgamini","kattappa","devsena","bahubali","bhalaldev","avantika"],
           "score":[16,3,67,55.6,np.nan,3],
           "attempts":[1,3,2,5,.33,4],
           "qualify":["yes","no","no","yes","no","yes"]
           }
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,labels)
print(df)
color=["savla","kala","gori","ujla","savla","ati gori"]
df["color"]=color
print("after adding column")
print(df)


#pandas program to iterate over rows

for index,row in df.iterrows():
    print(row["name"],row["score"])


###################################################################

df1=pd.read_csv("C:/2-python/Seeds_data.csv.xls")
print(df1)

#display all column till that column
df2=df1.loc[:,:"length"]
print(df2)

#add columns
import random
circle=[]
for i in range(210):
    circle.append(random.randrange(1,100))
df2=df1.assign(circle=circle)
print(df2)

#derive new column from existing column
df2=df1.assign(dis_percentage=lambda x: x.length * x.Width)
print(df2)

#add new column to specific position
df1.insert(0,'Circle',circle)
print(df1)

#count no of rows and column

row=len(df1.index)
print(row)
row=len(df1.axes[0])

column=len(df1.axes[1])
print(column)

row=df1.shape[0]
print(row)
column=df1.shape[1]
print(column)

#to get first and 3rd row of dataa frame
df2=df1.iloc[[1,3],[1,3]]
print(df2)

#write pandas program to select area between 15 and 20
print("area between 15 and 20")
df2=df1[df1['Area'].between(15,20)]
print(df2)

#check if there is null value
print(df1[df1["Compactness"].isnull()])

#check if area is less than 10
print(df1[df1["Area"]<15])

#write pandas program to change the score 

print("change the area in 3rd row")
df1.loc[3,"Area"]=11.5   #important
print(df1)

#calculate sum
print(df1["length"].sum())

#calculate mean
print(df1["Area"].mean())

#add row
df1.loc[210]=[15,20,45.3,34,22,45,89,10]
df1
df1.columns

#sort
df1=df1.sort_values(by=["Area"],ascending=[False])
df1=df1.sort_values(by=["Width"],ascending=[True])

#replace name
df1["len_ker_grove"]=df1["len_ker_grove"].replace(5.089,5)
df1

# to change "3" to "three" in type column
df1["Type"]=df1["Type"].map({3:"three",1:"one",2:"two"})

#add column
import random
circle=[]
for i in range(210):
    circle.append(random.randrange(1,100))
df1["Circle"]=circle

#pandas program to iterate over rows
for index,row in df1.iterrows():
    print(row["Area"],row["Width"])


















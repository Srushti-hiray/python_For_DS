# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:37:49 2023

@author: icon
"""

import pandas as pd
df=pd.read_csv("C:/CSV files/ethnic diversity.csv")
df

df.dtypes

#type casting
#converting float into int
df.Salaries=df.Salaries.astype(int)
df.dtypes
df.age=df.age.astype(float)


##identifing duplicate

df_new=pd.read_csv("C:/CSV files/education1.csv.xls")
df
duplicate=df_new.duplicated()
duplicate
sum(duplicate)

#duplicate -true
#not duplicate-false

df_new1=pd.read_csv("C:/CSV files/mtcars_dup.xls")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#row 17 is dup of 2

### drop
#drop_duplicates()

df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

# outliers treatment
import pandas as pd
df=pd.read_csv("C:/CSV files/ethnic diversity.csv")
df
df.shape

import seaborn as sns
sns.boxplot(df.Salaries)
#there as outlier now check in age column
sns.boxplot(df.age)
#no outlier

IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#IQR are not seen in variable explorer bcoz it is capital
iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)


lower_limit=df.Salaries.quantile(0.25)-1.5*iqr
upper_limit=df.Salaries.quantile(0.75)+1.5*iqr

#make lower limit value in variable explorer make it zero
###############################################
##Trimmming

import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#if there is outlier than true else false
#if > UL or < LL then True or else false
df_trimmed=df.loc[~outliers_df]
df_trimmed.shape

#before shape was  (310, 13) after removing outlier (306, 13)
##here we loss the data so we can go for replace

############################################
#
#replacement technique

df.describe()
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if values are greater tahn UL tahn replace it by UL
#if values are less than LL then replace by LL
#else keep salaries as it is

sns.boxplot(df_replaced[0])

#############################################
#Winsorizer

from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method="iqr",
                  tail="both",
                  fold=1.5,
                  variables=["Salaries"])
df_t=winsor.fit_transform(df[["Salaries"]])
sns.boxplot(df["Salaries"])
sns.boxplot(df_t["Salaries"])

##########################################
##Zero variance and near zero variance
'''
If there is no variance in the feature, then ML model will
not get any intelligence, so it is better to ignore those features'''

import pandas as pd
df=pd.read_csv("c:/2-dataset/ethnic diversity.csv")
df.var()

'''Here EmpID and Zip is nominal data
salary has 4.441953e+08 is 4441953000 which is not close to 0
similary for age both are having considerable variance
'''
df.var()==0
#none of them is equal to 0
'''
EmpID       False
Zip         False
Salaries    False
age         False'''

#axis=0 means rows 
#axis=1 means columns
df.var(axis=0)==0
'''
EmpID       False
Zip         False
Salaries    False
age         False'''

################ bins ###################

data=pd.read_csv("C:/CSV files/ethnic diversity.csv")
data["Salaries_new"]=pd.cut(data["Salaries"],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=["low","high"])
data.Salaries_new.value_counts()
# in above code we will divide the salaries in 2 parts , min to mean and mean to max

data["Salaries_new"]=pd.cut(data["Salaries"],bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)],labels=["group1","group2","group3","group4"])
data.Salaries_new.value_counts()

#################################################

#popular techique for encoding
#preparing for ordinal and nominal data
import numpy as np
import matplotlib.pyplot as pli
animal=pd.read_csv("C:/CSV files/animal_category.csv")
animal.shape
animal.drop(["Index"],axis=1,inplace=True)
animal.shape
#here we are getting 10 rows and 14 columns
#we are getting 2 columns for homly and gender so we will delete 1 column from homely and gender
animal_new=pd.get_dummies(animal)
animal_new.drop(["Gender_Male","Homly_Yes"],axis=1,inplace=True)
animal_new.shape
animal_new.rename(columns ={"Gender_female":"Gender","Homly_No":"Homly"},inplace=True)


#######################################

df=pd.read_csv("C:/CSV files/modified ethnic.csv.xls")
df.shape
df.drop(["Index"],axis=1,inplace=True)
df.shape

df_new=pd.get_dummies(df)
df_new.shape

##############################################
#encoding technique
#one hot encoder
#drawback : we need to rename column name after transforming
data=pd.read_csv("C:/CSV files/ethnic diversity.csv")
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()

#we have salary and age column as numeric so we will make them in 1st position 0 and 1 
#to make futher data  preprocessing
data.columns
data=data[['Salaries', 'age','Employee_Name', 'EmpID', 'Position', 'State', 'Zip', 'Sex','MaritalDesc', 'CitizenDesc', 'EmploymentStatus', 'Department','Race']]
#chech fdata frmae in varibale explorer we need only numeric and ordinal 
#data for preprosessing hence skipping 1st and 2nd column
enc_data=pd.DataFrame(enc.fit_transform(data.iloc[:,2:]).toarray())

##############################################
#label encoding
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
#craeting instance of label
labelencoder=LabelEncoder()
#split data into input and output varibales
x=data.iloc[:,0:9] ##first eight column x and 9 in y
y=data["Race"]
data.columns
#we have nominal data Sex,MaritialDesc,CitizenDesc
#we want to convert to label encoder 

x["Sex"]=labelencoder.fit_transform(x["Sex"])
x["MaritalDesc"]=labelencoder.fit_transform(x["MaritalDesc"])
x["CitizenDesc"]=labelencoder.fit_transform(x["CitizenDesc"])

y=labelencoder.fit_transform(y)
#it is arrya
y=pd.DataFrame(y)
data_new=pd.concat([x,y],axis=1)
#y do naot have column names
data_new=data_new.rename(columns={0:"Race"})

#####################################################

#standerdization
#standard normal distributed data we will get
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/CSV files/mtcars_dup.xls")
d.describe()
a=d.describe()
#initialize the scalar

scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()

#####################################################

#normalization
ethnic=pd.read_csv("C:/CSV files/ethnic diversity.csv")

ethnic.columns
ethnic.drop(['Employee_Name', 'EmpID','Zip'],axis=1,inplace=True)

al=ethnic.describe()
#check al dataframe
#yoy find minimum salary is 0 and maximum is108304
#same for age there is hude difference
#1st we will convert non numeric data to label encoding 
ethnic=pd.get_dummies(ethnic,drop_first=True)
#normalization written where ethnic arguments are passed
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
df_norm=norm_fun(ethnic)
b=df_norm.describe()
#if u will observe the b frame, it has dimensions 8,81 earlier in a there 
#were 8,11 it is because all non numeric
#daat has been converted to numeric using label encoding























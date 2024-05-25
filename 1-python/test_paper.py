# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:07:58 2023

@author: icon
"""

#1)
lst=[]
if len(lst)==0:
    print("list is empty")
else:
    print("not empty")
    

#2)
lst=[1,2,3]
lst2=[i*i for i in lst]
print(lst2)


#3)
dict={1:"one",2:"two",3:"three"}
key=int(input("enter key"))
flag=0
for i in dict:
    if i==key:
        flag=1
        print("key is present")
        break
    else:
        if flag==1:
            break
        else:
            print("not present")
        

#4)
a=range(100,160,10)
dict={x:x/100 for x in a}
print(dict)


#5)
import pandas as pd
tech={
      "courese":["python","java","cpp"],
      "fee":[3000,2000,1000],
      "duration":["50days","30days","10days"]}
df=pd.DataFrame(tech)
tutor=["sai","om","siddhi"]
df["tutor"]=tutor
print(df)


#6)to csv
df.to_csv("tech.csv")


#7)
def operation():
    a=10
    d=20
    c=a+d
    b=a*d
    yield c,b
next(operation())


#8)
y=lambda a,b:a*b
y(10,20)

def operation(a,b):
    return a*b
operation(10,20)


#9)
import numpy as np
arr=np.array([1,2,3])
a=any(arr)
print(a)


#10)write a program to plot two or more lines and set line markers

import matplotlib.pyplot as plt
a=np.arange(1,40)
plt.plot(a,a*1.5,"y",a,a*5,"o",a,a*3,"D")


#10)
a=["python","java","cpp","c","c#","sql"]
b=[22.2,23.7,8.8,8,7.7,6.7]
plt.bar(a,b)

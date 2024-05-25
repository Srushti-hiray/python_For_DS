# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:02:49 2023

@author: icon
"""

#write a python function that takes 2 list and returns True
# if they have at least one common member

def check(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i==j:
                return True
            else:
                return False
check([1,1,3],[1,4,6])

#use list comprehension to construct a new list but add 6 to each item
lst=[1,4,5,6]
lst1=[x+6 for x in lst]
print(lst1)


#write a python program to reverse a string
str="kefuhwil"
print(str[::-1])

#write a python program to iterate over dictionaries using for loop

dict={1:"one",
      2:"two",
      3:"three"}
for i,j in dict.items():
    print(i,":",j)

#using dict comprehension and conditional arguments create a dictionary from
# the current dictionary where only the key-value pairs with value above 2000
#are taken to the new dictionary
dict={1:2000,2:300,3:2300,4:90,5:3000}
dic={x:y for x,y in dict.items() if y>2000}
print(dic)

#open the file data.txt using file operation

# write python program to filter a list of integers using lambda
import pandas as pd
import numpy as np
names={"name":["anna","Dinu","Ramu","ganu","emily","mahesh","jayesh","venkat","ajay","dhanesh"],
       "score":[12.3,8,23,np.nan,3,34,56,4,5,2]}

df=pd.DataFrame(names)

print(df)






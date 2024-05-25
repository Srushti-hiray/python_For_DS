# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:23 2023

@author: icon
"""

#exception are handled with try catch block
#habdling the zeroDivisionError exception 


# usig try except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print(" u cannot divide by zero")

######################################################
    
a=5
b=6
c=a-b

try:
    print(5/0)
except ZeroDivisionError:
    print(" u cannot divide by zero")
    print(c)
######################################################


filename='alice.txt'
try:
    with open (filename,encoding='uft-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"sorry the file {filename} does not exit")

#####################################################

































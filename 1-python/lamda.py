# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:17:39 2023

@author: icon
"""

# anonimous function

def add(a,b,c):
    result=a+b+c
    return result
print(add(1,2,3))
add =lambda a,b,c:a+b+c
add(1,2,3)

def mul(a,b,c):
    result=a*b*c
    return result
print(add(1,2,4))
add =lambda a,b,c:a*b*c
add(1,2,4)

        ######          ##############           ######
val=lambda *args:sum(args)
val(1,2,3,4)
val(3,4,6)

        ######          ##############           ######
        
val=lambda **data:sum(data.values()) 
val(a=1,b=2,c=4)

        ######          ##############           ######
        
max=lambda a,b:a if (a>b) ##error
print(max(9,8)) 

        ######          ##############           ######
        
max=lambda a,b:a if (a>b) else b
print(max(9,8))

##############################################

#keyword argument

def person(name,**data):
    print(name)
    print(data)
person(name="navim",age=19,place="mumbai",mob=87466576)


def person(**data):
    print(data)
person(name="navim",age=19,place="mumbai",mob=87466576)

def person(name,**data):
    print(name)
    for i, j in data.items():
        print(i,j)
person(name="navim",age=19,place="mumbai",mob=87466576)





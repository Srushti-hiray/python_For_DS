# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:03:12 2023

@author: icon
"""

###################  list comprehension   ######################
#imp interview perspective
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#we can write same using list comprehension
lst=[num for num in range(0,20)]
print(lst)
#this is called as list comprehension

#modifying using list comprehension
#capitalize method using list comprehension
#its going to make first letter capital
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

#list comprehension with if statement
#when there is if satatement we need to write it on right side
#of for loop
#even no will be updated
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

#to display no in fashion 00 01 10
#for loop using comprehension
lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)

#######################  Set comprehension ###############
#set comprehension
#same logic but curly braces
set_one={x for x in range(3)}
print(set_one)

##################### dictionary comprehension  ################
dict={x:x*x for x in range(3)}
print(dict)

######################## GENERATOR  ############################
#generator
#it is another way of treating iterators
#it uses the keyword 'yield'
#just like fun returns multiple values
#to return multiple values it uses 'yield' instead of return
#one objectwill be created and u can access the values using
#for loop
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

#other way of accessing values using gen
#step by step u can aacess the values
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

#y tuples are not used, for list ,set , dict it was not
#creating obj but for tuples an obj is created

#fun that returns multiple values
def range_even(end):
    for num in range(0,end,2): #instead of using for in range
    # we r using fun name
        yield num
for num in range_even(6):
    print(num)
    

# this fun is gen some values hence acting like generator

#now instead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
next(gen)

#chaining generators
#ele*'*'
def lengths(itr):
    for ele in itr:
        yield len(ele)
        #this part is to count the len of passwd
def hide(itr):
    for ele in itr: 
        yield ele*'*'
        #this part is to convert passwd into *
passwords=["not-good","give 'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)

##########################  ENUMERATOR  #########################
# syntax=ennumerate(iterable,start=0)
#printing list with index
lst=["milk","eggs","bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
#same can be implemented using enumerate
lst=("milk","egg","bread")
for index,item in enumerate(lst,start=1):
    print(index,item)
    print(f'{index} {item}')


############   Assignments   ###########

#division with 7
div7=[n for n  in range(1,1000) if n%7==0]
print(div7)


#find all the no from 1-1000 that have 3 in them
three=[n for n in range(0,1000) if'3' in str(n)]
print(three)


#counyt the no of spaces in a string
some_string='the slow  through the slimy swap'
spaces=[s for s in some_string if s==' ']
print(len(spaces))


#create a list of all consonants in the string
sentence='''yellow yaks like yeiling and yawning and yesterday they youlded while eating yuky arms'''
consonants=[c for c in sentence if c not in 'a,e,i,o,u,","']
print(consonants)


#find the common no in to list without using tuple or set
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[a for a in list_a if a in list_b]
print(common)


#get only the numbers in a sentence like'In 19884 there were 13 instances of a protest with over 1000
#faq
sentence='In 19884 there were 13 instances of a protest with over 1000'
words=sentence.split()
result=[number for number in words if not number.isalpha()]
print(result) 


#given no=range(20),produce a list 
result=[]
for n in range(20):
    if n%2==0:
        result.append('even')
    else:
            result.append('odd')
print(result)
#if else condn on left side
#only if right sides
#list comprehension
result=['even' if n%2==0 else'odd' for n in range(20)]
print(result)


#produce a list of tuples consisiting matching no in the given lists
list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)


#find all the words in a string that are less than 4 letters
sentence='On a summer day ramnath sonar went swiming in the sun and his red skin stung'
examine=sentence.split()
result=[word for word in examine if len(word)<=4]
print(result)    


#write a py program to print a specified list 
#after removing the 0th, 4th,5th elements
color=['red','green','white','black','pink','yellow']
color=[x for(i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


#write a py progrm that creates a generator fun that
#yeilds cubes of no from 1 to n.Accept n from the user
def cube_generator(n):
    for i in range (1,n+1):
        yield i**3
#accept input from the users
n=int(input("Input a number:"))
#create the generator object
cubes=cube_generator(n)
#iterate over generators
print("Cubes of no from 1 to ",n)
for n in cubes:
    print(n)

#write a py program to implement a genertor that 
#generates random no within a given range
import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start,end)
        
#accept ip from the user
n=int(input("Input a number:"))
#create the generator object

#write a py program to generate 3*4*6 3d arrray whose each element
# if 2 square braces then it is 2d vector 3 then 3d
array=[[['*'for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#write a py program to print the no of a specified list after removing even no from it
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)



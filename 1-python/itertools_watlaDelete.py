# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



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


###############################################################

#division with 7

div7=[n for n in range(1,1000) if n%7==0]
print(div7)

#to find no from 1 to 100 which include 3

three= [n for n in range(0,1000) if '3' in str(n)]
print(three)

# count the no of spaces in string
#space=' '

some_string="the slow solid swam sumptuousliy  through the slimp swamp"
spaces=[s for s in some_string if s== " "]
print(len(spaces))

############################################################

# create a list of all consonants in a string 
#"yellow yaks like yelling and yawing and yesterday they yoled while 
#eating yuky yams

sentence="yellow yaks like yelling and yawing and yesterday they yoled while eating yuky yams" 
const=[n for n in sentence if n not in 'a,e,i,o,u," "']
print(const)


#\n is considered as sentence get stared in next line 

sentence='''yellow yaks like yelling and yawing and
 yesterday they yoled while eating yuky yams'''
const=[n for n in sentence if n not in 'a,e,i,o,u," "']
print(const)

#find the common no in two list witthout using tuplt or set
a=[1,4,6,7]
b=[4,1,8,5]
common=[com for com in a if  com in b]
print(common)

# it will take one number in a and compare with all the numbers
# in the b

#############################################################

#####&&&&&&&&& ready reference $$$$$$$$$$$

# get only the numbers from the sentence
#"in 1984 there was 13 instanes of a protest with over 1000"

sentence="In 1984 there was 13 instanes of a protest with over 1000"
words=sentence.split()
result=[ number for number in words if not  number.isalpha()]
print(result)

#############################################################


#when only if then right of for loop
#when if and else then on left of for loop
# given numbers=range(20), produce a list containing even and odd no. sepearte
result=[]
for i in range(0,20):
    if i%2==0:
        result.append("even")
    else:
        result.append("odd")
print(result)

##list comprehension
result=["even"if n%2==0 else "odd" for n in range(20) ]
print(result)


############################################################


#produce a list of tuples consisting only matching numbers in these list
# lista =[1,2,3,4,5,6,7,8,9] listb=[2,7,1,12]

lista =[1,2,3,4,5,6,7,8,9]
listb=[2,7,1,12]
result=[(a,b) for a in lista for b in listb if a==b]
print(result)


# find matching words in two sentences

a="an apple a day keeps doctor way"
b=" keep that doctor way from me"
asplit=a.split()
bsplit=b.split()
result=[(a,b) for a in asplit for b in bsplit if a==b ]
print(result)


# find all the words in string that are less tahn 4 letters
sentence="hello world how it is going"
examine=sentence.split()
result=[word for word in examine if len(word)<=4]
print(result)

# write python profram to print specified list after removing 0th, 
#4th, 5th element
color=["red","green","yellow",'pink',"blue","black","white"]
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#############################################################


# write a python program that create generator fun that yields cube of numbers from 1 to n,accept
# n from user

def cube_generator(n):
    for i in range(1,n+1):
        yield i**3
n=int(input("enter number"))

#create generator object
cubes=cube_generator(n)

#iterate over generator and print the cubes
for cube in cubes:
    print(cube)

#############################################################


# write python program to implement generator which generates randon number
import random
def ran_num_gene(start,end):
    while True:
        yield random.randint(start,end)
        
#accept the start and end
start=int(input("enter the start"))
end=int(input("enter the end"))

random_number=ran_num_gene(start,end)
for _ in range(10):
    print(next(random_number))
    

############################################################
"""
[[]]=2 dimensional vector
[[[]]]=3 dimensional vector
[[[[]]]]= tensor
"""
# write a python program to generate 3*4*6 3D array whose each element 
# is *

array=[[["*" for col in range(6)]for col in range(4)]for row in range(3)]
print(array)

#write a python program to print the specified no, of list 
#after removing even numbers

num=[1,2,3,4,56,7,9]
result=[a for a in num if  a%2!=0]
print(result)

##############################################################

# use of zip function

name=["dada","mama","kaka"]
info=[9850,9346,8632]
for nm,inf in zip(name,info):
    print(nm,inf)


name=["dada","mama","kaka","papa"] # ignores papa as it is excess 
                                    # item
info=[9850,9346,8632]
for nm,inf in zip(name,info):
    print(nm,inf)

# zip_longest will resolve such problem

#from itertools import zip_longest
import itertools
name=["dada","mama","kaka","papa"] 
info=[9850,9346,8632]
for nm,inf in itertools.zip_longest(name,info):
    print(nm,inf)


# replace none value with 0 

from itertools import zip_longest

name=["dada","mama","kaka","papa"] 
info=[9850,9346,8632]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

######################################################

# all()    
lst=[2,5,7,3,-1,0]
if all(lst):
    print("all values are true")
else:
    print("false")


########################################################

# any()

lst=[0,0,None,9]
if any(lst):
    print(" it has some value")
else:
    print("useless")

############################################################

#count()

from itertools import count
counter = count()     #starts the counter from 0
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter = count(start=5)     #starts the counter from 5
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter = count(7)     #starts the counter from 7
print(next(counter))
print(next(counter))
print(next(counter))


###############################################################

#cycle()

import itertools
instructions=['eat',"code","sleep"]
for instruction in itertools.cycle(instructions):
    
        print(instruction)


################################################################

# repeat()

from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)


    
################################################################

# combinations()

from itertools import combinations
players=["jay","sai","ram"]
for i in combinations(players,2):
    print(i)

################################################################

# permutations()

from itertools import permutations
players=["jay","sai","ram"]
for i in permutations(players,2):
    print(i)

################################################################

#product()

from itertools import product
team_a=["siddhi","anushri","sakshi"]
team_b=["sanika","trupti","srushti"]
team_c=["sanika","trupti","srushti"]
for i in  product(team_a,team_b,team_c):
    print(i)

##############################################################

#filter()

age=[18,17,21,80]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

##############################################################

#shallow copy and deep copy

list_a=[3,6,10,14]
list_b=list_a

list_a[0]=2      # we made change in a the same change will be 
                    #reflected in list b
print(list_a)
print(list_b)

# shallow copy

import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)  # we made change in a the change will  not be 
                     #reflected in list b
list_a[0]=10
print(list_a)
print(list_b)

# nested list 
import copy
list_a=[[1,2,3,4],[5,6]]
list_b=copy.copy(list_a )   # we made change in a the same change will be 
                    #reflected in list b
list_a[1][0]=8
print(list_a)
print(list_b)

                        ###################
                        
#deep copy

import copy
list_a=[[1,2,3,4],[5,6]]
list_b=copy.deepcopy(list_a )   # we made changes in a the changes will not be 
                    #reflected in list b
list_a[1][0]=8
print(list_a)
print(list_b)

##################################################################

#assignments

#write a python program to create iterator from several iterator in  
#a sequence and display type and element of iterator

from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result=chain_fun([1,2,3],["ab","cd"],[4,5])
print("type of new iterator")
print(type(result))
print("elements in iterator")
for i in result:
    print(i,end=" ")

# same can be done for Tuple 

from itertools import chain
def chain_fun(tup1,tup2,tup3):
    return chain(tup1,tup2,tup3)
result=chain_fun((1,2,3),("ab","cd"),(4,5))
print("type of new iterator")
print(type(result))
print("elements in iterator")
for i in result:
    print(i,end=" ")


# write python program that generate the running product of 
#elements in an iterable

from itertools import accumulate
import operator
def runing_product(lst):
    return accumulate(lst,operator.mul)
result=runing_product([1,2,3,4])
for i in result:
    print(i)


from itertools import accumulate
import operator
def runing_product(tup):
    return accumulate(tup)  #by default function is addition
result=runing_product((1,2,3,4))
for i in result:
    print(i)

# write python porgram to construct an infinite iterator that returns evenly 
#space values starting with specified number and steps

import itertools as it
start=10
step=1
print("the starting number is",start, "and step is" ,step)
my_counter=it.count(start,step)
# following loop will run forever
for i in my_counter:
    print(i)

#write python program to genearte infinite cyle of elememt 
#from an iterable

import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data((1,2,3,4))
for i in result:
    print(i)

import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data("hello world")
for i in result:
    print(i)

# write an python program to make an iterator thet drops elements
#from the iteratable as soon as an element is an positive no

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0,nums)
nums=[1,2,3,-2,-5,8,0,-1,-9]
print("orignal list",nums)
result=drop_while(nums)
print("drops the elements when positive no arises\n",list(result))
for i in result:
    print(i)




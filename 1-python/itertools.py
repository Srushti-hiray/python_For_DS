# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:35:45 2023

@author: icon
"""

#use of zip fun
name=['dada','mama','kaka']
info=[9850,6832,8149]
for nm,inf in zip(name,info):
    print(nm,inf)


#use of zip fun with mismatched list
   #it will not display the excess items and this is drawback of zip fun
name=['dada','mama','kaka','baba']
info=[9850,6832,8149]
for nm,inf in zip(name,info):
    print(nm,inf)


#other feature in py is ZIP LONGEST
#here non assigned value will be none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6832,8149]
for nm,inf in zip_longest(name,info):
    print(nm,inf)


from itertools import zip_longest
name=['dada','mama','kaka','baba','kaka']
info=[9850,6832,8149]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
#eg of zip fun


#use of fill value instead of none
#none values sometimes create some problem
#replace none values with 0

from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6832,8149]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)


#use of all(),if all the values are  non zero, None (true) then it will produce output

lst=[2,-3,6,9,None]
if all(lst):
    print('all the values are true')
else:
    print('useless')

#if zero is present
lst=[2,-3,6,9,0]
if all(lst):
    print('all the values are true')
else:
    print('useless')


#any fun()
#use of any if any one is positive
lst=[2,0,0,0,1,0]
if any(lst):
    print('all the values are true')
else:
        print('useless')

lst=[0,0,0]
if any(lst):
    print('all the values are true')
else:
    print('useless')

#count fun()
#used to count currency and many other
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


#cycle()
#suppose u have repeated tsks to be done then u can use this method
import itertools
instructions=("Eat","Code","SLEEP")
for instruction in itertools.cycle(instructions):
    print(instruction)
 
    
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)    

from itertools import repeat
for msg in repeat("keep patience"):#infinite
    print(msg)    

########################################
#permutation
#permutation relates to act of arranging all the members of a set into some sequence 
#or order.
#combination
#combination is a way of selecting items froma a collection such that(unlike permutation)
#the order of selction does not matter.

#combinations()
from itertools import combinations
player=['ram','sita','lakshman']
for i in combinations(player,2):
    print(i)

from itertools import permutations
player=['ram','ram','sita','lakshman']
for i in permutations(player,2):
    print(i)

######################################
#product()
#to pair 2 teams or 2 lists
from itertools import product
team_a=['ram','lakshman','sita']
team_b=['krishna','balram','radha']
for pair in product(team_a,team_b):
    print(pair)

#filter(bussiness logic,collection type)

#passing fun as alambda fun and a list
age=[27,19,21,17]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])
#to filter the entities we use filter

################# assignments ########################

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:56:44 2023

@author: icon
"""

#write a py program to create an iterator from several iterables 
#in a sequence and display type and element of a iterator
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result=chain_fun([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("type of the new iterator:")
print(type(result))
print("elements of the new iterator:")
for i in result:
    print(i)

#tuple
result=chain_fun((10,20,30),('a','b','c','d'),(40,50,60,70,80,90))
print("type of the new iterator:")
print(type(result))
print("elements of the new iterator:")
for i in result:
    print(i)


#write a py prog that generates the running product of elements in iterable
#accumulate()-this iterator takes 2 arguments ,iterable target and the fun which would be followed at#
#at each iteartion of value in the target.
#if no fun is passed then by default addition takes place
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result=running_product([1,2,3,4,5,6,7])
print("Running product of list")
for i in result:
    print(i)


#write a py program to construct an infinite iterator that returns
#evenly spaced values starting with a specified number nd step.
import itertools as it 
start=10
step=1
print("The starting number is ",start,"and step is ",step)
my_counter=it.count(start,step)
#fol loop will run for ever
print("The said fun print never-ending items:")
for i in my_counter:
    print(i)


#write python program to generate an infinite cycle of elements from an iterable
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#foll loops will run for ever
#list
result=cycle_data(['A','B','C','D'])
print("The said fun print never-ending items:")
for i in result:
    print(i)


#string
result=cycle_data('Python itertools')
print("The said fun never-ending items:")
for i in result:
    print(i)


#write an py program to make an iterator taht drops elements from the iterable
#as soon as an element is a positive no
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0,nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("Original list:",nums)
result=drop_while(nums)
print("Drop elements from the iterable when positive no arises \n",list(result))
for i in result:
    print(i)

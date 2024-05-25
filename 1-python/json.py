# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:04:39 2023

@author: icon
"""

#javascript object notation(json) store information 
#in form of dictionary

"""
json's formate qas orignalli developed by javascript
many of your programs will ask user to input certain kinds 
of information, you might allow user to store preferences or details
in this case u will have to store information in a single way to do
this is using json
"""
# using json.dump() and json.load()

import json
numbers=[2,3,5,7,11]
filename="numbers.json"
with open(filename,"w") as f:
    json.dump(numbers,f)
    
#######################################################

import json
username1=input("what is ur name?")
filename='username1.json'
with open(filename,"w") as f:
    json.dump(username1,f)
print(f"we will remember you when you come back {username1}")

########################################################

# now lets write program that greets a user whose
# name already has been stored

import json
filename='username1.json'
with open(filename) as f:
    username1=json.load(f)
print(f"welcom back {username1}")

#######################################################

# load username ,if it has been stored previously
#else prompt for username and store it
import json
filename='username1.json'
try:
    with open (filename) as f:
        username1=json.load(f)
except FileNotFoundError:
    username1=input("what is ur name")
    with open (filename,'w') as f:
        json.dump(username1,f)
        print(f"we will remember you when you come back {username1}")
else:
    print(f"welcom back {username1}")

########################################################

#write a python script to add a key to dictionarry
#sample dictionary :{0:10,1:20,2:30}
#expectrd result : {0:10,1:20,2:30}


d={0:10,1:20}
print(d)

d.update({2:30})
print(d)

###################

"""
write python script to concatenate followind dictionries:
    sample dictionary:
        dic1={1:10,2:20}
        dic2={3:30,4:40}
        dic3={5:50,6:60}
"""
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)

#########################################################

"""
to check whether key already excits in dictionary

"""
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_present(x):
    if x in d:
        print("key is present")
    else:
        print("key is not present")
key_present(9)

########################################################

""" to iterate over dictionary over for loop
"""
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key,value in d.items():
    print(key,":",value)

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for i in d:
    print(,":",i.values())






















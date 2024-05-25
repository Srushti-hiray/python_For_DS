# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:15:00 2023

@author: icon
"""

import string

adjective=["good","exellent","fast","slow","dirty",
           "clean","impressive","bc",]

noun=["siiddhi","bhurakne","turkane","kurkure","sursure",
      "guddhi","shiddhi"]
import random
#pick the adjective and noun
adjective=random.choice(adjective)
noun=random.choice(noun)
number=random.randrange(1,100)
spl_char=random.choice(string.punctuation)

password=adjective +  noun +str(number) + spl_char
print("ur new password is :%s"% password)

           #############################
import string
while True:
    adjective=["good","exellent","fast","slow","dirty",
               "clean","impressive","bc",]

    noun=["siiddhi","bhurakne","turkane","kurkure","sursure",
          "guddhi","shiddhi"]
    import random
    #pick the adjective and noun
    adjective=random.choice(adjective)
    noun=random.choice(noun)
    number=random.randrange(1,100)
    spl_char=random.choice(string.punctuation)

    password=adjective +  noun +str(number) + spl_char
    print("ur new password is :%s"% password)
    response=input("do you want to generate more[y/n]")
    if response=="n":
        break
    
#######################################################
#check is password is good or not
#atleat one uppercase,one lowwercase,special character, 8 character
import string
def checkpassword(password):
    has_upper = False
    has_lower =False
    numic=False
   
    for ch in password:
        if(ch>="A" and ch<="Z"):
            has_upper=True
        elif(ch>="a" and ch<="z"):
            has_lower=True
        elif(ch>="0" and ch<="9"):
            numic=True
        if((len(password)>=8) and has_upper and has_lower and numic ):
          return  True
    else:
        return False
a=input("enter:")

checkpassword(a)   
if (checkpassword(a) ==True):
    print("strong password")
else:
    print("weak password")
    
###################################################

#using generator hiding the  random password

import string
while True:
    adjective=["good","exellent","fast","slow","dirty",
               "clean","impressive","bc",]

    noun=["siiddhi","bhurakne","turkane","kurkure","sursure",
          "guddhi","shiddhi"]
    import random
    #pick the adjective and noun
    adjective=random.choice(adjective)
    noun=random.choice(noun)
    number=random.randrange(1,100)
    spl_char=random.choice(string.punctuation)

    password =adjective +  noun +str(number) + spl_char
    def lengths(password):
        for ele in password:
            yield len(password)
            #this part is to count the len of passwd
    def hide(password):
        for ele in password :
            yield ele*'*'
            #this part is to convert passwd into *
    print(password)
    a=hide(lengths(password))
    print(next(a))
    
    response=input("do you want to generate more[y/n]")
    if response=="n":
        break
#################################################################

#using generator hiding the password

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







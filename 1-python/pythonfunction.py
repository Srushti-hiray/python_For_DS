# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:17:13 2023

@author: icon
"""

##############################################
#functions
def prime(num):
    for i in range (2,num):
        if num%i==0:
            return "the number is not prime"
            break
        
    return "the number is prime"
num=int(input("number"))
prime(num)
#############################################
def hello():
    print("hi")
hello()
#############################################
def table(a):
    for i in range (1,11):
        print(a*i,end=" ")
table(5)
############################################
def add(name):
    print(f"my name is {name}")
add("srushti")

def add(name,age):
    a="my name is {} and my age is {}"
    print(a.format(name,age))
add("srushti",19)

############# format  ###########################

def add(name,age=19):
    a="my name is guu {} having age {}"
    print(a.format(name,age))
add('siddhi')

#############  direct ######################

def add(name,age=19):
    print(f"my name is guu {name} having age {age}")
    
add('siddhi')

########### 00000 11111 ####################

def add(name,age=19):
    a="my name is guu {0} having age {1}"
    print(a.format(name,age))
    
add('siddhi')
####################################################
def life(age,month,day):
    age1=365*age
    month1=30*month
    add=age1+month1
    add1=add+day
    year1=29200-add1
    print(year1)
    print(year1/365)
   #if(months==1 or months==3 or months==5 or months==7 or months==9 or months==11):
    yearfinal=year1//365
    daysfinal=year1%365
   # elif(months==2):
    
    fmon=daysfinal//30
    fday=daysfinal%30
    
    print(f"No.of year person will live is {yearfinal},{fmon} months and {fday} days")     
    
   # elif(months==4 or months==6 or months==8 or months==10 or months==12):"""
        
    #print("you will live until next",a,"years",b,"months",c,"days")
year=int(input("enter your age year"))
mon=int(input("enter your age month exceeds year"))
d=int(input("enter your age days exceeds month"))
#print("select current month:\n1)jan\n2)feb\n3)mar\n4)april\n5)may\n6)june\n7)july\n8)august\n9)september\n10)oct\n11)nov\n12)dec")

life(year,mon,d)
#######################################################
#Roller coaster
print("welcome to the roller coaster")
h= int(input("enter height of person"))
a= int(input("enter age of person"))
if(h>=120):
    if(12<=a<=15 and h>=120):
        print("price of ticket is 15")
    elif(a<12):
            print("price of ticket is 10")
    elif(a<18):
        print("price of ticket is 20")
    elif(a>18):
        print("price of ticket is 50")
    
    
else:
    print("ur not eligible")
    
#######################################################
      
users=["employee","staff","clerk","manager"]
print(users)
user=input("enter")
for user in users:
    if user=="employee":
        print("hello employee")
    elif user=="staff":
        print("hello staff")
        
    elif user=="clerk":
        print("hello clerk")
    else:
        print("hello manager ")
######################################################

 
print("******welcome to pizzahut******")  
pizza=input("enter size of pizza \n1)small\n2)mid\n3)large:")         
extra=input("do u want to add extra pepper[y/n]:")

if(pizza=="small"):
    if(extra=="y"):
        price=17
    else:
        price=15
elif(pizza=="mid"):
    if(extra=="y"):
        price=23
    else:
        price=20
    
   
elif(pizza=="large"):
    if(extra=="y"):
        price=28
    else:
        price=25
cheeze=input("do u want to add extra cheeze[y/n]:") 
if(cheeze=="y"):
     print(f"ur price is :{ price+1}")
else:
     print(f"ur price is : {price}")
     
#############################################

#passing dictionary in function

def user(first_name,last_name):
    person={"first name":first_name,"last name":last_name}
    return person

music=user('ram','setu')
print(music)

###############################################

#passing list

def user(name):
    for i in name:
        print("hello",i)
        
names=["siddhi","trupti"]
user(names)

##############################################

#passing arbitary arguments

def make_pizza(size,*toppings) :
    for topping in toppings:
        print(size,topping)
        
make_pizza(16,"toppings")
make_pizza(12,"toppings","cheese","green pepper")
        
###############################################



#scope of variable
x=x+1
x=6
print(x)
#you cannot call the variable before initializing 
 
#############################################


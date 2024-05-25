# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""
print("hello")
print(2+3)
##############################
age=input("enter age:")
print(type(age))
print(age)
age2=input("enter age2:")
print(type(age2))
print(age2)
print(age+age2)
##################################
age=int(input("enter age:"))
print(type(age))
print(age)
age2=int(input("enter age2:"))
print(type(age2))
print(age2)
print(age+age2)
###################################
#COMPLEX
C1 = 1
C2 = 1j
print(C1.real)
print(C2.imag)
print(C1,C2)
print(type(C1))
print(type(C2))
################################
#NONE DATA TYPE
winner=None
print(type(winner))
###############################
#is and isnot
c=5
print(c is 5)
#################################
amount=float(input("enter amount:"))
if amount>10:
    print("good")
elif amount>40:
    print("better")
elif amount>100:
    print("best")
else:
    print("exellent")
#################################
count=1
print(count)
while(count<10):
    print(count)
    count+=1
##############################
for i in range(1,10):
    print(i)
print("done")
###############################
num=int(input("enter the number"))
for i in range(1,10):
    if(i==num):
        print("found")
        break
    else:
        print(i)
 ###############################
 #print() for new line
for _ in range(1,10):
    print(".",end="    ")
    print()      
 ###############################   
for _ in range(1,10):
    print(".",end="    ")
 ################################
for i in range(1,10):
     if i%2==0:
         continue
     else:
       
         print(i,end=" ")
 ################################
for i in range(1,10):
     if i%2==0:
         print(i,end=" ")
     else:
       continue
##############################
for i in range(2,40,2):
     
         print(i,end=" ")
###############################
for i in range(1,40,2):
     
         print(i,end=" ")
     
###################################
start=int(input("enter start"))
end=int(input("enter end"))
a=int(input("press 1 for even \n press 2 for odd"))
for i in range(start,end):
    if a==1:
        if i%2==0:
            print(i)
        else:
            continue
        
    else:
        if i%2==0:
            continue
        else:
            print(i)
###################################
#PRIME NO
num=int(input("Enter number:"))
b=0
for i in range(2,10):
    if(i!=num):
        a=num%i
        if a==0:
            b=1
       # print("not prime no")
if b==1:
    print("not prime no")
else:
    print("prime no")
##################################
#leap year
num=int(input("Enter year:"))
if num%4==0:
    print("leap year")
else:
    print("not leap year")
################################## 
#PRIME WITH RANGE
start=int(input("enter start"))
end=int(input("enter end"))

for i in range(start,end):
    b=0
    for j in range(2,10):
        
   
        if i!=j:
            a=i%j
            if a==0:
                b=1
               
    if b==0:
        print(i,end=" ")
###############################
num=int(input("enter no of row"))
i=0
j=num
while i<=num:
    while j<=num:
        print("*",end=" ")
    j -=1
i +=1
    
    

 

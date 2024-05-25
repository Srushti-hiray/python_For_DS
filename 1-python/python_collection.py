# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:36:18 2023

@author: icon
"""

##############################################

#collection types tuples,list,dic,set
#holypython.com  hackerank

########&&&&&&&&&&&&&    tuple     ########&&&&&&&&&&&&&&&

tup1=(1,2,3)
print(f"tup1[0] \t {tup1[0]}") 
print(f"tup1[0] \t {tup1[1]}")  
print(f"tup1[0] \t {tup1[2]}") 
 

tup1=(1,2,"a",2,-23.8,1)
for i in tup1:
    print(i,"\t", type(i),end=" ")
    print()
print(len(tup1))        ##########   functions in tuple
print(tup1.count(1))
print(tup1.count(3))

print(tup1.index(1))#at which position the element is
if "a" in tup1:
    print("there is a in tuple")
    
###############      nested tuple       ##############

tup1=(1,2,(3,4),5)
print(f"tup1[0] \t {tup1[0]}") 
print(f"tup1[1] \t {tup1[1]}")  
print(f"tup1[2] \t {tup1[2]}") 
print(f"tup1[3] \t {tup1[3]}") 
    
tup1=(1,2,(3,4),5)
for i in tup1:
    print(i)
print(tup1)    
print(tup1[2][1]) # print 4
tup2=(1,2)
tup1=(3,tup2)
print(tup1)

#it is not possible to add or remove element from tuple

########&&&&&&&&&&&&&    list     ########&&&&&&&&&&&&&&&
 
#list is mutable i.e we can add or delete element

lst1=[1,2,"apple"]
print(lst1)

lst1=[1,2,"apple",[5,'mango']]
print(lst1)
for i in lst1:
    print(i)

lst2=["mngo",3.4]
lst1=[2,"banana",lst2]
print(lst1)

lst1=[1,"srushti","truptuu",6.9]
lst1.append("guddhi")            ####### list function (mutable)####### 
print(lst1)

lst1=[1,"srushti","truptuu",6.9]
lst1.append(["sakshi","anushri"])
print(lst1)#nested list will form

lst1=[1,"srushti","truptuu",6.9]
lst1.extend(["sakshi","anushri"])
print(lst1)#nested list will not form

lst1=[1,"srushti","truptuu",6.9]
lst1.insert(1,"guddhi")
print(lst1)

###########$$$$$$$ list concatenation $$$$$$$##########

lst1=[1,"srushti","truptuu",6.9]
lst2=["2","hiray","nabriya",7]
print(lst1+lst2)

print(f"lst1[0] \t {lst1[0]}") 
print(lst1[1:3])
print(lst1[:3])
print(lst1[1:])

#####################################################

################# ASSIGNMENTS  ######################

#take 5 random no in list and find min and max

lst=[1,8,3,2,4,5]     
print(max(lst))
print(min(lst))
 
#take 5 string in list and make it reverse

lst=["apple","mango","banana","cheery","watermelon"]
print(lst[::-1])

#take 10 no in list write script to search for value
while True:
    lst=[1,2,3,4,5,6,7,8,9,0]

    a=int(input("input:"))
    b=0
    for i in lst:
        if i==a:
            b=1
        
    if(b==1):
            print("word is present")
    else:
            print("word is not present")
    ask=input("do u want to continue:[y/n]")
    if ask=="n":
            break
        
"""
    take 10 no in list insert some duplicate
    n write script to find duplicate
"""

lst=[7,2,2,4,6,6,2,1]
b=[]
counts=0
for i in lst:
    
   a=lst.count(i)
   if a>1:
    b.append(i)
   print(i,"count:",a)
print("duplicates are:",b) 
 
"""
    take 10 no in list insert some duplicate
    n write script to find duplicate
"""

lst=[7,2,2,4,6,6,2,1]
b=[]
counts=0
for i in lst:
    if i not in b:
        a=lst.count(i)
        if a>1:
            b.append(i)
        print(i,"count:",a)
print("duplicates are:",b) 
 

 #take vowel and non vowel and find count of vowel    

lst=["a","e","b","i","c","d","a"]
counts=0
for i in lst:
    if(i=="a" or i=="e" or i== "i" or i=="o" or i=="u"):
        counts=counts+1
print(f"vowel count is:{counts}")   

###########################################################

######################  list  #############################

#### removing from list 

another_list=["srushti","trupti","siddhi","sakshi","anushri"]
another_list.remove("srushti")

print(another_list)

#using pop method (input as index)

another_list=["srushti","trupti","siddhi","sakshi","anushri"]
another_list.pop(0)
print(another_list)

# inserting into list

another_list=["srushti","trupti","siddhi","sakshi","anushri"]
another_list.insert(0,"akshii")
print(another_list)

#################$$$$$$$$  set   $$$$$$$$$#####################

# no dublicate

basket={"apple","mango","orange","grapes","watermelon","grapes"}
print(basket)
print(len(basket))

for item in basket:
    print(item)

basket.add("cheery")
print(basket)

basket.update(["sid","akshada"])  #updating using tuple
print(basket)

basket={"56","12","14","33","82"}
print(min(basket))
print(max(basket))

basket={"apple","mango","orange","grapes","watermelon","grapes"}
basket.remove("apple")
print(basket)

basket.discard("mango")
print(basket)

################ union intersection ###############

s1={"apple","mango","orange","watermelon"}
s2={"grapes","watermelon","grapes"}

print("union",s1 | s2)

print(f"intersection {s1 & s2}")

print("difference",s1-s2)

print("difference",s2-s1)


###########&&&&&&&&&   dictionary    &&&&&&&&&&###########

# unordered and mutable, no duplicates
#dic cannot have two items with samee key

capital={
    "maharashtra":"mumbai",
    "gujrat":"ahemdabad",
    "up":"laknow",
    "karnataka":"banglore",
    "andrapradesh":"hydrabad"}
print(capital)
    
print(capital["maharashtra"])   ####adding
capital["west bengal"]="kolkata"
print(capital)

capital["siddhi"]="guu"
print(capital)

capital.pop('karnataka')#########deleting
print(capital)

del capital['up']
print(capital)


capital={
    "maharashtra":"mumbai",
    "gujrat":"ahemdabad",
    "up":"laknow",
    "karnataka":"banglore",
    "andrapradesh":"hydrabad"}
for state in capital:           ######  displaying only keys
    print(state,end=" ,")

for dict_key,dict_values in capital.items():
    print(dict_key,":",dict_values)        ######  displaying key with values
    print(capital[state])
print(capital.values())
print(capital.keys())
print(capital.items())

## ##checking key membership## ##

capital={
    "maharashtra":"mumbai",
    "gujrat":"ahemdabad",
    "up":"laknow",
    "karnataka":"banglore",
    "andrapradesh":"hydrabad"}
print("maharashtra" in capital)


seasons={"summer":("jan","feb","mar","april"),
        "rainy":("may",'june',"july","aug"),
        "winter":("sep","oct","nov","dec")}
print(seasons)
print(seasons["summer"][2])
print(seasons["summer"])


seasons={"summer":("jan","feb","mar","april"),  ###cannot have same
                                                     #key name
        "summer":("may",'june',"july","aug"),
        "winter":("sep","oct","nov","dec")}
print(seasons)

aplha={"a":"apple",
       "b":"banana",
       "c":"cheery"}
for key in aplha:
    print(key,end=" , ")
    print(aplha[key])

###########################################################

#write python program to add all item in list

lst=[2,5,7,3,1]
sum=0
for num in lst:
    sum=sum+num
print("sum",sum)

def sum_list(items):          ##addition using function
    sum=0
    for num in items:
        sum=sum+num
    return sum
print(sum_list([3,6,8]))

#write python program to mul all item in list

def mul_list(items):          ##mulipling using function
    mul=1
    for num in items:
        mul=mul*num
    return mul
print(mul_list([3,6,2]))

#write python program to get largest no and smallest no from list

def large_list(items):
    print("max",max(items))
    print("min",min(items))
large_list([3,7,4,9])

############################################

#write python program to count no of string which satisfies
#the condition that string lenght is 2 or more and the
# first and last characters must be same from given list of strings.
#given list["abc","xyz ,"aba","1221"]

lst=["abc","xyz" ,"aba","1221","bab"]
count=0
for i in lst:
    if((len(i)>=2) and i[0]==i[-1]):
        count+=1
print("count",count)

############################################  

"""
write a python program to get a list ,sorted in 
increasing order by the last element in each tuple frm given list
of non empty tuple;
sample list : [(2,5),[1,2],(4,4) ,(2,3),(2,1)]

expected result: [(2,1),(1,2),(2,3) ,(4,4),(2,5)]

"""
lst =  [(2,5),(1,2),(4,4) ,(2,3),(2,1)]

def last(n):
    return n[-1]
def sort_list(tuples):
    result=sorted(tuples,key=last)
    return result   
    
print(sort_list([(2,5),(1,2),(4,4) ,(2,3),(2,1)]))

############################################

"""
write a program to remove duplicates from list
""" 

def checklst(items):
    lstn=[]           
    
    for item in items:
        if item not in lstn:
            a=items.count(item)
            if a>1:
                lstn.append(item)
    return lstn        
print(checklst([1,2,2,5,5]))

############################################

"""
removing repeated items
"""
lst1=[10,20,10,20,30,40]
st1=set(lst1) #as set remove duplicate item hence list is converted into set
print(st1)
st2=list(st1)
print(st2)

############################################

"""
program to clone or copy list
"""
lst1=[10,20,10,20,30,40]
lstnew=list(lst1)
print(lstnew)

############################################

"""
program to find the list of word that are longer than n frm given
list  of words
"""
def longword(n,str):
    word_len=[]
    txt= str.split(" ")
    for i in txt:
        if len(i)>3:
            word_len.append(i)
    return word_len
print(longword(3,"the quick brown fox jump over lazy dog"))

###########################################

"""
write program that takes two list and return
 true if they have common member

"""

def lst(lst1,lst2):
    for x in lst1:
        for y in lst2:
            if x==y:
                return True
            else:
                return False
lst([1,2,3],[8,4,5])

def lst(lst1,lst2):
    setlst1=set(lst1)
    setlst2=set(lst2)
    if(setlst1 & setlst2):
        return True
    else:
        return False
lst([1,2,3],[2,4,5])       


############################################

"""
write python program to calculate difference between two list
as list1 - list2 and list2- list1 and add both the difference
"""

def lst(lst1,lst2):
    setlst1=set(lst1)
    setlst2=set(lst2)
    diff1=list(setlst1-setlst2)
    diff2=list(setlst2-setlst1)
    print(diff1+diff2)
lst([1,2,3],[2,4,5])       

#############################################

# convert list of character in string

def lst(lst1):
    str=''.join(lst1)
    print(str)
lst(["a","b",'c',"d"]) 
 
lsti=[1,4,6,7]
print(lsti.index(4))

##############################################

#program to append one list to other

lst1=[1,4,6,7]
lst2=[4,7,8]
print(lst1 + lst2)



































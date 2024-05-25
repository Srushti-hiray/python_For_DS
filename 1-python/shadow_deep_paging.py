# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:38:15 2023

@author: icon
"""

################ shallow ,deep copy #####################
#faq
#shallow copies
#deep copies
#lets take an eg
#assignment operation
#this will only create a new variables
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]=-10
print(list_a)
print(list_b)

#shallow copy
#one level deep.Modifying on 1
#creates one level instance and separate obj 1 for list a and other for list 2
#shallow copies create data obj one level deep copy.
#modifying on level one doesnt affect the other list
#in order to create shallow copy copy fun of copy module is used
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
#not affects other list
list_b[0]=-10
print(list_a)
print(list_b)

import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
#not affects other list
list_b[0]=0
print(list_a)
print(list_b)
#other eg 

#2 level deeper list
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affects other
list_a[0][0]=-10
print(list_a)
print(list_b)

#deep copies
#in shallow copies with nested objects modifying on level 2 or deeper
#does affect the other
#full independent clones.use copy.deepcopy()
#2 independent clones are created
#to create deep copy u need to use deepcopy() fun or copy module
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
list_a[0][0]=-10
print(list_a)
print(list_b)

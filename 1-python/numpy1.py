# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:27:26 2023

@author: icon
"""
#numpy is used for scientific computing application
#and it stands for numerical python which consist of multidimentional 
#array

"""
to install numpy= pip install numpy
"""
##########################  numpy #######################
"""
array cannot contain differnt datatype,list may contain different data
type
"""
#create n array
import numpy as np
arr=np.array([10,20,30]) # one dimension
print(arr.ndim)
print(arr)

#create multidimentional array
arr=np.array([[10,20,30],[40,50,60],[1,4,6]])
print(arr.ndim)# two dimension
print(arr)

#use ndmin param to specify how many minimum dimension you wanted
#to create an array with minimum dimension

arr=np.array([10,20,39,40,45,78,23],ndmin=3) # 3 dimension
print(arr)

#change the datatype
#dtype parameter
arr=np.array([10,20,39,40],dtype=complex)
print(arr)

#to get dimension of array  # 2 dimensional
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[2,3,1]])
print(arr.ndim)
print(arr)

#to get array type
arr=np.array([10,20,30])
print("each item is of type ",arr.dtype)

arr=np.array([[1,2,3],[4,5,6]])
print("array size:",arr.size)
print("shape:",arr.shape)

#create sequence of integer using range function
arr=np.arange(0,20,3)
print("a sequence array with step of 3:",arr)

#accessig using index 
arr=np.arange(11)
print(arr)
#2
print(arr[2])
#9
print(arr[-2])

#accessing multidimensional array element
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
print(arr[1,2]) #60
print(arr[0,2]) # 30
print(arr[0,-1]) #30


arr=([1,2,3,4,5,6,7,8,9,0])
print(arr)
x=arr[1:8:2]  #start:end:step 1 to 8 in step of 2
print(x)

x=arr[-2:3:-1] #-2 to 3 in step of 1
print(x)

x=arr[-2:11] #from -2 to 11
print(x)

arr=np.array([[1,2,3,4,7],[4,5,6,8,3],[7,8,9,7,2],[1,5,3,7,2],[7,3,7,33,12]])
print(arr)
arr[1,2]
arr[1,:] # one row all column
arr[:,2] # 2nd column will be represented in array

arr[:3,::2] #all rows and alternate columns

# integer array indexing,allows selction of arbitary items
arr=np.arange(35).reshape(5,7)
print(arr)

#boolen array indexing

arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,True,True]) #0=false  1,2=true
wanted_row=arr[rows,:]
print(wanted_row)

#### convert array into list
array=np.array([1,2,3,4])
print("array:",array)
print(type(array))

    #convert into list
lst=array.tolist()
print("list:",lst)
print(type(lst))


#multi dimensional array into list
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
lst=arr.tolist()
print("list:",lst)
print(type(lst))

####### convert list into array

lst=[1,30,40,55]
array=np.array(lst)
print(array)
print(type(array))

lst=[1,30,40,56]
array=np.asarray(lst)
print(array)

####### numpy array properties
# resize of array
array=np.array([[1,2,3],[4,5,6]])
print(array.shape)

    #resize
array.shape=(3,2)
print(array)
print(array.shape)

print(array)
print(array.reshape(3,2))


#numpys operation are divided into 3 main categories:

"""
1)fourier transform and shape manipulation
2)mathematical and logic operation
3)linear algebra and random number generation"""

    
    ################    asignments   ###################
    
# find numpy program to check none of the element is zero
#if array consists of zero then it is false
####all()
import numpy as np
x=np.array([1,4,2,3])
print(np.all(x))

y=np.array([0,3,4,2])
print(np.all(y))

#write numpy programe to check if any of element in array is non zero
####any()
#true if any number in array is non zero
x=np.array([1,0,0,0])
print("orignal array",x)
print(np.any(x))

y=np.array([0,0,0])
print("orignal array",y)
print(np.any(y))

#write a numpy program to test a given array  elememnt wise for finitness
#(not indefinite or not a number)

####isfinite()
x=np.array([1,np.nan,np.inf,0])
print("orignal array",x)
print("testing element by element ")
print(np.isfinite(x))

####isnan()
x=np.array([1,np.nan,np.inf,0])
print("orignal array",x)
print("testing element by element ")
print(np.isnan(x))

# write numpy programe to do element wise comparision of 2 arrays 

x=np.array([4,3])
y=np.array([2,5])
print(x,y)
print("comparision -greater")
print(np.greater(x,y))

print("comparision -greater_equal")
print(np.greater_equal(x,y))

print("comparision -less")
print(np.less(x,y))

print("comparision -less_equal")
print(np.less_equal(x,y))

#write numpy program to create 3 * 3 dimentional matrix

array=np.identity(3)
print("3*3 matrix:")
print(array)

#write numpy program to generate random number between 0 and 1
rand_num=np.random.normal(0,1,1) #center of location, scale, size
print(rand_num)

#write numpy program to create 3*4 array and iterate over it

arr=np.arange(10,22).reshape(3,4)  # arange should include 3*4 element
print("array:\n",arr)
for x in np.nditer(arr):
    print(x,end=" ")
    print()

#create vector of lenght 5 with values starting between 10 to 50
# syntax start,end,lenght

v=np.linspace(10,49,5)
print(v)

# write numpy programe to create 3*3 matrix with value from 2 to 10
x=np.arange(2,11).reshape(3,3)
print(x)

#write numpy program to reverse an array
x=np.arange(1,10)
print(x)
x=x[::-1]
print(x)

# write numpy program to compute multiplication of 2 matrix

x=[[1,2],[3,2]]
y=[[3,2],[3,5]]
print(x,y)
result=np.dot(x,y)
print(result)

# write numpy program to compute  cross multiplication of 2 matrix

x=[[1,2],[3,2]]
y=[[3,2],[3,5]]
print(x,y)
result1=np.cross(x,y)
result2=np.cross(y,x)
print(result1)
print(result2)

# comput determinant of given square array
from numpy import linalg as la
a=np.array([[1,2],[3,1]])
print(a)
print("determinant:")
print(np.linalg.det(a))

#compute eigenvalues and right eigenvector of given square array

#dimentionality reduction uses eigen vector
#dimentionality reductiion means reducing 1000s of featutes into certain number of feature
#PCA  is dimentionality reductiion method uses eigenvalues and right eigenvector

m=np.mat("3 -2;1 0")
print("matrix\n",m)
w,v=np.linalg.eig(m)
print("eigen values:",w)
print("eigen vector",v)

#compute inverse of given matrix
a=np.array([[1,2],[3,4]])
print("inverse:")
result=np.linalg.inv(a)
print(result)




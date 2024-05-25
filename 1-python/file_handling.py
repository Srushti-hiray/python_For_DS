# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:45:28 2023

@author: icon
"""

with open('pi_digits.txt') as file_object: # relative path
    #The open() function needs 
    #one argument: the name of the file you want to open
    contents=file_object.read()  # it will display unwanted space 
print(contents)

                     #######################
              
with open('pi_digits.txt') as file_object:
    #The open() function needs 
    #one argument: the name of the file you want to open
    contents=file_object.read()   #unwanted space is reduced
print(contents.rstrip())           

                     #######################
                    
file_path='c:/1-python/pi_digits.txt'  # absolute path
with open('pi_digits.txt') as file_object:
    
    contents=file_object.read()   #unwanted space is reduced
print(contents.rstrip()) 

                    ##########################
                    
#reading line by line 
filename='pi_digits.txt'
with open(filename) as file_object:
#we again use the with syntax to
#let python open and close the file properli
    for line in file_object:
        print(line)
        
                  ###########################
                    
filename='pi_digits.txt'
with open(filename) as file_object:
#we again use the with syntax to
#let python open and close the file properli
    for line in file_object:
        print(line.rstrip())    

                ##############################
                
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+=line.rstrip()
        print(pi_string)
        print(len(pi_string))

                ##############################
                
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("i love programming.")
    
                #############################

filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("i love programming.\n")   
    file_object.write("i love creating new game.\n") 

                #############################
 
###### if you are writing the file than previous data
####### get cleared but it will not happen in append, 
######as append inseert new data without clearing previous one

filename='programming.txt'
with open(filename,'a') as file_object:
    # use the a argument to open the file for appending
    # rather than write over existing file
    file_object.write("i love finding meaning in large data set.\n")   
    file_object.write("i love creating apps that run in browser.\n") 

             








               
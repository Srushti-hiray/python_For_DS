# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:26:21 2023

@author: icon
"""

def make_pizza(size,*toppings) :
    for topping in toppings:
        print(size,topping)
        
make_pizza(16,"toppings")
make_pizza(12,"toppings","cheese","green pepper")
        
    

            
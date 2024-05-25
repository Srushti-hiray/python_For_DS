# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:18:58 2023

@author: icon
"""

# CREATING HEADER FILE  

import pizza
pizza.make_pizza(16,"toppings")
pizza.make_pizza(12,"toppings","cheese","green pepper")

  
from pizza import make_pizza
pizza.make_pizza(16,"toppings")
make_pizza(12,"toppings","cheese","green pepper") 


from pizza import make_pizza as mp
mp(16,"toppings")
mp(12,"toppings","cheese","green pepper")

import pizza as p
p.make_pizza(16,"toppings")         
p.make_pizza(12,"toppings","cheese","green pepper")


from pizza import *
make_pizza(16,"toppings")
make_pizza(12,"toppings","cheese","green pepper") 

###########################################
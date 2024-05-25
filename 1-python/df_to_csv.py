# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:31:45 2023

@author: icon
"""
#### importing csv and excel file  ###
import pandas as pd
f1=pd.read_csv("C:/1-python/age.csv.xls")
f1

import pandas as pd
f1=pd.read_csv('age.csv.xls')


import pandas as pd
f1=pd.read_excel("C:/1-python/Bahaman.xlsx")
f1

import pandas as pd
f2=pd.read_excel('Bahaman.xlsx')

import pandas as pd
technologies ={
    "courses":["sparks","pysparks","hadoop","python"],
    "fee":[2000,25000,3000,4200],
    "duration":["30days","40days","25days","50days"],
    "discount":[1000,2000,999,440]
    }
df=pd.DataFrame(technologies)
df        # prints output


# convert dataframe to csv 
df.to_csv('data_file.csv')

#convert csv file to dataframe
df=pd.read_csv('data_file.csv')
df=pd.read_csv("C:/1-python/age.csv.xls")
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:18:20 2023

@author: icon
"""

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()

#multilple plots

x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()

##############################

#same code as above but include grid

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()


##############################

#handling axes

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

plt.axis()
plt.axis([0,5,-1,13])#set new axes limits
#[xmin,xmax,ymin,ymax]
#[0,5,-1,-13]
plt.grid(True)
plt.show()


##############################

#adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4],"y")
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.show()


##############################

#adding title

plt.plot([2,4,5])
plt.title("simple plot")
plt.show()


##############################

#adding legend

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*3,label="Normal")
plt.plot(x,x*1.5,label="Fast")
plt.plot(x,x/3.0,label="Slow")
plt.legend()
plt.show()

##############################

#control color

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,"y")
plt.plot(y+1,"m")
plt.plot(y+2,"c")
plt.show()


##############################

#specifying style in multiline plot

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,"--",y+1,"-.",y+2,":")
plt.show()


##############################

#markers

y=np.arange(1,3,0.2)
plt.plot(y,"x",y+0.5,"o",y+1,"D",y+1.5,"^",y+2,"s")
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.show()



##############################

#histogram charts

import matplotlib.pyplot as plt
import numpy as np
import random
y=np.random.randn(1000)  #see difference between two random
plt.hist(y)
plt.show()

y=random.randrange(1000)
plt.hist(y)
plt.show()


##############################

#bar graph

plt.bar([1,2,3],[3,2,5]) #x coordinates ,y coordinates
plt.show()


##############################

#scater plots 
#displays values of 2 set of data at x,y axis
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()


##############################

#change size and color

size=50*np.random.randn(1000)
color=np.random.randn(1000)
plt.scatter(x,y,s=size,c=color)
plt.show()


##############################

#adding text
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-4,4,1024)
Y=.25 * (X+4.) * (X+1.) * (X-2.)
plt.text(-0.5,-0.25,"brackmard minimum")
plt.plot(X,Y,c="k")


##############################




















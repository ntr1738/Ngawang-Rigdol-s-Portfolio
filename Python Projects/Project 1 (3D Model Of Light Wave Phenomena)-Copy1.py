#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d


axes = plt.axes(projection = '3d')

A = 1                    # This Is Our Amplitude

lambd = 450*(10**-9)     # Our Wavelength Of Light (Lambda) In Nanometers ("lambd" Is Not A Typo, I Wrote It This Way Because 'lambda' In Python Means Something Else) 

c = 3*(10**8)            # The Speed Of Light In Meters Per Second

f = c/lambd              # The Frequency Given By c/lambd. Derived From The Speed Of Light Equation c = Lambda Times Frequency

w = 2*np.pi * f          # Angular Frequency Equation

k = 2*np.pi/lambd        # Angular Wave Number Equation

t = 1                    # Time In Seconds

phi = 0                  #The Phase Difference 

                       
x_axis = np.linspace(0,10*lambd,1000)   #I've Set My Range From 0 to 10 Times Our Wavelength (0 nm to 4.5 micrometers) Along The X-Axis 
 
y_axis = np.linspace(0,10*lambd,1000)   #I've Set My Range From 0 to 10 Times Our Wavelength (0 nm to 4.5 micrometers) Along The Y-axis As Well

X, Y = np.meshgrid(x_axis,y_axis)      

z_axis = A*np.sin(k*X-w*t-phi)         #This Is Our Wave Function When Phi = 0 
       

wavefunc = axes.plot_surface(X, Y, z_axis, alpha = 0.09, color = 'blue')    #Now I Am Plotting The Wave Function


axes.set_xlabel('x (micrometers)')
axes.set_ylabel('y (micrometers)')
axes.set_zlabel('z (Amplitude)')
plt.title('3D Light Wave')


# In[11]:


axes = plt.axes(projection = '3d')

A = 1                   

lambd = 450*(10**-9)      

c = 3*(10**8)           

f = c/lambd              

w = 2*np.pi * f          

k = 2*np.pi/lambd       

t = 1                    

phi = 0                  

phi2 = 2*np.pi           #The Phase Difference Of Our Second Wave Relative To The First Wave


x_axis = np.linspace(0,10*lambd,1000)   

y_axis = np.linspace(0,10*lambd,1000)   

X, Y = np.meshgrid(x_axis,y_axis)      

z_axis = A*np.sin(k*X-w*t-phi)         #This Is Our First Wave Function When Phi = 0 From Our First Graph Earlier

z_axis2 = A*np.sin(k*X-w*t-phi2)       #This Is Our Second Wave Function When Phi = 2Pi

total_constructive = z_axis + z_axis2  #Now We Add Both Waves 

wavefunc1 = axes.plot_surface(X, Y, total_constructive, alpha = 0.2, color = 'blue')    #Now I Am Plotting The Resultant Wave Function

axes.set_xlabel('x (micrometers)')
axes.set_ylabel('y (micrometers)')
axes.set_zlabel('z (Amplitude)')
plt.title('3D Constructive Interference In Light Waves')


# In[154]:


axes = plt.axes(projection = '3d')

A = 1                    

lambd = 450*(10**-9)     

c = 3*(10**8)            

f = c/lambd              
w = 2*np.pi * f          
k = 2*np.pi/lambd        
t = 1                    

phi = 0                  

phi2 = 2*np.pi             #The Phase Difference Of Our Second Wave Relative To The First


x_axis = np.linspace(0,10*lambd,10)   

y_axis = np.linspace(0,10*lambd,10)   

X, Y = np.meshgrid(x_axis,y_axis)      

z_axis = A*np.sin(k*X-w*t-phi)        

z_axis2 = A*np.sin(k*X-w*t-phi2)      

wavefunc1 = axes.plot_surface(X, Y, z_axis, alpha = 0.09, color = 'blue')    

wavefunc2 = axes.plot_surface(X, Y, z_axis2, alpha = 0.09, color = 'blue')   


plt.title('3D Constructive Interference In Light Waves Just Before Combining')


# In[12]:


axes = plt.axes(projection = '3d')

A = 1                    

lambd = 450*(10**-9)     

c = 3*(10**8)            

f = c/lambd              

w = 2*np.pi * f          

k = 2*np.pi/lambd        

t = 1                    

phi = 0                 

phi2 = np.pi             


x_axis = np.linspace(0,10*lambd,13)   

y_axis = np.linspace(0,10*lambd,13)   

X, Y = np.meshgrid(x_axis,y_axis)      

z_axis = A*np.sin(k*X-w*t-phi)         

z_axis2 = A*np.sin(k*X-w*t-phi2)       #This Is Our Third Wave Function When Phi = Pi


wavefunc1 = axes.plot_surface(X, Y, z_axis, alpha = 0.09, color = 'blue')    #Now I Am Plotting My First Wave Function
wavefunc2 = axes.plot_surface(X, Y, z_axis2, alpha = 0.09, color = 'blue')   #Now The Third Wave Function 

plt.title('3D Deestructive Interference In Light Waves Just Before Combining')


# In[13]:


axes = plt.axes(projection = '3d')

x_axis = np.linspace(0,10*lambd,13)   

y_axis = np.linspace(0,10*lambd,13)    

X, Y = np.meshgrid(x_axis,y_axis) 

axes.set_xlabel('x (micrometers)')
axes.set_ylabel('y (micrometers)')
axes.set_zlabel('z (Amplitude)')

plt.title('3D Destructive Interference In Light Waves')


# In[14]:


#Let's Put Our Waves Into A DataFrame

waves = {
    'A': [1, 1, 1],
    'lambd': [450*(10**-9), 450*(10**-9), 450*(10**-9)],
    'c': [3*(10**8), 3*(10**8), 3*(10**8)],
    'f': [3*(10**8)/450*(10**-9), 3*(10**8)/450*(10**-9), 3*(10**8)/450*(10**-9)],
    'w': [2*np.pi * 3*(10**8)/450*(10**-9)] * 3,  
    'k': [2*np.pi/450*(10**-9)] * 3,  
    't': [1, 1, 1],
    'phi': [0, 2*np.pi, np.pi]}

df = pd.DataFrame(waves, index = ['Wave_1','Wave_2','Wave_3'])

df


# In[15]:


#Let's Make More Crazy Wave Functions

axes = plt.axes(projection = '3d')

A = 5                     

lambd = 500*(10**-9)     

c = 3*(10**8)           

f = c/lambd             

w = 2*np.pi * f          

k = 2*np.pi/lambd        

t = 10                   

phi = 3/2*np.pi          

phi2 = 0

phi3 = np.pi

phi4 = 2*np.pi
          
x_axis = np.linspace(0,10,20)    
 
y_axis = np.linspace(0,10,20)  

X, Y = np.meshgrid(x_axis,y_axis)      

z_axis = A*np.sin(k*X-w*t-phi)
z_axis2 = A*np.sin(k*X-w*t-phi2)
z_axis3 = A*np.sin(k*X-w*t-phi3)
z_axis4 = A*np.sin(k*X-w*t+phi4)

Resultant = z_axis + z_axis2 + z_axis3 + z_axis4

wavefunc1 = axes.plot_surface(X, Y, z_axis, alpha = 0.1, color = 'red')    
wavefunc2 = axes.plot_surface(X, Y, z_axis2, alpha = 0.1, color = 'black')    
wavefunc3 = axes.plot_surface(X, Y, z_axis3, alpha = 0.1, color = 'blue')    
wavefunc4 = axes.plot_surface(X, Y, z_axis4, alpha = 0.1, color = 'yellow')    
wavefunc5 = axes.plot_surface(X, Y, Resultant, alpha = 0.5, color = 'green')    

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('z')
plt.title('Uh-Oh Wave')


# In[16]:


#Now Let's Put These New Waves Into A DataFrame As Well

new_waves = {
    'A': [5, 5, 5, 5],
    'lambd': [500*(10**-9), 500*(10**-9), 500*(10**-9), 500*(10**-9)],
    'c': [3*(10**8), 3*(10**8), 3*(10**8), 3*(10**8)],
    'f': [3*(10**8)/450*(10**-9), 3*(10**8)/450*(10**-9), 3*(10**8)/450*(10**-9), 3*(10**8)/450*(10**-9)],
    'w': [2*np.pi * 3*(10**8)/450*(10**-9)] * 4,  # Repeated value for w
    'k': [2*np.pi/450*(10**-9)] * 4,  # Repeated value for k
    't': [10, 10, 10, 10],
    'phi': [3/2*np.pi, 3/2*np.pi, 3/2*np.pi, 3/2*np.pi]}


new_table = pd.DataFrame(new_waves, index = ['Wave_4','Wave_5','Wave_6','Wave_7'])


new_table


# In[143]:


#Let's Combine Both Tables

concat_data = pd.concat([df,new_table])

concat_data


# In[144]:


#Let's Find Some Stats About Our Table

concat_data.describe()


# In[9]:


#Now I Will Create A Super Wave Using The Mean Of All Our Wave Characteristics

axes = plt.axes(projection = '3d')

A = 3.285714                   

lambd = 4.785714e-07     

c = 300000000.0            

f = 6.666667e-04              

w = 0.004189          

k = 1.396263e-11        

t = 6.142857                   

phi = 4.039191  

x_axis = np.linspace(0,50,2000)   

y_axis = np.linspace(0,50,2000)

X,Y = np.meshgrid(x_axis,y_axis)

super_wavee = A*np.sin(k*X-w*t-phi)  

axes.plot_surface(X, Y, super_wavee, alpha = 0.75, color = 'red')    

plt.title('3D Killer Light Wave')


# In[ ]:


#That Is The End Of This Presentation


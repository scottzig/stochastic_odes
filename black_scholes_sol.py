oes #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The program models solutions to the Black-Scholes SDE
"""
import numpy as np
import matplotlib.pyplot as plt

mu = 0.75
sig = 0.30
x_0 = 250
t_start = 0
t_end = 1

################################################

plt.figure()
del_t = 0.1
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+2)

t = 0
i = 1
sol[0] = x_0
while t < 1:
    t = t+del_t
    w = np.random.normal(0,del_t)
    x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*w)
    sol[i] = x
    i = i+1

txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+2)
plt.plot(vec,sol)
plt.title("Black Scholes Solution, del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")

################################################

plt.figure()
del_t = 0.01
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+1)

t = 0
i = 1
sol[0] = x_0
while t < 1:
    t = t+del_t
    w = np.random.normal(0,del_t)
    x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*w)
    sol[i] = x
    i = i+1
    
txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+1)
plt.plot(vec,sol)
plt.title("Black Scholes Solution, del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")

################################################
 
plt.figure()
del_t = 0.005
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+1)

t = 0
i = 1
sol[0] = x_0
while t < 1:
    t = t+del_t
    w = np.random.normal(0,del_t)
    x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*w)
    sol[i] = x
    i = i+1
    
txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+1)
plt.plot(vec,sol)
plt.title("Black Scholes Solution, del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")
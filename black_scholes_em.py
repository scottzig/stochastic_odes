#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The program approximates solutions to the Black-Scholes SDE
using Euler-Maruyama
"""
import numpy as np
import matplotlib.pyplot as plt

mu = 0.75
sig = 0.30
x_0 = 250
t_start = 0
t_end = 1

def a(w):
    return mu*w

def b(w):
    return sig*w

################################################

plt.figure()
del_t = 0.1
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+2)
apprx = np.zeros([num_steps+2,10])

for ii in range(0,10):
    t = 0
    i = 1
    w = x_0
    sol[0] = x_0
    apprx[0,ii] = w
    while t < 1:
        t = t+del_t
        z = np.random.normal(0,del_t)
        x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*z)
        sol[i] = x
        z_nor = np.random.normal(0,1)
        del_w = z_nor*np.sqrt(del_t)
        w_new = w + a(w)*del_t+b(w)*del_w
        apprx[i,ii] = w_new
        w = w_new
        i = i+1
        
apprx = apprx.mean(1)

txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+2)
plt.plot(vec,sol,'-')
plt.plot(vec,apprx,'-o')
plt.title("Black Scholes (Euler-Maruyama), del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")

################################################

plt.figure()
del_t = 0.01
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+1)
apprx = np.zeros([num_steps+1,10])

for ii in range(0,10):
    t = 0
    i = 1
    w = x_0
    sol[0] = x_0
    apprx[0,ii] = w
    while t < 1:
        t = t+del_t
        z = np.random.normal(0,del_t)
        x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*z)
        sol[i] = x
        z_nor = np.random.normal(0,1)
        del_w = z_nor*np.sqrt(del_t)
        w_new = w + a(w)*del_t+b(w)*del_w
        apprx[i,ii] = w_new
        w = w_new
        i = i+1
        
apprx = apprx.mean(1)

txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+1)
plt.plot(vec,sol,'-')
plt.plot(vec,apprx,'-o')
plt.title("Black Scholes (Euler-Maruyama), del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")

################################################
 
plt.figure()
del_t = 0.005
num_steps = (t_end-t_start)/del_t
num_steps = int(num_steps)
sol = np.zeros(num_steps+1)
apprx = np.zeros([num_steps+1,10])

for ii in range(0,10):
    t = 0
    i = 1
    w = x_0
    sol[0] = x_0
    apprx[0,ii] = w
    while t < 1:
        t = t+del_t
        z = np.random.normal(0,del_t)
        x = x_0*np.exp((mu-(1/2)*sig**2)*t+sig*z)
        sol[i] = x
        z_nor = np.random.normal(0,1)
        del_w = z_nor*np.sqrt(del_t)
        w_new = w + a(w)*del_t+b(w)*del_w
        apprx[i,ii] = w_new
        w = w_new
        i = i+1
        
apprx = apprx.mean(1)

txt = str(del_t)
vec = np.linspace(t_start,t_end,num_steps+1)
plt.plot(vec,sol,'-')
plt.plot(vec,apprx,'-o')
plt.title("Black Scholes (Euler-Maruyama), del_t = " + txt)
plt.xlabel("Time in years")
plt.ylabel("Price in Dollars")
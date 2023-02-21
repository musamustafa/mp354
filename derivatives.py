# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


delta = 0.5

x = np.arange(0.0, 10.0, delta)

f = np.sin(x)
c = np.cos(x)

# Calculate the forward derviative in array (faster)

dff = np.zeros(len(x)-1)
for i in range(len(x)-1):
    dff[i] = (f[i+1] - f[i])/delta

dfb = np.zeros(len(x) - 1)
for i in range(1, len(x)):
    dfb[i-1] = (f[i] - f[i-1])/delta

dfs = np.zeros(len(x)-2)
for i in range(1,len(x)-1):
    dfs[i-1] = (f[i+1] -f[i-1])/(2*delta)

#



plt.figure()

plt.plot(x, f)
plt.plot(x[1:], dff, label="forward")
plt.plot(x[:-1], dfb, label='backward')
plt.plot(x[1:-1],dfs, label='std')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('dff dfb and dfs plots for sin(x)')
plt.grid()
plt.show()
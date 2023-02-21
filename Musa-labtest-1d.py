# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


delta = 0.001

x = np.arange(-1, 2.5, delta)



f = np.tanh(x)*((1-(x/2)**2))**4
c = np.cos(x)

# Calculate the forward derviative in array (faster)


def dfs(f, x):
    dfs = np.zeros(len(x)-2)
    for i in range(1,len(x)-1):
        dfs[i-1] = (f[i+1] -f[i-1])/(2*delta)
    return dfs



plt.figure()

plt.plot(x, f, label="Function")
plt.plot(x[1:-1],dfs(f, x), label='first std derivative')
plt.plot(x[2:-2],dfs(dfs(f, x),x[1:-1]), label='second std derviative')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('lab test 1d Musa abdin ')
plt.grid()
plt.show()
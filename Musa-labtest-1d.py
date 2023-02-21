# -*- coding: utf-8 -*-
"""
Musa Abdin Submission for MP354 lab test 1d
"""
import numpy as np
import matplotlib.pyplot as plt

# define the step size
delta = 0.01


x = np.arange(-1,2.5, delta)


# function to be differentiated
f = ((1 - ((x/2)**2))**4) * (np.tanh(x/2))

# defninition of a function to calculate the dtd derivative
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
#plt.savefig("Musa_lab_test_1d.jpg")
plt.show()
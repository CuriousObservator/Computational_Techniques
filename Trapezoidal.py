# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:31:34 2020

@author: Abhishek
"""
 
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    val=(0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))
    return(val)
funvalue=[]
ivalue=[]
def integrand(x):
    return (0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))

import scipy.integrate as intg

a=float(input("Initial point."))
b=float(input("Final point."))
result=intg.quad(integrand,a,b)
#print(result)

n=int(input("Provide the number of applications."))
h=float((b-a)/n)
#print(h)
for i in np.linspace(a,b,n+1):
    # print("i"+str(i))
    funvalue.append(f(i))
    ivalue.append(i)
#print(ivalue)
#print(funvalue)
k=1
integration=0
#print(len(ivalue))
while(k<(len(ivalue))):
    integration=integration+((h/2)*(funvalue[k-1]+funvalue[k]))
    k=k+1
print(str(integration)+" is the value of your integration.")                        
print(str(result[0])+" is the true value of integration.")
print("The relative error is: "+str(abs((integration-result[0])*100/result[0])))


a, b = 0, 0.8
n = 10
h = (b - a) / n

x_smooth = np.linspace(a, b, 500)
y_smooth = f(x_smooth)

x_trap = np.linspace(a, b, n + 1)
y_trap = f(x_trap)


plt.plot(x_smooth, y_smooth, 'r-', lw=2, label='Actual Smooth Function')

plt.plot(x_trap, y_trap, 'bo-', label='Trapezoidal Fit (Estimate)')

plt.fill_between(x_trap, y_trap, color='blue', alpha=0.2, label='Trapezoidal Area')

for x in x_trap:
    plt.vlines(x, 0, f(x), colors='gray', linestyles='--', alpha=0.5)

plt.title(f"Trapezoidal Method: Actual Curve vs. Piecewise Linear Fit (n={n})")
plt.xlabel("x--->")
plt.ylabel("f(x)--->")
plt.legend()
plt.grid(True, alpha=0.3)

        
        
        
    
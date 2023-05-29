# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:36:13 2020

@author: Abhishek
"""
import numpy as np
import scipy.integrate as integ
def f(m):
    return(0.2+(25*m)-(200*(m**2))+(675*(m**3))-(900*(m**4))+(400*(m**5)))
def integrand(x):
    return (0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))
a=float(input("Please provide the lower limit of intergration."))
b=float(input("Please provide the upper limit of intergration."))
n=int(input("Please provide the number of iterations."))
result=integ.quad(integrand,a,b)
h=(b-a)/(3*n)
funvalue=[]
xvalue=[]
for l in np.arange(a,b+h,h):
    funvalue.append(f(l))
    xvalue.append(l)
print(len(xvalue))
print(len(funvalue))
print(xvalue)
print(funvalue)
print(h)
i=3
integration=0
while(i<(len(xvalue))):
    integration=integration+((3*h/8)*(funvalue[i-3]+(3*funvalue[i-2])+(3*funvalue[i-1])+funvalue[i]))
    i+=3
print(str(integration)+" is the value of your integration.")                        
print(str(result[0])+" is the true value of integration.")
print("The relative error is: "+str(abs((integration-result[0])*100/result[0])))   
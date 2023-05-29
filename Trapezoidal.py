# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:31:34 2020

@author: Abhishek
"""
 
import numpy as np
def f(a):
    val=float(0.2+(25*a)-(200*(a**2))+(675*(a**3))-(900*(a**4))+(400*(a**5)))
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
    print("i"+str(i))
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





# def summ(n):
#     add=0 
#     i=1
#     while(i<n):
#         add=add+funvalue[i]
#         i=i+1
#     return(add)
# n=int(input("Provide the number of applications."))

# h=(10-0)/n
# trap=(h/2)*(funvalue[0]+2*summ(n)+funvalue[-1])
# print("THe value of integration using Trapezoidal rule is"+str(trap))
# print(mvalue)
# print(funvalue)
#import matplotlib.pyplot as mtplt
#import matplotlib.pyplot as mtplt
#mtplt.plot(ivalue,funvalue)

#indpvar=[]
# depvar=[]
# for l in np.arange(a,b+h,h):
#     indpvar.append(l)
#     depvar.append(f(l))
# mtplt.plot(indpvar,depvar,color="purple")



        
        
        
    
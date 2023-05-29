# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:35:52 2020

@author: Abhishek
"""
import numpy as np
import scipy.integrate as integ
import math as m
def f(q):
    r=float((1/(2*m.pi)**0.5)*((m.e)**((-q**2)/2)))
    return(r)
def integrand(x):
    return ((1/(2*m.pi)**0.5)*((m.e)**((-x**2)/2)))

a=float(input("Provide the initial point. "))
b=float(input("Provide the final point. "))
result=integ.quad(integrand,a,b)
n=int(input("Provide the number of applications."))
if(n==1):
    h=float((b-a)/2)
else:
    h=float((b-a)/n)
print(h)
funval=[]
xivalue=[]
for q in np.arange(a,b+h,h):
    funval.append(f(q))
    xivalue.append(q)
print(funval)
def oddsum(p):
    sum=0
    k=1
    while(k<=p):
        sum=sum+funval[k]
        k+=2
    return(sum)
def evensum(p):
    sum=0
    k=2
    while(k<=p):
        sum=sum+funval[k]
        k+=2
    return(sum)
if(n==1):
    integration=(b-a)*((funval[0]+(4*funval[1])+funval[2])/6)
else:
    integration=(h)*((funval[0]+(4*(oddsum(n-1)))+(2*(evensum(n-2)))+funval[n])/3)
print(str(integration)+" is the value of your integration.")                        
print(str(result[0])+" is the true value of integration.")
print("The relative error is: "+str(abs((integration-result[0])*100/result[0])))
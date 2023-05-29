# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:54:48 2020

@author: Abhishek
"""
import numpy as np
def f(q):
    val=float(0.2+(25*q)-(200*(q**2))+(675*(q**3))-(900*(q**4))+(400*(q**5)))
    return(val)
def integrand(x):
    return (0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))
import scipy.integrate as intg

h=[]
n=int(input("Please provide the number of applications. "))
a=float(input("Please provide the initial point. "))
b=float(input("Please provide the final point. "))
result=intg.quad(integrand,a,b)
#rel=input("Please provide the relation of h for successive" 
#           "values of integrations.(h2/h1) ")
#the default relation is taken as h2/h1 is 1/2.
h.append(b-a)
m=0
i=[]
# print(h)
while(m<n-1):
    h.append(h[m]/2)
    m+=1
for y in h:
    sum=0
    for l in np.arange(a,b,y):
        sum=sum+((y/2)*(f(l)+f(l+y)))
    i.append(sum)
k=1
while(k<n):
    t=1
    integral=[]
    while(t<len(i)):
        z=(((4**k)*(i[t]))-i[t-1])/(4**k-1)
        integral.append(z)
        t+=1
    i=integral 
    k+=1
print(str(integral[0])+" is the value of your integration.")                        
print(str(result[0])+" is the true value of integration.")
print("The relative error is: "+str(abs((integral[0]-result[0])*100/result[0])))








# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:42:07 2020

@author: Abhishek
"""
import matplotlib.pyplot as mtplt
import numpy as np
y=[0,0]
import math
def f(x,y):
    return((y*x**2)-(1.1*y))
def act(x):
    return(math.e**((x**3/3)-(1.1*x)))
    
x0=float(input("Please provide the initial conditions. x0: "))
y0=float(input("Please provide the initial condition for y at x0. y0: "))
xn=int(input("Please provide the final value x where you want to find y. xn: "))
h=float(input("Please provide the value of h. "))
x=x0
ys1=[]
ys1.append(y0)
xval=[]
xj=x0
xval.append(x0)
while(x<xn):
    if(x!=xj):
        ch=input("Do you want to change the value of h? [y/n]")
        if(ch=="y" or ch=="Y"):
            h=float(input("Please provide the new value of h."))
        else:
            pass
    ys=y0+f(x0,y0)*h/2
    ys=y0+(f(x0+h/2,ys))*h
    ys1.append(ys)
    x0=x0+h
    y0=ys
    x=x0
    xval.append(x)
    error=round((abs((act(x0)-y0)/act(x0)))*100,3)
    print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %.")
funval=[]
for i in np.arange(0,x+h):
    funval.append(act(i))
mtplt.plot(np.arange(0,x+h),funval)
mtplt.plot(xval,ys1)
mtplt.xlabel("x value")
mtplt.ylabel("function value")
mtplt.legend(["function value","estimate value"])
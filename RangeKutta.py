# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 02:26:27 2020

@author: Abhishek
"""
import math
import numpy as np
import matplotlib.pyplot as mtplt
def f(x,y):
    return((y*x**2)-(1.1*y))
def act(x):
    return(math.e**((x**3/3)-(1.1*x)))

h=float(input("Please provide the value of h. "))
x0=float(input("Please provide the x0 point. "))
y0=float(input("Please provide the y0 point. "))
xn=float(input("Please provide the final value x where you want to find y. xn: "))
k=int(input("Please provide the order of RK method to be applied. (2/3/4)"))

x=x0
y1=[]
y1.append(y0)
xval=[]
xval.append(x0)
if(k==2):
    met=int(input("Which method do you want to use "
                   "1)Heuns?"
                   "2)Midpoint?"
                   "3)Ralston's method?"
                   "(1/2/3)"))
    if(met==1):
        a1,a2=0.5,0.5
        meth="Heun's Method."
        while(x<xn):
            k1=f(x0,y0)
            k2=f(x0+h,y0+h)
            y=y0+((a1*k1)+(a2*k2))*h
            y1.append(y)
            x0=x0+h
            y0=y
            x=x0
            xval.append(x)
            error=round(((act(x0)-y0)/act(x0))*100,3)
            print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %. using the "+str(meth))
    if(met==2):
        a1,a2=0,0.5
        meth="Midpoint Method."
        while(x<xn):
            k1=f(x0,y0)
            k2=f(x0+h/2,y0+h/2)
            y=y0+((a1*k1)+(a2*k2))*h
            y1.append(y)
            x0=x0+h
            y0=y
            x=x0
            xval.append(x)
            error=round(((act(x0)-y0)/act(x0))*100,3)
            print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %. using the "+str(meth))
        
    if(met==3):
        a1,a2=1/3,2/3
        meth="Ralston's Method."
        while(x<xn):
            k1=f(x0,y0)
            
            k2=f(x0+(3*h/4),y0+(3*h/4))
            y=y0+((a1*k1)+(a2*k2))*h
            y1.append(y)
            x0=x0+h
            y0=y
            x=x0
            xval.append(x)
            error=round(((act(x0)-y0)/act(x0))*100,3)
            print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %. using the "+str(meth))
        
    while(x<xn):
        y=y0+((a1*k1)+(a2*k2))*h
        y1.append(y)
        x0=x0+h
        y0=y
        x=x0
        xval.append(x)
        error=round(((act(x0)-y0)/act(x0))*100,3)
        print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %. using the "+str(meth))

if(k==3):
    while(x<xn):
         k1=f(x0,y0)
         k2=f(x0+h/2,y0+h/2)
         k3=f(x0+h,y0-(k1*h)+(2*(k2)*h))
         y=y0+(k1+(4*k2)+k3)*h/6
         y1.append(y)
         x0=x0+h
         y0=y
         x=x0
         xval.append(x)
         error=round(((act(x0)-y0)/act(x0))*100,3)
         print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %.")
if(k==4):
    while(x<xn):
         k1=f(x0,y0)
         k2=f(x0+h/2,y0+(k1*h/2))
         k3=f(x0+h/2,y0+(k2*h/2))
         k4=f(x0+h,y0+(k3*h))
         y=y0+(k1+(2*k2)+(2*k3)+k4)*h/6
         y1.append(y)
         x0=x0+h
         y0=y
         x=x0
         xval.append(x)
         error=round(((act(x0)-y0)/act(x0))*100,3)
         print("y("+str(x0)+") = "+str(round(y0,3))+" with an error of "+str(error)+" %.")


funval=[]
for i in np.arange(0,x+h):
    funval.append(act(i))
mtplt.plot(np.arange(0,x+h),funval)
mtplt.plot(xval,y1)
mtplt.xlabel("x value")
mtplt.ylabel("function value")
mtplt.legend(["function value","estimate value"])
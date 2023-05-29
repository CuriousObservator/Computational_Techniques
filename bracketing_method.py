# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:49:40 2020

@author: Abhishek
"""
import math as m
def f(i):
    p=((i**m.log(i,m.e))-(m.e**m.sin(i))-(50*i))
    return(p)

xl=float(input("Give the lower limit "))
xu=float(input("Give the upper limit "))
#v=float(input("Give the velocity "))
#m=float(input("Give the mass of the object "))
#t=float(input("Provide the time of simulation "))
tre=float(input("What is the threshold relative error(Provide 17 digit)"))
g=9.8
ea=100

while(ea>tre):
    if(ea<=tre):
        print(ea)
        break
    xr1=(xl+xu)/2
    if((f(xl)*f(xu))<0):
        if((f(xl)*f(xr1))<0):
            xu=xr1
        else:
            xl=xr1
    else:
        print("The given bracket is not valid.")
    xr2=(xl+xu)/2
    print(xr2)
    print(xl)
    print(xu)
    ea=abs(((xr2-xr1)*100)/xr2)
    print(ea)
    
#xr1=str(xr1)
#ea=str(ea)
#print("The value of the index is "+xr1+" with a relative error of "+ea)
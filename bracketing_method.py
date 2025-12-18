# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:49:40 2020

@author: Abhishek
"""
import math as m
def f(x):
    p=(x**2 - x - 2)
    return(p)

xl=float(input("Give the lower limit "))
xu=float(input("Give the upper limit "))
tre=float(input("Threshold of relative error"))

print(f(xl))

if (f(xl)*f(xu)) >= 0:
    print("Invalid Brackets.")
else:
    ea = 100
    xr = xl
    while(ea>tre):
        xr_new = (xl+xu)/2
        if((f(xl)*f(xr_new))<0):
            xu=xr_new
        else:
            xl=xr_new
        if xr_new != 0:
            ea = abs(((xr_new - xr) / xr_new) * 100)
        xr = xr_new
        
        print(f"Root estimate: {xr_new:.6f} | Error: {ea:.6f}%")
        

    
print(f"The root is:{xr_new:6f}")
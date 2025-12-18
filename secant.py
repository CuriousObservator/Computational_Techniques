# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:51:06 2020

@author: Abhishek
"""
import math as m
def f(x):
    p=(pow(m.e, -0.2*x)*m.sin(5*x+2)-(x/10))
    return(p)


xcur=float(input("Please provide guess 1"))
xprev=float(input("Provide guess 2"))
thr=float(input("Please provide the threshold error"))
ea=100

while(ea>thr):
    xfut=xcur-((f(xcur)*(xprev - xcur))/(f(xprev)-f(xcur)))
    ea=abs(((xfut-xcur)*100)/xcur)
    # print(xcur)
    # print(xfut)
    # print(xprev)
    # print(f(xcur))
    # print(ea)
    xprev=xcur
    xcur=xfut
    print(f"Root estimate: {xcur:.6f} | Error: {ea:.10f}%")
       
print(f"Final Root estimate: {xcur:.6f} | Error: {ea:.10f}%")

    
    
    
    

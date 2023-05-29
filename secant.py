# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:51:06 2020

@author: Abhishek
"""
import math as m
def f(i):
    p=((i**m.log(i,m.e))-(m.e**m.sin(i))-(50*i))    
    return(p)

xcur=float(input("Please provide guess 1"))
xprev=float(input("Provide guess 2"))
thr=float(input("Please provide the threshold error"))
ea=100

while(ea>thr):
    xfut=xcur-(f(xcur)/abs((f(xcur)-f(xprev))/(xcur-xprev)))
    ea=abs(((xfut-xcur)*100)/xcur)
    print(xcur)
    print(xfut)
    print(xprev)
    print(f(xcur))
    print(ea)
    xprev=xcur
    xcur=xfut
       
    

    
    
    
    

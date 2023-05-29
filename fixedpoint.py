# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:13:00 2020

@author: Abhishek
"""
import math as m
import numpy as np
def f(i):
    p=((i**m.log(i,m.e))-(m.e**m.sin(i))-(50*i))    
    return(p)
def g(i):
    n=((i**m.log(i,m.e))-(m.e**m.sin(i)))/50
    return(n)
def h(i):
    j=((np.arcsin(m.log*(i**m.log(i,m.e))-m.sin(i))))
    return(j)
ea=100
xcur=float(input("provide the guess"))
thr=float(input("Provide the threshold error"))
while(ea>thr):
    print(f(xcur))
    xnew=h(xcur)
    ea=abs(((xnew-xcur)*100)/xcur)
    print(ea)
    print(h(xcur))
    xcur=xnew
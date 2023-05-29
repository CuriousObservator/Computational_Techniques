# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:59:41 2020

@author: Abhishek
"""
import math as m
def f(i):
    p=((i**m.log(i,m.e))-(m.e**m.sin(i))-(50*i))    
    return(p)
    
def fd(i):
    pd=((2*(i**(m.log(i,m.e)-1))*(m.log(i,m.e)))-(m.e**(m.sin(i))*m.cos(i))-50)
    return(pd)
xcur=float(input("Please provide the guess"))
thr=float(input("Please provide the threshold error"))
ea=100
while(ea>thr):
    newx=xcur-(f(xcur)/fd(xcur))
    ea=abs(((newx-xcur)/newx)*100)
    print(ea)
    print(newx)
    print(f(newx))
    print(xcur)
    print(f(xcur))
    xcur=newx

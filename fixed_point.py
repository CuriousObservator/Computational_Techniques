#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 12:27:56 2025

@author: rbarcrosspbar
"""

import math as m
import numpy as np
def f(x):
    p=((x**m.log(x,m.e))-(m.e**m.sin(x))-(50*x))    
    return(p)
def g(x):
    n=((x**m.log(x,m.e))-(m.e**m.sin(x)))/50
    return(n)

ea=100
xcur=float(input("provide the guess"))
thr=float(input("Provide the threshold error"))
while(ea>thr):
    if(xcur<=0):
        print("Choose different guess, negative values and 0 dont work with log.")
        break
    print(f(xcur))
    xnew=g(xcur)
    ea=abs(((xnew-xcur)*100)/xcur)
    print(ea)
    print(g(xcur))
    xcur=xnew
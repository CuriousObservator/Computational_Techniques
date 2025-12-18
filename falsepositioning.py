# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 04:40:40 2025

@author: rbarcrosspbar
"""

import math as m
def f(x):
    p=(pow(m.e, -0.2*x)*m.sin(5*x+2)-(x/10))
    return(p)
xl=float(input("Give lowe limit"))
xu=float(input("Give upper limit"))
thr=float(input("Provide threshold error"))
ea=100

if (f(xl)*f(xu)) >= 0:
    print("Invalid Brackets.")
else:
    while(ea>thr):
        newx=xu-(f(xu)*(xu-xl)/(f(xu)-f(xl)))
        ea=abs(((newx-xl)/xl)*100)
        # print(xl)
        # print(f(xl))
        xl=newx
        # print(ea)
        # print(xu)
        # print(f(xu))
        print(f"Root estimate: {newx:.6f} | Error: {ea:.10f}%")
        
print(f"Final Root estimate: {newx:.6f} | Error: {ea:.10f}%")
    
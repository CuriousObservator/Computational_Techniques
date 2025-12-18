# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:59:41 2020

@author: Abhishek
"""
import math as m

def f(x):
    p=(pow(m.e, -0.2*x)*m.sin(5*x+2)-(x/10))
    return(p)
    
def df(x):
    term1 = -0.2 * m.exp(-0.2 * x) * m.sin(5 * x + 2)
    term2 = 5 * m.exp(-0.2 * x) * m.cos(5 * x + 2)
    return term1 + term2 - 0.1


xcur=float(input("Please provide the guess"))
thr=float(input("Please provide the threshold error"))
ea=100
iterations = 100
iterr = 0

while(ea>thr and iterr<100):
    newx=xcur-(f(xcur)/df(xcur))
    ea=abs(((newx-xcur)/newx)*100)
    # print(ea)
    # print(newx)
    # print(f(newx))
    # print(xcur)
    # print(f(xcur))
    xcur=newx
    print(f"Root estimate: {newx:.6f} | Error: {ea:.10f}%")
    if(iterr==99):
        print("----"*10)
        print("Choose a better first guess.")
    iterr+=1

print(f"Final Root estimate: {newx:.6f} | Error: {ea:.10f}%")
    

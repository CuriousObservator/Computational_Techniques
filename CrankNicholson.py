# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:12:34 2020

@author: Abhishek
"""
import numpy as np
import matplotlib.pyplot as mtplt
l=float(input("Please provide the length of the rod."))
n=int(input("Please provide the number of datapoints on the rod."))
dx=float(l/n)
dt=float(input("Please provide the time increment of time."))
lambd=0.835*dt/(dx**2)
tmax=float(input("Please provide the maximum time till which you want to observe."))
proxy=np.zeros((n-2,n-2))
print(proxy)
m=0
while(m<n-2):
    if(m==0):
        proxy[m][m]=2*(1+lambd)
        proxy[m][m+1]=-lambd
        m+=1
        continue
    if(m==(n-3)):
        proxy[m][m]=2*(1+lambd)
        proxy[m][m-1]=-lambd
        break
    else:
        proxy[m][m]=2*(1+lambd)
        proxy[m][m+1]=-lambd
        proxy[m][m-1]=-lambd
    m+=1
prox=proxy.copy()
print(prox)
T0=float(input("Please provide the initial value at x0."))
Tn=float(input("Please provide the initial value at xn."))
t=0
tnum=int(tmax/dt)
i=0
sol=[]
while(t<=tnum):
    sol.append(np.zeros((n,1)))
    sol[t][0]=T0
    sol[t][n-1]=Tn
    t+=1
pick=np.zeros((n-2,1))
t=0
while(t<tnum):
    s=0
    while(s<n-2):
        if(s==0):
            pick[s]=(2*lambd*T0)+(2*(1-lambd)*sol[t][s+1])+(lambd*sol[t][s+2])
        if(s==n-3):
            pick[s]=(2*lambd*Tn)+(2*(1-lambd)*sol[t][n-3])+(lambd*sol[t][n-4])
        else:
            pick[s]=lambd*sol[t][s-1]+(2*(1-lambd)*sol[t][s])+(lambd*sol[t][s+1])
        s+=1
    aug=np.concatenate((prox,pick),axis=1)
    q=len(aug)
    w=len(aug[0])
    i=0
    while(i<=(q-1)):
        aug[i]=aug[i]/aug[i][i]
        for j in range(w-1):
            if(j==i):
                continue
            aug[j]=aug[j]-(aug[j][i]*aug[i])           
        i=i+1
    aug1=np.reshape(aug[:,-1],(n-2,1))
    b=1
    while(b<n-1):
        sol[t+1][b]=aug1[b-1]
        b+=1
    t+=1
# print(sol)
j=0
xaxis=[]
while(j<n):
    xaxis.append([j+1])
    j+=1
# print(xaxis)
t=0
while(t<tnum):
    mtplt.plot(xaxis,sol[t])
    t+=1
mtplt.xlabel("Datapoints --->",bbox=dict(boxstyle='round',color='#4ef71e'))
mtplt.ylabel("Temperature --->",bbox=dict(boxstyle='round',color='#4ef29e'))
mtplt.title("Cranck Nicholson Method",bbox=dict(boxstyle='round',color='#f7c179'))








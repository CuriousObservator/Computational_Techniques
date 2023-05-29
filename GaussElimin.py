# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:20:19 2020

@author: Abhishek
"""
import numpy as np
#m=np.array([[3,2,-1,8],[2,5,3,9],[-5,2,-1,0]],dtype="float")
r=3
c=4
entries=list(map(float,input("Please provide elements").split()))
m=np.array(entries).reshape(r,c)
print(str(m)+"\n")


m1=np.empty(shape=(3,4),dtype="float")
m1[0]=m[0]

i=1
j=0
while(True):
    while(True):
        m1[i]=m[i]-((m[i][j]/m[j][j])*m[j])    
        if(m1[i][j]==0 and m1[i-1][j]==0):
            break
        elif(i<2):
            i=i+1
        else:
            break
    m=m1

    print(str(m1)+"\n")
    if(m1[i][j+1]==0):
        break
    elif(j<1):
        j=j+1
    else:
        break

d=np.array([[0],[0],[0]],dtype="float")
k=2

def sigma(i,j,k=2):
    sum=0
    while(j<=k):
        sum=sum+(m1[i][j]*d[j])
        j=j+1
    return(sum)
    
for i in range(2,-1,-1):
    d[i]=(m1[i][3]-sigma(i,i+1,))/m1[i][i]
    
for i in range(3):
    print("x"+str(i+1)+"="+str(d[i]))


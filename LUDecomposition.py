# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:51:21 2020

@author: Abhishek
"""
import numpy as np
def mat():
    m=int(input("please provide the number of rows "))
    n=int(input("Please provide the number of columns "))
    mat=np.zeros((m,n))
    i=0
    while(i<m):
        j=0
        while(j<n):
            mat[i][j]=input("please provide element "+str(i+1)+str(j+1)+"= ")
            j=j+1
        i=i+1
    return(mat)
mat=mat()
c=mat
mat1=np.zeros(shape=(3,4),dtype="float")
mat1[0]=c[0]
i=1
while(i<=2):
   mat1[i]=c[i]-((c[i][0]/c[0][0])*c[0]) 
   i=i+1
lowt=np.zeros(shape=(3,3),dtype="float")
i=0
j=0
print(c)
while(i<3):
    j=0
    while(j<3):
        if(i==j):
            lowt[i][j]=1
        elif(j>i):
            lowt[i][j]=0
        else:
            lowt[i][j]=c[i][j]/c[0][0]
        if(i==2 and j==1):
            lowt[i][j]=mat1[i][j]/mat1[i-1][j]
        j=j+1
    i=i+1
print(str(lowt)+"is the lower triangular matrix.")

#finding the upper triangular matrix (Code from Gauss Elimination)
m1=c
m=c
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
    if(m1[i][j+1]==0):
        break
    elif(j<1):
        j=j+1
    else:
        break

upt=np.zeros(shape=(3,3),dtype="float")
i=0
j=0
while(i<3):
    j=0
    while(j<3):
        upt[i][j]=m1[i][j]
        j=j+1
    i=i+1
print(str(upt)+"is the upper triangular matrix.")

lu=np.zeros(shape=(3,3),dtype="float")
#print(lu)

k=0
i=0
while(i<3):
    k=0
    while(k<3):    
        j=0
        while(j<3): 
            lu[i][k]=lu[i][k]+(lowt[i][j]*upt[j][k])
            j=j+1
        k=k+1
    i=i+1

print(str(lu)+"is the product matrix A, from, LU=A.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
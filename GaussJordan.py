# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:21:44 2020

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

#r=3
#c=4
#entries=list(map(float,input().split()))
#m=np.array(entries).reshape(r,c)
#print(str(m)+"\n")

#mat=np.array([[3,1,1,10],[4,3,2,20],[2,4,-2,0]],dtype='float')
matr=mat()
m=len(matr)
n=len(matr[0])
print(matr)
i=0
while(i<=(m-1)):
    matr[i]=matr[i]/matr[i][i]
    for j in range(n-1):
        if(j==i):
            continue
        matr[j]=matr[j]-(matr[j][i]*matr[i])           
    i=i+1
    print(matr)

for i in range(n-1):
    print("x"+str(i+1)+"="+str(matr[i][n-1]))

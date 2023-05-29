# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:19:54 2020

@author: Abhishek
"""
#n=input("Please provide the nummber of the data points.")
n=5
datavalues=[0.1411,-0.6878,-0.9962,-0.5507,-0.3115]
datapoints=[1,1.3,1.6,1.9,2.2]

#for m in range(0,int(n)):
#    datapoints.append(float(input("Put in the independent variables. ")))
#    datavalues.append(float(input("Put in the data values. ")))

def Lag(i,x,k):
    j=0
    prod=1
    for j in range(0,int(k)):
        if(j==i):
            continue
        prod=prod*((x-datapoints[j])/(datapoints[i]-datapoints[j]))
    return(prod)

x=float(input("Please provide the point at which you want the function value."))

l=int(input("Please provide the order of the polynomial"))
sum=0
for p in range(0,(int(l)+1)):
    sum=sum+(Lag(p, x, l+1)*datavalues[p])
print(sum)
#i=0
#j=0
#diff=[]
#for i in datapoints:
#    diff.append(abs(x-i))

#diff.ascend()

#for p in range(0,(int(l)+1))
#    sum=sum+Lag(p, x, l+1)*data   
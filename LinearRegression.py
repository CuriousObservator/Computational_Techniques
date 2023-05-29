# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:34:13 2020

@author: Abhishek
"""
import matplotlib.pyplot as mtplt
def summ(x=[],y=[]):
    add=0
    if(y==[]):
        for x in x:
            add=add+x
    if(x==[]):
        for y in y:
            add=add+y
    else:
        for i in range(len(y)):
            add=add+(x[i]*y[i])
    return(add)
def square(x):
    return(x*x)
def sqsum(x=[],y=[]):
    add=0
    if(y==[]):
        for x in x:
            add=add+(x*x)
    if(x==[]):
        for y in y:
            add=add+(y*y)
    return(add)   
y=[0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7,7.2,7.4,7.6,7.8,8,8.2,8.4,8.6,8.8,9,9.2,9.4,9.6,9.8,10]
x=[26.461,10.002,22.681,45.613,44.013,5.341,38.251,25.73,30.452,42.159,42.161,65.814,59.416,53.825,62.658,65.005,86.411,64.923,76.696,63.189,41.705,93.804,100.967,80.868,130.046,78.185,104.686,105.192,134.992,138.04,122.324,129.672,114.683,102.288,130.781,142.345,162.454,166.036,146.19,151.465,144.272,142.7,142.406,201.262,168.355,173.429,165.208,199.662,167.792,192.809,186.568]
# n=int(input("Please provide the number of observations. "))
n=51
m=n


a1=((n*(summ(x,y)))-(summ(x)*summ(y)))/((n*sqsum(x))-square(summ(x)))
a0=(summ(y)/m)-((a1*summ(x))/n)
r=((n*summ(x,y))-(summ(x)*summ(y)))/((((n*sqsum(x))-square(summ(x)))**0.5)*(((n*sqsum(y))-square(summ(y)))**0.5))
print("square sum x "+str(sqsum(x)))
print("sum x*y"+str(summ(x,y)))
print("sum y "+str(summ(y)))
print("sum x "+str(summ(x)))
print("avg y "+str(summ(y)/m))
print("avg x "+str(summ(x)/n))
print("a1= "+str(a1))
print("a0= "+str(a0))
print("r^2= "+str(r*r))
z=[]
for i in x:
    z.append(a0+(a1*i))
mtplt.plot(x,z,linestyle='dotted',color='blue')
mtplt.scatter(x,y,color='red')

#plot styling
#fig=mtplt.figure()
#fig.suptitle('Linear Regression',fontsize=14,fontweight='bold')
#axis=fig.add_subplot(111)
#axis.set_xlabel('Independent Variable')
#axis.set_ylabel('Dependent Variable')
#axis.text(150,25,r'y='+str(a0)+str(a1)+'x',style='italic',
#          bbox={'facecolor':'red','alpha':0.5})
eq='y='+str(float("{:.2f}".format(a0)))+"+"+str(float("{:.2f}".format(a1)))+'x'
mtplt.xlabel('Independent Variable  -->')
mtplt.ylabel('Dependent Variable  -->')
mtplt.title('Linear Regression',loc='center',color='#4ef29e',bbox=dict(boxstyle='round'))


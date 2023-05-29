import math as m
def f(i):
    p=((i**m.log(i,m.e))-(m.e**m.sin(i))-(50*i))
    return(p)
xl=float(input("Give lowe limit"))
xu=float(input("Give upper limit"))
thr=float(input("Provide threshold error"))
ea=100
while(ea>thr):
    newx=xu-(f(xu)*(xu-xl)/(f(xu)-f(xl)))
    ea=abs(((newx-xl)/xl)*100)
    print(xl)
    print(f(xl))
    xl=newx
    print(ea)
    print(xu)
    print(f(xu))
    
    
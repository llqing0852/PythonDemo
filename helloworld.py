#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from collections import Iterable

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad oerand type')

    if(x>0):
        return x
    else:
        return -x

def enroll(name,gender,age=6,city='BeiJing'):
    print('Name：', name)
    print('Gender：', gender)
    print('Age：', age)
    print('City:', city)

def Calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

def Person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw) #kw是传入dict的拷贝
    kw['gender']='F'
    kw['heigh']=180
    print(kw)

def Person2(name,age,*,gender='M',heigh):
    print("name:",name,180,"gender",gender,"heigh:",heigh) 

def Fun(name,age=20,*others,lengh,**kw):
    print('name:',name,'age:',age)
    for other in others:
        print('other:',other) 
    print('lengh',lengh)
    print('keyword:',kw)

def fact(n):
    print(n)
    if n==1:
        return 1
    return n * fact(n - 1)

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def trim(str):
    l=len(str)
    while(l>0):
        l=l-1
        if(str[l]==' '):
            continue
        else:
            break
    return str[0:l+1]

def findMinAndMax(L):
    mi=L[0]
    ma=L[0]
    for l in L:
        if(l<mi):
            mi=l
        if(l>ma):
            ma=l
    return mi,ma

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():#杨辉三角
    N=[1]  
    while True:  
        yield N        #generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行  
        N.append(0)  
        N=[N[i-1] + N[i] for i in range(len(N))]


#g=fib(10)

g=triangles()
i=0
for gg in g:
    print(gg)
    i=i+1
    if i==10:
        break

#lis=[3,2,5,73,2,-3]

#for i,va in enumerate(lis):
#    print(i,va)

#print(findMinAndMax(lis))

#str=trim('abc  ab  ')
#print(len(str))


#nums=[1,2,3,4]
#print(Calc(*nums))

#kw={'gender':'M','heigh':170}
#Person('Harry',34,**kw)
#print(kw)

#Person2('Harry',34,gender='F',heigh=170)

#print(fact2(1000))

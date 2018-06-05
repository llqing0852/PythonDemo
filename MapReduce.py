# -*- coding:utf-8 -*-

from functools import reduce

def fn(x,y):
    return x*10 + y

def char2num(x):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[x]

def str2int(s):
    return reduce(fn,map(char2num,s))

def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def is_odd(n):
    return n%2==1

def not_empty(s):
    return s and s.strip()

s=list(filter(not_empty,'a b sdf aa'))
print(s)

#过滤奇数
l=list(filter(is_odd, range(1,10)))
print(l)

i=str2int('13457')
print(i)


# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:50:12 2021

@author: Admin
"""

from matplotlib import pyplot
import scipy as sp
from time import time
import numpy as np
import math

fx=input('Ingrese la funcion a evaluar: ')
xl=float(input('Ingrese el limite inferior del intervalo: '))
xu=float(input('Ingrese el limite superior: '))
er=float(input('Ingrese el error aceptado: '))
n=int(input("Ingrese el numero de iteraciones: "))


def f(x):
    return eval(fx)
i=1
while True:
    xr=(xl+xu)/2
    if f(xr)==0.0:
        break
    if(f(xl)*f(xr))<0:
        xl=xl
        xu=xr
    else:
        xl=xr
        xu=xu
    if i>1:
        xr2=(xl+xu)/2
        error=abs((xr2-xr)/xr2)*100
        print('error: ',error)
        
    print('Iteracion: ',i)
    print('xl=',xl)
    print('xu=',xu)
    print('xr=',xr)
    print('f(xl)=',f(xl))
    print('f(xu)=',f(xu))
    print('f(xr)=',f(xr))
    
    i=i+1
    
    if i==n+1:
        break
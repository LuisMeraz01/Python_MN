# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:38:59 2021

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


def f(x):
    return eval(fx)
i=1
while True:
    xr=(xu-((f(xu)*(xl-xu))/(f(xl)-f(xu))))
    if f(xr)==0.0:
        break
    if(f(xl)*f(xr))<0:
        xl=xl
        xu=xr
    else:
        xl=xr
        xu=xu
    if i>1:
        xr2=(xu-((f(xu)*(xl-xu))/(f(xl)-f(xu))))
        error=abs((xr2-xr)/xr2)*100
        if error<er:
            print('error: ',error)
            break
        xr2=xr
    print('Iteracion: ',i)
    print('xl=',xl)
    print('xu=',xu)
    print('xr=',xr)
    print('f(xl)=',f(xl))
    print('f(xu)=',f(xu))
    print('f(xr)=',f(xr))
    i=i+1
    
    
    
    
    
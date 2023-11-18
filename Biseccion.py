# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:56:21 2021

@author: Admin
"""

'''
(668.06/x)*(1-np.exp(-0.146843*x))-40
'''

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
        if error<er:
            print('error: ',error)
            break
    print('Iteracion: ',i)
    print('xl=',xl)
    print('xu=',xu)
    print('xr=',xr)
    print('f(xl)=',f(xl))
    print('f(xu)=',f(xu))
    print('f(xr)=',f(xr))
    i=i+1

































'''

fx=input('Ingrese la funcion a evaluar: ')
xl=float(input('Ingrese el limite inferior del intervalo: '))
xu=float(input('Ingrese el limite superior: '))
er=float(input('Ingrese el error aceptado: '))


#start_time = time.time() 


def f(x):
    return eval(fx)
# (668.06/x)*(1-e)

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
         if error<er:
             print('error: ',error)
             break
     print('Iteracion: ',i)
     print('xl=',xl)
     print('xu=',xu)
     print('xr=',xr)
     print('f(xl)=',f(xl))
     print('f(xu)=',f(xu))
     print('f(xr)=',f(xr))
     i=i+1    
    
       
    
  
elapsed_time = time.time() - start_time        
print("TImepo de ejecucion: %0.5f seconds."% elapsed_time)
'''    





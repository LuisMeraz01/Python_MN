# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:36:56 2021

@author: Admin

4*exp(0.8*x)-0.5*y
"""

from sympy import*
import numpy as np
import math as ma

fx=input('Funcion: ')
yi=float(input('Cuando "y" vale: '))
xi=float(input('"x" vale: '))
a=float(input('Desde: '))
b=float(input('Hasta: '))
h=float(input('Salto: '))
n=(b/h)

def f(x,y):
    return eval (fx)

print('\nx=',xi)
print('y=',yi)
xn=a

for i in np.arange(0,n):
    
    yimas1=yi+((f(xi,yi))*h) # yi+1
    xn=xn+h
    yi1=(yi+((f(xi,yi)+f(xn,yimas1))/2))*h # Nueva y
    print('\nx=',xn)
    print('y=',yi1)
    yi=yi1
    xi=xn
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
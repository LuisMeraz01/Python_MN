# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:08:34 2021

@author: Admin
 -2*x**3+12*x**2-20*x+8.5
"""

import numpy as np

fx=input('Funcion: ')
yi=float(input('Cuando "y" vale: '))
yi3=yi
xi=float(input('"x" vale: '))
a=float(input('Desde: '))
b=float(input('Hasta: '))
h=float(input('Salto: '))
n=(b/h)

def f(x,y):
    return eval (fx)


print('\nx=',xi)
print('y=',yi)

for i in np.arange(0,n):
    
    a=xi+h
    k1=f(xi,yi)
    k2=f(xi+h,yi+(k1*h))
    yimas1=yi+((h/2)*(k1+k2))
    print('\nx=',a)
    print('y=',yimas1)
    yi=yimas1
    xi=a
    
    
    
    
    
    
    
    
    
    
    
    
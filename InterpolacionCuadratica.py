# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:20:23 2021

@author: Admin
"""

from sympy import*
import numpy as np
import math as ma

fx=input('Funcion: ')
x=float(input('x: '))
x0=float(input('Primer valor del intervalo: '))
x1=float(input('Segundo valor del intervalo: '))
x2=float(input('Tercer valor del intervalo: '))

def f(x):
    return eval (fx)
vr=f(x)

fx0=f(x0)
fx1=f(x1)
fx2=f(x2)

b0=f(x0)
b1=((fx1-fx0)/(x1-x0))
b2=(((fx2-fx1)/(x2-x1))-((fx1-fx0)/(x1-x0)))/(x2-x0)

a2=b2
a1=(b1-(b2*x0)-(b2*x1))
a0=b0-(b1*x0)+(b2*x0*x1)

vapr=a0+a1*x+a2*x**2
er=abs(vr-vapr/vr)*100

print('\n---------------------------------------------------')
print('Valor verdadero=',vr)
print('Valor aproximado=',vapr)
print('Polinomio=',a2,'x**2+',a1,'x',a0)
print('Error=',er,'%')
print('-----------------------------------------------------')

























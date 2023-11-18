# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:02:10 2021

@author: Admin
"""

from sympy import*
import numpy as np
import math as ma

fx=input('Funcion: ')
x=float(input('x: '))
x0=float(input('Desde: '))
x1=float(input('Hasta: '))

def f(x):
    return eval (fx)

fx0=f(x0)
fx1=f(x1)

vapr=fx0+((fx1-fx0)/(x1-x0))*(x-x0)
vr=f(x)
er=abs((vr-vapr)/vr)*100

print('\n---------------------------------------------------')
print('Valor real=',vr)
print('Valor aproximado=',vapr)
print('Ecuacion=',vapr,'x',-vapr)
print('Error=',er,'%')
print('-----------------------------------------------------')

    



# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:16:13 2021

@author: Admin
 -2*x**3+12*x**2-20*x+8.5
y=1
x=0
desde=0
hasta=4
h=1
"""
from sympy import*
import numpy as np
import math as ma


print('************** Metodo de Runge Kutta 3 Orden **************')
op=int(input('La funcion es de 1 o 2 variables: '))
fx=input('Funcion: ')
yi=float(input('Cuando "y" vale: '))
yi3=yi
xi=float(input('"x" vale: '))
a=float(input('Desde: '))
b=float(input('Hasta: '))
h=float(input('Salto: '))
n=(b/h)


if op==1:
    
    x=symbols('x')
    ing=integrate(fx,x)
    gx=str(ing)

    def g(x):
        return eval (gx)

    c=(g(xi)*(-1))+yi3 # Calculando el valor de la constante de integracion
    intgx=str(ing+c)

    def intg(x):
        return eval (intgx)
    
    
    
def f(x,y):
    return eval (fx)

print('\n------------------------------------------------')
print('x=',xi)
print('y=',yi)

for i in np.arange(0,n):
    
    a=a+h
    k1=f(xi,yi)
    k2=f((xi+(3/4*h)),(yi+((3/4)*k1*h)))
    yin=yi+(((1/3)*(k1))+((2/3)*k2))*h
    print('------------------------------------------------')
    print('x=',a)
    print('y=',yin)
    yi=yin
    xi=a
    
    if op==1:    
        print('Valor verdadero=',intg(a))
        er=abs((intg(a)-yin)/intg(a))*100
        print('Error=',er,'%')
    
print('------------------------------------------------')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
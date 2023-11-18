# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:52:45 2021

@author: Admin
Funcion ejemplo: -2*x**3+12*x**2-20*x+8.5
"""
from sympy import*
import numpy as np
import math as ma

print('\n*************** METODO DE EULER ***************')
op=int(input('La funcion es de 1 o 2 variables: '))
fx=input('Funcion: ')
yi=float(input('Cuando "y" vale: '))
yi3=yi
xi=float(input('"x" vale: '))
a=float(input('Desde: '))
b=float(input('Hasta: '))
h=float(input('Salto: '))
n=(b/h)+1

if op==1:
    
    def f(x):
        return eval (fx)

    x=symbols('x')
    ing=integrate(fx,x)
    gx=str(ing)

    def g(x):
        return eval (gx)

    c=(g(xi)*(-1))+yi3 # Calculando el valor de la constante de integracion
    intgx=str(ing+c)

    def intg(x):
        return eval (intgx)
    
    for i in np.arange(0,n):
        
        if i==0:
            print('\n*********************************************************')
            print('x=',xi)
            print('y=',yi)
            print('Valor verdadero=',intg(a))
            er=abs(((intg(a))-yi)/intg(a))*100
            print('Eror=',er)
            fxy=f(xi)
            xi2=a+h
            
        if i!=0:
            
            y2=yi+(h*fxy)
            fxy=f(xi2)
            print('*********************************************************')
            print('x=',xi2)
            print('y=',y2)
            print('Valor verdadero=',intg(xi2))
            er=abs(((intg(xi2))-y2)/intg(xi2))*100
            print('Eror=',er)
            yi=y2
            xi2=xi2+h
    
    print('*********************************************************')

if op==2:
    
    def f(x,y):
        return eval (fx)
    
    for i in np.arange(0,n):
        
        if i==0:
            print('\n*********************************************************')
            print('x=',xi)
            print('y=',yi)
            fxy=f(xi,yi)
            xi2=a+h
            
        if i!=0:
            
            y2=yi+(h*fxy)
            fxy=f(xi2,y2)
            print('*********************************************************')
            print('x=',xi2)
            print('y=',y2)
            yi=y2
            xi2=xi2+h
            
    
print('*********************************************************')
#print('Valor verdadero=',intg(h))
    
    
    
        
    
    

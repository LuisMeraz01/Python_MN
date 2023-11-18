# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:25:35 2021

@author: Admin
-2*x**3+12*x**2-20*x+8.5
4*exp(0.8*x)-0.5*y
"""

import numpy as np

print('******* METODO DEL PUNTO MEDIO *******')
op=int(input('Su funcion tiene 1 o 2 variables? '))
    
fx=input('Funcion: ')
yi=float(input('Cuando "y" vale: '))
yi3=yi
xi=float(input('"x" vale: '))
a=float(input('Desde: '))
b=float(input('Hasta: '))
h=float(input('Salto: '))
n=(b/h)

s=a

if op==1: # ********************* En caso de funcion de una sola variable *********************
    
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
    
    print('\nx=',xi)
    print('y=',yi)
    print('Valor verdadero=',intg(s))
    print('Error=',0)
    
    for i in np.arange(n):
        
        s=s+h
        k1=f(xi)
        k2=f(xi+h/2)
        yimas1=yi+k2*h
        print('\nx=',s)
        print('y=',yimas1)
        print('Valor verdadero=',intg(s))
        er=abs((intg(s)-yimas1)/intg(s))*100
        print('Error=',er,'%')
        yi=yimas1
        xi=s
            
    
if op==2: # ********************* En caso de funcion de dos variables *********************
    
    def f(x,y):
        return eval (fx)
    
    print('\nx=',xi)
    print('y=',yi)
    #print('Valor verdadero=',intg(s))
    
    for i in np.arange(n):
        
        s=s+h
        k1=f(xi,yi)
        m=yi+((h/2)*2)
        k2=f(xi+h/2,m)
        yimas1=yi+k2*h
        print('\nx=',s)
        print('y=',yimas1)
        #print('Valor verdadero=',intg(s))
        #er=abs((intg(s)-yimas1)/intg(s))*100
        #print('Error=',er,'%')
        yi=yimas1
        xi=s
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
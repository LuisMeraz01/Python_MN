# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:46:06 2021

@author: Admin
"""
'''
(668.06/x)*(1-np.exp(-0.146843*x))-40

(668.06/x.exp(2))*((-1+np.exp(-0.146843*x)*(0.146843*x+1))

(668.06/x.exp(2))*((-1+np.exp(-0.146843*x))*(0.146843*x+1))

(668.06/pow(x,2)*((-1+(pow(e,-0.146843*x)))*(0.146843*x+1))

(668.06*x**2)*((-1+e**-0.146843*x)))*(0.146843*x+1))

(668.06/x**2)*((-1+np.exp(-0.146843*x))*(0.146843*x+1))
'''


import numpy as np
import sympy as sp
import math

fx=input("Ingrese la funcion a evaluar: ")
gx=input("Ingrese la derivada de la funcion: ")
xi=float(input("Ingrese el valor de x inicial: "))
er=float(input("Ingrese el valor aceptado: "))

def f(x):
    return eval(fx)

def g(x):
    return eval(gx)

error=100
i=1

while True:
    error>er
    
    fxi=f(xi)
    gxi=g(xi)
    xi2=xi-(fxi/gxi)
    
    if i>1:    
        error=abs((xi2-xi)/xi2)*100 
        if error<er:
            
            print ("Error=",error)
            break
    
    
    
    print("Iteracion=",i)
    print("xi=",xi)
    print("f(xi)=",fxi)
    print("F'(xi)",gxi)
    i=i+1
    xi=xi2    
        
        
        
        
        
        

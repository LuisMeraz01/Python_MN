# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:33:43 2021

@author: Admin
"""

'''
((668.06/x)*(1-np.exp(-0.146843*x))-40)+x
'''
import math
import numpy as np

fx=input("Ingrese la funcion a evaluar(sumandole una x etra al final): ")
xi=float(input("Ingrese el valor inicial: "))
er=float(input("Ingrese el error aceptado: "))

def f(x):
    return eval(fx)


error=100
i=1

while True:
    error>er
    
    
    xi2=f(xi)
    
     
    if i>1:
        error=abs((xi2-xi)/xi2)*100
        if error<er:
            
            print ("Error=",error)
            break
    
    
    
    print("Iteracion=",i)
    print("xi=",xi)
    print("f(xi)=",xi2)
    i=i+1
    xi=xi2 
    
    
    
    
    
    
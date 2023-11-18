# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:31:31 2021

@author: Admin
"""

import math
import numpy as np

fx=input("Ingrese la funcion a evaluar(sumandole una x etra al final): ")
xi=float(input("Ingrese el valor inicial: "))
er=float(input("Ingrese el error aceptado: "))
n=int(input("Ingrese la iteraciones que desea: "))

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
    
    if i==n+1:
        break
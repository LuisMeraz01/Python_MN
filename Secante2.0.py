# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:27:54 2021

@author: Admin
"""
import math
import numpy as np

fx=input("Ingrese la funcion a evaluar: ")
xi=float(input("Valor iniclal de xi: "))
xi2=float(input("Valor anterior: "))
er=float(input("Error aceptado: "))
n=int(input("Numero de iteraciones deseada: "))

def f(x):
    return eval(fx)

error=100
i=1
while True:
    error>er
      
    fxi=f(xi)
    fxi2=f(xi2)

    
    if i>1:
        
        a=xi
        xi=xi-(f(xi)*(xi2-xi))/(f(xi2)-f(xi))
        xi2=a
        error=abs((xi-xi2)/xi)*100
        print("Error: ",error)
            
              
    print("Iteracion: ",i)
    print("xi: ",xi)
    print("f(xi): ",fxi)
    print("f(xi-1): ",fxi2)
    
    i=i+1
    
    if i==n+1:
        break
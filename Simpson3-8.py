# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:42:40 2021

@author: Admin
"""

from sympy import*
import numpy as np

fx=input('Funcion: ')
a=float(input("Intervalo inferior: "))
b=float(input("Intervalo superior: "))
n=int(input("Valor de la n: "))

x=symbols('x')
intg=integrate(fx,x)
gx=str(intg)

def f(x):
    return eval (fx)

def g(x):
    return eval (gx)

h=(b-a)/n
n=n+1

y = np.zeros(shape=(n))
x = np.zeros(shape=(n))
k=1
suma=0
for i in range (n): # FOR PARA ASIGNAR LOS VALORES DE X EN EL ARREGLO 
    
    if k==1:
        x[i]=a
        y[i]=f(x[i])
        
    if k>1 and k<n:
        x[i]=x[i-1]+h
        fxo=f(x[i])
        y[i]=fxo # AQUI VA A IR GUARDANDO LOS VALORES DE LAS EVALUACIONES EN EL ARREGLO "Y"
        suma=suma+y[i]
    k=2
    
    if i==n:
        x[i]=b
        y[i]=f(x[i])
   

n=n-1
suma=suma-f(b)
vr=(g(b)-g(a)) # Teorema fundamental del calculo
iaprox=(b-a)*((f(a)+(3*suma)+f(b))/(8))
er=(abs((vr-iaprox)/vr))*100


print(x)
print(y)
print("\n***************************************************")
print("\nValor verdadero=",vr)  
print("Integral aproximada= ",iaprox) 
print("Error=",er,"%")    
print("****************************************************")
   
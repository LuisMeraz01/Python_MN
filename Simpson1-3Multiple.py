# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:56:50 2021

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
pares=0
impares=0
for i in range (n): # FOR PARA ASIGNAR LOS VALORES DE X EN EL ARREGLO 
    
    if k==1:
        x[i]=a
        y[i]=f(x[i])
        
    if k>1 and k<n:
        
        x[i]=x[i-1]+h
        fxo=f(x[i])
        y[i]=fxo # AQUI VA A IR GUARDANDO LOS VALORES DE LAS EVALUACIONES EN EL ARREGLO "Y"
        
        res=i%2
        if res==0:
            pares=pares+y[i]
            
        if res!=0:
            impares=impares+y[i]
    k=2
    
    if i==n:
        x[i]=b
        y[i]=f(x[i])

resul=n%2

if resul==0:
    impares=impares-f(b)
if resul!=0:
    pares=pares-f(b)
    
    
n=n-1

vr=(g(b)-g(a)) # Teorema fundamental del calculo
intapx=(b-a)*((f(a)+(4*impares)+(2*pares)+f(b))/(3*n))
er=(abs(vr-intapx)/vr)*100

print(x)
print(y)
print(n)
print(impares)
print(pares)
print("\n***************************************************")
print("Valor verdadero=",vr)
print("Integral aproximada= ",intapx)
print("Error=",er,"%")
print("*****************************************************")



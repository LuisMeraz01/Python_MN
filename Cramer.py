# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:31:44 2021

@author: Admin
"""

import numpy as np


m=int(input("Numero de Filas: "))
n=int(input("Numero de Columnas: "))

# ************************ Llenado de las matrices ******************************************* 

x = np.zeros(shape=(m,n))

for i in range (m):
    for k in range (n):
        x[i,k]=float(input("Ingresa valor de elemento a"+repr(i+1)+repr(k+1)+": "))
        
print(x)

print("\nIntroducir los valores del lado derecho del igual de arriba hacia abajo")

x2= np.zeros(shape=(m))

for i in range (m):
    x2[i]=float(input("Ingrese el valor de elemento "+repr(i)+": "))

print("\nLaado izquierdo matriz")

for i in range (m):
    
    print(x2[i])


# ************************* Determinante del sistema *****************************************
dx=np.linalg.det(x)
print("\nDeterminante del sistema: ",dx)

# ************************ Determinantes de las incognitas **********************************

L=len(x2)
xdet=np.zeros(L)

for i in range (L):
    copx=x.copy()
    copx.T[i]=x2
    dxcop=np.linalg.det(copx)
    sol=dxcop/dx
    print("Soluciones:")
    print("Solucion",(i+1),": ",sol)




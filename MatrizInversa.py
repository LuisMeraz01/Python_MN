# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:03:56 2021

@author: Admin
"""

import numpy as np

while True:
        print("Introducir el numero de columnas y filas solo del lado izquierdo del igual")
        m=int(input("Numero de Filas: "))
        n=int(input("Numero de Columnas: "))
        
        if m==n:
            break
        else:
            print("\nSi el numero de filas y columnas es diferente la matriz no tendra inversa")
            print("Vuelva a intentarlo :D\n")
 
arr = np.zeros(shape=(m,n))

for i in range (m):
    for k in range (n):
        arr[i,k]=float(input("Ingresa valor de elemento a"+repr(i+1)+repr(k+1)+": "))
        
print("\nMatriz original")        
print(arr)
arrx=np.linalg.inv(arr)
print("Matriz inversa")
print(arrx)


print("\nIntroducir los valores del lado derecho del igual de arriba hacia abajo")

arr2= np.zeros(shape=(m))

for j in range (m):
    arr2[j]=float(input("Ingrese el valor de elemento "+repr(j)+": "))

print("\nLaado izquierdo matriz")

for i in range (m):
    
    print(arr2[i])

x=np.dot(arrx,arr2)
print("\nSoluciones:")
print(x)




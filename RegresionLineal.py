# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:09:08 2021

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

print('\n* * * * * * REGRESION LINEAL * * * * * *')

n=int(input("Numero de n's: "))

sumax=0
sumay=0
sumamul=0
sumacuad=0
promx=0
promy=0

print('\n------------------------------------------------')
x = np.zeros(shape=(n))
z= np.zeros(shape=(n))
x2= np.zeros(shape=(n)) # TODOS LOS ARREGLOS QUE UTILIZAREMOS CON SU "N" DE RANGO
y = np.zeros(shape=(n))

for i in range (n):
    
    x[i]=float(input('Valor '+repr(i+1)+' de xi: ')) # LLENANDO EL ARREGLO DE LAS XI
    
    sumax=sumax+x[i] # SUMANDO LOS VALORES DEL ARREGLO DE LA XI
    x2[i]=x[i]*x[i] # LLENAR EL ARREGLO DE X AL CUADRADO
    sumacuad=sumacuad+x2[i] # SUMA DE LOS VALORES DEL ARREGLO X AL CUADRADO
    
print('\n------------------------------------------------')

for i in range (n):
    
    
    y[i]=float(input('Valor '+repr(i+1)+' de yi: ')) # LLENANDO EL ARREGLO DE LAS YI
    
    sumay=sumay+y[i] # SUMA DEL ARREGLO DE LAS YI
    z[i]=x[i]*y[i] # LLENANDO EL ARREGLO DE LAS MULTIPLICACION DE LAS X POR LAS Y
    sumamul=sumamul+z[i] # SUMANDO LO VALORES DEL ARREGLO DE MULTIPLICACION DE X POR Y
    
promx=sumax/n # CALCULADNO EL PROMEDIO DE LA SUMA DE LOS VALORES DEL ARREGLO X
promy=sumay/n # CALCULANDO EL PROMEDIO DE LA SUMA DE LOS VALORES DEL ARREGLO Y

a1=((n*(sumamul)-(sumax*sumay))/((n*sumacuad)-(sumax*sumax)))
a0=promy-a1*(promx)

print('\n-----------------------------------------------------------------------')
print('Polinomio=',a0,'+',a1,'x') # IMPRIMIENDO EL POLINOMIO
print('-----------------------------------------------------------------------')

pol=np.poly1d([a1,a0])
print(pol)

plt.plot(x,y,'ro')
plt.plot(pol(x))
plt.show











    
'''
print(x)
print('\ny')
print(y)
print('\nMultiplicacion de arreglos')
print(z)
print('\nCuadrado de arreglo x')
print(x2)

print('Suma de las x=',sumax)
print('Suma de las y=',sumay)
print('Suma de x por y=',sumamul)
print('Suma de x al cuadrado=',sumacuad)
'''





    
    
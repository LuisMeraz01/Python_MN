# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:07:53 2021

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


# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:09:12 2021

@author: Admin
"""

from sympy import*

fx=input('Funcion: ')
xi=float(input("Valor de xi: "))

x=symbols('x')
dfx=diff(fx,x)
print(dfx)
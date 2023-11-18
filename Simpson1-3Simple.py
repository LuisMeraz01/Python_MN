# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:36:54 2021

@author: Admin
"""

from sympy import*

fx=input('Funcion: ')
a=float(input("Intervalo inferior: "))
b=float(input("Intervalo superior: "))

x=symbols('x')
intg=integrate(fx,x)
gx=str(intg)

def f(x):
    return eval (fx)

def g(x):
    return eval (gx)

h=(b-a)/2

vr=(g(b)-g(a)) # Teorema fundamental del calculo

intapr=(b-a)*((f(a)+4*(f(h))+f(b))/6)

er=(abs(vr-intapr)/vr)*100

print("\n***************************************************")
print("\nIntegral aprox=",intapr)
print("Valor real=",vr)
print("Error=",er,"%")
print("*****************************************************")
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:55:12 2021

@author: Admin
"""

"""
Funcion ejemplo: 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
"""

from sympy import*

fx=input('Funcion: ')
inf=float(input("Intervalo inferior: "))
sup=float(input("Intervalo superior: "))

x=symbols('x')
intg=integrate(fx,x)
gx=str(intg)

def f(x):
    return eval (fx)

def g(x):
    return eval (gx)

vr=(g(sup)-g(inf)) # Teorema fundamental del calculo

intg=(sup-inf)*((f(inf)+f(sup))/2)

er=(abs(vr-intg)/vr)*100

print("\n***************************************************")
print("\nIntegral aprox=",intg)
print("Valor real=",vr)
print("Error=",er,"%")
print("*****************************************************")

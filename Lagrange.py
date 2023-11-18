# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:29:52 2021

@author: Admin
"""
from sympy import*

while True:

    print('\n1/Primer grado')
    print('2/Segundo grado')
    print('3/Tercer grado')
    op=int(input('Opcion: '))


    fx=input('Funcion: ')
    x=float(input('x: '))
    x0=float(input('Primer valor del intervalo: '))
    x1=float(input('Segundo valor del intervalo: '))
    x2=float(input('Tercer valor del intervalo: '))
    
    def f(x):
        return eval (fx)
    
    vr=f(x)
    fx0=f(x0)
    fx1=f(x1)
    fx2=f(x2)
    
    if op==1:
        
        vapr=(((x-x1)/(x0-x1))*(fx0))+((x-x0)/(x1-x0))*(fx1)
        print('Polinomio=',vapr,'x+',vapr)
    
    if op==2:
        
        vapr=((((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))*(fx0))+((((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))*(fx1))+((((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))*(fx2))
       
    if op==3:
        
        x3=float(input('Cuarto valor del intervalo: '))
        fx3=f(x3)
        vapr=((((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3)))*(fx0))  +  ((((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3)))*(fx1))  +  ((((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3)))*(fx2))  +  ((((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2)))*(fx3))                                   
        
        
        
    er=abs((vr-vapr)/vr)
    print('\n---------------------------------------------------')
    print('Valor real=',vr)
    print('Valor aproximado=',vapr)
    print('Error=',er,'%')
    print('---------------------------------------------------')
    
    print("1/ Nueva Interpolacion")
    print("2/ Salir")
    re=int(input("Opcion: "))
    
    if re==2:
        break


#((((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))*(fx0))+((((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))*(fx1))+((((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))*(fx2))

# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:58:29 2021

@author: Admin
"""
from sympy import*
import numpy as np
import math as ma

while True:

    print('\n1/ Interpolacion de grado 1')
    print('2/ Interpolacion de grado 2')
    print('3/ Interpolacion de grado 3')
    op=int(input('Opcion: '))
    
    '''
    fx=input('Funcion: ')
    x=float(input('x: '))
    
    def f(x):
        
        return eval (fx)
    
    vr=f(x)
    '''
    
    if op==1:
        
        x=float(input('X: '))
        
        x0=float(input('Desde: '))
        x1=float(input('Hasta: '))
        
        fx0=float(input('Primer valor: '))
        fx1=float(input('Segundo valor: '))
        
        
        
        
        vapr=fx0+((fx1-fx0)/(x1-x0))*(x-x0)
        
        
        
        #er=abs((vr-vapr)/vr)*100
        
        print('\n---------------------------------------------------')
        #print('Valor real=',vr)
        print('Valor aproximado=',vapr)
        #print('Ecuacion=',vapr,'x',-vapr)
        #print('Error=',er,'%')
        print('-----------------------------------------------------')
        
    if op==2:
        
        x0=float(input('Primer valor del intervalo: '))
        x1=float(input('Segundo valor del intervalo: '))
        x2=float(input('Tercer valor del intervalo: '))
        
        fx0=f(x0)
        fx1=f(x1)
        fx2=f(x2)
        
        b0=f(x0)
        b1=((fx1-fx0)/(x1-x0))
        b2=(((fx2-fx1)/(x2-x1))-((fx1-fx0)/(x1-x0)))/(x2-x0)
        
        a2=b2
        a1=(b1-(b2*x0)-(b2*x1))
        a0=b0-(b1*x0)+(b2*x0*x1)
        
        vapr=a0+a1*x+a2*x**2
        er=abs(vr-vapr/vr)*100
        
        print('\n---------------------------------------------------')
        print('Valor verdadero=',vr)
        print('Valor aproximado=',vapr)
        print('Polinomio=',a2,'x**2+',a1,'x',a0)
        print('Error=',er,'%')
        print('-----------------------------------------------------')
        
    if op==3:
        
        x0=float(input('Primer valor del intervalo: '))
        x1=float(input('Segundo valor del intervalo: '))
        x2=float(input('Tercer valor del intervalo: '))
        x3=float(input('Cuarto valor del intervalo: '))
        
        fx0=f(x0)
        fx1=f(x1)
        fx2=f(x2)
        fx3=f(x3)
        
        b0=f(x0)
        b1=((fx1-fx0)/(x1-x0))
        b2=(((fx2-fx1)/(x2-x1))-((fx1-fx0)/(x1-x0)))/(x2-x0)
        b3=((((((fx3-fx2)/(x3-x2))-(((fx2-fx1))/(x2-x1))))/(x3-x1))-((((fx2-fx1)/(x2-x1))-(((fx1-fx0))/((x1-x0))))/(x2-x0)))/(x3-x0)
        
        vapr=(b0+(b1*(x-x0)))+(b2*(x-x0)*(x-x1))+(b3*(x-x0)*(x-x1)*(x-x2))
        er=abs(vr-vapr/vr)*100
        
        print('\n---------------------------------------------------')
        print('Valor verdadero=',vr)
        print('Valor aproximado=',vapr)
        print('Error=',er,'%')
        print('-----------------------------------------------------')
        
    print("1/ Nueva Interpolacion")
    print("2/ Salir")
    re=int(input("Opcion: "))
    
    if re==2:
        break
                         
    

       
        
        

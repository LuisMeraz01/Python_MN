# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:30:33 2021

@author: El Meraz
"""

from sympy import*
import numpy as np
import math as ma

print("* * * * * * * * INTEGRACION NUMEIRCA * * * * * * * *")
print("\nEscoja el numero de la metodo que desea utilizar que desee utilizar")


while True:
    
    print("\n1/ Regla del trapecio simple")
    print("2/ Regla del trapecio multiple")
    print("3/ Regla de Simpson 1/3 simple")
    print("4/ Regla de Simpson 1/3 multiple")
    print("5/ Regla de Simpson 3/8")
    op=int(input("Opcion: "))
    
    if op>5:
        print("Opcion invalida**")
        
    
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
    
    vr=(g(b)-g(a)) # Teorema fundamental del calculo
    
    
    
    if op==1: # REGLA DEL TRAPECIO SIMPLE ***************************************************
        
        intg=(b-a)*((f(a)+f(b))/2)
    
        er=(abs(vr-intg)/vr)*100
        
        print("\n***************************************************")
        print("Integral aprox=",intg)
        print("Valor real=",vr)
        print("Error=",er,"%")
        print("*****************************************************")
        
    if op==2: # REGLA DEL TRAPECIO MULTIPLE **************************************************
        
        n=int(input("Valor de la n: "))
        h=(b-a)/n
        y = np.zeros(shape=(n))
        x = np.zeros(shape=(n))
        k=1
        suma=0
        for i in range (n): # FOR PARA ASIGNAR LOS VALORES DE X EN EL ARREGLO 
            
            if k==1:
                x[i]=a
                
            if k>1 and k<n:
                x[i]=x[i-1]+h
                fxo=f(x[i])
                y[i]=fxo # AQUI VA A IR GUARDANDO LOS VALORES DE LAS EVALUACIONES EN EL ARREGLO "Y"
                suma=suma+y[i]
            k=2        
            if i==n:
                x[i]=b            
            
        vr=(g(b)-g(a)) # Teorema fundamental del calculo
        iaprox=(b-a)*((f(a)+(2*suma)+f(b))/(2*n))
        er=(abs((vr-iaprox)/vr))*100
        print("\n***************************************************")
        print("Valor verdadero=",vr)  
        print("Integral aproximada= ",iaprox) 
        print("Error=",er,"%")    
        print("****************************************************")
        
    if op==3: # REGLA DE SIMPSON 1/3 SIMPLE **************************************************
        
        h=(b-a)/2
        intapr=(b-a)*((f(a)+4*(f(h))+f(b))/6)
    
        er=(abs(vr-intapr)/vr)*100
    
        print("\n***************************************************")
        print("Integral aprox=",intapr)
        print("Valor real=",vr)
        print("Error=",er,"%")
        print("*****************************************************")
        
    if op==4: # REGLA DE SIMPSON 1/3 MULTIPLE ************************************************
        
        n=int(input("Valor de la n: "))
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
        
        print("\n***************************************************")
        print("Valor verdadero=",vr)
        print("Integral aproximada= ",intapx)
        print("Error=",er,"%")
        print("*****************************************************")
        
    if op==5: # REGLA DE SIMPSON 3/8 *********************************************************
        
        n=3
        h=(b-a)/n
        n=n+1
        y = np.zeros(shape=(n))
        x = np.zeros(shape=(n))
        k=1
        suma=0
        for i in range (n): # FOR PARA ASIGNAR LOS VALORES DE X EN EL ARREGLO 
            
            if k==1:
                x[i]=a
                y[i]=f(x[i])
                
            if k>1 and k<n:
                x[i]=x[i-1]+h
                fxo=f(x[i])
                y[i]=fxo # AQUI VA A IR GUARDANDO LOS VALORES DE LAS EVALUACIONES EN EL ARREGLO "Y"
                suma=suma+y[i]
            k=2
            
            if i==n:
                x[i]=b
                y[i]=f(x[i])
        n=n-1
        suma=suma-f(b)
        vr=(g(b)-g(a)) # Teorema fundamental del calculo
        iaprox=(b-a)*((f(a)+(3*suma)+f(b))/(8))
        er=(abs((vr-iaprox)/vr))*100
        print("\n***************************************************")
        print("Valor verdadero=",vr)  
        print("Integral aproximada= ",iaprox) 
        print("Error=",er,"%")    
        print("****************************************************")
    
    
    print("1/ Nueva Integracion")
    print("2/ Salir")
    re=int(input("Opcion: "))
    
    if re==2:
        break
        
    
    
    
# FIN ***************************************************************************************************************************  



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
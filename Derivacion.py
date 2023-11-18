# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:29:57 2021

@author: El Meraz

-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

"""

from sympy import*

while True:

    print("               MENU DE DERIVACION           ")
    
    print("\nEscoja el numero de opcion que vaya necesitando")
    print("\n1/ Fórmulas de diferencias finitas divididas hacia adelante")
    print("2/ Fórmulas de diferencias finitas divididas hacia atras")
    print("3/ Fórmulas de diferencias finitas divididas centradas")
    op=int(input("Opcion: "))
    
    print("\n1/ Primera derivada")
    print("2/ Segunda derivada")
    print("3/ Tercera derivada")
    print("4/ Cuarta derivada")
    opp=int(input("Opcion: "))
    
    print("\n1/ Terminos de la primera derivada")
    print("2/ Terminos de la segunda derivada")
    oppp=int(input("Opcion: "))
    
    fx=input('Funcion: ')
    xi=float(input("Valor de xi: "))
    h=float(input("Valor de h o salto: "))
    
    x=symbols('x')
    dfx=diff(fx,x)
    gx=str(dfx) # PRIMERA DERIVADA
    ddosfx=diff(gx,x)
    ix=str(ddosfx) # SEGUNDA DERIVADA
    dtresfx=diff(ix,x)
    jx=str(dtresfx) # TERCERA DERIVADA
    dcuatrofx=diff(jx,x) 
    kx=str(dcuatrofx) # CUARTA DERIVADA
    
    
    
    def f(x):
        return eval(fx)
    
    
    fxi=f(xi) # f(xi)
    
    ximas1=xi+h # xi+1
    fximas1=f(ximas1) # f(xi+1)
    ximas2=ximas1+h # xi+2
    fximas2=f(ximas2) # f(xi+2)
    ximas3=ximas2+h # xi+3
    fximas3=f(ximas3) # f(xi+3)
    ximas4=ximas3+h # xi+4
    fximas4=f(ximas4) # f(xi+4)
    ximas5=ximas4+h # xi+5
    fximas5=f(ximas5) # f(xi+5)
    
    
    
    if op==1: # IF DE LAS FORMULAS HACIA ADELANTE *********************************
        
        if opp==1: # IF DE LA PRIMERA DERIVADA ************************************
            
            def g(x):
                return eval(gx)
            
            vr=g(xi) # f'(xi) o Valor real
            print("\nValor verdadero=",vr)
    
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fximas1-fxi)/h
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
            
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(-(fximas2)+4*(fximas1)-3*(fxi))/(2*h)
                print("f'(xi)=",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==2: # IF DE LA SEGUNDA DERIVADA ************************************
            
            def i(x):
                return eval(ix)
                
            vr=i(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=((fximas2-(2*(fximas1))+fxi))/(h**2)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(-fximas3+(4*(fximas2))-(5*(fximas1))+2*(fxi))/(h**2)
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==3: # IF DE LA TERCERA DERIVADA ************************************
            
            def j(x):
                return eval(jx)
            
            vr=j(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=((fximas3)-3*(fximas2)+3*(fximas1)-fxi)/(h**3)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(-3*(fximas4)+14*(fximas3)-24*(fximas2)+18*(fximas1)-5*(fxi))/(2*(h**3))
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if oppp==4: # IF DE LA CUARTA DERIVADA ************************************
            
            def k(x):
                return eval(kx)
            
            vr=k(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fximas4(-4*(fximas3))+6*(fximas2)-4*(fximas1)+fxi)/(h**4)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(-2*(fximas5)+11*(fximas4)-24*(fximas3)+26*(fximas2)-14*(fximas1)+3*(fxi))/(h**4)
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
    
    ximenos1=xi-h  # xi-1
    fximenos1=f(ximenos1) # f(xi-1)
    ximenos2=ximenos1-h  # xi-2
    fximenos2=f(ximenos2) # f(xi-2)
    ximenos3=ximenos2-h  # xi-3
    fximenos3=f(ximenos3) # f(xi-3)
    ximenos4=ximenos3-h  # xi-4
    fximenos4=f(ximenos4) # f(xi-4)
    ximenos5=ximenos4-h  # xi-5
    fximenos5=f(ximenos5) # f(xi-5)
     
            
    if op==2: # IF DE LAS FORMULAS HACIA ATRAS ***************************************************************************
        
        if opp==1: # IF DE LA PRIMERA DERIVADA ************************************
            
            def g(x):
                return eval(gx)
            
            vr=g(xi) # f'(xi) o Valor real
            print("\nValor verdadero=",vr)
    
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fxi-(2*(fximenos1))+fximenos2)/(h**2)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
            
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(2*(fxi)-5*(fximenos1)+4*(fximenos2)-fximenos3)/(h**2)
                print("f'(xi)=",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==2: # IF DE LA SEGUNDA DERIVADA ************************************
            
            def i(x):
                return eval(ix)
                
            vr=i(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fxi-(2*(fximenos1))+fximenos2)/(h**2)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(2*(fxi)-5*(fximenos1)+4*(fximenos2)-fximenos3)/(h**2)
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==3: # IF DE LA TERCERA DERIVADA ************************************
            
            def j(x):
                return eval(jx)
            
            vr=j(xi)
            print("/nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fxi-(3*(fximenos1))+3*(fximenos2)-fximenos3)/(h**3)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(5*(fxi)-18*(fximenos1)+24*(fximenos2)-14*(fximenos3)+3*(fximenos4))/(2*(h**3))
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if oppp==4: # IF DE LA CUARTA DERIVADA ************************************
            
            def k(x):
                return eval(kx)
            
            vr=k(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fxi-(4*(fximenos1))+6*(fximenos2)-4*(fximenos3)+fximenos4)/(h**4)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(3*(fxi)-14*(fximenos1)+26*(fximenos2)-24*(fximenos3)+11*(fximenos4)-2*(fximenos5))/(h**4)
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
                
    
    
    
    
    if op==3: # IF DE LAS FORMULAS CENTRADAS ***************************************************************************
        
        if opp==1: # IF DE LA PRIMERA DERIVADA ************************************
            
            def g(x):
                return eval(gx)
            
            vr=g(xi) # f'(xi) o Valor real
            print("\nValor verdadero=",vr)
    
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=(fximas1-fximenos1)/(2*h)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
            
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=(-fximas2+(8*(fximas1))-8*(fximenos1)+fximenos2)/(h**2)
                print("f'(xi)=",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==2: # IF DE LA SEGUNDA DERIVADA ************************************
            
            def i(x):
                return eval(ix)
                
            vr=i(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=((fximas1)-2*(fxi)+fximenos1)/(h**2)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=((-fximas2)+16*(fximas1)-30*(fxi)+16*(fximenos1)-fximenos2)/(12*(h**2))
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if opp==3: # IF DE LA TERCERA DERIVADA ************************************
            
            def j(x):
                return eval(jx)
            
            vr=j(xi)
            print("/nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=((fximas2)-2*(fximas1)+2*(fximenos1)-fximenos2)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=((-fximas3)+8*(fximas2)-13*(fximas1)+13*(fximenos1)-8*(fximenos2)+fximenos3)/(8*(h**3))
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
                
        if oppp==4: # IF DE LA CUARTA DERIVADA ************************************
            
            def k(x):
                return eval(kx)
            
            vr=k(xi)
            print("\nValor verdadero=",vr)
            
            if oppp==1: # IF DE TERMINOS DE LA PRIMERA DERIVADA *******************
                
                fpxi=((fximas2)-4*(fximas1)+6*(fxi)-4*(fximenos1)+fximenos2)/(h**4)
                print("f'(xi)=",fpxi)
                er=abs((vr-fpxi)/vr)*100
                print("Error verdadero= ",er,"%")
                
            if oppp==2: # IF DE TERMINOS DE LA SEGUNDA DERIVADA *******************
                
                fpxi2=((-fximas3)+12*(fximas2)+39*(fximas1)+56*(fxi)-39*(fximenos1)+12*(fximenos2)+fximenos3)
                print("f'(xi):",fpxi2)
                er=abs((vr-fpxi2)/vr)*100
                print("Error verdadero= ",er,"%")
            
    print("\n1/ Nueva Derivacion")
    print("2/ Salir")
    re=int(input("Opcion: "))
    
    if re==2:
        break            
        
            
            
        
        
        
        
    
        
        
        


            
            
    
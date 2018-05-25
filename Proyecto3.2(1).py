#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:37:03 2018

@author: tadssd
"""

Articulos={'A':{'Costo':6000,'Tiempo':10},'B':{'Costo':2000,'Tiempo':3},'C':{'Costo':4000,'Tiempo':10},'D':{'Costo':4000,'Tiempo':1},'E':{'Costo':3000,'Tiempo':4},'F':{'Costo':1000,'Tiempo':8},'G':{'Costo':5000,'Tiempo':6}}
MinimosArticulosEmpleados=[]


        
def imprimirDiccionario():
    for i in Articulos:
        print(i, ":", Articulos[i])

#def optimizarFB(mH,mA):
    

def optimizarTiempo(mH,mA):
    contador=0
    sumaTiempos=0
    for i in Articulos:
        while (Articulos[i]['Tiempo']<mH-sumaTiempos and sumaTiempos<mH and contador<=mA):
            contador=contador+1
            MinimosArticulosEmpleados.append([i,Articulos[i]])
            TiempoEmpleado=Articulos[i]['Tiempo']
            sumaTiempos=sumaTiempos+TiempoEmpleado

def primero(fin,Articulos):
    return Articulos[['A']:[fin]]

def validar(numArticulos):#Validar el número de productos
    if (numArticulos<=5):
        return True
    return False

def mostrar(opcion, producto, horasT):#mostrar todas las combinaciones 
    print("Opción de creación {}, producto {}".format(opcion,producto,horasT))
    return

def siguiente(c,t):
    c=c+1
    if c<len(t):
        return c
    return -1

def fuerzaBrutaPiezas():
    n=len(s)
    m=len(cadena)
    c=primero(len (s),cadena)
    pos=0
    numocur=0
    while pos!=m-n+1:
        if validar(c,s):
            numocur=numocur+1
            mostrar(c,numocur,pos)
        pos=pos+1    
        c=siguiente(n,cadena,pos)
 
def main():
    reinicio=1
    while reinicio==1:
        opcion=int(input("\n1.-Fuerza Bruta 2.-Avidos"))
        if opcion==1:
            c=primero()
            while(valido(c,20)==False):
                c=siguiente(c)
        elif opcion==2:  
                del MinimosArticulosEmpleados[:]
                maximoHoras=0
                maximoArticulos=0
                imprimirDiccionario()
                while maximoHoras<=0:
                    maximoHoras=int(input("\nDe cuanto desea el valor maximo de horas empleadas? "))
                while maximoArticulos<=0:
                    maximoArticulos=int(input("\nDe cuanto es la cantidad maxima de articulos empleados? "))
                optimizarTiempo(maximoHoras,maximoArticulos)
                print(MinimosArticulosEmpleados)
        reinicio=int(input("\nDesea volver a optimizar en base a tiempos y cantidad? Ingrese 1 para volver "))
        
        
    print("\nEjercicio adicional: Optimizar la venta de 8 articulos para sacar la maxima utilidad en el menor tiempo posible")
        
        
main()
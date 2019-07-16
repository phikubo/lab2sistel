

#import network
#import network
import math
import time

import gc
import ondas #->modulo ondas
import calculadora
from machine import Pin, SPI
from machine import DAC
import plotdac


def menu2(opcion2):
    time.sleep(0.1)
    while opcion2==0:
        print("0->Repetir menu")
        print("1->Default")
        print("2->Custom")
        print("<otro numero>->Terminar")
        print("--------")
        try:
            opcion2=int(input())
            print("--------")
        except:
            print("Ingresa un numero")
            print("--------")
    return opcion2
    
def custom_input(opcion3):
    print("Custom. Escriba los valores: ")
    try:
        max=1
        puntos=90
        print("Onda 1 <int>(s->1,r->2,t->3): ")
        tipo1=int(input())
        print("--------")
        print("Onda 2 <int>(s->1,r->2,t->3): ")
        tipo2=int(input())
        print("--------")
        print("Amplitud <int>(1-20): ")
        amplitud=int(input())
        print("--------")
        print("Frecuencia <int>(2-10): ")
        f=int(input())
        print("--------")
        print("Fase 1 <int>")
        phi1=int(input())
        print("Fase 2 <int>")
        phi2=int(input())
        print("--------")
        print("Input:", "onda1:{",tipo1,"} onda2: {", tipo2,"} A: {", amplitud,"} F: ", f, 4, phi1, phi2)
        print("Un momento, procesando")
        time.sleep(1)
        func1=ondas.onda(max, puntos, 4, amplitud, f, phi1, tipo1)
        func2=ondas.onda(max, puntos, 4, amplitud, f, phi2, tipo2)
        for i in range(len(func1)):
            print("{",func1[i],"}", "{",func2[i],"}")
            func1[i]=128+round(func1[i])
            func2[i]=128+round(func2[i])
            
        gc.collect()
        dac1 = DAC(Pin(25, Pin.OUT))
        dac2 = DAC(Pin(26, Pin.OUT))
        
        try:
            plotdac.pltdac(func1,func2, dac1, dac2)
        except Exception as e:
            print(e)
        
        
    except:
        print("Ingresa valores validos")
        print("--------")
    while opcion3 != 9:
        try:
            #print("1->Continuar")
            #print("--------")
            print("9 ->Salir")
            print("--------")
            opcion3=int(input())
            #if opcion3==1:
            #    custom_input(opcion3)
            #elif opcion3==9:
            #    opcion2=0
            #    opcion2=menu2(opcion2)
            #    return opcion2
            
                
            print("--------")
        except:
            print("Ingresa valores validos")
            print("--------")
        
        #print("8->Todas")
        


def udefault():
    #tipo1=1
    #tipo2=2
    maxx=1
    puntos=90
    presicion=4
    amplitud=16
    f=5
    phi=0
    print("Default. Procesando...")
    #print("holi")
    func1=ondas.onda(maxx, puntos, presicion, amplitud, f, phi, 2)
    func2=ondas.onda(maxx, puntos, presicion, amplitud, f, phi, 1)

    for i in range(len(func1)):
        print("{",func1[i],"}", "{",func2[i],"}")
        func1[i]=128+round(func1[i])
        func2[i]=128+round(func2[i])
        
    gc.collect()
    dac1 = DAC(Pin(25, Pin.OUT))
    dac2 = DAC(Pin(26, Pin.OUT))
    
    try:
        plotdac.pltdac(func1,func2, dac1, dac2)
    except Exception as e:
        print(e)
    
    
def ucustom():
    opcion3=0
    #tipo1=1
    #tipo2=2
    #max=84
    #puntos=84
    #presicion=4
    #amplitud=100
    #w0=0.1
    #phi=0
    custom_input(opcion3)

    #flag=False
    #while == False:
    #    pass
        #una iteracion completa y luego reinicia.
        #una iteracion consiste en pedir datos, simularlos y luego de 1min de ploteo se detiene y retorna al menu.
        #el menu permite salir cuando se desee
        


    '''
    func1=ondas.ondas(max, puntos, presicion, amplitud, w0, phi, tipo1)
    func2=ondas.ondas(max, puntos, presicion, amplitud, w0, phi, tipo2)

    for i in range(len(func1)):
        print("{",func1[i],"}", "{",func2[i],"}")
        func1[i]=128+round(func1[i])
        func2[i]=128+round(func2[i])
        
    gc.collect()
    dac1 = DAC(Pin(25, Pin.OUT))
    dac2 = DAC(Pin(26, Pin.OUT))
    
    try:
        plotdac.pltdac(func1,func2, dac1, dac2)
    except Exception as e:
        print(e)
    '''

if __name__ == "__main__":
    #Main para el menu de opciones.
    print("-----------")
    print("Bienvenido a Micropython Digital Signal Generator (uDSG")
    print("-----------")
    #opcion2=0
    #opcion2=menu2(opcion2)
    #opcion=inicio(opcion)
    #if opcion==1:
    #    opcion2=menu2(opcion2)
    '''
    cc=0
    opcion2=0
    while cc!=3:
        
        opcion2=menu2(opcion2)

        if opcion2==1:
            print("Execute default")
            udefault()
        elif opcion2==2:
            print("Execute escritura de parametros")
            ucustom()
        cc=cc+1
    
    
    cc=0
    while cc!=3:
        if opcion2==1:
            print("Execute default")
            udefault()
        elif opcion2==2:
            print("Execute escritura de parametros")
            ucustom()
        cc=cc+1
    '''
    cc=0
    while cc!=2:
      opcion2=0
      opcion2=menu2(opcion2)
      if opcion2==1:
          print("Execute default")
          udefault()
      elif opcion2==2:
          print("Execute escritura de parametros")
          ucustom()
      cc=cc+1
    
 
else:
    print("networking importado")






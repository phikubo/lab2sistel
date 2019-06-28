#import network
#import network
import math
import time
'''
import gc
import ondas #->modulo ondas
import calculadora3
import plotear
from machine import Pin, SPI
from machine import DAC
import pcd8544
import framebuf
import plotdac
'''
def what_type(tipo):
    if tipo ==1:
        print("S")
    elif tipo==2:
        print("R")
    else:
        print("T")

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
    print("Escriba los valores: ")
    try:
        print("Onda 1 <str>(s,r,t): ")
        tipo1=str(input())
        print("--------")
        print("Onda 2 <str>(s,r,t): ")
        tipo2=str(input())
        print("--------")
        print("Presicion <int>(1-10): ")
        presicion=int(input())
        print("--------")
        print("Amplitud <int>(1-20): ")
        amplitud=int(input())
        print("--------")
        print("Frecuencia <int>: ")
        f=int(input())
        w0=2*math.pi*f
        print("--------")
        print("Fase <int>")
        phi=int(input())
        print("--------")
        
        print(tipo1,tipo2, amplitud, f, w0, presicion, phi)
        time.sleep(10)
        
    except:
        print("Ingresa valores validos")
        print("--------")
    while opcion3 != 9:
        try:
            print("1->Continuar")
            print("--------")
            print("9->Salir")
            print("--------")
            opcion3=int(input())
            print("--------")
        except:
            print("Ingresa valores validos")
            print("--------")
        
        #print("8->Todas")
        


def udefault():
    tipo1=1
    tipo2=2
    max=84
    puntos=84
    presicion=4
    amplitud=100
    w0=0.1
    phi=0
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
    print("--------")
    opcion2=0
    opcion2=menu2(opcion2)
    #opcion=inicio(opcion)
    #if opcion==1:
    #    opcion2=menu2(opcion2)
    if opcion2==1:
        print("Execute default")
        udefault()
    elif opcion2==2:
        print("Execute escritura de parametros")
        ucustom()
 
else:
    print("networking importado")

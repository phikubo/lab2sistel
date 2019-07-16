#Implemtenado por Michael para obtener un linspace.
import math
import time

def ulinspace(maxx, puntos):
    '''Ejecuta una operacion similar a linspace pero para microcontroladores. Puntos debe ser par si se desean separaciones equidistantes
    en numeros enteros.'''
    cambio=maxx/puntos
    maxim=maxx
    resultado=[maxim]
    #max=max+1

    #for i in range(1,max+1):
    #    print(max-i+1)
        #print(i-puntos)
    #max=max-1
    cambio=maxx/puntos
    #print("Rata de cambio: ",cambio)
    while maxx > cambio:
        maxx=maxx-cambio
        resultado.append(maxx)
        #print(maxim, max)
    return resultado



if __name__ == "__main__":
    #Entradas:
    #max: El rango en el que las operaciones se ejecutan.
    #puntos: La cantidad de salidas que se desean obtener del rango.
    max=20
    puntos=3
    res=ulinspace(maxx,puntos)
    print("ok => ", res)

    #Pruebas esperadas:
    #output 20,10 si p=2
    #output 20, 15, 10, 5 si p=4
    #output 20,18,16,14,12,10,8,6,4,2, si p=10
    #output 20:1 si p =20
    
else:
    print("importado ulinspace")
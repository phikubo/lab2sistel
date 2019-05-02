#Implemtenado por Michael para plotear funciones sin librerias.
#Name: ufunctions.
#import numpy as np
import math
import time
import calculadora
from machine import Pin, SPI
import pcd8544
import gc
#ecuacion de fourier para generar un pulso rectangular con la ecuacion del fenomeno de gibbs    
'''
La ecuacion que simula la suma parcial de armonicos de un pulso rectangular
y(t)=(4/pi)*sum((sen(2*k-1)/(2*k-1))*t), k=1->n
Fuente:http://sistemyse.blogspot.com/
El indice ha cambiado para evitar los numeros pares:
http://mathworld.wolfram.com/FourierSeriesSquareWave.html

Solucion al bug de fase: la ecuacion de la onda cambia:
y(t)=(4/pi)*sum((sen((2*k-1)(w0*t+phi))/(2*k-1))*t), k=1->n
'''

def urectangular(max, puntos, K, amplitud, w0, phi):
    print("urectangular")

    import framebuf
    spi = SPI(1, baudrate=328125, polarity=0, phase=0)
    cs = Pin(2) #D4
    dc = Pin(15) #D8
    rst = Pin(0) #D3
    #bl = Pin(12, Pin.OUT, value=1) #D6
    print("Variables:OK")
    lcd = pcd8544.PCD8544(spi, cs, dc, rst)
    print("lcd ok")
    buffer = bytearray((lcd.height // 8) * lcd.width)
    framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)
    framebuf.fill(1)
    lcd.data(buffer)
    time.sleep(1)
    framebuf.fill(0)
    lcd.data(buffer)

    print("Iniciando...")
    count=0
    y_record=[] #
    y_res=[]
    T = calculadora.ulinspace(max,puntos)

    #print(T)
    for k in range(1,K+1):
        #print("k -> ",k)
        for t in T:
            #print("Operacion: ", "k -> ",k, ", t -> ",t)
            y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))
            y_record.append(y) #Lista de puntos de la funcion.
            time.sleep_ms(10)
        count=count+1
        gc.collect()
        #diseno: esta agregando a la lista ambas funciones.
        
    #
    print(count, "ok")
    time.sleep(1)
    print("Puntos: ",len(T), ", tamano del arreglo ", len(y_record), " presicion: ",K)
    for i in range(puntos):
                #print("Suma: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res.append(y_record[i]+y_record[i+(K-1)*puntos])
                time.sleep_ms(10)
    K=K-1
    
    while K!=1:
        for i in range(puntos):
                #print("Suma while: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res[i]=y_res[i]+y_record[i+(K-1)*puntos]
                time.sleep_ms(10)
        print("Tamano del arreglo res", len(y_res), "presicion: ",K)
        K=K-1
    print(len(y_res))

    count=1
    for y in y_res:
        print(y,round(y))
        time.sleep_ms(10)
        framebuf.pixel(count,24-round(y),1)
        count=count+1
    #eje y
    framebuf.vline(0, 0, 96, 0xffff)
    #eje x
    framebuf.hline(0, 24, 96, 0xffff)
    #escribiendo datas
    lcd.data(buffer)
    
    





if __name__ == "__main__":
    #input: max, puntos para ulinspace. Presicion = n, {n E N}. Indica que tan parecida debe ser la funcion a la curva ideal
    max=84
    puntos=84 #no funciona para puntos>200
    presicion=4 #K =presicion
    amplitud=16
    w0=0.1
    phi=90 #con la fase, genera una onda diente de sierra de -100, con conf. anterior.
    urectangular(max, puntos, presicion, amplitud, w0, phi)

else:
    print("importado gibss")











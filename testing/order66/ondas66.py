import math
import calculadora
import time
import plotear66
from machine import Pin, SPI
import pcd8544
import framebuf
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.

'''
seno
y=24-amplitud*math.sin((i*w)+phi)

rectangular
y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))

tringular
y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(w0*t+phi)))/(2*k-1)**2)


'''

def pltwave(max, puntos, K, amplitud, w0, phi, tipo):
    '''Calcula puntos de una onda de tipo tipo con los parametros dados'''
    count=0
    y_record=[] #
    y_record2=[]
    y_res=[]
    T = calculadora.ulinspace(max,puntos)
    if tipo==1:
        for t in range(puntos):
            #y_sen=24-amplitud*math.sin((t*w0)+phi)
            y_sen=amplitud*math.sin((t*w0)+phi)
            y_record2.append(y_sen)
        print(len(y_record2))
    else:
        for k in range(1,K+1):
            for t in T:
                if tipo==2:
                    y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))
                    y_record.append(y)
                elif tipo==3:
                    y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(w0*t+phi)))/(2*k-1)**2)
                    y_record.append(y)
                
                #y_record.append(y) #Lista de puntos de la funcion.
                time.sleep_ms(10)
            count=count+1
            #gc.collect()

        print(count, "ok")
        time.sleep(1)
        #print("Puntos: ",len(T), ", tamano del arreglo ", len(y_record), " presicion: ",K)
        for i in range(puntos):
                    y_res.append(y_record[i]+y_record[i+(K-1)*puntos])
                    time.sleep_ms(10)
                    gc.collect()
        K=K-1
        
        while K!=1:
            for i in range(puntos):
                    y_res[i]=y_res[i]+y_record[i+(K-1)*puntos]
                    time.sleep_ms(10)
            print("Tamano del arreglo res", len(y_res), "presicion: ",K)
            K=K-1
            gc.collect()
    
    if tipo==1:
        return y_record2
    else:
        return y_res


def what_type(tipo):
    if tipo ==1:
        print("Seno")
    elif tipo==2:
        print("Rect")
    else:
        print("Triang")
  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    #tipo=int(input("escriba el tipo\n"))
    #1: seno
    #2: rectangular
    #3: triang
    tipo=3
    #parametros=[max, puntos, presicion, amplitud, w0, phi]
    max=84
    puntos=84 #no funciona para puntos>200
    presicion=4 #K =presicion
    amplitud=16 #16 en lcd
    w0=0.1
    phi=0 #90
    print("Procesando..")
    try:
        func1=pltwave(max, puntos, presicion, amplitud, w0, phi, 1)
        func1=pltwave(max, puntos, presicion, amplitud, w0, phi, 2)
        
    except Exception as e:
        print(e)
    print("ok, onda")
    

else:
    print("Ondas.py importado")










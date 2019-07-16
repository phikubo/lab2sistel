import math
import calculadora
import time
#import plotear
from machine import Pin, SPI
from machine import DAC
#import pcd8544
#import framebuf
import gc
import plotdac
#from machine import Pin
#import time
#los pines estan ajustados a GPIO y no a las etiquetas internas.

'''
seno
y=24-amplitud*math.sin((i*w)+phi)

rectangular
y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))

tringular
y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(w0*t+phi)))/(2*k-1)**2)


'''

def onda(maxx, puntos, K, amplitud, f, phi, tipo):
    '''Calcula puntos de una onda de tipo tipo con los parametros dados'''
    count=0
    y_record=[] #
    y_record2=[]
    y_res=[]

    T = calculadora.ulinspace(maxx,puntos)
    tx=[]
    for i in T:
        tx.append(maxx-i)

    if tipo==1:
        for t in tx:
            #y_sen=24-amplitud*math.sin((t*w0)+phi)
            y_sen=24-amplitud*math.sin((t*2*math.pi*f)+phi)
            y_record2.append(y_sen)
        print(len(y_record2))
    else:
        for k in range(1,K+1):
            for t in tx:
                if tipo==2:
                    y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(2*math.pi*f*t+phi)))/(2*k-1))
                    y_record.append(y)
                elif tipo==3:
                    y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(2*math.pi*f*t+phi)))/(2*k-1)**2)
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

  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    #tipo=int(input("escriba el tipo\n"))
    #1: seno
    #2: rectangular
    #3: triang
    tipo=3
    #parametros=[max, puntos, presicion, amplitud, w0, phi]
    max=1
    puntos=90 #no funciona para puntos>200
    presicion=4 #K =presicion
    amplitud=16 #16 en lcd
    f=5
    phi=0 #90
    
    func1=onda(max, puntos, presicion, amplitud, f, phi, 2)
    func2=onda(max, puntos, presicion, amplitud, f, phi, 1)

    print("ok, onda:")
    
    for i in range(len(func1)):
        print("{",func1[i],"}", "{",func2[i],"}")
        time.sleep_ms(30)
        func1[i]=128+round(func1[i])
        func2[i]=128+round(func2[i])        
    gc.collect()
    print("ok number")
    dac1 = DAC(Pin(25, Pin.OUT))
    dac2 = DAC(Pin(26, Pin.OUT))
    
    try:
        plotdac.pltdac(func1,func2, dac1, dac2)
    except Exception as e:
        print(e)

else:
    print("Ondas.py importado")










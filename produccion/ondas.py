import math
import calculadora
import time
from machine import Pin, SPI
from machine import DAC
import gc
import plotdac


#experimental lib 
#import matplotlib.pyplot as plt

#los pines estan ajustados a GPIO y no a las etiquetas internas.

'''
seno
y=24-amplitud*math.sin((i*w)+phi)

rectangular
y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))

tringular origina, luego se aumenta la amplitud para coincidir con las otras señales.
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
            y_sen=amplitud*math.sin((t*2*math.pi*f)+phi)
            y_record2.append(y_sen)
        print(len(y_record2))
    else:
        for k in range(1,K+1):
            for t in tx:
                if tipo==2:
                    y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(2*math.pi*f*t+phi)))/(2*k-1))
                    y_record.append(y)
                elif tipo==3:
                    y = (8*amplitud/math.pi**2)*(math.cos(((2*k-1)*(2*math.pi*f*t+phi)))/(2*k-1)**2)
                    y_record.append(y)
            count=count+1
            gc.collect()

        #print(count, "ok")
        time.sleep_ms(10)
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

if __name__ == "__main__":
    maxx=1
    puntos=100 #no funciona para puntos>200
    presicion=3 #K =presicion
    amplitud=15 #maximo 100
    f=2
    #phi1=math.pi/2 #90
    #phi2=3*math.pi/2
    tipo1=3
    tipo2=1
    phi1=0
    phi2=0

    print("Procesando Ondas...")
    func1=onda(maxx, puntos, presicion, amplitud, f, phi1, tipo1)
    func2=onda(maxx, puntos, presicion, amplitud, f, phi2, tipo2)
    gc.collect()    

    print("Ajustando DAC...")
    for i in range(len(func1)):
        print("{",func1[i],"}", "{",func2[i],"}")
        time.sleep_ms(30)
        func1[i]=128+round(func1[i])
        func2[i]=128+round(func2[i])        
    gc.collect()

    dac1 = DAC(Pin(25, Pin.OUT))
    dac2 = DAC(Pin(26, Pin.OUT))
    
    print("Ejecutando Dac:")
    try:
        plotdac.pltdac(func1,func2, dac1, dac2)
    except Exception as e:
        print(e)
    
    fs=[]
    for x,y in zip(func1,func2):
        fs.append(x+y)
        
    T = calculadora.ulinspace(maxx,puntos)
    tx=[]
    for i in T:
        tx.append(maxx-i)

    print("f1 ",len(func1), "f2 ", len(func2), "esp ", len(tx), "suma " ,len(fs))

    
    plt.plot( tx, func1, '-', label="F1")
    plt.plot( tx, func2, '-', label="F2")
    #plt.plot( tx, fs, '-', label="Suma")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()

else:
    print("Ondas.py importado")










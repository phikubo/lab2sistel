import math
import calculadora
import time
import matplotlib.pyplot as plt
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

def ondas(max, puntos, presicion, amplitud, w0, phi):
    buf = bytearray(puntos)
    for i in range(len(buf)):
        buf[i] = 128 + int(amplitud*math.sin((i*w0)+phi))
        print(buf[i])
    return buf


  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    #parametros=[max, puntos, presicion, amplitud, w0, phi]
    max=100
    puntos=100 #no funciona para puntos>200
    presicion=9 #K =presicion
    amplitud=16
    w0=0.1
    phi=90 
    res=ondas(max, puntos, presicion, amplitud, w0, phi)
    T = calculadora.ulinspace(max,puntos)
    #plt.plot(res[0],res[0])
    plt.plot(T, res, '*' )
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Onda test', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
else:
    print("Ondas.py importado")

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

def ondas(max, puntos, K, amplitud, w0, phi, tipo):
    count=0
    y_record=[] #
    y_res=[]
    T = calculadora.ulinspace(max,puntos)

    for k in range(1,K+1):
        for t in T:
            if tipo==1:
                y=24-amplitud*math.sin((t*w0)+phi)
                
            elif tipo==2:
                y = amplitud*(4/math.pi)*(math.sin(((2*k-1)*(w0*t+phi)))/(2*k-1))
            elif tipo==3:
                y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(w0*t+phi)))/(2*k-1)**2)
            
            y_record.append(y) #Lista de puntos de la funcion.
            #time.sleep_ms(10)
        count=count+1
        #gc.collect()

    print(count, "ok")
    time.sleep(1)
    print("Puntos: ",len(T), ", tamano del arreglo ", len(y_record), " presicion: ",K)
    for i in range(puntos):
                y_res.append(y_record[i]+y_record[i+(K-1)*puntos])
                #time.sleep_ms(10)
    K=K-1
    
    while K!=1:
        for i in range(puntos):
                y_res[i]=y_res[i]+y_record[i+(K-1)*puntos]
                #time.sleep_ms(10)
        print("Tamano del arreglo res", len(y_res), "presicion: ",K)
        K=K-1
    return y_res


  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    tipo=3
    #parametros=[max, puntos, presicion, amplitud, w0, phi]
    max=84
    puntos=84 #no funciona para puntos>200
    presicion=9 #K =presicion
    amplitud=16
    w0=0.1
    phi=90 
    resultado=ondas(max, puntos, presicion, amplitud, w0, phi, tipo)
    print(len(resultado))
    T = calculadora.ulinspace(max,puntos)
    plt.plot(T, resultado)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
else:
    print("Ondas.py importado")

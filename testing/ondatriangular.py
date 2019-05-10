#Implemtenado por Michael para plotear funciones sin librerias.
#Este archivo permite ejecutar scripts en python para su implementacion en micropython.
#la diferencia radica en que en micropython no existe matplotlib. El resto es igual.
#Name: ufunctions.
#import numpy as np
import matplotlib.pyplot as plt
import math
import time
import tesingconcepts as calculadora
#ecuacion de fourier para generar un pulso rectangular con la ecuacion del fenomeno de gibbs    
'''
La ecuacion que simula la suma parcial de armonicos de un pulso rectangular
y(t)=(4/pi)*sum((sen(2*k-1)/(2*k-1))*t), k=1->n
Fuente:http://sistemyse.blogspot.com/
El indice ha cambiado para evitar los numeros pares:
http://mathworld.wolfram.com/FourierSeriesSquareWave.html 

triangular:
https://www.chegg.com/homework-help/questions-and-answers/show-fourier-series-triangle-wave-form-bottom-waveform-f-t-2-4a-pi2-infinity-n-1-cos-2n-1--q555651
http://mathworld.wolfram.com/FourierSeriesTriangleWave.html

'''


def main(max, puntos, K, amplitud, w0, phi):
    print("main")
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
            y = (4*amplitud/math.pi**
2)*(math.cos(((2*k-1)*(w0*t+phi)))/(2*k-1)**2)
            y_record.append(y) #Lista de puntos de la funcion.
            
        count=count+1

        #diseno: esta agregando a la lista ambas funciones.
        
    #
    print(count, "ok")
    time.sleep(1)
    print("Puntos: ",len(T), ", tamano del arreglo ", len(y_record), " presicion: ",K)
    for i in range(puntos):
                #print("Suma: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res.append(y_record[i]+y_record[i+(K-1)*puntos])
                
    K=K-1
    
    while K!=1:
        for i in range(puntos):
                #print("Suma while: ", i, " con ", i+(K-1)*puntos )
                #time.sleep(0.2)
                y_res[i]=y_res[i]+y_record[i+(K-1)*puntos]
                
        print("Tamano del arreglo res", len(y_res), "presicion: ",K)
        K=K-1
    print(len(y_res))
    plt.plot(T, y_res)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
    
    





if __name__ == "__main__":
    #input: max, puntos para ulinspace. Presicion = n, {n E N}. Indica que tan parecida debe ser la funcion a la curva ideal
    max=84
    puntos=84 #no funciona para puntos>200
<<<<<<< HEAD
    presicion=9000 #K =presicion
=======
    presicion=100 #K =presicion
>>>>>>> d26bd8fa00682639002d125e7c93a2818f4d6a51
    amplitud=16
    w0=0.1
    phi=-90 #con la fase, genera una onda diente de sierra de -100, con conf. anterior.
    main(max, puntos, presicion, amplitud, w0, phi)

else:
    print("importado gibss")
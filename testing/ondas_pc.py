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

def ondas(maxx, puntos, K, amplitud, f, phi, tipo):
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
                    y = (4*amplitud/math.pi**2)*(math.cos(((2*k-1)*(2*math.pi*f*t+phi)))/(2*k-1)**2)
                    y_record.append(y)
                
                #y_record.append(y) #Lista de puntos de la funcion.
                #time.sleep_ms(10)
            count=count+1
            #gc.collect()

        print(count, "ok")
        time.sleep(1)
        #print("Puntos: ",len(T), ", tamano del arreglo ", len(y_record), " presicion: ",K)
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
    
    if tipo==1:
        return y_record2
    else:
        return y_res


  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    #parametros
    maxx=1
    puntos=100 #no funciona para puntos>200
    presicion=4 #K =presicion
    amplitud=16
    f=2

    tipo1=1
    phi1=0

    tipo2=2
    phi2=0 #antes:3*math.pi/2

    f1=ondas(maxx, puntos, presicion, amplitud, 4*f+5, phi1, tipo1)
    f2=ondas(maxx, puntos, presicion, amplitud, f, phi2, tipo2)
    
    
    fs=[]
    for x,y in zip(f1,f2):
        #print(x,y)
        #time.sleep(1)
        fs.append(x+y)
    #print(fs)
    
    T = calculadora.ulinspace(maxx,puntos)
    tx=[]
    for i in T:
        tx.append(maxx-i)

    plt.plot( tx, f1, '-', label="F1")
    plt.plot( tx, f2, '-', label="F2")
    plt.plot( tx, fs, '-', label="Suma")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
else:
    print("Ondas.py importado")

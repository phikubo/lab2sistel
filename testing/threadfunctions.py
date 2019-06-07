
from machine import DAC
from machine import Pin
import _thread
import time
import math
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.
#test reflush directory, not working
'''
def test1(myloc):
    for i in range(500):
        time.sleep(1)
        print(1, "{",i,"}")
    print("end test1")
    
def test2(myloc):
    myloc.release()
    for i in range(500):
        time.sleep(1)
        print(2, "{",i,"}")
    print("end test2")
'''

def test(myloc, tipo):
    #myloc.acquire()
    if tipo==1:
        myloc.acquire()
        for i in range(500):
            time.sleep(1)
            print(1, "{",i,"}")
    elif tipo==2:
        myloc.release()
        for i in range(500):
            time.sleep(1)
            print(1, "{",i,"}")


if __name__ == "__main__":
    print("Esp32 Funcionando correctamente")
    myloc = _thread.allocate_lock()
    tipo1=1
    tipo2=2
    gc.collect()
    print("Prueba de bloqueo")
    time.sleep(1)
    _thread.start_new_thread(test,(myloc,tipo1))
    _thread.start_new_thread(test,(myloc,tipo2))
    print("Fin prueba")
    time.sleep(1)
    gc.collect()
else:
    pass





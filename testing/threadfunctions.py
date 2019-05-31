
from machine import DAC
from machine import Pin
import _thread
import time
import math
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.
#test reflush directory, not working
def test1(myloc):
    myloc = _thread.allocate_lock()
    myloc.acquire()
    for i in range(500):
        time.sleep(0.2)
        print(1, "{",i,"}")
    print("end test1")
    return myloc
    
def test2(myloc):
    myloc.release()
    for i in range(500):
        time.sleep(0.2)
        print(2, "{",i,"}")
    print("end test2")


if __name__ == "__main__":
    print("Esp Funcionando correctamente")
    myloc = _thread.allocate_lock()
    gc.collect()
    print("Prueba de bloqueo")
    time.sleep(1)
    _thread.start_new_thread(test1, (myloc,))
    _thread.start_new_thread(test2,(myloc,))
    print("Fin prueba")
    time.sleep(1)
    gc.collect()
else:
    pass





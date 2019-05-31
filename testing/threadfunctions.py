
from machine import DAC
from machine import Pin
import _thread
import time
import math
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.
#test reflush directory, not working
def test1():
    for i in range(500):
        time.sleep(1)
        print(i)
    print("end test1")
    
def test2():
    for i in range(500):
        time.sleep(1)
        print(i)
    print("end test2")


if __name__ == "__main__":
    print("Esp Funcionando correctamente")
    #test()
    gc.collect()
    print("Test thread1")
    time.sleep(1)
    test = _thread.allocate_lock()
    test.acquire(1)
    test.start_new_thread(tes1, ())
    
    print("Test thread2")
    time.sleep(1)
    #gc.collect()
    #test1.release()
    #_thread.start_new_thread(test2, ())
    #test.release()
    
else:
    pass





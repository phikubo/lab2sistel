
from machine import DAC
from machine import Pin
import _thread
import time
import math
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.
#test reflush directory, not working
def test():
    buf = bytearray(100)
    dac = DAC(Pin(25, Pin.OUT))
    for i in range(len(buf)):
        buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
        #print(1 "{",buf[i],"}")
        #dac.write(buf[i])
    test_count=0
    flag= False
    while flag==False:
        for i in range(len(buf)):
            print(1, "{",buf[i],"}")
            dac.write(buf[i])
            time.sleep(0.1)
            test_count=test_count+1
            if test_count==9000:
                flag=True
    print("end 1")


def test2():
    buf = bytearray(100)
    dac = DAC(Pin(26, Pin.OUT))
    for i in range(len(buf)):
        buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
        #print(buf[i])
        #dac.write(buf[i])
    test_count=0
    flag= False
    while flag==False:
        for i in range(len(buf)):
            print(2, "{",buf[i],"}")
            dac.write(buf[i])
            time.sleep(0.1)
            test_count=test_count+1
            if test_count==9000:
                flag=True
    print("end 2")
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
if __name__ == "__main__":
    print("Esp Funcionando correctamente")
    #test()
    gc.collect()
    print("Test thread1")
    time.sleep(1)
    test1 = _thread.allocate_lock()
    test1.acquire(1)
    #_thread.start_new_thread(test, ())
    #a_lock = _thread.allocate_lock()
    #a_lock.acquire(1)
    print("Test thread2")
    time.sleep(1)
    gc.collect()
    test1.release()
    _thread.start_new_thread(test2, ())
    test1.release()
    
else:
    pass




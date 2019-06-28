


import math
from machine import DAC
from machine import Pin
import time
import gc
#los pines estan ajustados a GPIO y no a las etiquetas internas.

def pltdac(func1, func2, dac1, dac2):
    test_count=0
    flag= False
    print("Ploting dac...")
    while flag==False:
        for i in range(len(func1)):
            #print("{",func1[i],"}", "->","{",func2[i],"}")
            dac1.write(func1[i])
            dac2.write(func2[i])
            time.sleep(0.1)
            test_count=test_count+1
            if test_count==9000:
                flag=True

if __name__ == "__main__":
    print("Modulo two dac")
    dac1 = DAC(Pin(25, Pin.OUT))
    dac2 = DAC(Pin(26, Pin.OUT))
    func1 = bytearray(100)
    func2 = bytearray(100)
    for i in range(len(func1)):
        func1[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(func1)))
        func2[i] = 128 + int(127 * math.cos(2 * math.pi * i / len(func1)))
    print("ploteando")
    pltdac(func1,func2, dac1, dac2)

else:
    print("Modulo two dac importado")







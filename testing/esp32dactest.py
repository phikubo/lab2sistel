import math
from machine import DAC
from machine import Pin
import time
#los pines estan ajustados a GPIO y no a las etiquetas internas.
print("Esp Funcionando correctamente")
#test reflush directory
buf = bytearray(100)
dac = DAC(Pin(25, Pin.OUT))
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
    print(buf[i])
    dac.write(buf[i])
test_count=0
flag= False
while flag==False:
    for i in range(len(buf)):
        print(buf[i])
        dac.write(buf[i])
        time.sleep(0.1)
        test_count=test_count+1
        if test_count==100:
            flag=True


  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)



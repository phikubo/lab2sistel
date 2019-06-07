

import math
from machine import DAC
from machine import Pin
import time
#los pines estan ajustados a GPIO y no a las etiquetas internas.
print("Esp Funcionando correctamente")

buf = bytearray(100)
buf2 = bytearray(100)
dac = DAC(Pin(25, Pin.OUT))
dac2= DAC(Pin(26, Pin.OUT))

for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
    buf2[i]= 128 + int(127 * math.cos(2 * math.pi * i / len(buf)))
    
    #print(buf[i])
    #dac.write(buf[i])
test_count=0
flag= False
while flag==False:
    for i in range(len(buf)):
        print("{",buf[i],"}", "->","{",buf2[i],"}")
        dac.write(buf[i])
        dac2.write(buf2[i])
        time.sleep(0.1)
        test_count=test_count+1
        if test_count==9000:
            flag=True


  
#dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)






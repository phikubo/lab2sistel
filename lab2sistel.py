#Por michael y juan 
#no implementado
#test
import gc
import sys, time
import pcd8544, framebuf
from machine import Pin, SPI
#import time, ustruct
gc.collect()
'''
Referencias:
https://github.com/phikubo/Micropython-para-Esp8266-ejemplos-
https://es.wikipedia.org/wiki/Sinusoide
http://andidinata.com/2017/11/nokia-5110-micropython/
https://lastminuteengineers.com/nokia-5110-lcd-arduino-tutorial/
http://docs.micropython.org/en/latest/library/framebuf.html
'''

def test():
    print("Prueba exitosa")
    spi = SPI(1, baudrate=80000000, polarity=0, phase=0)
    #antes
    ##spi = SPI(1, baudrate=328125, polarity=0, phase=0)
    cs = Pin(2) #D4
    dc = Pin(15) #D8
    rst = Pin(0) #D3
    bl = Pin(12, Pin.OUT, value=1) #D6
    print("Variables:OK")
    lcd = pcd8544.PCD8544(spi, cs, dc, rst)
    buffer = bytearray((lcd.height // 8) * lcd.width)
    #framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height) 
    #lcd.data(buffer)


if __name__ == "__main__":
    test()
    print(“fin”)
else:
    pass



#Por michael para probar el lcd 5110. Plotea onda seno
import gc
import sys, time
import pcd8544
from machine import Pin, SPI
import math
import ondas66
#import framebuf


def plot(dato1, dato2):
    import framebuf
    spi = SPI(1, baudrate=328125, polarity=0, phase=0)
    cs = Pin(2) #D4
    dc = Pin(15) #D8
    rst = Pin(0) #D3
    #bl = Pin(12, Pin.OUT, value=1) #D6
    print("Variables:OK")
    lcd = pcd8544.PCD8544(spi, cs, dc, rst)
    print("lcd ok")
    buffer = bytearray((lcd.height // 8) * lcd.width)
    framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)
    framebuf.fill(1)
    lcd.data(buffer)
    time.sleep(1)
    framebuf.fill(0)
    lcd.data(buffer)

    for i,y in zip(range(84),dato1):
        print(i, " {" ,round(y), "} ")
        time.sleep_ms(40)
        framebuf.pixel(i,22-round(y),1)
    for i,y in zip(range(84),dato2):
        print(i, " {" ,round(y), "} ")
        time.sleep_ms(40)
        framebuf.pixel(i,22-round(y),1)
    #eje y
    #print(save)
    framebuf.vline(0, 0, 96, 0xffff)
    #eje x
    framebuf.hline(0, 24, 96, 0xffff)
    #escribiendo datas
    lcd.data(buffer)

if __name__ == "__main__":
    w=0.09
    max=84
    puntos=84 #no funciona para puntos>200
    presicion=3 #K =presicion
    amplitud=10#antes 16
    w0=0.1
    phi=90
    tipo1=1
    tipo2=2
    try:
        dato1=ondas66.pltwave(max, puntos, presicion, amplitud, w0, phi, tipo1)
        dato2=ondas66.pltwave(max, puntos, presicion, amplitud, w0, phi, tipo2)
        plot(dato1, dato2)
    except Exception as e:
        print(e)
    #plot(datos)
else:
    pass
















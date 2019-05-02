#Por michael para probar el lcd 5110. Plotea onda seno
import gc
import sys, time
import pcd8544
from machine import Pin, SPI
import math
#import framebuf


def plotseno(w,phi,amplitud):
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
    for i in range(84):
        y=24-amplitud*math.sin((i*w)+phi)
        print(i,round(y), y)
        time.sleep_ms(40)
        framebuf.pixel(i,round(y),1)
    #eje y
    framebuf.vline(0, 0, 96, 0xffff)
    #eje x
    framebuf.hline(0, 24, 96, 0xffff)
    #escribiendo datas
    lcd.data(buffer)

if __name__ == "__main__":
    w=0.09
    phi=0
    amplitud=16
    plotseno(w,phi,amplitud)
else:
    pass










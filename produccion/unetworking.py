import network
mired=network.WLAN(network.AP_IF)
#mired.config(essid="Red_de_prueba_phi")
mired.config(essid="Red michael upython", authmode=network.AUTH_WPA_WPA2_PSK, password="123456789")
mired.active(True)
print(mired.ifconfig())
#mired.ifconfig()

def create_net(ap_name,passw):
    mired=network.WLAN(network.AP_IF)
    mired.config(essid=ap_name, authmode=network.AUTH_WPA_WPA2_PSK, password=passw)
    mired.active(True)
    mired.ifconfig('ip')
    mired.ifconfig('gateway')



if __name__ == "__main__":
    #mired=network.WLAN(network.AP_IF)
    ap_name="upylab2sistel"
    passw=str(123456789)
    #create_net(ap_name,passw)
else:
    print("networking importado")

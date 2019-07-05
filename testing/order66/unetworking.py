
import network

def create_net(ap_name,passw):
    mired=network.WLAN(network.AP_IF)
    #mired.config(essid="Red_de_prueba_phi")
    mired.config(essid=ap_name, authmode=network.AUTH_WPA_WPA2_PSK, password=passw)
    mired.active(True)
    print(mired.ifconfig())

if __name__ == "__main__":
    #mired=network.WLAN(network.AP_IF)
    ap_name="upyl2s"
    passw=str(123456789)
    create_net(ap_name,passw)
else:
    print("networking importado")



import network
from time import sleep

def wifi(): 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.config(dhcp_hostname="esp8266")
    wlan.connect('e2', '9204800026')
    return wlan

if __name__ == '__main__':
    wlan = wifi()
    while not wlan.isconnected():
        pass
    print(wlan.ifconfig())
    
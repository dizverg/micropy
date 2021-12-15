import dht
from machine import Pin
from time import sleep
from wifi import wifi


def main():
    dht1 = dht.DHT11(Pin(2))
    while True:
            print(dht1.measure() or '', 't=',dht1.temperature(),'C', ' h=', dht1.humidity(),'%')
            sleep(4)


if __name__ == '__main__':
    wlan = wifi()
    while not wlan.isconnected():
        pass
    print(wlan.ifconfig())
    main()

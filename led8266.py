
from machine import Pin
from time import sleep
from wifi import wifi


from machine import Pin
led = Pin(2, Pin.OUT)
led.off()

def main():
    while True:
        led.on()
        sleep(4)
        led.off()
        sleep(4)


if __name__ == '__main__':
    wlan = wifi()
    while not wlan.isconnected():
        pass
    print(wlan.ifconfig())
    main()


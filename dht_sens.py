from uasyncio import sleep, run, gather
import dht
from machine import Pin


async def dht_func():
    dht_1 = dht.DHT11(Pin(23))
    while True:
        try:
            dht_1.measure() 
            print('', dht_1.temperature(), dht_1.humidity())
            await sleep(1)
        except:
            pass


if __name__ == '__main__':
    run(dht_func())

# import upip
# upip.install('uasyncio')

from uasyncio import sleep, run, gather
from wifi import wifi
from dht_sens import dht_func


async def x():
    i = 0
    while True:
        print(i)
        i += 1
        await sleep(6)

async def main():
    wlan = wifi()
    await gather(dht_func(), x())    

if __name__ == '__main__':
    run(main())
    

i2c = I2C(1, scl = Pin(22), sda = Pin(21), freq = 400000)
print(i2c.scan())


import ds1307
import ntptime

ds = ds1307.DS1307(i2c)
print('initial datetime on ds1307 is...', ds.datetime())

#set the time by ntptime
print('ntp time is set at')
ntptime.settime()

f=utime.localtime()
g=f[0],f[1],f[2],f[6],(f[3]+8),f[4],f[5]

#ds.halt(False)
ds.datetime(g)
print('new datetime on ds1307 is...', ds.datetime())

utime.sleep(5)
print('5secs later is...', ds.datetime())

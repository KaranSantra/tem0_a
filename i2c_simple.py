import smbus
import time
bus=smbus.SMBus(1)
address = 0x8
i=0
while True:
    if i%2 == 0:
        bus.write_byte(address,0x0)
        print(bus.read_byte(address))
        time.sleep(1)
    else:
        bus.write_byte(address,0x1)
        time.sleep(1)
    i+=1
    if i==5:
        break

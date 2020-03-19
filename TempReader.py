import machine
import time
import onewire, ds18x20

TEMPSENSORPIN = 12
LED1 = 16
LED2 = 5
LED3 = 4
LED4 = 0
LED5 = 2
LED6 = 14

module = machine.Pin(TEMPSENSORPIN)
ds = ds18x20.DS18X20(onewire.OneWire(module))
memories = ds.scan()

pin_D0 = machine.Pin(16, machine.Pin.OUT)
pin_D1 = machine.Pin(5,machine.Pin.OUT)
pin_D2 = machine.Pin(4,machine.Pin.OUT)
pin_D3 = machine.Pin(0,machine.Pin.OUT)
pin_D4 = machine.Pin(2,machine.Pin.OUT)
pin_D5 = machine.Pin(14,machine.Pin.OUT)

pin_D0.off()
pin_D1.off()
pin_D2.off()
pin_D3.off()
pin_D4.off()
pin_D5.off()

def DisplayBinary(decimalNumber):
    binaryString = '{0:06b}'.format(decimalNumber)
    pin_D0.value(int(binaryString[5]))
    pin_D1.value(int(binaryString[4]))
    pin_D2.value(int(binaryString[3]))
    pin_D3.value(int(binaryString[2]))
    pin_D4.value(int(binaryString[1]))
    pin_D5.value(int(binaryString[0]))

module = machine.Pin(TEMPSENSORPIN)
ds = ds18x20.DS18X20(onewire.OneWire(module))
memories = ds.scan()

while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    for memory in memories:
        print(ds.read_temp(rom), end=' ')
        DisplayBinary(int(ds.read_temp(rom)))
        print()

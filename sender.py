from machine import Pin, I2C, UART
from ina219lib import INA219
from time import sleep

print("PROGRAM START")

# I2C
i2c = I2C(0, scl=Pin(18), sda=Pin(19))

print("I2C OK")

# INA219
ina = INA219(i2c)

print("INA219 OK")

# UART
uart = UART(2, 9600, tx=17, rx=16)

print("UART OK")

while True:

    voltage = ina.supply_voltage()
    current = ina.current()
    power = ina.power()

    text = "Voltage: {:.3f} V | Current: {:.3f} mA | Power: {:.3f} mW".format(
        voltage, current, power
    )

    # Send over UART
    uart.write(text + "\r\n")

    # Print i Thonny
    print(text)

    sleep(1)
from machine import UART
from time import sleep

uart = UART(2, 9600, tx=17, rx=16)

print("Receiver Started")

while True:
    if uart.any():
        data = uart.read()
        print(data)
    sleep(0.5)
# ESP32 to ESP32 UART Communication w/ INA219 Measurements
This project demonstrates how two ESP32 boards can communicate using UART (RX/TX) to transfer measurement data from one board to another.
The main purpose is to allow one ESP32 to collect data from an INA219 sensor and send the measurements to a second ESP32, where they can be received and displayed. This can be useful for projects where measurements need to be collected in one place but monitored or processed somewhere else

## Example use case
I used this setup to measure the voltage, current and power consumption of an astable multivibrator circuit using an INA219 sensor connected to the sender ESP32.
The sender reads the measurements from the INA219 and transmits them over UART to the receiver ESP32. Both boards were connected to separate PCs, allowing me to test and monitor the communication through the MicroPython shell.
The setup was tested with two ESP32 boards on a breadboard, and the measurements were successfully transferred between them.

## Files needed
### For the sender ESP32, you need:

-> sender.py : Reads the INA219 measurements and sends them over UART.

-> ina219lib.py : Library used to communicate with the INA219 sensor.

### For the receiver ESP32, you need:

-> receiver.py : Simple, unformatted receiver; could be improved for better ease of reading

> This setup can be used as a starting point for remote sensor monitoring, distributed measurement systems or projects where one ESP32 collects data and another handles the display or further processing.

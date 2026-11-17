from machine import I2C

# INA219 registre
_REG_BUSVOLTAGE = 0x02
_REG_CURRENT = 0x04
_REG_POWER = 0x03
_REG_CALIBRATION = 0x05
_REG_CONFIG = 0x00


class INA219:

    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.buf = bytearray(2)

        self.current_lsb = 0.1
        self.power_lsb = 0.002
        self.cal_value = 4096

        self.configure()

    def write_register(self, reg, value):
        self.buf[0] = (value >> 8) & 0xFF
        self.buf[1] = value & 0xFF
        self.i2c.writeto_mem(self.address, reg, self.buf)

    def read_register(self, reg):
        self.i2c.readfrom_mem_into(
            self.address, reg, self.buf
        )
        return (self.buf[0] << 8) | self.buf[1]

    def configure(self):
        self.write_register(_REG_CALIBRATION, self.cal_value)
        self.write_register(_REG_CONFIG, 0x399F)

    def supply_voltage(self):
        raw = self.read_register(_REG_BUSVOLTAGE)
        return (raw >> 3) * 0.004

    def current(self):
        self.write_register(_REG_CALIBRATION, self.cal_value)
        raw = self.read_register(_REG_CURRENT)

        if raw > 32767:
            raw -= 65536

        return raw * self.current_lsb

    def power(self):
        raw = self.read_register(_REG_POWER)
        return raw * self.power_lsb * 1000
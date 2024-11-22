import board
import digitalio
import adafruit_max31856
import time

spi = board.SPI()
cs = digitalio.DigitalInOut(board.PA7)
cs.direction = digitalio.Direction.OUTPUT


class Leitor_temp:
    def __init__(self):
        self.tc = adafruit_max31856.MAX31856(spi, cs)
        #self.tc.averaging = 2

    def read_temp(self):
        return self.tc.temperature

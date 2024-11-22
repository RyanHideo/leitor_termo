import board
import digitalio
import adafruit_max31856
spi = board.SPI()
import time

cs = digitalio.DigitalInOut(board.PA7)
cs.direction = digitalio.Direction.OUTPUT
tc = adafruit_max31856.MAX31856(spi, cs)

while(True):
    time.sleep(0.5)
    print(tc.temperature)
    print(tc.reference_temperature)

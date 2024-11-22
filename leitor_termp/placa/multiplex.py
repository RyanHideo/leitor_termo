import board
import digitalio

#pins used for sensors
pa6 = digitalio.DigitalInOut(board.PA6)
pa6.direction = digitalio.Direction.OUTPUT

pa1 = digitalio.DigitalInOut(board.PA1)
pa1.direction = digitalio.Direction.OUTPUT

pa0 = digitalio.DigitalInOut(board.PA0)
pa0.direction = digitalio.Direction.OUTPUT

pa3 = digitalio.DigitalInOut(board.PA3)
pa3.direction = digitalio.Direction.OUTPUT

#pins used for channels
pa20 = digitalio.DigitalInOut(board.PA20)
pa20.direction = digitalio.Direction.OUTPUT

pa10 = digitalio.DigitalInOut(board.PA10)
pa10.direction = digitalio.Direction.OUTPUT

pa9 = digitalio.DigitalInOut(board.PA9)
pa9.direction = digitalio.Direction.OUTPUT

pa8 = digitalio.DigitalInOut(board.PA8)
pa8.direction = digitalio.Direction.OUTPUT


class Multiplex:

    def set_canal(self, canal):
        bits_canal = (canal - 1)
        pa20.value = self.is_set(bits_canal, 0)
        pa10.value = self.is_set(bits_canal, 1)
        pa9.value =  self.is_set(bits_canal, 2)
        pa8.value =  self.is_set(bits_canal, 3)

    def set_sensor(self, sensor):
        bit_sensor = self.de_para(sensor)
        pa6.value = self.is_set(bit_sensor, 0)
        pa1.value = self.is_set(bit_sensor, 1)
        pa0.value = self.is_set(bit_sensor, 2)
        pa3.value = self.is_set(bit_sensor, 3)

    def is_set(self, x, n):
        return x & 1 << n != 0

    def de_para(self, val):
        switcher = {
            1: 0,
            2: 15,
            3: 1,
            4: 14,
            5: 2,
            6: 13,
            7: 3,
            8: 12,
            9: 4,
            10: 11,
            11: 5,
            12: 10,
            13: 6,
            14: 9,
            15: 7,
            16: 8,

        }
        return switcher.get(val, "nothing")

#board C-16S-V1
class Multiplex2:

    def set_canal(self, canal):
        bits_canal = self.to_for_channel(canal)
        pa20.value = self.is_set(bits_canal, 0)
        pa10.value = self.is_set(bits_canal, 1)
        pa9.value =  self.is_set(bits_canal, 2)
        pa8.value =  self.is_set(bits_canal, 3)

    def set_sensor(self, sensor):
        bit_sensor = self.to_for_sensor(sensor)
        pa6.value = self.is_set(bit_sensor, 0)
        pa1.value = self.is_set(bit_sensor, 1)
        pa0.value = self.is_set(bit_sensor, 2)
        pa3.value = self.is_set(bit_sensor, 3)

    def is_set(self, x, n):
        return x & 1 << n != 0

    def to_for_sensor(self, val):
        switcher = {
            1: 15,
            2: 14,
            3: 13,
            4: 12,
            5: 11,
            6: 10,
            7: 9,
            8: 8,
            9: 0,
            10: 1,
            11: 2,
            12: 3,
            13: 4,
            14: 5,
            15: 6,
            16: 7,

        }
        return switcher.get(val, "nothing")
    
    def to_for_channel(self, val):
        switcher = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 8,
            6: 7,
            7: 6,
            8: 5,
            9: 11,
            10: 10,
            11: 9,
            12: 8,
            13: 15,
            14: 14,
            15: 13,
            16: 12,

        }
        return switcher.get(val, "nothing")

#board 16chanel V3.0 
class Multiplex3:

    def set_canal(self, canal):
        bits_canal = self.to_for_channel(canal )
        pa20.value = self.is_set(bits_canal, 0)
        pa10.value = self.is_set(bits_canal, 1)
        pa9.value =  self.is_set(bits_canal, 2)
        pa8.value =  self.is_set(bits_canal, 3)

    def set_sensor(self, sensor):
        bit_sensor = self.to_for_sensor(sensor)
        pa6.value = self.is_set(bit_sensor, 0)
        pa1.value = self.is_set(bit_sensor, 1)
        pa0.value = self.is_set(bit_sensor, 2)
        pa3.value = self.is_set(bit_sensor, 3)

    def is_set(self, x, n):
        return x & 1 << n != 0

    def to_for_sensor(self, val):
        switcher = {
            1: 7,
            2: 6,
            3: 5,
            4: 4,
            5: 3,
            6: 2,
            7: 1,
            8: 16,
            9: 8,
            10: 9,
            11: 10,
            12: 11,
            13: 12,
            14: 13,
            15: 14,
            16: 15,

        }
        return switcher.get(val, "nothing")

    def to_for_channel(self, val):
        switcher = {
            1: 3,
            2: 2,
            3: 1,
            4: 16,
            5: 7,
            6: 6,
            7: 5,
            8: 4,
            9: 11,
            10: 10,
            11: 9,
            12: 8,
            13: 15,
            14: 14,
            15: 13,
            16: 12,

        }
        return switcher.get(val, "nothing")





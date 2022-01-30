from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def temperature():
    temp = sense.get_temperature()
    return temp


sense.show_message(temperature())

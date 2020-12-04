#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()


def rgb(r,g,b):
    return [r,g,b]

try:
    while True:
        for i in xrange(0,8):
            for j in xrange(0,8):
                sense.set_pixel(i, j, rgb(randint(0,255), randint(0,255), randint(0,255)))
        sleep(0.1)
except KeyboardInterrupt:
    sense.clear()

#!/usr/bin/python
from time import sleep
from random import randint
from sense_hat import SenseHat

sense = SenseHat()

def rgb(r, g, b):
    return [r, g, b]

def isMatch(pixel):
    return pixel[0] + pixel[1] + pixel[2] < 200 and pixel[0] > pixel[1] + pixel[2]

sense.set_pixels([rgb(randint(0, 255), randint(0, 255), randint(0, 255)) for x in xrange(0, 64)])
RAND_GRID = sense.get_pixels()

iteration = 0
running = True
try:
    while running:
        allSame = True
        currGrid = sense.get_pixels()
        matches = 0
        for i in xrange(0, 64):
            if not isMatch(currGrid[i]):
                allSame = False
                currGrid[i] = rgb(randint(0, 255), randint(0, 255), randint(0, 255))
            else:
                matches += 1
        if matches == 64:
            running = False
            print "Took {} iterations to all match goal".format(iteration)
        else:
            iteration += 1
            sense.set_pixels(currGrid)
finally:
    sense.clear()

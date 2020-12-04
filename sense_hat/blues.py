#!/usr/bin/python
from time import sleep
from random import randint
from sense_hat import SenseHat

sense = SenseHat()

def isBlue(pixel):
    return pixel[2] > 125 and pixel[0] + pixel[1] < pixel[2]

sense.set_pixels(list([randint(0, 255), randint(0, 255), randint(0, 255)] for x in xrange(0, 64)))

iteration = 0
running = True
try:
    matches = 0
    while matches < 64:
        allSame = True
        currGrid = sense.get_pixels()
        matches = 0
        
        for i in xrange(0, 64):
            if not isBlue(currGrid[i]):
                allSame = False
                currGrid[i] = [randint(0, 255), randint(0, 255), randint(0, 255)]
            else:
                matches += 1
        if matches == 64:
            running = False
            print "Took {} iterations to all match goal".format(iteration)
        else:
            iteration += 1
            sense.set_pixels(currGrid)
            sleep(0.1)
finally:
    sense.clear()

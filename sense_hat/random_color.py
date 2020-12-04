#!/usr/bin/python
from time import sleep
from random import randint
from sense_hat import SenseHat

sense = SenseHat()

def rgb(r, g, b):
    return [r, g, b]

sense.set_pixels([[randint(0, 255), randint(0, 255), randint(0, 255)] for x in xrange(0, 64)])
RAND_GRID = sense.get_pixels()

goalR = RAND_GRID[0][0]
goalG = RAND_GRID[0][1]
goalB = RAND_GRID[0][2]

print "Goal is {}".format(rgb(goalR, goalG, goalB))

def isMatch(pixel):
    global goalR, goalG, goalB
    return pixel[0] == goalR and pixel[1] == goalG and pixel[2] == goalB

iteration = 0
matches = 0
matchesLastRun = 0
try:
    while matches < 64:
        currGrid = sense.get_pixels()
        matchesLastRun = matches
        matches = 0
        for i in xrange(0,64):
            if not isMatch(currGrid[i]):
                currGrid[i] = rgb(randint(0,255), randint(0,255), randint(0, 255)) 
            else:
                matches+=1
        if matches > matchesLastRun:
            print("Iteration {} got {} new matches".format(iteration, matches - matchesLastRun))
        if matches < 64:
            iteration+=1
            sense.set_pixels(currGrid)
            sleep(0.1)
    print("Took {} iterations to all match goal".format(iteration))
except KeyboardInterrupt:
 sense.clear()

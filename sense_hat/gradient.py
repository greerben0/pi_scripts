#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()


def rgb(r,g,b):
    return [r,g,b]

def getNextColor(color):
    for i in xrange(0,3):
        color[i]+=25
        if color[i] > 255:
            color[i] = 55
    return color 

def blueGradient():
    r=0
    g=255
    b=55
    grid = [[rgb(0,0,0) for x in range(8)] for y in range(8)]
    for i in xrange(0,8): 
        for j in xrange(0,8):
            #print("[{},{},{}]".format(r,g,b))
            sense.set_pixel(i,j,rgb(r,g,b))
        b+=25
        g-=25

blueGradient()

try:
    while True:
        for i in xrange(0,8):
            for j in xrange(0,8):
                #print("{}".format(sense.get_pixel(i,j)))
                sense.set_pixel(i, j, getNextColor(sense.get_pixel(i,j)))
        sleep(0.02)
except KeyboardInterrupt:
    sense.clear()

#!/usr/bin/python
import sys, getopt, inspect
from time import sleep
from random import randint
from sense_hat import SenseHat

sense = SenseHat()

red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)

def isRed(pixel):
    return pixel[0] + pixel[1] + pixel[2] < 200 and pixel[0] > pixel[1] + pixel[2]

def isGreen(pixel):
    return pixel[1] > 125 and pixel[0] + pixel[2] < pixel[1]

def isBlue(pixel):
    return pixel[2] > 125 and pixel[0] + pixel[1] < pixel[2]

def isMatch(pixel):
    return (red-5 <= pixel[0] and red+5 >= pixel[0]) and (green-5 <= pixel[1] and green+5 >= pixel[1]) and (blue-5 <= pixel[2] and blue+5 >= pixel[2])

try:
    opts, args = getopt.getopt(sys.argv[1:], "hlrgb", ["rgb="])
except getopt.GetoptError:
    print 'c.py -h -l -r -g -b  --rgb=<rgbvaluecommadelim>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print 'c.py --rgb=<rgbvalue>'
        sys.exit()
    elif opt == "-r":
        isMatch = isRed
    elif opt == "-g":
        isMatch = isGreen
    elif opt == "-b":
        isMatch = isBlue
    elif opt == "-l":
        sense.low_light = True
    elif opt == "--rgb":
        rgb = arg.split(',')
        print "arg {}, rgb {}".format(arg, rgb)
        red = int(rgb[0])
        green = int(rgb[1])
        blue = int(rgb[2])

#Initialize the pixels with random colors
sense.set_pixels([[randint(0, 255), randint(0, 255), randint(0, 255)] for x in xrange(0, 64)])

print "rgb={},{},{}, isMatch={}".format(red, green, blue, inspect.getsourcelines(isMatch))

iteration = 0
try:
    matches = 0
    while True:
        grid = sense.get_pixels()
        for i in xrange(0, len(grid)):
            if not isMatch(grid[i]):
                grid[i] = [randint(0, 255), randint(0, 255), randint(0, 255)]
            else:
                #print "Pixel {} matches [{},{},{}]".format(i, red, green, blue)
                matches += 1
        if matches == 64:
            print "Took {} iterations to all match goal".format(iteration)
            try:
                input("Press Enter to exit")
            except NameError:
                pass
            finally:
                sys.exit()
        else:
            #print "Iteration {} had {} matches".format(iteration, matches)
            iteration += 1
            matches = 0
            sense.set_pixels(grid)
            sleep(0.1)
finally:
    sense.clear()

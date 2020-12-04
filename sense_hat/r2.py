#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def rgb(r,g,b):
 return [r,g,b]

goalGrid = [rgb(0, 0, 0) for x in xrange(0, 64)]
randGrid = [rgb(randint(0,255), randint(0,255), randint(0,255)) for x in xrange(0, 64)]

sense.set_pixels(goalGrid)
goalGrid = sense.get_pixels()

sleep(2)

sense.set_pixels(randGrid)
randGrid  = sense.get_pixels()

goalPixel = goalGrid[0]

print("finished setting up. rand={}, goal={}".format(randGrid, goalGrid))

iteration = 0
running = True
try:
    while running:
        allSame = True
        currGrid = sense.get_pixels()
        for i in xrange(0,64):
            #print("Checking pixel {}. goal {}, curr {}".format(i, goalGrid[i], currGrid[i]))
            if goalPixel[0] != currGrid[i][0] or goalPixel[1] != currGrid[i][1] or goalPixel[2] != currGrid[i][2]:

                #print("pixel {} goal {} curr {}".format(i, goalPixel, currGrid[i]))


                allSame = False
                currGrid[i] = rgb(randint(0,255), randint(0,255), randint(0, 255)) 
            #else:
                #print("pixel {} is match {}".format(i, goalGrid[i]))
                #print("pixel {} is match {}".format(i, goalPixel))
#    for k in xrange(0,3):
#     if goal[k] != currPixel[k]:
#      currPixel[k] = randint(0, 255)
#      allSame = False
        if allSame:
            running  = False
            msg = "Took {} iterations to all match goal {}".format(iteration, goalPixel)
            print(msg)
            sense.clear()
            sense.show_message("{}".format(iteration))
        else:
            #print("Completed iteration {}".format(iteration))
            iteration+=1
            sense.set_pixels(currGrid)
            #sleep(0.1)
except KeyboardInterrupt:
 sense.clear()

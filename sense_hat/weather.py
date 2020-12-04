#!/usr/bin/python
from sense_hat import SenseHat, ACTION_RELEASED

sense = SenseHat()

running = True

def pushed_middle(event):
	global running
	running = False

sense.stick.direction_middle = pushed_middle

while running:
	t = sense.get_temperature()
	p = sense.get_pressure()
	h = sense.get_humidity()

	t = round(t, 1)
	p = round(p, 1)
	h = round(h, 1)

	msg = "T:{0}, P:{1}, H:{2}".format(t,p,h)

	sense.show_message(msg, 0.05)

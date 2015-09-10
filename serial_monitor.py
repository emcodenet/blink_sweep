from time import sleep
import serial
from termcolor import colored, cprint
import random
from random import randint

ser = serial.Serial('/dev/ttyACM0', 9600)

colors = ['grey','red','green','yellow','blue','magenta','cyan','white']

i = 1;

while True:

	distance = ser.readline()

	if(distance):

		d = int(distance.strip('\0'))

		if(d < 10):

			print ( colored ("Yoda says: Touch me not, you must. " + str(i) + " attempts You've made so far ", colors[randint(0,7)] ) )
			i += 1

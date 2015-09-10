from time import sleep
import serial
from termcolor import colored, cprint
import random
from random import randint

ser = serial.Serial('/dev/ttyACM0', 9600)

colors = ['grey','red','green','yellow','blue','magenta','cyan','white']

while True:

	distance = ser.readline()

	if(distance):

		d = int(distance.strip('\0'))

		if(d < 10):

			print ( colored ('Yoda says: Touch me not, you must.', colors[randint(0,7)] ) )

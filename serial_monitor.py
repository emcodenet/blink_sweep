from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:

	distance = ser.readline()

	if(distance):

		d = int(distance.strip('\0'))

		if(d < 10):

			print('Yoda says: Touch me not, you must.')

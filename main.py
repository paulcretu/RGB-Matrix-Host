import serial
import time

arduino = serial.Serial('/dev/tty.usbserial-A800ewMw', 115200, timeout=1)

time.sleep(2)


print(arduino.read())

color = 0xFF

while 1:
	for i in range(64):
		arduino.write(chr(color))
	color -= 101
	color %= 2
	color += 4
	time.sleep(1/100000)
#	print(arduino.read())
import ASUS.GPIO as GPIO
import unittest   
import time     
# to use ASUS tinker board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel, we set GPIO4 (Pin 7) to OUTPUT

n = 40

for counter in range (1, n+1):
	if counter == 1 or \
	   counter == 2 or \
           counter == 4 or \
           counter == 6 or \
           counter == 9 or \
           counter == 14 or \
           counter == 17 or \
           counter == 20 or \
           counter == 25 or \
           counter == 30 or \
           counter == 34 or \
           counter == 39 :
		continue
	GPIO.setup(counter, GPIO.OUT)
	GPIO.output(counter,GPIO.HIGH)
	time.sleep(1)


for counter in range (1, n+1):
        if counter == 1 or \
           counter == 2 or \
           counter == 4 or \
           counter == 6 or \
           counter == 9 or \
           counter == 14 or \
           counter == 17 or \
           counter == 20 or \
           counter == 25 or \
           counter == 30 or \
           counter == 34 or \
           counter == 39 :
                continue
        GPIO.output(counter,GPIO.LOW)
	time.sleep(1)	


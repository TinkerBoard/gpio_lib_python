#Testing for software PWM
import ASUS.GPIO as GPIO
import unittest   
import time   

GPIO.setmode(GPIO.ASUS)
GPIO.setup(252, GPIO.OUT)
pwm = GPIO.PWM(252, 50)
pwm.start(100)

while True:
	for i in range(0,3):
		for x in range(0,101,5):
			pwm.ChangeDutyCycle(x)
			time.sleep(0.1)
		for x in range(100,-1,-5):
			pwm.ChangeDutyCycle(x)
			time.sleep(0.1)

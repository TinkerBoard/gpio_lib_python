#Testing for software PWM
import ASUS.GPIO as GPIO
import unittest   
import time   

GPIO.setmode(GPIO.ASUS)

while True:
	gpiovalue = int(input("Enter the gpio number:"))
	freqvalue = int(input("Enter the frequency value:"))	
	GPIO.setup(gpiovalue, GPIO.OUT)
	pwm = GPIO.PWM(gpiovalue, freqvalue)
	pwm.start(50)


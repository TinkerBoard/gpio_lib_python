#!/usr/bin/env python2.7  
# demo of "BOTH" bi-directional edge detection  
# script by Alex Eames http://RasPi.tv  
# http://raspi.tv/?p=6791  
  
import ASUS.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
  
GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering  
GPIO.setup(3, GPIO.IN)    # set GPIO25 as input (button)  
  
# Define a threaded callback function to run in another thread when events are detected  
def my_callback(channel):  
    if GPIO.input(3):     # if port 25 == 1  
        print "Rising edge detected on 25"  
    else:                  # if port 25 != 1  
        print "Falling edge detected on 25"  
  
# when a changing edge is detected on port 25, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(3, GPIO.BOTH, callback=my_callback)  
  
print "Program will finish after 30 seconds or if you press CTRL+C\n"  
print "Make sure you have a button connected, pulled down through 10k resistor"  
print "to GND and wired so that when pressed it connects"  
print "GPIO port 25 (pin 22) to GND (pin 6) through a ~1k resistor\n"  
  
print "Also put a 100 nF capacitor across your switch for hardware debouncing"  
print "This is necessary to see the effect we're looking for"  
raw_input("Press Enter when ready\n>")  
  
try:  
    print "When pressed, you'll see: Rising Edge detected on 252"  
    print "When released, you'll see: Falling Edge detected on 252"  
    sleep(30)         # wait 30 seconds  
    print "Time's up. Finished!"  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  

ASUS PYTHON GPIO LIB README 
===========================

#Download source code\
git clone https://github.com/TinkerBoard/gpio_lib_python.git

#Build\
 sudo apt-get install python-dev python2.7-dev python3-dev\
 cd ASUS_GPIO_PYTHON_PATH/gpio/\
 sudo python setup.py install

#A Simple Python Program\
 import ASUS.GPIO as GPIO\
 GPIO.setmode(GPIO.ASUS)\
 GPIO.setup(17, GPIO.OUT)\
 GPIO.output(17, GPIO.HIGH)

#More Informaion\
 Send an email to scorpio_chang@asus.com

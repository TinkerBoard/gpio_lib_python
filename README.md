ASUS PYTHON GPIO LIB README 
===========================

<h1>Download source code</h1>
<code>git clone https://github.com/TinkerBoard/gpio_lib_python.git</code>

<h1>Build</h1>
<pre>
sudo apt-get install python-dev python2.7-dev python3-dev
cd ./gpio_lib_python
sudo python setup.py install
sudo pip3 install .
</pre>

<h1>A Simple Python Program</h1>
<pre>
import ASUS.GPIO as GPIO
GPIO.setmode(GPIO.ASUS)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
</pre>

<h1>More Information</h1>
Send an email to <a href="mailto:scorpio_chang@asus.com">scorpio_chang@asus.com</a>

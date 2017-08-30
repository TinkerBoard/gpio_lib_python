PROG=ASUS.GPIO

install:
	sudo python setup.py install --record log
	sudo python setup_RPi.py install --record log
uninstall:
	cat log |xargs rm -rf
clean:
	sudo python setup.py clean
	sudo python setup_RPi.py clean
	

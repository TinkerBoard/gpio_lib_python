PROG=ASUS.GPIO

install:
	sudo python setup.py install --record log
uninstall:
	cat log |xargs rm -rf
clean:
	sudo python setup.py clean
	

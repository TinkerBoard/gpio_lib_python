/*
Copyright (c) 2012-2015 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include "c_gpio.h"
#include "common.h"
#include "wiringTB.h"

void short_wait(void)
{
    int i;

    for (i=0; i<150; i++) // wait 150 cycles
	{   
        asm volatile("nop");
    }
}

int setup(void)
{
	return tinker_board_setup(0);
}

void set_pullupdn(int gpio, int pud)
{
	asus_pullUpDnControl(gpio, pud);
}

int setup_gpio(int gpio, int direction, int pud)
{
	asus_pullUpDnControl(gpio, pud);
	asus_set_pin_mode(gpio, direction);
	return 1;
}

 
int gpio_function(int gpio)
{
	return asus_get_pin_mode(gpio);
}

void output_gpio(int gpio, int value)
{
	asus_digitalWrite(gpio, value);
}

int input_gpio(int gpio)
{
	return asus_digitalRead(gpio);
}

void cleanup(void)
{
	asus_cleanup();
}

/* tinkerboard function*/

void hard_pwmWrite(int gpio, int value)
{
	asus_pwm_write(gpio, value);
}
void hard_pwmToneWrite(int gpio, int freq)
{
	asus_pwmToneWrite(gpio, freq);
}
void hard_pwm_set_Frequency(int gpio, int divisor)
{
	asus_set_pwmFrequency(gpio, divisor);
}
void hard_pwm_set_Period(int gpio, unsigned int period)
{
	asus_set_pwmPeriod(gpio, period);
}

void gpio_set_drive(int gpio, int drv_type)
{
	asus_set_GpioDriveStrength(gpio, drv_type);

}
int  gpio_get_drive(int gpio)
{
	return asus_get_GpioDriveStrength(gpio);
}

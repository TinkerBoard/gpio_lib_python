/*
Copyright (c) 2012-2013 Ben Croston

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

int  setup					(void);
int  setup_gpio				(int gpio, int direction, int pud);
int  gpio_function			(int gpio);
void output_gpio			(int gpio, int value);
int  input_gpio				(int gpio);
void set_rising_event		(int gpio, int enable);
void set_falling_event		(int gpio, int enable);
void set_high_event			(int gpio, int enable);
void set_low_event			(int gpio, int enable);
int  eventdetected			(int gpio);
void cleanup				(void);

/* tinkerboard */
void hard_pwmWrite			(int gpio, int value);
void hard_pwmToneWrite		(int gpio, int freq);
void hard_pwm_set_Frequency	(int gpio, int divisor);
void hard_pwm_set_Period	(int gpio, unsigned int period);
void gpio_set_drive			(int gpio, int drv_type);
int  gpio_get_drive			(int gpio);

#define SETUP_OK          0
#define SETUP_DEVMEM_FAIL 1
#define SETUP_MALLOC_FAIL 2
#define SETUP_MMAP_FAIL   3
// Pin modes

#define	INPUT			 0
#define	OUTPUT			 1
#define	PWM_OUTPUT		 2
#define	GPIO_CLOCK		 3
#define	SOFT_PWM_OUTPUT		 4
#define	SOFT_TONE_OUTPUT	 5
#define	PWM_TONE_OUTPUT		 6

#define	LOW			 0
#define	HIGH			 1

// Pull up/down/none

#define	PUD_OFF			 0
#define	PUD_DOWN		 1
#define	PUD_UP			 2

// Drive Strength 2mA, 4mA, 8mA, 12mA
#define	E_2MA			0
#define	E_4MA		 	1
#define	E_8MA			2
#define	E_12MA			3

#define RK3288

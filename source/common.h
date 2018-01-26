/*
Copyright (c) 2013-2015 Ben Croston

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

#include "cpuinfo.h"

#define MODE_UNKNOWN -1
#define BOARD        10
#define BCM          11
#define RK	    	 12
#define ASUS         13

#define SERIAL       40
#define SPI          41
#define I2C          42
#define PWM          43
#define GPIO		 44
#define TS_XXXX		 45
#define RESERVED	 46
#define I2S			 47
#define GPS_MAG		 48
#define HSADCT		 49
#define USB			 50
#define HDMI		 51
#define SC_XXX		 52
#define GPIOIN		 53
#define GPIOOUT		 54
#define CLKOUT		 55
#define CLK1_27M	 56
#define VOP0_PWM	 57
#define VOP1_PWM	 58



int gpio_mode;
const int pin_to_gpio_rev[41];
const int (*pin_to_gpio)[41];
int gpio_direction[300];
asuspi_info asuspiinfo;
int setup_error;
int module_setup;
int check_gpio_priv(void);
int get_gpio_number(int channel, unsigned int *gpio);

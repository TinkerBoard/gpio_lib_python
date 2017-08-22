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

static int  mem_fd0;
static void* gpio_map0[GPIO_BANK];
static volatile unsigned* gpio0[GPIO_BANK];

static int  mem_fd4;
static void *grf_map;
static volatile unsigned *grf;

static int  mem_fdpmu;
static void *pmu_map;
static volatile unsigned *pmu;

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
	int i;
	for(i=0;i<GPIO_BANK;i++)
	{
		if ((mem_fd0 = open("/dev/mem", O_RDWR|O_SYNC) ) < 0) 
		{
		printf("can't open /dev/mem \n");
		return SETUP_DEVMEM_FAIL;
		}

		// mmap GPIO 
		gpio_map0[i] = mmap(
		NULL,             // Any adddress in our space will do 
		PAGE_SIZE,       // Map length 
		PROT_READ|PROT_WRITE, // Enable reading & writting to mapped memory 
		MAP_SHARED,       // Shared with other processes 
		mem_fd0,           // File to map 
		RK3128_GPIO(i)         //Offset to GPIO peripheral 
		);

		if ((uint32_t)gpio_map0[i] < 0)
		return SETUP_MMAP_FAIL;
		close(mem_fd0); // No need to keep mem_fd open after mmap 
		gpio0[i] = (volatile unsigned *)gpio_map0[i];
	}


	if((mem_fd4 = open("/dev/mem", O_RDWR|O_SYNC) ) < 0) 
	{
		printf("can't open /dev/mem \n");
		return SETUP_DEVMEM_FAIL;
	}

	// mmap GPIO 
	grf_map = mmap(
		NULL,             // Any adddress in our space will do 
		PAGE_SIZE,       // Map length 
		PROT_READ|PROT_WRITE, // Enable reading & writting to mapped memory 
		MAP_SHARED,       // Shared with other processes 
		mem_fd4,           // File to map 
		RK3128_GRF_PHYS         //Offset to GPIO peripheral 
		);
	
	if ((uint32_t)grf_map < 0)
		return SETUP_MMAP_FAIL;
	close(mem_fd4); // No need to keep mem_fd open after mmap
	grf = (volatile unsigned *)grf_map;

	if((mem_fdpmu = open("/dev/mem", O_RDWR|O_SYNC) ) < 0) {
		printf("fdpmu can't open /dev/mem \n");
		return SETUP_DEVMEM_FAIL;
    	}
	pmu_map = mmap(
                NULL,             // Any adddress in our space will do 
                PAGE_SIZE,       // Map length 
                PROT_READ|PROT_WRITE, // Enable reading & writting to mapped memory 
                MAP_SHARED,       // Shared with other processes 
                mem_fdpmu,           // File to map 
                RK3288_PMU         //Offset to GPIO peripheral 
                );

	if ((uint32_t)pmu_map < 0)
        	return SETUP_MMAP_FAIL;
    	close(mem_fdpmu); // No need to keep mem_fdpmu open after mmap
    	pmu = (volatile unsigned *)pmu_map;
	tinker_board_setup(0);
	return SETUP_OK;
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




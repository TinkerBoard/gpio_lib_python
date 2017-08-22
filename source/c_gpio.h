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

int setup(void);
int setup_gpio(int gpio, int direction, int pud);
int gpio_function(int gpio);
void output_gpio(int gpio, int value);
int input_gpio(int gpio);
void set_rising_event(int gpio, int enable);
void set_falling_event(int gpio, int enable);
void set_high_event(int gpio, int enable);
void set_low_event(int gpio, int enable);
int eventdetected(int gpio);
void cleanup(void);

#define SETUP_OK          0
#define SETUP_DEVMEM_FAIL 1
#define SETUP_MALLOC_FAIL 2
#define SETUP_MMAP_FAIL   3

#define INPUT  0 // is really 0 for control register!
#define OUTPUT 1 // is really 1 for control register!
#define ALT0   4

#define HIGH 1
#define LOW  0

#define PUD_OFF  0
#define PUD_DOWN 1
#define PUD_UP   2
#define RK3288
#ifdef RK3288
#define RK3288_GPIO0 		0xff750000
#define RK3288_GPIO1 		0xff780000
#define RK3288_GPIO2 		0xff790000
#define RK3288_GPIO3 		0xff7A0000
#define RK3288_GPIO4 		0xff7B0000
#define RK3288_GPIO5 		0xff7C0000
#define RK3288_GPIO6 		0xff7D0000
#define RK3288_GPIO7 		0xff7E0000
#define RK3288_GPIO8 		0xff7f0000

#define GPIO_LENGTH 		0x00010000
#define GPIO_CHANNEL 		0x00020000
#define GPIO_BASE			0xff750000
		
#define GPIO_BANK			9

#define GRF_BASE			0XFF770000
#define RK3128_GRF_PHYS 	GRF_BASE //this is in use
#define RK3288_PMU		0xff730000

#define PMU_GPIO0C_IOMUX	0x008C
#define PMU_GPIO0C_P		0x006C

#define GRF_GPIO5B_IOMUX	0x0050
#define GRF_GPIO5C_IOMUX	0x0054
#define GRF_GPIO6A_IOMUX	0x005C
#define GRF_GPIO7A_IOMUX	0x006c
#define GRF_GPIO7B_IOMUX	0x0070
#define GRF_GPIO7CL_IOMUX	0x0074
#define GRF_GPIO7CH_IOMUX	0x0078
#define GRF_GPIO8A_IOMUX	0x0080
#define GRF_GPIO8B_IOMUX	0x0084

#define GRF_GPIO5B_P	0x0184
#define GRF_GPIO5C_P	0x0188
#define GRF_GPIO6A_P	0x0190
#define GRF_GPIO6B_P	0x0194
#define GRF_GPIO6C_P	0x0198
#define GRF_GPIO7A_P	0x01A0
#define GRF_GPIO7B_P	0x01A4
#define GRF_GPIO7C_P	0x01A8
#define GRF_GPIO8A_P	0x01B0
#define GRF_GPIO8B_P	0x01b4






#else
#define GPIO_LENGTH			0x00004000
#define GPIO_CHANNEL 		0
#define GPIO_BASE			0x2007c000
#define GPIO_BANK			4
#define GRF_BASE			0x20000000
#define RK3128_GRF_PHYS 	(GRF_BASE+0x8000) //this is in use
#define GRF_GPIO0A_IOMUX 	(0x00a8)	//this is in use 
#endif








//#define RK3128_GPIO0		0x2007c000
//#define RK3128_GPIO1		0x20080000
//#define RK3128_GPIO2		0x20084000
//#define RK3128_GPIO3		0x20088000

#define RK3128_GPIO(x)		(GPIO_BASE+x*GPIO_LENGTH+(x>0)*GPIO_CHANNEL)
#define RK3368_GPIO(x)		(0xff780000+x*0x00010000)
#define RK3368_GRF_PHYS		(0xff770000)
#define RK3368_GRF_GPIO1A_IOMUX	(0x0000)
#define RK3368_GRF_GPIO1B_IOMUX	(0x0004)
#define RK3368_GRF_GPIO1C_IOMUX	(0x0008)
#define RK3368_GRF_GPIO1D_IOMUX	(0x000c)
#define RK3368_GRF_GPIO2A_IOMUX	(0x0010)
#define RK3368_GRF_GPIO2B_IOMUX	(0x0014)
#define RK3368_GRF_GPIO2C_IOMUX	(0x0018)
#define RK3368_GRF_GPIO2D_IOMUX	(0x001c)
#define RK3368_GRF_GPIO3A_IOMUX	(0x0020)
#define RK3368_GRF_GPIO3B_IOMUX	(0x0024)
#define RK3368_GRF_GPIO3C_IOMUX	(0x0028)
#define RK3368_GRF_GPIO3D_IOMUX	(0x002c)
#define RK3368_GRF_GPIO1A_P	(0x0100)	//this is in use but not imply
#define RK3368_GRF_GPIO1B_P	(0x0104)
#define RK3368_GRF_GPIO1C_P	(0x0108)
#define RK3368_GRF_GPIO1D_P	(0x010c)
#define RK3368_GRF_GPIO2A_P	(0x0110)
#define RK3368_GRF_GPIO2B_P	(0x0114)
#define RK3368_GRF_GPIO2C_P	(0x0118)
#define RK3368_GRF_GPIO2D_P	(0x011c)
#define RK3368_GRF_GPIO3A_P	(0x0120)
#define RK3368_GRF_GPIO3B_P	(0x0124)
#define RK3368_GRF_GPIO3C_P	(0x0128)
#define RK3368_GRF_GPIO3D_P	(0x012c)
#define GPIO_SWPORTA_DR_OFFSET		0x0000	//this is in use write data
#define	GPIO_SWPORTA_DDR_OFFSET		0x0004  //this is in use direction
#define GPIO_INTEN_OFFSET		0x0030		
#define GPIO_INTMASK_OFFSET		0x0034
#define GPIO_INTTYPE_LEVEL_OFFSET	0x0038
#define GPIO_INT_POLARITY_OFFSET	0x003c
#define GPIO_INT_STATUS_OFFSET		0x0040
#define GPIO_INT_RAWSTATUS_OFFSET	0x0044
#define GPIO_DEBOUNCE_OFFSET		0x0048	
#define GPIO_PORTA_EOI_OFFSET		0x004c
#define GPIO_EXT_PORTA_OFFSET		0x0050  //this is in use read data
#define GPIO_LS_SYNC_OFFSET		0x0060



#define PAGE_SIZE  (4*1024)
#define BLOCK_SIZE (4*1024)

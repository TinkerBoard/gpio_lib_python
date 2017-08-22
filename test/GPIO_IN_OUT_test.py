#Testing for GPIO
import ASUS.GPIO as GPIO

GPIO.setwarnings(False)

#Pin Table [Begin]
pinTable = []
pinTable += [{'phys':  1, 'wPi': -1, 'TB':  -1}, {'phys':  2, 'wPi': -1, 'TB':  -1}]          #[1]3.3V			    |	[2]5V
pinTable += [{'phys':  3, 'wPi':  8, 'TB': 252}, {'phys':  4, 'wPi': -1, 'TB':  -1}]          #[3]GP8A4_I2C1_SDA	    |	[4]5V
pinTable += [{'phys':  5, 'wPi':  9, 'TB': 253}, {'phys':  6, 'wPi': -1, 'TB':  -1}]          #[5]GP8A5_I2C1_SCL	    |	[6]GND
pinTable += [{'phys':  7, 'wPi':  7, 'TB':  17}, {'phys':  8, 'wPi': 15, 'TB': 161}]          #[7]GP0C1_CLKOUT		    |	[8]GP5B1_UART1TX
pinTable += [{'phys':  9, 'wPi': -1, 'TB':  -1}, {'phys': 10, 'wPi': 16, 'TB': 160}]          #[9]GND			    |	[10]GP5B0_UART1RX
pinTable += [{'phys': 11, 'wPi':  0, 'TB': 164}, {'phys': 12, 'wPi':  1, 'TB': 184}]          #[11]GP5B4_SPI0CLK_UART4CTSN  |	[12]GP6A0_PCM/I2S_CLK
pinTable += [{'phys': 13, 'wPi':  2, 'TB': 166}, {'phys': 14, 'wPi': -1, 'TB':  -1}]          #[13]GP5B6_SPI0_TXD_UART4TX   |	[14]GND
pinTable += [{'phys': 15, 'wPi':  3, 'TB': 167}, {'phys': 16, 'wPi':  4, 'TB': 162}]          #[15]GP5B7_SPI0_RXD_UART4RX   |	[16]GP5B2_UART1CTSN
pinTable += [{'phys': 17, 'wPi': -1, 'TB':  -1}, {'phys': 18, 'wPi':  5, 'TB': 163}]          #[17]3.3V			    |	[18]GP5B3_UART1RTSN
pinTable += [{'phys': 19, 'wPi': 12, 'TB': 257}, {'phys': 20, 'wPi': -1, 'TB':  -1}]          #[19]GP8B1_SPI2TXD	    |	[20]GND
pinTable += [{'phys': 21, 'wPi': 13, 'TB': 256}, {'phys': 22, 'wPi':  6, 'TB': 171}]          #[21]GP8B0_SPI2RXD	    |	[22]GP5C3
pinTable += [{'phys': 23, 'wPi': 14, 'TB': 254}, {'phys': 24, 'wPi': 10, 'TB': 255}]          #[23]GP8A6_SPI2CLK	    |	[24]GP8A7_SPI2CSN0
pinTable += [{'phys': 25, 'wPi': -1, 'TB':  -1}, {'phys': 26, 'wPi': 11, 'TB': 251}]          #[25]GND			    |	[26]GP8A3_SPI2CSN1
pinTable += [{'phys': 27, 'wPi': 30, 'TB': 233}, {'phys': 28, 'wPi': 31, 'TB': 234}]          #[27]GP7C1_I2C4_SDA	    |	[28]GP7C2_I2C4_SCL
pinTable += [{'phys': 29, 'wPi': 21, 'TB': 165}, {'phys': 30, 'wPi': -1, 'TB':  -1}]          #[29]GP5B5_SPI0CSN0_UART4RTSN |	[30]GND 
pinTable += [{'phys': 31, 'wPi': 22, 'TB': 168}, {'phys': 32, 'wPi': 26, 'TB': 239}]          #[31]GP5C0_SPI0CSN1	    |	[32]GP7C7_UART2TX_PWM3
pinTable += [{'phys': 33, 'wPi': 23, 'TB': 238}, {'phys': 34, 'wPi': -1, 'TB':  -1}]          #[33]GP7C6_UART2RX_PWM2	    |	[34]GND
pinTable += [{'phys': 35, 'wPi': 24, 'TB': 185}, {'phys': 36, 'wPi': 27, 'TB': 223}]          #[35]GP6A1_PCM/I2S_FS	    |	[36]GP7A7_UART3RX 
pinTable += [{'phys': 37, 'wPi': 25, 'TB': 224}, {'phys': 38, 'wPi': 28, 'TB': 187}]          #[37]GP7B0_UART3TX	    |	[38]GP6A3_PCM/I2S_SDI
pinTable += [{'phys': 39, 'wPi': -1, 'TB':  -1}, {'phys': 40, 'wPi': 29, 'TB': 188}]          #[39]GND			    |	[40]GP6A4_PCM/I2S_SDO  

pairPins = [( 3,  8),
            ( 5, 10),
            ( 7, 12),
            (11, 13),
            (15, 16),
            (19, 18),
            (21, 22),
            (23, 24),
            (27, 26),
            (29, 28),
            (31, 32),
            (33, 36),
            (35, 38),
            (37, 40)]
modeMap = {'phys': GPIO.BOARD, 'wPi': GPIO.ASUS, 'TB': GPIO.ASUS}
modeNameMap = {'phys': 'GPIO.BOARD', 'wPi': 'GPIO.BCM', 'TB': 'GPIO.ASUS'}
#Pin Table [End]

#Testing [Begin]
for mode in ['phys', 'TB']:
    GPIO.setmode(modeMap[mode])
    LPin = [pinTable[pins[0] - 1][mode] for pins in pairPins]
    RPin = [pinTable[pins[1] - 1][mode] for pins in pairPins]
    if(-1 in LPin or -1 in RPin):
        print('Some pins use the 3.3V or GND pin.')
        exit()
    #L: INPUT  R: OUTPUT
    GPIO.setup( LPin, GPIO.IN)
    GPIO.setup( RPin, GPIO.OUT)
    print([(pin, GPIO.gpio_function(pin)) for pin in LPin])
    print([(pin, GPIO.gpio_function(pin)) for pin in RPin])
    if(False in [GPIO.gpio_function(pin) == GPIO.IN for pin in LPin] or
       False in [GPIO.gpio_function(pin) == GPIO.OUT for pin in RPin]):
        print('Check GPIO.gpio_function or GPIO.setup.')
        exit()
    #HIGH LEVEL
    GPIO.output(RPin, GPIO.HIGH)
    OResult = [GPIO.input(pin) == GPIO.HIGH for pin in RPin]
    IResult = [GPIO.input(LPin[i]) == GPIO.input(RPin[i]) for i in range(len(LPin))]
    if(False in OResult):
        print('Check Pin[%d].' % (RPin[OResult.index(False)]))
        exit()
    if(False in IResult):
        print('Check Pin[%d].' % (LPin[IResult.index(False)]))
        exit()
    #LOW LEVEL
    GPIO.output(RPin, GPIO.LOW)
    OResult = [GPIO.input(pin) == GPIO.LOW for pin in RPin]
    IResult = [GPIO.input(LPin[i]) == GPIO.input(RPin[i]) for i in range(len(LPin))]
    if(False in OResult):
        print('Check Pin[%d].' % (RPin[OResult.index(False)]))
        exit()
    if(False in IResult):
        print('Check Pin[%d].' % (LPin[IResult.index(False)]))
        exit()
    #L: OUTPUT R: INPUT
    GPIO.setup( LPin, GPIO.OUT)
    GPIO.setup( RPin, GPIO.IN)
    if(False in [GPIO.gpio_function(pin) == GPIO.OUT for pin in LPin] or
       False in [GPIO.gpio_function(pin) == GPIO.IN for pin in RPin]):
        print('Check GPIO.gpio_function or GPIO.setup.')
        exit()
    #HIGH LEVEL
    GPIO.output(LPin, GPIO.HIGH)
    OResult = [GPIO.input(pin) == GPIO.HIGH for pin in LPin]
    IResult = [GPIO.input(LPin[i]) == GPIO.input(RPin[i]) for i in range(len(RPin))]
    if(False in OResult):
        print('Check Pin[%d].' % (LPin[OResult.index(False)]))
        exit()
    if(False in IResult):
        print('Check Pin[%d].' % (RPin[IResult.index(False)]))
        exit()
    #LOW LEVEL
    GPIO.output(LPin, GPIO.LOW)
    OResult = [GPIO.input(pin) == GPIO.LOW for pin in LPin]
    IResult = [GPIO.input(LPin[i]) == GPIO.input(RPin[i]) for i in range(len(RPin))]
    if(False in OResult):
        print('Check Pin[%d].' % (LPin[OResult.index(False)]))
        exit()
    if(False in IResult):
        print('Check Pin[%d].' % (RPin[IResult.index(False)]))
        exit()
    print("[PASS] GPIO.setmode(%s)" % (modeNameMap[mode]))
#Testing [End]

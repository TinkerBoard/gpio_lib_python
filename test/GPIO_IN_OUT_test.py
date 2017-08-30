#Testing for GPIO
import ASUS.GPIO as GPIO

GPIO.setwarnings(False)

#Pin Table [Begin]
pinTable = []
pinTable += [{'phys':  1, 'wPi': -1, 'TB':  -1, 'BCM': -1}, {'phys':  2, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[1]3.3V			    |	[2]5V
pinTable += [{'phys':  3, 'wPi':  8, 'TB': 252, 'BCM':  2}, {'phys':  4, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[3]GP8A4_I2C1_SDA	    |	[4]5V
pinTable += [{'phys':  5, 'wPi':  9, 'TB': 253, 'BCM':  3}, {'phys':  6, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[5]GP8A5_I2C1_SCL	    |	[6]GND
pinTable += [{'phys':  7, 'wPi':  7, 'TB':  17, 'BCM':  4}, {'phys':  8, 'wPi': 15, 'TB': 161, 'BCM': 14}]          #[7]GP0C1_CLKOUT		    |	[8]GP5B1_UART1TX
pinTable += [{'phys':  9, 'wPi': -1, 'TB':  -1, 'BCM': -1}, {'phys': 10, 'wPi': 16, 'TB': 160, 'BCM': 15}]          #[9]GND			    |	[10]GP5B0_UART1RX
pinTable += [{'phys': 11, 'wPi':  0, 'TB': 164, 'BCM': 17}, {'phys': 12, 'wPi':  1, 'TB': 184, 'BCM': 18}]          #[11]GP5B4_SPI0CLK_UART4CTSN  |	[12]GP6A0_PCM/I2S_CLK
pinTable += [{'phys': 13, 'wPi':  2, 'TB': 166, 'BCM': 27}, {'phys': 14, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[13]GP5B6_SPI0_TXD_UART4TX   |	[14]GND
pinTable += [{'phys': 15, 'wPi':  3, 'TB': 167, 'BCM': 22}, {'phys': 16, 'wPi':  4, 'TB': 162, 'BCM': 23}]          #[15]GP5B7_SPI0_RXD_UART4RX   |	[16]GP5B2_UART1CTSN
pinTable += [{'phys': 17, 'wPi': -1, 'TB':  -1, 'BCM': -1}, {'phys': 18, 'wPi':  5, 'TB': 163, 'BCM': 24}]          #[17]3.3V			    |	[18]GP5B3_UART1RTSN
pinTable += [{'phys': 19, 'wPi': 12, 'TB': 257, 'BCM': 10}, {'phys': 20, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[19]GP8B1_SPI2TXD	    |	[20]GND
pinTable += [{'phys': 21, 'wPi': 13, 'TB': 256, 'BCM':  9}, {'phys': 22, 'wPi':  6, 'TB': 171, 'BCM': 25}]          #[21]GP8B0_SPI2RXD	    |	[22]GP5C3
pinTable += [{'phys': 23, 'wPi': 14, 'TB': 254, 'BCM': 11}, {'phys': 24, 'wPi': 10, 'TB': 255, 'BCM':  8}]          #[23]GP8A6_SPI2CLK	    |	[24]GP8A7_SPI2CSN0
pinTable += [{'phys': 25, 'wPi': -1, 'TB':  -1, 'BCM': -1}, {'phys': 26, 'wPi': 11, 'TB': 251, 'BCM':  7}]          #[25]GND			    |	[26]GP8A3_SPI2CSN1
pinTable += [{'phys': 27, 'wPi': 30, 'TB': 233, 'BCM':  0}, {'phys': 28, 'wPi': 31, 'TB': 234, 'BCM':  1}]          #[27]GP7C1_I2C4_SDA	    |	[28]GP7C2_I2C4_SCL
pinTable += [{'phys': 29, 'wPi': 21, 'TB': 165, 'BCM':  5}, {'phys': 30, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[29]GP5B5_SPI0CSN0_UART4RTSN |	[30]GND 
pinTable += [{'phys': 31, 'wPi': 22, 'TB': 168, 'BCM':  6}, {'phys': 32, 'wPi': 26, 'TB': 239, 'BCM': 12}]          #[31]GP5C0_SPI0CSN1	    |	[32]GP7C7_UART2TX_PWM3
pinTable += [{'phys': 33, 'wPi': 23, 'TB': 238, 'BCM': 13}, {'phys': 34, 'wPi': -1, 'TB':  -1, 'BCM': -1}]          #[33]GP7C6_UART2RX_PWM2	    |	[34]GND
pinTable += [{'phys': 35, 'wPi': 24, 'TB': 185, 'BCM': 19}, {'phys': 36, 'wPi': 27, 'TB': 223, 'BCM': 16}]          #[35]GP6A1_PCM/I2S_FS	    |	[36]GP7A7_UART3RX 
pinTable += [{'phys': 37, 'wPi': 25, 'TB': 224, 'BCM': 26}, {'phys': 38, 'wPi': 28, 'TB': 187, 'BCM': 20}]          #[37]GP7B0_UART3TX	    |	[38]GP6A3_PCM/I2S_SDI
pinTable += [{'phys': 39, 'wPi': -1, 'TB':  -1, 'BCM': -1}, {'phys': 40, 'wPi': 29, 'TB': 188, 'BCM': 21}]          #[39]GND			    |	[40]GP6A4_PCM/I2S_SDO  

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
gpioUsedPins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 40]
PullUpDnPins = {3: GPIO.PUD_UP, 5: GPIO.PUD_UP, 27: GPIO.PUD_UP, 28: GPIO.PUD_UP}
modeMap = {'phys': GPIO.BOARD, 'TB': GPIO.ASUS, 'BCM': GPIO.BCM}
modeNameMap = {'phys': 'GPIO.BOARD', 'TB': 'GPIO.ASUS', 'BCM': 'GPIO.BCM'}
InternalPullUpDnValue = {GPIO.PUD_UP: GPIO.HIGH, GPIO.PUD_DOWN: GPIO.LOW}
#Pin Table [End]

def GPIO_IO_TESTING():
    print('== Testing GPIO INPUT/OUTPUT ==')
    for mode in ['phys', 'TB', 'BCM']:
        GPIO.setmode(modeMap[mode])
        LPin = [pinTable[pins[0] - 1][mode] for pins in pairPins]
        RPin = [pinTable[pins[1] - 1][mode] for pins in pairPins]
        if(-1 in LPin or -1 in RPin):
            print('Some pins use the 3.3V or GND pin.')
            exit()
        for IPin, OPin in [(LPin, RPin), (RPin, LPin)]:
            GPIO.setup( IPin, GPIO.IN)
            GPIO.setup( OPin, GPIO.OUT)
            if(False in [GPIO.gpio_function(pin) == GPIO.IN for pin in IPin] or
                False in [GPIO.gpio_function(pin) == GPIO.OUT for pin in OPin]):
                print('Check GPIO.gpio_function or GPIO.setup.')
                exit()
            for volt in [GPIO.HIGH, GPIO.LOW]:
                GPIO.output(OPin, volt)
                OResult = [GPIO.input(pin) == volt for pin in OPin]
                IResult = [GPIO.input(IPin[i]) == GPIO.input(OPin[i]) for i in range(len(IPin))]
                if(False in OResult):
                    print('Check Pin[%d].' % (OPin[OResult.index(False)]))
                    exit()
                if(False in IResult):
                    print('Check Pin[%d].' % (IPin[IResult.index(False)]))
                    exit()
        print("[PASS] GPIO.setmode(%s)" % (modeNameMap[mode]))
        GPIO.cleanup()
    print('===============================')

def GPIO_PULL_UPDW_TESTING():
    checkPins = []
    print('== Testing GPIO PULL_UP_DOWN ==')
    testPin = gpioUsedPins
    print("Check that nothing connects to those pins: %s" % (','.join([str(x) for x in testPin])))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(testPin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for pin in testPin:
        if (GPIO.input(pin) != InternalPullUpDnValue[PullUpDnPins[pin] if pin in PullUpDnPins else GPIO.PUD_UP]):
            checkPins.append(pin)
    GPIO.setup(testPin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for pin in testPin:
        if (GPIO.input(pin) != InternalPullUpDnValue[PullUpDnPins[pin] if pin in PullUpDnPins else GPIO.PUD_DOWN]):
            checkPins.append(pin)
    print("[%s] Pull Up and Down" % ('PASS' if len(checkPins) <= 0 else 'FAILED'))
    if(len(checkPins) > 0 ):
        print('Please check those pins: %s' % (','.join([str(x) for x in checkPins])))
    GPIO.cleanup()
    print('===============================')

GPIO_IO_TESTING()
GPIO_PULL_UPDW_TESTING()

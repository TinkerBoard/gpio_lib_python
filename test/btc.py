#!/usr/bin/env python2.7
import unittest
from threading import Timer,activeCount
import time
import ASUS.GPIO as GPIO

LOOP_IN = 16
LOOP_OUT = 22

class TestEdgeDetection(unittest.TestCase):
    def setUp(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LOOP_IN, GPIO.IN)
        GPIO.setup(LOOP_OUT, GPIO.OUT)

    def testWaitForEdgeInLoop(self):
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)

        count = 0
        timestart = time.time()
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        while True:
            t = Timer(0.1, makelow)
            t.start()
            GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            count += 1
            if time.time() - timestart > 5 or count > 150:
                break

    def testWaitForEdgeWithCallback(self):
        def cb():
            raise Exception("Callback should not be called")
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)

        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(0.1, makehigh)

        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_callback(LOOP_IN, callback=cb)
        with self.assertRaises(RuntimeError):   # conflicting edge exception
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

        GPIO.remove_event_detect(LOOP_IN)

    def testWaitForEventSwitchbounce(self):
        self.finished = False
        def bounce():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            self.finished = True

        GPIO.output(LOOP_OUT, GPIO.LOW)
        t1 = Timer(0.1, bounce)
        t1.start()

        starttime = time.time()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=100)
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=100)
        finishtime = time.time()
        self.assertGreater(finishtime-starttime, 0.2)
        while not self.finished:
            time.sleep(0.1)

    def testInvalidBouncetime(self):
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.RISING, bouncetime=-1)
        with self.assertRaises(ValueError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=-1)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, bouncetime=123)
        with self.assertRaises(RuntimeError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=321)
        GPIO.remove_event_detect(LOOP_IN)

    def testAlreadyAdded(self):
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        with self.assertRaises(RuntimeError):
            GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        GPIO.remove_event_detect(LOOP_IN)

    def testHighLowEvent(self):
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.LOW)
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.HIGH)

    def testFallingEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.add_event_detect(LOOP_IN, GPIO.FALLING)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.remove_event_detect(LOOP_IN)

    def testRisingEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.remove_event_detect(LOOP_IN)

    def testBothEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.BOTH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.remove_event_detect(LOOP_IN)

    def testWaitForRising(self):
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(0.1, makehigh)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

    def testWaitForFalling(self):
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        t = Timer(0.1, makelow)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)

    def testExceptionInCallback(self):
        self.run_cb = False
        def cb(channel):
            with self.assertRaises(ZeroDivisionError):
                self.run_cb = True
                a = 1/0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, callback=cb)
        time.sleep(0.01)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(self.run_cb, True)
        GPIO.remove_event_detect(LOOP_IN)

    def testAddEventCallback(self):
        def cb(channel):
            self.callback_count += 1

        # falling test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.add_event_detect(LOOP_IN, GPIO.FALLING)
        GPIO.add_event_callback(LOOP_IN, cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 2048)

        # rising test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, callback=cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 2048)

        # both test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.BOTH, callback=cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 4096)

    def testEventOnOutput(self):
        with self.assertRaises(RuntimeError):
            GPIO.add_event_detect(LOOP_OUT, GPIO.FALLING)

    def testAlternateWaitForEdge(self):
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(2.0, makehigh)
        t2 = Timer(2.0, makelow)
        t.start()
        t2.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)
        GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)

    def tearDown(self):
        GPIO.cleanup()

if __name__ == '__main__':
    unittest.main()

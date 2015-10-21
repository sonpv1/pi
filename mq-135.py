import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

try:
    while True:
	#print GPIO.input(17)
	time.sleep(1)
        if GPIO.input(4) == 0:
            print "GAS DETECTED"
	    #GPIO.output(7, False)
            #time.sleep(5)
            GPIO.output(7,True)
	else:
	    GPIO.output(7, False)
 
except KeyboardInterrupt:
    GPIO.cleanup()

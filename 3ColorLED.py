# External module imports
import RPi.GPIO as GPIO
import time

#define colors
red = 15
blue = 19
green = 21

#define pin needs
on = 0
off = 1

#GPIO setup
GPIO.setmode(GPIO.board) # Board pin-numbering scheme
GPIO.setup(red, GPIO.OUT) 
GPIO.setup(green, GPIO.OUT) 
GPIO.setup(blue, GPIO.OUT)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(red, on)
        time.sleep(1)
		GPIO.output(red, off)
        GPIO.output(blue, on)
        time.sleep(1)
		GPIO.output(blue, off)
		GPIO.output(green, on)
        time.sleep(1)
		GPIO.output(green, off)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

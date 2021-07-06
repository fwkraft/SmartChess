# gpio_hello_world.py
# Written by William Kraft on 7/5/2021
#
# Basic program to demonstrate RPi GPIO interfaces with LED and Hall Effect Switch circuits
# 	LED is wired to GPIO2 pin on RPi
#	Hall Effect Switch Module is wired to GPIO14 on RPi
# Software will toggle LED state on rising & falling edges of Hall Effect input signal
# 	Output LED should match state with LED on Hall mdoule

import RPi.GPIO as GPIO
import time

# GPIO Wirings
HALL = 14
LED = 2

# Configure GPIO pin# vs board pin# setting
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

# Setup GPIOs
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(HALL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Toggle LED when called
# Set initial state to False (off) during init
def toggleLED():
	toggleLED.state = not toggleLED.state
	GPIO.output(LED,toggleLED.state)
toggleLED.state = True

# Function called when GPIO in event is triggered
# Setup to run on both edges of input signal
def hallInputEvent(null):
	# Just toggle LED for now
	toggleLED()

# Add hall Effevt function to event trigger
# Can use GPIO.FALLING, GPIO.RISING, or GPIO.BOTH
GPIO.add_event_detect(HALL, GPIO.BOTH, callback=hallInputEvent, bouncetime=200)


# main loop
try:
	while True: 
		time.sleep(1)
# Cleanup after the program is finished
except KeyboardInterrupt: 
	GPIO.cleanup()


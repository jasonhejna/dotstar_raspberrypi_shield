#!/usr/bin/python

import time
import math
from dotstar import Adafruit_DotStar

numpixels = 150 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin   = 17
clockpin  = 27
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf

# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)
strip.begin()           # Initialize pins for output
strip.setBrightness(128) # Limit brightness to ~1/4 duty cycle

multiplier = 255 / numpixels

# green, red, blue

for i in range(numpixels):
    increase = int(math.floor(i*multiplier))
    decrease = 255 - int(math.floor(i*multiplier))
    strip.setPixelColor(i, increase, decrease, increase)

strip.show()                     # Refresh strip

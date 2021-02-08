""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi

from grove_rgb_lcd import *


"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4

setRGB(0, 255, 255) #sets the screen to be cyan
setText("Lab 2 - Sensors\nAlexander Nemzek") #splash screen
time.sleep(1.0)

grovepi.analogRead(2) #setting the A2 port to read from the ADC rotary encoder


while True:

    #So we do not poll the sensors too quickly which may introduce noise,
    #sleep for a reasonable time of 200ms between each iteration.
    time.sleep(0.2)

    
    distance = grovepi.ultrasonicRead(PORT) #poll distance from ultrasonic sensor
    threshold = grovepi.analogRead(2) #poll rotary encoder input

    if distance < threshold: #object sensed is closer than threshold
        setRGB(255, 0, 0) #sets the screen to be red
        setText_norefresh(str(threshold) + "cm OBJ PRES  \n" + str(distance) + "cm")
    else:
        setRGB(0, 255, 0) #sets the screen to be green
        setText_norefresh(str(threshold) + "cm           \n" + str(distance) + "cm") #otherwise, just prints the values

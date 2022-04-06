
#!/usr/bin/env python3
from ev3dev.ev3 import *

btn = Button() # will use any button to stop script

# Connect EV3 color sensor.
cl = ColorSensor() 

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
cl.mode='COL-REFLECT'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while not btn.any():    # exit loop when any button pressed
    if cl.value()<30:   # weak reflection so over black line
        # medium turn right
        mB.run_forever(speed_sp=450)
        mC.stop(stop_action='brake')
    else:   # strong reflection (>=30) so over white surface
        # medium turn left
        mB.stop(stop_action='brake')
        mC.run_forever(speed_sp=450)
      
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')



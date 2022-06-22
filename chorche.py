#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

prava = Motor(Port.D)
leva = Motor(Port.A)
poklop = Motor(Port.C)
barvicky = ColorSensor(Port.S1)

while True:

    if barvicky.color() == Color.GREEN:
        prava.run_time(250, 3000)
        leva.run_time(250, 3000)
    
    elif barvicky.color() == Color.WHITE:
        prava.run(250)
        leva.run(250)
        
    elif barvicky.color() == Color.BLUE:
        poklop.run_time(250, 100000)
        
    elif barvicky.color() == Color.RED:
        prava.run_time(250, 2000)
        leva.run_time(250, 2000)
        prava.run(250)
        leva.run(250)

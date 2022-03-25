#!/usr/bin/env python3

import os,sys
from sre_constants import CALL
from time import sleep
from ev3dev.ev3 import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.motor import *
from ev3dev2.sound import *
from ev3dev2.wheel import *

# state constants
ON = True
OFF = False



def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


# set the console just how we want it
reset_console()
set_cursor(OFF)
set_font('Lat15-Terminus24x12')
print('Hello there!')

num_laps = 3
CALLIBRATION = 8.47058824 #CARDBOARD
#CALLIBRATION = 7.2 #PAPER

steer_pair = MoveSteering(OUTPUT_D,OUTPUT_B)
# steer_pair.on_for_seconds(steering=0, speed=50, seconds=2)
Y_DIST = 1200
ROBO_SPEED = 50
gy = GyroSensor(INPUT_2)

tire_class = EV3Tire
mdiff = MoveDifferential(OUTPUT_D, OUTPUT_B, tire_class, 118)
sound = Sound()


mdiff.odometry_start()
list = []
INITIAL_ANGLE = gy.angle


for i in range(num_laps):
    INITIAL_ANGLE = gy.angle
    #Forward
    mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)
    mdiff.turn_degrees(ROBO_SPEED, 15)
    mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)
    mdiff.turn_degrees(ROBO_SPEED, 15)

    #Turn 180
    mdiff.turn_degrees(ROBO_SPEED, -90 * CALLIBRATION)
    mdiff.turn_degrees(ROBO_SPEED, -90 * CALLIBRATION)

    INITIAL_ANGLE = gy.angle
    #Backward
    mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)
    mdiff.turn_degrees(ROBO_SPEED, 15)
    mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)
    mdiff.turn_degrees(ROBO_SPEED, 15)

    #Turn 180
    mdiff.turn_degrees(ROBO_SPEED, 90 * CALLIBRATION)
    mdiff.turn_degrees(ROBO_SPEED, 90 * CALLIBRATION)

mdiff.odometry_stop()

debug_print(list)
print(list)
sleep(10)



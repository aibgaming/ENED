#!/usr/bin/env python3

from calendar import TUESDAY
from curses import COLOR_BLACK, COLOR_WHITE
import os,sys
from re import T
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

#my functions
def move_front(tankpair, distance):
    tankpair.on_for_seconds(69.5,70, distance/ROBO_SPEED, False)

def move_back(tankpair, distance):
    tankpair.on_for_seconds(-69.5,-70, distance/ROBO_SPEED, False)

def turn(tankpair, direction, gyrosens):
    gyrosens.reset()

    if direction == -1:
        while gyrosens.angle() > -90:
            tankpair.on_for_seconds(0,70, 1, False)

    elif direction == 1:
        while gyrosens.angle() < 90:
            tankpair.on_for_seconds(0,-70, 1, False)

def read_colour(color_sensor):
    col = 0
    if color_sensor.color() == COLOR_WHITE:
        col = 0
    elif color_sensor.color() == COLOR_BLACK:
        col = 1

    return col

def brake_robot(tankpair):
    tankpair.off(brake=True)


# set the console just how we want it
reset_console()
set_cursor(OFF)
set_font('Lat15-Terminus24x12')
print('Hello there!')

tank_pair = MoveTank(OUTPUT_D, OUTPUT_B)
lift = MediumMotor(OUTPUT_C)
gy = GyroSensor(INPUT_3)
colS = ColorSensor(INPUT_2)
sound = Sound()

#ults = UltrasonicSensor(INPUT_1)
# if (ults.MODE_US_DIST_IN < 1):
#     brake_robot(tank_pair)

ROBO_SPEED = 9.5 #Inch/second
reqDist = 15 # middle of my box

move_front(tank_pair, 30)
turn(tank_pair, 1, gy)
move_front(tank_pair, (6 + reqDist) )   # 21 = 6 + 15
sound.speak("Stopping")
sleep(5)
move_front(tank_pair, 102 - (6 + reqDist) )
turn(tank_pair, 1, gy)
move_front(tank_pair, 30)

sleep(2)
#subtask2
move_back(tank_pair, 6)
turn(tank_pair, 1, gy)
move_front(tank_pair, 96)
turn(tank_pair, -1, gy)
move_front(tank_pair, 6)

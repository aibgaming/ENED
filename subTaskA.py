#!/usr/bin/env python3

from curses import COLOR_BLACK, COLOR_WHITE
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

#my functions
def move_front(tankpair, distance):
    tankpair.on_for_seconds(69.5,70, distance/ROBO_SPEED, False)

def move_back(tankpair, distance):
    tankpair.on_for_seconds(-69.5,-70, distance/ROBO_SPEED, False)

def turn(tankpair, direction, gyrosens):
    gyrosens.reset()

    if direction==-1:
        while gyrosens.angle() > -90:
            tankpair.on_for_seconds(0,70, 1, False)
    elif direction==1:
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
sound.speak("Hello")
turn(tank_pair, 1, gy)
sleep(2)
turn(tank_pair, -1, gy)
sleep(2)
turn(tank_pair, 1, gy)


###########################################################################################################################
# steer_pair = MoveSteering(OUTPUT_D,OUTPUT_B)
# steer_pair.on_for_seconds(steering=0, speed=50, seconds=2)

# tank_pair.on_for_seconds(0,70, 90/ANGULAR_ROBO_SPEED)
# tank_pair.on_for_seconds(70,70, 96/ROBO_SPEED)

# tire_class = EV3Tire
# mdiff = MoveDifferential(OUTPUT_D, OUTPUT_B, tire_class, 118)
# sound = Sound()


# mdiff.odometry_start()
# list = []
# list.append(INITIAL_ANGLE)


# for i in range(num_laps):

#     #FORWARD
#     mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)
#     mdiff.turn_degrees(ROBO_SPEED, 10)
#     mdiff.on_for_distance(ROBO_SPEED, Y_DIST/2)

#     print("Degrees: ",INITIAL_ANGLE - gy.angle,"\n")

#     #BACKWARD
#     mdiff.on_for_distance(ROBO_SPEED, -Y_DIST/2)
#     mdiff.turn_degrees(ROBO_SPEED, 10)
#     mdiff.on_for_distance(ROBO_SPEED, -Y_DIST/2)

#     print("Degrees: ",INITIAL_ANGLE - gy.angle,"\n")

# mdiff.odometry_stop()


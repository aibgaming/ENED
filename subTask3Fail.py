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

#my functions
def move_front(tankpair, distance):
    tankpair.on_for_seconds(69.5,70, distance/ROBO_SPEED, False)

def move_back(tankpair, distance):
    tankpair.on_for_seconds(-69.5,-70, distance/ROBO_SPEED, False)

def turn(tankpair, direction, gyrosens):
    gyrosens.reset()
    if direction==-1:
        while gyrosens.angle > -90:
            tankpair.on_for_seconds(0,50, 0.05, False)
    elif direction==1:
        while gyrosens.angle < 90:
            tankpair.on_for_seconds(0,-50, 0.05, False)

def read_colour(color_sensor):
    col = 5
    if color_sensor.color == 6:
        col = 0
    elif color_sensor.color == 1:
        col = 1
    return col

def read_black(color_sensor):
    perc = color_sensor.reflected_light_intensity
    if perc < 9:
        return 5
    elif perc < 40:
        return 1
    else:
        return 0

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



barcode1 = [1, 0, 0, 0]
barcode2 = [1, 0, 1, 0]
barcode3 = [1, 1, 0, 0]
barcode4 = [1, 0, 0, 1]
mybarcode = []
ROBO_SPEED = 9.5 #Inch/second

run_code = True
while run_code:
    sleep(0.25)
    if read_black(colS) == 1:
        mybarcode.append(1)
    elif read_black(colS) == 0:
        mybarcode.append(0)
    else:
        if len(mybarcode) > 3:
            run_code = False

    move_front(tank_pair,0.35)


mybarcode = mybarcode[-4:]
if mybarcode==barcode1:
    print(mybarcode)
    print("Barcode number 1")
elif mybarcode==barcode2:
    print(mybarcode)
    print("Barcode number 2")
elif mybarcode==barcode3:
    print(mybarcode)
    print("Barcode number 3")
else:
    print(mybarcode)
    print("Barcode number 4")

sleep(10)

#!/usr/bin/env python3
from ev3dev2.sound import Sound
from time import sleep
sound = Sound()
#please download the sounds folder to your ev3 browser
#testing sound of a dog bark
sound.play('/home/robot/sounds/Dog bark 1.wav')
#testing sound of another file 
sound.play('/home/robot/sounds/cat_yowl.wav')
sound.beep()
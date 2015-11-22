"""
pi-alarm.py

Simple python program to take input from a hall-effect sensor
on a raspi and play an alarm when there is no magnetic field
detected by the sensor.

Jim Craveiro <jim.craveiro@gmail.com>
"""

import RPi.GPIO as GPIO
import subprocess
import datetime
import pygame
import time
import sys

# Global Constants

HALL_SENSOR = 11

# Other Globals

music = pygame.mixer.music

"""
Initializes the GPIO pin for the hall effect sensor
as well as initializing mixer for the alarm, and loading
the alarm audio file.

If the audio file is not found, then it will use one specified as
a command line argument.
"""
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    pygame.mixer.init()

    try:
        music.load('alarm.mp3')
        print('Loaded alarm.mp3')

    except pygame.error:

        try:
            music.load(sys.argv[1])
            print('Loaded ' + sys.argv[1])
        
        except IndexError:
            print('ERROR: Alarm could not be found and no secondary alarm file was specified, exiting.')
            sys.exit(1)
    
    print("STATUS: MONITORING")

"""
Returns 0 if the hall effect sensor detects a magnetic field,
and 1 if it does not.
"""
def hallStatus():
    return GPIO.input(HALL_SENSOR)

"""
Function that returns a timestamp string in a human readable format.
"""
def timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S UTC')

"""
Called by alarm to log the time the alarm was tripped in a log file in root's homedir,
as well as broadcasting it on the pi's terminal.
"""
def log():
    notify_string = 'ALARM TRIGGERED: ' + timestamp()
    
    subprocess.call(['wall', notify_string])
    
    log = open('/root/alarm.log', 'a+')
    log.write(notify_string + '\n')
    log.close()

"""
Plays the alarm audio file over the raspberry pi's analog audio out.
Calls log to log the time that the alarm was tripped.
"""
def alarm():
    music.play(loops = -1)
    log()

"""
Main function (sort of, python...)

Inside main loop it checks the status of the hall effect sensor
once every second until it detects that there is no longer a
magnetic field present.
"""
if __name__ == "__main__":
    init()
    
    # main loop, waits until hallStatus is high, then breaks
    while(True):
        if(hallStatus()):
            break
    
    alarm()
    
    # would have been busy wait, but python wont let me do nothing in a while loop
    while(True):
        time.sleep(sys.maxsize)

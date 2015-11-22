"""
pi-alarm.py

Simple python program to take input from a hall-effect sensor
on a raspi and play an alarm when there is no magnetic field
detected by the sensor.

Jim Craveiro <jim.craveiro@gmail.com>
"""

from pygame import mixer
import time
import sys
import RPi.GPIO as GPIO

HALL_SENSOR = 11

"""
Initializes the GPIO pin for the hall effect sensor
as well as initializing mixer for the alarm, and loading
the alarm audio file.
"""
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    mixer.init()
    mixer.music.load('alarm.mp3')

"""
Returns 1 if the hall effect sensor detects a magnetic field,
and zero if it does not.
"""
def hallStatus():
    return GPIO.input(HALL_SENSOR)
"""
Called by alarm to log the time the alarm was tripped in a log file in root's homedir.
"""
def log():
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    log = open('/root/alarm_log', 'r+')
    log.write('ALARM TRIGGERED: ' + timestamp)
    log.close()

"""
Plays the alarm audio file over the raspberry pi's analog audio out.
Calls log to log the time that the alarm was tripped.
"""
def alarm():
    mixer.music.play(loops = -1)
    log()

"""
Main function (sort of, python...)

Inside main loop it checks the status of the hall effect sensor
once every second until it detects that there is no longer a
magnetic field present.
"""
if __name__ == "__main__":
    init()
    while(True):
        time.sleep(1)
        if(hallStatus() == 0):
            break
    alarm()
    

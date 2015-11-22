# Pi-Alarm
Simple alarm system using raspberry pi and a hall-effect sensor, written in python.

Note: This is currently set up in such a way that once the alarm is triggered, you must go and kill the program
      manually; any kind of further functionality is currently out-of-scope.

Required Hardware:
    1) Raspberry Pi (I use version 1 model B, follow your specific hardware's pinout if it is different)
    2) Hall effect sensor (the kind I use: http://www.amazon.com/gp/product/B00B67DTM2 but any kind should work)
    3) Decent magnet (I use a hard drive magnet)
    4) Speakers with 3.5mm male audio in (or 3.5mm female and you have an aux cable)
    5) Fishing line, floss, or something else that can be used as a tripwire or cable to move the magnet
    
Setup:
    1) Connect everything to power
    2) Connect hall effect sensor to raspi
        - [VCC, GND, DATA] (from left to right on my hall effect sensors, looking at the side with numbers)
        - Connect VCC to pin 2 (+5v) on raspi (depending on your sensor, you may need 3.3v from pin 1 instead)
        - Connect GND to pin 6 (GND) on raspi
        - Connect DATA to pin 11 (GPIO) on raspi (or whatever one you specify if you change the code)
    3) Connect speakers to raspi
    4) Connect your tripwire to the magnet and place the magnet in front of the hall effect sensor
        - Test to make sure the alarm does not go off the second you run the program, that means your magnet
          could be facing the wrong way, or you have something set up incorrectly
    5) Run program as root
        - As root I generally run 'nohup python pi-alarm.py &' so that it runs in the background and nohup
          captures output

Thanks to Audio Productions on Youtube for the alarm sound.

    Alarm sound -> https://www.youtube.com/watch?v=2dE4lQYuY5Q
    
    User        -> https://www.youtube.com/user/JustAudio2008/about

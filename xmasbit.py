#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from datetime import datetime

PIN0 = 7
PIN1 = 11
PIN2 = 12
PIN3 = 13
PIN4 = 15

#pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN0, GPIO.OUT)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

month = 12
day = 24

#calculate here days till christmas
def calculate_days():
    currentMonth = int(time.strftime("%m"))
    currentDay = int(time.strftime("%d"))
    monthLeft = month - currentMonth

    #if it's november, calculate here
    if (month > currentMonth):
        daysLeft = day+(30-currentDay)

    #if december, calculate here
    else:
        daysLeft = 24-currentDay
    return daysLeft

print(calculate_days())


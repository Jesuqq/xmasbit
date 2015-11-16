import RPi.GPIO as GPIO
import time
from datetime import datetime

PIN0 = 7
PIN1 = 11
PIN2 = 12
PIN3 = 13
PIN4 = 15

#pin setup
GPIO.setwarmings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN0, GPIO.OUT)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)



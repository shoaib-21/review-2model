#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
def readRfid():
    GPIO.setwarnings(False)
    reader = SimpleMFRC522()

    try:
            print("place your rfid card")
            id, text = reader.read()
            text=text.rstrip()
    finally:
            GPIO.cleanup()
    return id,text

# print("mus "+str(readRfid()))
# time.sleep(2)
# print("noo "+str(readRfid()))
# time.sleep(2)
# print("sho "+str(readRfid()))
#print(readRfid())
import time
from machine import Pin

time.sleep(0.5)  # Wait for USB to become ready


red = Pin(15, 1)
green = Pin(14, 1)

button = Pin(13, 0, Pin.PULL_UP)


buzzer = Pin(11, 1)

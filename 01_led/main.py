from machine import Pin
import time

time.sleep(0.1)  # Wait for USB to become ready

print("Hello, Pi Pico W!")

red = Pin(15, 1)
yellow = Pin(13,1)
green = Pin(10, 1)

while True:

    red.value(1)
    yellow.value(0)
    green.value(0)

    time.sleep(3)

    red.value(0)
    yellow.value(1)
    green.value(0)

    time.sleep(3)

    red.value(0)
    yellow.value(0)
    green.value(1)

    time.sleep(5)

from machine import Pin
from time import sleep

sleep(1)

led_internal = Pin("LED", 1)

while True:
    led_internal.toggle()
    sleep(.5)
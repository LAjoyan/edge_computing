from machine import Pin
from time import sleep

sleep(1)

led_internal = Pin("LED", 1)

while True:
    led_internal.value(1)
    sleep(2)
    led_internal.value(0)
    sleep(2)
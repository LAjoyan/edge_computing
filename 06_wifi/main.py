from wifi import connect_wifi
from machine import Pin

status_led = Pin(15,1)

print(connect_wifi())

if connect_wifi():
    status_led.value(1)
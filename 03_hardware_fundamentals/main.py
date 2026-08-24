import time
from machine import Pin

time.sleep(0.5)  # Wait for USB to become ready


red = Pin(15, 1)
green = Pin(14, 1)

button = Pin(13, 0, Pin.PULL_UP)

button_state = {"pressed": False, "last_interrupt_time": 0}

buzzer = Pin(11, 1)


def button_callback(pin):
    current_time = time.ticks_ms()
    if (current_time - button_state["last_interrupt_time"]) > 200:
        button_state["pressed"] = False if button_state["pressed"] else True
        button_state["last_interrupt_time"] = current_time


button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)
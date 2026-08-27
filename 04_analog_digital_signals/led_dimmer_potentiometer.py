from machine import Pin, PWM, ADC
import time

time.sleep(0.1) # Wait for USB to become ready

potentiometer = ADC(Pin(26))
led_dimmer = PWM(Pin(15,1))
led_dimmer.freq(1000)

while True:
    print(potentiometer.read_u16())
    led_dimmer.duty_u16(potentiometer.read_u16())
    time.sleep(.1)


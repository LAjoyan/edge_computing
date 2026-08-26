import time
from machine import Pin, PWM

time.sleep(0.5)

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(11))
buzzer.duty_u16(0)

button_state = {
    "pressed": False,
    "last_interrupt_time": 0,
}


def button_callback(pin):
    current_time = time.ticks_ms()

    if time.ticks_diff(current_time, button_state["last_interrupt_time"]) > 200:
        button_state["pressed"] = True
        button_state["last_interrupt_time"] = current_time


def play_nokia_tune():
    melody = [
        (659, 150),  # E5
        (587, 150),  # D5
        (370, 300),  # F#4
        (415, 300),  # G#4
        (554, 150),  # C#5
        (494, 150),  # B4
        (294, 300),  # D4
        (330, 300),  # E4
        (494, 150),  # B4
        (440, 150),  # A4
        (277, 300),  # C#4
        (330, 300),  # E4
        (440, 600),  # A4
    ]

    for frequency, duration in melody:
        buzzer.freq(frequency)
        buzzer.duty_u16(20000)
        time.sleep_ms(duration)

        buzzer.duty_u16(0)
        time.sleep_ms(30)


button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

red.value(1)
green.value(0)

while True:
    if button_state["pressed"]:
        button_state["pressed"] = False

        red.value(0)
        green.value(1)

        play_nokia_tune()

        for _ in range(10):
            green.toggle()
            time.sleep_ms(500)

        red.value(1)
        green.value(0)

    time.sleep_ms(50)
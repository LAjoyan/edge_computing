import time
from dht import DHT22
from machine import Pin

time.sleep(0.5)

sensor = DHT22(Pin(16))

while True:
    sensor.measure()
    print(f"Temperature:{sensor.temperature()}°C")
    print(f"Humidity:{sensor.humidity()}%")
    time.sleep(1)

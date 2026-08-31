import time
from wifi import connect_wifi
from machine import Pin
import requests

time.sleep(0.1)

status_led = Pin(15,Pin.OUT)

if connect_wifi():
    status_led.value(1)

url = "https://api.open-meteo.com/v1/forecast?latitude=59.3613&longitude=17.9711&current=temperature_2m&timezone=UTC"

response = requests.get(url).json()

outdoor_temperature = response.get("current").get("temperature_2m")

print(f"Outdoor temperature is {outdoor_temperature} °C ")
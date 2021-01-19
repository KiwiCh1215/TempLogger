#!./venv/bin/python3

import Adafruit_DHT
import time


class TempMeasurer:
    def __init__(self):
        self.DHT_sensor = Adafruit_DHT.DHT22
        self.DHT_pin = 4
        self.newVal = [None, None]

    def measure(self):
        humidity, temperature = Adafruit_DHT.read(self.DHT_sensor, self.DHT_pin)
        while(temperature == None):
                time.sleep(1)
                humidity, temperature = Adafruit_DHT.read(self.DHT_sensor, self.DHT_pin)
        self.newVal[0] = '{:.2f}'.format(temperature)
        self.newVal[1] = '{:.1f}'.format(humidity)
        return self.newVal

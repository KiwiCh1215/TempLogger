#!./venv/bin/python3

import csv
import time
from temp_measurer import TempMeasurer


class Logger:
    def __init__(self):
        print('initlog')
        self.path = './dataValues.csv'
#        self.sensor = TempMeasurer()

    def log(self):
        while True:
#            newVal = sensor.measure()
            newVal = self.newReadings()
            date = self.currentDate()
            t = self.currentTime()

            self.saveData(newVal, date, t)
            print('New row added')

            time.sleep(5)

    def saveData(self, newVal, date, t):
        with open(self.path, 'a+', newline='') as data:
            fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            writer.writerow({'Date': date, 'Time' : t, 'Temperature': newVal[0], 'Humidity': newVal[1]})

#   def newReadings(self):
#       values = [12, 33]
#       return values

    def currentDate(self):
        return time.strftime("%d/%m/%Y")

    def currentTime(self):
        return time.strftime("%X")

#! bin/python3.9

import csv
import time


class Logger:



    def log(self):
        with open(path, 'a+', newline='') as data:
            fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            while True:
                newVal = self.newReadings()
                time = self.currentTime()
                date = self.currentDate()

                writer.writerow({'Date': date, 'Time': time, 'Temperature': newVal[0], 'Humidity': newVal[1]})

                time.sleep(5)

    def newReadings(self):
        values = [12, 33]
        return values

    def currentTime(self):
        return 0

    def currentDate(self):
        return 1

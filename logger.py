#! bin/python3.9

import csv
from time import sleep


class Logger:
    def __init__(self):
        print('initlog')
        self.path = './dataValues.csv'

    def log(self):
        with open(self.path, 'a+', newline='') as data:
            fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            while True:
                newVal = self.newReadings()
                time = self.currentTime()
                date = self.currentDate()

                writer.writerow({'Date': date, 'Time': time, 'Temperature': newVal[0], 'Humidity': newVal[1]})
                print('New row added')

                sleep(5)

    def newReadings(self):
        values = [12, 33]
        return values

    def currentTime(self):
        return 0

    def currentDate(self):
        return 1

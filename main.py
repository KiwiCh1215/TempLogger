#! bin/python3.9

import csv
import os



print("starting")
path = './dataValues.csv'
with open(path, 'w', newline='') as data:
    fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
    writer = csv.DictWriter(data, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Date' : 0, 'Time' : 0, 'Temperature' : 0, 'Humidity' : 0})

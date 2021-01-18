#! bin/python3.9

import csv
import os



print("starting")
path = './dataValues.csv'

if os.path.isfile(path) == False:
    print('if')
    with open(path, 'w', newline='') as data:
        fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
        writer = csv.DictWriter(data, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Date' : 0, 'Time' : 0, 'Temperature' : 0, 'Humidity' : 0})

else:
    print('else')
    with open(path, 'a+', newline='') as data:
        fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writerow({'Date': 2, 'Time': 2, 'Temperature': 2, 'Humidity': 2})
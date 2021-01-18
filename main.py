#! bin/python3.9

import csv
import os
from logger import Logger


print("starting")
path = './dataValues.csv'
logger = Logger()

if os.path.isfile(path) == False:
    print('if')
    with open(path, 'w', newline='') as data:
        fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
        writer = csv.DictWriter(data, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Date' : 0, 'Time' : 0, 'Temperature' : 0, 'Humidity' : 0})

logger.log()
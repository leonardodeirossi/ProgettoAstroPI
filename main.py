# AstroPI - Giving young people the chance to run their computer programs in space
# Project of group "Astro PIO" - Calculate pendolum period using ISS data

# Importing required data
from os import times
from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import calendar

import math
import csv
import time

# Initializing SenseHat board
sense = SenseHat()
sense.low_light = True
sense.set_rotation(90)

""" 8x8 LED screen animation """
sfondo = (255, 255, 255)    # Defining colors
filo = (255, 0, 0)          # Defining colors
palla = (0, 115, 5)         # Defining colors

W = palla     # Colors constants
M = filo      # Colors constants
O = sfondo    # Colors constants


# Get current timestamp (UNIX Epoch)
curr_dt = datetime.now()
timestamp = time.gmtime()

current_epoch = time.time()
# last_epoch = current_epoch + 10797
last_epoch = current_epoch + 3000.0
i = current_epoch


# Animation frames definition
def a():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, M, O, O, O, O, O, O,
        O, O, M, M, O, O, O, O,
        O, O, O, O, M, M, O, O,

    ]
    return logo

# Animation frames definition
def b():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, M, M, O, O, O, O, O,
        O, O, O, M, M, O, O, O,
        O, O, O, O, O, M, O, O,

    ]
    return logo

# Animation frames definition
def c():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, M, O, O, O, O, O, O,
        O, O, M, M, O, O, O, O,
        O, O, O, O, M, M, O, O,
        O, O, O, O, O, O, W, W,

    ]
    return logo

# Animation frames definition
def d():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, M, M, M, O, O, O, O,
        O, O, O, O, M, M, O, O,
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, O, W, W,

    ]
    return logo

# Animation frames definition
def e():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, M, M, M, M, O, O, O,
        O, O, O, O, O, M, W, W,
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def f():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, M, M, M, M, M, W, W,
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def g():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        M, M, M, M, M, M, W, W,
        M, M, M, M, M, M, W, W,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def h():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, W, W,
        M, M, M, M, M, M, W, W,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def i():
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, M, W, W,
        M, M, M, M, M, O, O, O,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def j():
    logo = [
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, O, W, W,
        O, O, O, O, M, M, O, O,
        M, M, M, M, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def k():
    logo = [
        O, O, O, O, O, O, W, W,
        O, O, O, O, M, M, O, O,
        O, O, M, M, O, O, O, O,
        M, M, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def l():
    logo = [
        O, O, O, O, O, M, O, O,
        O, O, O, M, M, O, O, O,
        O, M, M, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo

# Animation frames definition
def m():
    logo = [
        O, O, O, O, M, M, O, O,
        O, O, M, M, O, O, O, O,
        O, M, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        M, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,

    ]
    return logo


# Generating data from SenseHat sensor
def get_sense_data():
    sense_data = [[], [], [], [], [], []] # Array - contains returned data

    sense_data[0] = datetime.now() # Contains rilevation timestamp

    # Collecting environment data
    sense_data.append(sense.get_temperature())  # Temperature data from sensor
    sense_data.append(sense.get_pressure())     # Pressure data from sensor
    sense_data.append(sense.get_humidity())     # Humidity data from sensor

    # Collecting accelerometer data
    accelerometer = [] # Array - A sub-array that will be appended to the returned one
    acc = sense.get_accelerometer_raw() # Collecting raw data (x, y, z)

    accX = acc["x"]                  # Local variable x coordinate
    accY = acc["y"]                  # Local variable y coordinate
    accZ = acc["z"]                  # Local variable z coordinate

    accelerometer.append(accX)       # Appending x coordinate
    accelerometer.append(accY)       # Appending y coordinate
    accelerometer.append(accZ)       # Appending z coordinate
    
    sense_data[1] = accelerometer    # Appending sub-array to the main one

    # Calculating gravitational acceleration
    somma = (pow(accX, 2)) + (pow(accY, 2)) + (pow(accZ, 2)) # Calculating vector sum of x, y, z
    acc = math.sqrt(somma) # Square root for grav. acc. expressed in G
    grav = acc * 9.81 # Converting G in m/s^2 (1G = 9.81 m/s^2)


    # Calculating rope lenght assuming period equals 1 second
    t1 = 1  # time - 1 second
    lenght1 = (pow((t1 / (2 * 3.14)), 2)) * grav

    # Calculating rope lenght assuming period equals 1 milisecond
    t2 = 0.1  # time - 1 millisecond
    lenght2 = (pow((t2 / (2 * 3.14)), 2)) * grav

    sense_data[2] = lenght1          # Appending pendolum period to main array
    sense_data[3] = lenght2          # Appending pendolum period to main array

    # Collecting compass data
    compass = [] # Array - A sub-array that will be appended to the returned one
    mag = sense.get_compass_raw() # Collecting raw data (x, y, z)

    compass.append(mag["x"])         # Appending x coordinate
    compass.append(mag["y"])         # Appending y coordinate
    compass.append(mag["z"])         # Appending z coordinate

    sense_data[4] = compass          # Appending sub-array to the main one

    # Collecting gyroscope data
    gyroscope = [] # Array - A sub-array that will be appended to the returned one
    gyro = sense.get_gyroscope_raw() # Collecting raw data (x, y, z)

    gyroscope.append(gyro["x"])         # Appending x coordinate
    gyroscope.append(gyro["y"])         # Appending y coordinate
    gyroscope.append(gyro["z"])         # Appending z coordinate

    sense_data[5] = gyroscope           # Appending sub-array to the main one

    # Function end - return data
    return sense_data


# Anination display settings
images = [a, b, c, d, e, f, g, h, i, j, k, l, m, l, k, j, i, h, g, f, e, d, c, b, a]
count = 0

# Timestamp for data collecting
timestamp = datetime.now()
delay = 1



# Creating CSV file and inserting first-line header
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp', 'pres', 'hum',
                          'acc_x', 'acc_y', 'acc_z', 'len_s1', 'len_s2'
                          'mag_x', 'mag_y', 'mag_z',
                          'gyro_x', 'gyro_y', 'gyro_z',
                          'datetime'])

    # Performing calculation
    while True:
        # Animation update
        sense.set_pixels(images[count % len(images)]())
        time.sleep(.1)
        count += 1

        # Generating SenseData
        data = get_sense_data()
        # dt = data[-1] - timestamp
        # if dt.seconds > delay:
        data_writer.writerow(data)
        timestamp = datetime.now()   

        i = time.time()
        print(i)
        print(last_epoch)



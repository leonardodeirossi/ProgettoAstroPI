# Importing required libraries
from os import times
from sense_hat import SenseHat
from datetime import datetime
from csv import writer

import math
import csv

# Initializing sense hat
sense = SenseHat()
timestamp = datetime.now()
delay = 1

# Function - return array with required data
def get_sense_data():
  sense_data = [[],[],[],[],[]] # Array - main array

  sense_data[0] = datetime.now() # Date / time of data generation

  # Accelerometer data
  accelerometer = [] # Array - contains accelerometer raleted data
  acc = sense.get_accelerometer_raw()
  accX = acc["x"]
  accY = acc["y"]
  accZ = acc["z"]
  accelerometer.append(accX) # Appending generated coordinates
  accelerometer.append(accY) # Appending generated coordinates
  accelerometer.append(accZ) # Appending generated coordinates
  sense_data[1] = accelerometer # Adding array to main array

  # Gravitational acceleration
  somma = (pow(accX,2))+(pow(accY,2))+(pow(accZ,2)) # Calculating using vector sum
  acc = math.sqrt(somma) # Square root of vector sum
  sense_data[2] = acc # Appending to main array
  
  # Compass data
  compass=[] # Array - contains compass data
  mag = sense.get_compass_raw()
  compass.append(mag["x"]) # Appending generated coordinates
  compass.append(mag["y"]) # Appending generated coordinates
  compass.append(mag["z"]) # Appending generated coordinates
  sense_data[3] = compass # Adding array to main array

    
  # Gyroscope data
  gyroscope = [] # Array - contains gyroscope data
  gyro = sense.get_gyroscope_raw()
  gyroscope.append(gyro["x"]) # Appending generated coordinates
  gyroscope.append(gyro["y"]) # Appending generated coordinates
  gyroscope.append(gyro["z"]) # Appending generated coordinates
  sense_data[4] = gyroscope # Adding array to main array
  
  return sense_data # Return the main array


while True:
  data = get_sense_data()
  dt = data[-1] - timestamp

  with open ('data.csv','w',newline='') as f:
    data_writer = csv.writer(f)
    data_writer.writerow(['temp','pres','hum',
                        'acc_x','acc_y','acc_z','acc_grav'
                        'mag_x','mag_y','mag_z',
                        'gyro_x', 'gyro_y', 'gyro_z',
                        'datetime'])

  if dt.seconds > delay:
    data_writer.writerow(data)
    timestamp = datetime.now()

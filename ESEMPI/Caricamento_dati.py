from sense_hat import SenseHat
from datetime import datetime
from csv import writer

import math
import csv

sense = SenseHat()

#timestamp = datetime.now()
#delay = 1

def get_sense_data():
  sense_data = [[],[],[],[],[]]#1) datetime/2) accelerometer/

  sense_data[0] = datetime.now()
  
  #sense_data.append(sense.get_temperature())
  #sense_data.append(sense.get_pressure())
  #sense_data.append(sense.get_humidity())

  #acellerometro
  accelerometer = []
  acc = sense.get_accelerometer_raw()
  accX = acc["x"]
  accY = acc["y"]
  accZ = acc["z"]
  accelerometer.append(accX)
  accelerometer.append(accY)
  accelerometer.append(accZ)
  sense_data[1] = accelerometer

  #calcolo accellerazione gravitazionale 
  somma = (pow(accX,2))+(pow(accY,2))+(pow(accZ,2))
  acc = math.sqrt(somma)
  sense_data[2] = acc
  
  #bussola
  compass=[]
  mag = sense.get_compass_raw()
  compass.append(mag["x"])
  compass.append(mag["y"])
  compass.append(mag["z"])
  sense_data[3] = compass

    
  #giroscopio
  gyroscope = []
  gyro = sense.get_gyroscope_raw()
  gyroscope.append(gyro["x"])
  gyroscope.append(gyro["y"])
  gyroscope.append(gyro["z"])
  sense_data[4] = gyroscope
  
  return sense_data


while True:
  print(get_sense_data())

"""
with open ('data.csv','w',newline='') as f:
  data_writer = csv.writer(f)
  data_writer.writerow(['temp','pres','hum',
                      'acc_x','acc_y','acc_z','acc_grav'
                      'mag_x','mag_y','mag_z',
                      'gyro_x', 'gyro_y', 'gyro_z',
                      'datetime'])
  
while True:
  data = get_sense_data()
  #dt = data[-1] - int(str(timestamp))
  
  #if dt.seconds > delay:
  with open ('data.csv','w',newline='') as f:
    data_writer = csv.writer(f)
    data_writer.writerow(data)
    #timestamp = datetime.now()
"""
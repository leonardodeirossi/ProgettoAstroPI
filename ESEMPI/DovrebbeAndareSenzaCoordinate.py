from os import times
from sense_hat import SenseHat
from datetime import datetime
from csv import writer

import math
import csv
import time

sense = SenseHat()
sense.low_light = True

sfondo = (255,255,255)
filo  = (255,0,0)
palla = (0,115,5)

W = palla
M = filo
O = sfondo

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



def get_sense_data():
  sense_data = [[],[],[],[],[],[]]#1) datetime/2) accelerometer/

  sense_data[0] = datetime.now()
  
  sense_data.append(sense.get_temperature())
  sense_data.append(sense.get_pressure())
  sense_data.append(sense.get_humidity())

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
  grav = acc*9,81 

  #calcolo lunghezza corda in metri se il periodo è di un secondo
  t1 = 1 #second
  lenght1 = (pow((t1/(2*3,14)),2))*grav

  #calcolo lunghezza corda in metri se il periodo è di un millisecondo
  t2 = 0,1 #millisecond
  lenght2 = (pow((t2/(2*3,14)),2))*grav

  sense_data[2] = lenght1 
  sense_data[3] = lenght2
  
  #bussola
  compass=[]
  mag = sense.get_compass_raw()
  compass.append(mag["x"])
  compass.append(mag["y"])
  compass.append(mag["z"])
  sense_data[4] = compass

    
  #giroscopio
  gyroscope = []
  gyro = sense.get_gyroscope_raw()
  gyroscope.append(gyro["x"])
  gyroscope.append(gyro["y"])
  gyroscope.append(gyro["z"])
  sense_data[5] = gyroscope
  
  return sense_data

images = [a,b,c,d,e,f,g,h,i,j,k,l,m,l,k,j,i,h,g,f,e,d,c,b,a]
count = 0

timestamp = datetime.now()
delay = 1

with open ('data.csv','w',newline='') as f:
  #data_writer = csv.writer(f)
  data_writer = writer(f)
  data_writer.writerow(['temp','pres','hum',
                        'acc_x','acc_y','acc_z','len_s1','len_s2'
                        'mag_x','mag_y','mag_z',
                        'gyro_x', 'gyro_y', 'gyro_z',
                        'datetime'])

  while True:
    sense.set_pixels(images[count % len(images)]())
    time.sleep(.1)
    count += 1
    
    data = get_sense_data()
    dt = data[-1] - timestamp
    if dt.seconds > delay:
      data_writer.writerow(data)
      timestamp = datetime.now()

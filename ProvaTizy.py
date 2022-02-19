import logging
import logzero
from logzero import logger
from sense_hat import SenseHat
import ephem
from picamera import PiCamera
import datetime
from time import sleep
import random
import os

# RLAG Trento Team for AstroPI 2018-2019
# Alexander Perathoner
# Davide Sarcletti
# Lorenzo Finco
# Rocca Mattia

# prof. Massimo Saiani

#Code copied from the official astropi webpage to do a photo every x seconds, save it with additional infos and run an animation to show that the experiment is going on
dir_path = os.path.dirname(os.path.realpath(__file__))

# Connect to the Sense Hat
sh = SenseHat()

# Set a logfile name
logzero.logfile(dir_path+"/data01.csv")

# Set a custom formatter
formatter = logging.Formatter('%(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)


# Latest TLE data for ISS location
name = "ISS (ZARYA)"
l1 = "1 25544U 98067A   19037.70547068  .00001546  00000-0   31541-4   9991"
l2 = "2 25544  51.6426 290.1204 0005164   0.3452  96.3870 15.53238968154984"
iss = ephem.readtle(name, l1, l2)

# Set up camera
cam = PiCamera()
cam.resolution = (1944, 1458) #3/4 of the max resolution


def timeAtCoord(lng): #returns the approximated time zone at the given longitude
    asd = int(lng/15) #every 15 degrees there's another time zone
    if asd > 0: #if longitude is positive the time zone is positive, too
        return asd + 1
    return asd #if not the time zone is negative

# function to write lat/long to EXIF data for photographs
def get_latlon():
    """
        A function to write lat/long to EXIF data for photographs
        """
    iss.compute() # Get the lat/long values from ephem
    
    long_value = [float(i) for i in str(iss.sublong).split(":")]
    long2 = long_value[0]
    if long_value[0] < 0:
        long_value[0] = abs(long_value[0])
        cam.exif_tags['GPS.GPSLongitudeRef'] = "W"
        long0 = "W"
    else:
        cam.exif_tags['GPS.GPSLongitudeRef'] = "E"
        long0 = "E"
    cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (long_value[0], long_value[1], long_value[2]*10)
    lat_value = [float(i) for i in str(iss.sublat).split(":")]
    
    lat2 = lat_value[0]
    if lat_value[0] < 0:
        lat_value[0] = abs(lat_value[0])
        cam.exif_tags['GPS.GPSLatitudeRef'] = "S"
        lat0 = "S"
    else:
        cam.exif_tags['GPS.GPSLatitudeRef'] = "N"
        lat0 = "N"
    cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (lat_value[0], lat_value[1], lat_value[2]*10)
    return(lat0, long0, lat2, long2, str(lat_value), str(long_value))

# define a function to update the LED matrix

g = (254, 255, 90)
a = (242, 168, 59)
b = (0, 0, 102)
r = (228, 50, 85)
m = (168, 81, 53)
v = (0, 153, 204)
n = (0, 0, 0)
con = 0
t = 0.1
def avanti():
        pikachu = [
           n, b, b, n, n, n, n, b,
           n, n, g, a, n, n, n, a,
           n, n, n, g, g, g, g, a,
           a, a, n, a, v, a, a, v,                      #intero
           a, a, n, r, g, g, g, a,
           n, a, n, g, a, a, a, n,
           n, a, g, a, g, a, g, n,
           n, n, g, a, m, m, a, n
           ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
          n, n, b, b, n, n, n, n,
          n, n, n, g, a, n, n, n,
          n, n, n, n, g, g, g, g,
          n, a, a, n, a, v, a, a,                   #7
          n, a, a, n, r, g, g, g,
          n, n, a, n, g, a, a, a,
          n, n, a, g, a, g, a, g,
          n, n, n, g, a, m, m, a
          ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
           n, n, n, b, b, n, n, n,
           n, n, n, n, g, a, n, n,
           n, n, n, n, n, g, g, g,
           n, n, a, a, n, a, v, a,                       #6
           n, n, a, a, n, r, g, g,
           n, n, n, a, n, g, a, a,
           n, n, n, a, g, a, g, a,
           n, n, n, n, g, a, m, m
           ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
           n, n, n, n, b, b, n, n,
           n, n, n, n, n, g, a, n,
           n, n, n, n, n, n, g, g,
           n, n, n, a, a, n, a, v,
           n, n, n, a, a, n, r, g,                      #5
           n, n, n, n, a, n, g, a,
           n, n, n, n, a, g, a, g,
           n, n, n, n, n, g, a, m
           ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, b, b, n,
            n, n, n, n, n, n, g, a,
            n, n, n, n, n, n, n, g,
            n, n, n, n, a, a, n, a,                        #4
            n, n, n, n, a, a, n, r,
            n, n, n, n, n, a, n, g,
            n, n, n, n, n, a, g, a,
            n, n, n, n, n, n, g, a
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, b, b,
            n, n, n, n, n, n, n, g,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, a, a, n,
            n, n, n, n, n, a, a, n,                        #3
            n, n, n, n, n, n, a, n,
            n, n, n, n, n, n, a, g,
            n, n, n, n, n, n, n, g
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, b,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, a, a,
            n, n, n, n, n, n, a, a,                    #2
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, n,
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, a,                  #1
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,                    #0
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)

        # RITORNO

        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, b,
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, v,
            n, n, n, n, n, n, n, a,                    #1
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, b, n,
            n, n, n, n, n, n, a, n,
            n, n, n, n, n, n, a, g,
            n, n, n, n, n, n, v, a,
            n, n, n, n, n, n, a, g,                   #2
            n, n, n, n, n, n, n, a,
            n, n, n, n, n, n, n, g,
            n, n, n, n, n, n, n, a
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, b, n, n,
            n, n, n, n, n, a, n, n,
            n, n, n, n, n, a, g, g,
            n, n, n, n, n, v, a, a,
            n, n, n, n, n, a, g, g,                  #3
            n, n, n, n, n, n, a, a,
            n, n, n, n, n, n, g, a,
            n, n, n, n, n, n, a, m
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, b, n, n, n,
            n, n, n, n, a, n, n, n,
            n, n, n, n, a, g, g, g,
            n, n, n, n, v, a, a, v,
            n, n, n, n, a, g, g, g,                 #4
            n, n, n, n, n, a, a, a,
            n, n, n, n, n, g, a, g,
            n, n, n, n, n, a, m, m
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, b, n, n, n, n,
            n, n, n, a, n, n, n, a,
            n, n, n, a, g, g, g, g,
            n, n, n, v, a, a, v, a,
            n, n, n, a, g, g, g, r,                #5
            n, n, n, n, a, a, a, g,
            n, n, n, n, g, a, g, a,
            n, n, n, n, a, m, m, a
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, b, n, n, n, n, b,
            n, n, a, n, n, n, a, g,
            n, n, a, g, g, g, g, n,
            n, n, v, a, a, v, a, n,
            n, n, a, g, g, g, r, n,              #6
            n, n, n, a, a, a, g, n,
            n, n, n, g, a, g, a, g,
            n, n, n, a, m, m, a, g
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, b, n, n, n, n, b, b,
            n, a, n, n, n, a, g, n,
            n, a, g, g, g, g, n, n,
            n, v, a, a, v, a, n, a,
            n, a, g, g, g, r, n, a,             #7
            n, n, a, a, a, g, n, a,
            n, n, g, a, g, a, g, a,
            n, n, a, m, m, a, g, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, n, n, n, n, b, b, n,
            a, n, n, n, a, g, n, n,
            a, g, g, g, g, n, n, n,
            v, a, a, v, a, n, a, a,
            a, g, g, g, r, n, a, a,                      #8
            n, a, a, a, g, n, a, n,
            n, g, a, g, a, g, a, n,
            n, a, m, m, a, g, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, b, b, n, n,
            n, n, n, a, g, n, n, n,
            g, g, g, g, n, n, n, n,
            a, a, v, a, n, a, a, n,
            g, g, g, r, n, a, a, n,                            #7
            a, a, a, g, n, a, n, n,
            g, a, g, a, g, a, n, n,
            a, m, m, a, g, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, b, b, n, n, n,
            n, n, a, g, n, n, n, n,
            g, g, g, n, n, n, n, n,
            a, v, a, n, a, a, n, n,
            g, g, r, n, a, a, n, n,                         #6
            a, a, g, n, a, n, n, n,
            a, g, a, g, a, n, n, n,
            m, m, a, g, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, b, b, n, n, n, n,
            n, a, g, n, n, n, n, n,
            g, g, n, n, n, n, n, n,
            v, a, n, a, a, n, n, n,
            g, r, n, a, a, n, n, n,                         #5
            a, g, n, a, n, n, n, n,
            g, a, g, a, n, n, n, n,
            m, a, g, n, n, n, n, n,
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, b, b, n, n, n, n, n,
            a, g, n, n, n, n, n, n,
            g, n, n, n, n, n, n, n,
            a, n, a, a, n, n, n, n,
            r, n, a, a, n, n, n, n,                        #4
            g, n, a, n, n, n, n, n,
            a, g, a, n, n, n, n, n,
            a, g, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, b, n, n, n, n, n, n,
            g, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, a, a, n, n, n, n, n,
            n, a, a, n, n, n, n, n,                       #3
            n, a, n, n, n, n, n, n,
            g, a, n, n, n, n, n, n,
            g, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            a, a, n, n, n, n, n, n,
            a, a, n, n, n, n, n, n,                      #2
            a, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,                    #1
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,                    #0
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,
            v, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,                    #1
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n,
            n, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, b, n, n, n, n, n, n,
            n, a, n, n, n, n, n, n,
            g, a, n, n, n, n, n, n,
            a, v, n, n, n, n, n, n,
            g, a, n, n, n, n, n, n,                    #2
            a, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n,
            a, n, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, b, n, n, n, n, n,
            n, n, a, n, n, n, n, n,
            g, g, a, n, n, n, n, n,
            a, a, v, n, n, n, n, n,
            g, g, a, n, n, n, n, n,                    #3
            a, a, n, n, n, n, n, n,
            a, a, n, n, n, n, n, n,
            m, a, n, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, b, n, n, n, n,
            n, n, n, a, n, n, n, n,
            g, g, g, a, n, n, n, n,
            v, a, a, v, n, n, n, n,
            g, g, g, a, n, n, n, n,                     #4
            a, a, a, n, n, n, n, n,
            g, a, a, n, n, n, n, n,
            m, m, a, n, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            n, n, n, n, b, n, n, n,
            a, n, n, n, a, n, n, n,
            g, g, g, g, a, n, n, n,
            a, v, a, a, v, n, n, n,
            r, g, g, g, a, n, n, n,                      #5
            g, a, a, a, n, n, n, n,
            a, g, a, a, n, n, n, n,
            a, m, m, a, n, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, n, n, n, n, b, n, n,
            g, a, n, n, n, a, n, n,
            n, g, g, g, g, a, n, n,
            n, a, v, a, a, v, n, n,
            n, r, g, g, g, a, n, n,                       #6
            n, g, a, a, a, n, n, n,
            g, a, g, a, a, n, n, n,
            g, a, m, m, a, n, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)
        pikachu = [
            b, b, n, n, n, n, b, n,
            n, g, a, n, n, n, a, n,
            n, n, g, g, g, g, a, n,
            a, n, a, v, a, a, v, n,
            a, n, r, g, g, g, a, n,                        #7
            a, n, g, a, a, a, n, n,
            a, g, a, g, a, a, n, n,
            n, g, a, m, m, a, n, n
            ]
        sh.set_pixels(pikachu)
        sleep(t)


# create a datetime variable to store the start time
start_time = datetime.datetime.now()
# create a datetime variable to store the current time
# (these will be almost the same at the start)
now_time = datetime.datetime.now()
# run a loop for 2 minutes
photo_counter = 1

# it will end from minutes 179 to 180
while (now_time < start_time + datetime.timedelta(minutes = 179)):
    try:
        
        
        lat0, lon0, lat, lon, lat2, lon2 = get_latlon()
        # Save the data to the file
                
        longitude = str(lon).split('.')[0]
        
        logger.info("n. %s, time-shift %s, %s %s, %s %s, photo file name : %s", photo_counter, timeAtCoord(int(longitude)), lat2, lat0, lon2, lon0, "photo_"+ str(photo_counter).zfill(3)+".jpg") 
        # use zfill to pad the integer value used in filename to 3 digits (e.g. 001, 002...)
        cam.capture(dir_path+"/photo_"+ str(photo_counter).zfill(3)+".jpg")
        photo_counter+=1
        #latitude = str(iss.sublat).split(':')[0]
        
    
    
        #UPDATE VIEW AND WAIT 50 SECONDS
        
        #spoiler: pikachu is coming 4 you
        counter = 0
        while counter < 5:
            avanti() #very accurate delay of about 3,6 seconds
            counter += 1
        
        sh.set_rotation(180)
        
        counter = 0
        while counter < 5:
            avanti() #very accurate delay of about 3,6 seconds
            counter += 1

        sh.set_rotation(0)

        
        
        # update the current time
        now_time = datetime.datetime.now()
    except Exception as e:
        logger.error("An error occurred: " + str(e))

from sense_hat import SenseHat
from datetime import datetime
from orbit import ISS
from skyfield.api import load
"""https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/4
"""

sense = SenseHat()
while True:
    def get_sense_data():
        sense_data = []
        orientation = sense.get_orientation()
        orientation["yaw"]
        orientation["pitch"]
        orientation["roll"]
        mag = sense.get_compass_raw()
        mag["x"]
        mag["y"]
        mag["z"]
        acc = sense.get_accelerometer_raw()
        acc["x"]
        acc["y"]
        acc["z"]
        gyro = sense.get_gyroscope_raw()
        gyro["x"]
        gyro["y"]
        gyro["z"]
        datetime.now()
        sense_data.append(sense.get_compass_raw())
        sense_data.append(sense.get_accelerometer_raw())
        sense_data.append(sense.get_gyroscope_raw())
        sense_data.append(datetime.now())
        return sense_data

    get_sense_data()
    print(get_sense_data())

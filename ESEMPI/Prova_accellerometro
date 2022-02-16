from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def get_sense_data():
	sense_data = []
  
  sense_data.append(sense.get_temperature())
  sense_data.append(sense.get_pressure())
  sense_data.append(sense.get_humidity())
  
  return sense_data
  
  
while True:
	print(get_sense_data())


def get_sense_data():
  sense_data = []
  
  sense_data.append(sense.get_temperature())
  sense_data.append(sense.get_pressure())
  sense_data.append(sense.get_humidity())

  #acellerometro
  acc = sense.get_accelerometer_raw()
  sense_data.append(acc["x"])
  sense_data.append(acc["y"])
  sense_data.append(acc["z"])

  #bussola
  mag = sense.get_compass_raw()
  sense_data.append(mag["x"])
  sense_data.append(mag["y"])
  sense_data.append(mag["z"])
  
  #giroscopio
  gyro = sense.get_gyroscope_raw()
  sense_data.append(gyro["x"])
  sense_data.append(gyro["y"])
  sense_data.append(gyro["z"])
  
  return sense_data
  
  
while True:
	print(get_sense_data())

#parte 1
from skyfield.api import *
import time
attuale = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()

ts = load.timescale()
line1 = '1 25544U 98067A   22032.08513699  .00005650  00000+0  10793-3 0  9998'
line2 = '2 25544  51.6446 290.5992 0006744  84.8658  57.9745 15.49721019324076'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
print(satellite)

#parte2
print(satellite.epoch.utc_jpl())

#parte 3
t = ts.utc(attuale)

days = t - satellite.epoch
print('{:.3f} days away from epoch'.format(days))

if abs(days) > 14:
    satellites = load.tle_file(stations_url, reload=True)
    
#parte 4
    #t = ts.utc(2014, 1, 23, 11, 18, 7)

geocentric = satellite.at(t)
print(geocentric.position.km)

#parte 5
lat, lon = wgs84.latlon_of(geocentric)
print('Latitude:', lat)
print('Longitude:', lon)

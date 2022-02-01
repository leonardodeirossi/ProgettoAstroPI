#parte 1
from skyfield.api import *

ts = load.timescale()
line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
print(satellite)

#parte2
print(satellite.epoch.utc_jpl())

#parte 3
t = ts.utc(2014, 1, 23, 11, 18, 7)

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

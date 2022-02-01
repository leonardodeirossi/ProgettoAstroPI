from skyfield.api import load, wgs84, EarthSatellite


ts = load.timescale()
t = ts.utc(2014, 1, 23, 11, 18, 7)
line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
print(satellite)


geocentric = satellite.at(t)


lat, lon = wgs84.latlon_of(geocentric)
print('Latitude:', lat)
print('Longitude:', lon)

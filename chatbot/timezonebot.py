#!/usr/bin/env python
from geopy.geocoders import Nominatim
from tzwhere import tzwhere

def main():
	pass

def get_coordinates(location_string='clay street'):
	geolocator=Nominatim()
	location=geolocator.geocode(location_string)
	if location:
		print location.address
		return (location.latitude,location.longitude)
	else:
		print "Location not found"
		return None

def get_timezone_string(lat=35,longi=-89.66):
	tz=tzwhere.tzwhere()
	return tz.tzNameAt(lat,longi)

if __name__=='__main__':
	print get_coordinates()
	print get_timezone_string()

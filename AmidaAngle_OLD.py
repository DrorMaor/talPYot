import math
import sys

def DaveningAngle(coords):
    kosel = [31.7767, 35.2345]
    dLng = kosel[1] - coords[1]
    dLat = kosel[0] - coords[0]
    omg = math.atan2(dLng, dLat)
    return (math.degrees(omg))

if __name__ == "__main__":
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent='myapplication')
    locationString = ""
    for i in sys.argv[1:]:
        locationString += i + " "
    location = geolocator.geocode(locationString)
    if location is None:
        print("Location not found")
        sys.exit(1)
    else:
        lat = float(location.raw["lat"])
        lon = float(location.raw["lon"])
        print (location.raw["display_name"])
        print (DaveningAngle([lat, lon]))

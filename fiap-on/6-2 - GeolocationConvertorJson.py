from geopy.geocoders import Nominatim
from functions.JsonFunctions import read_file, save_file

geolocator = Nominatim(user_agent="myapp")
dictonary = read_file("in.json")
listt = dictonary['address']
address = listt[1] + " " + listt[2] + " " + listt[3]
print(address)
location = geolocator.geocode(address)

out = {"coordinates": (location.latitude, location.longitude)}
save_file(out, "out.json")
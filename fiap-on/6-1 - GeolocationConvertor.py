from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myapp")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
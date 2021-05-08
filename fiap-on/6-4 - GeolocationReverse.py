from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myapp")

latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

result = str(geolocator.reverse(f"{latitude}, {longitude}"))
result = result.split(",")

if "None" != result:
    print("Endereço Completo: ", result)
    print("Dado 1...........: ", result[0])
    print("Dado 2...........: ", result[1])
    print("Dado 3...........: ", result[2])
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myapp")
address = input("Digite um endereco com número e cidade. \n Exemplo: avenida paulista, 100 São Paulo: ")
result = str(geolocator.geocode(address)).split(",")

if result[0]!='None':
    print("Endereço completo.: ", result)
    print("Bairro............: ", result[1])
    print("Cidade............: ", result[2])
    print("Regiao............: ", result[3])
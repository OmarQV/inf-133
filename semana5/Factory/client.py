import requests
# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/delivery"

# Definimos los encabezados HTTP que vamos a enviar con la petición
headers = {"Content-Type": "application/json"}

# Definimos el tipo de vehículo como "motorcycle"
vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
print(response.text)

vehicle_type1 = "drone"
data = {"vehicle_type": vehicle_type1}
response = requests.post(url, json=data, headers=headers)
print(response.text)

vehicle_type2 = "scout"
data = {"vehicle_type": vehicle_type2}
response = requests.post(url, json=data, headers=headers)
print(response.text)

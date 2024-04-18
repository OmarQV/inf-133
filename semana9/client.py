import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
# Manda una solicitud get a la ruta '/'
response = requests.get(url)

# Verificar si la solicitud fue exitosa (codigo de estado 200)
if response.status_code == 200:
   print("Respuesta del servidor:")
   print(response.text)
else:
   print("Error al conectar con el servidor:", response.status_code)

# 2. Saludar
params = {
   'nombre': 'Omar'
}
response = requests.get(url + 'saludar', params=params)

# Verificar si la solicitud GET fue exitosa (codigo de estado 200)
if response.status_code == 200:
   data = response.json()
   mensaje = data['mensaje']
   print("Respuesta del servidor (GET):", mensaje)
else:
   print("Error al conectar con el servidor (GET):", response.status_code)

# 3. Sumar
params = {
   'num1': 5,
   'num2': 3
}
response = requests.get(url + 'sumar', params=params)

# Verificar si la solicitud fue exitosa (codigo de estado 200)
if response.status_code == 200:
   print("Respuesta del servidor (GET):")
   print(response.text)
else:
   print("Error al conectar con el servidor:", response.status_code)
   
# 4. Agrega /palindromo?cadena=”reconocer”
params = {
   'cadena': 'reconocer'
}
response = requests.get(url + 'palindromo', params=params)

# Verificar la respuesta
if response.status_code == 200:
   print("Respuesta del servidor (GET):")
   print(response.text)
else:
   print("Error al conectar con el servidor:", requests.status_codes)

# 5./contar?cadena=”exepciones”&vocal=”e”
params = {
   'cadena': 'exepciones',
   'vocal': 'e'
}
response = requests.get(url + 'contar', params=params)

# Verificar la respuesta
if response.status_code == 200:
   print("Respuesta del servidor (GET):")
   print(response.text)
else:
   print("Error al conectar con el servidor:", requests.status_codes)


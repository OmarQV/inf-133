import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

print("+++++++++++++++++++++++++++++++++++")
# GET - Agrega una ruta para mostrar todas las carreras
ruta_carreras = url + "/estudiantes/?nombre=Omar"
get_carreras = requests.request(method="GET", url=ruta_carreras)
print("- Agrega una ruta para mostrar todas las carreras")
print(get_carreras.text)
print("---------------------------------------------------")

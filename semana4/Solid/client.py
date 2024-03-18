import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

print("+++++++++++++++++++++++++++++++++++")
# GET - Agrega una ruta para mostrar todas las carreras
ruta_carreras = url + "carreras"
get_carreras = requests.request(method="GET", url=ruta_carreras)
print("- Agrega una ruta para mostrar todas las carreras")
print(get_carreras.text)
print("---------------------------------------------------")

# GET - Agrega una ruta que devuelva a todos los estudiantes de 
# la carrera de “Economía”
ruta_economia = url + "economia"
get_economia = requests.request(method="GET", url=ruta_economia)
print("- Todos los estudiantes de la carrera de “Economía”")
print(get_economia.text)
print("---------------------------------------------------")

# POST - Agrega a 2 estudiantes de “Economía”
    # 1er estudiante
ruta_post = url + "economia"
nuevo_estudiante = {
    "nombre": "Maria",
    "apellido": "Vega",
}
post_new_economia = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
#print(post_new_economia.text)
print("*****************************")
    # 2do estudiante
ruta_post = url + "economia"
nuevo_estudiante = {
    "nombre": "Lucas",
    "apellido": "Olivera",
}
post_new_economia = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
#print(post_new_economia.text)
print("---------------------------------------------------")

"""
# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", url=ruta_eliminar)
print(eliminar_response.text)

ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
"""
import requests

BASE_URL = "http://localhost:5000/api"

headers = {"Content-Type": "application/json"}

# ? POST
# ! CREAR UN NUEVO LIBRO
print("\n--------- NUEVO LIBRO ---------")
url = f"{BASE_URL}/books"
libro1 = {
   "title": "La Sombra del Viento",
   "author": "Carlos Ruiz Zafón",
   "edition": "10ma edicion",
   "available": "Si",
}
response = requests.post(url, json=libro1, headers=headers)
print("Creando un nuevo libro")
print(response.json())
# ! CREAR UN NUEVO LIBRO
print("\n--------- NUEVO LIBRO ---------")
url = f"{BASE_URL}/books"
libro2 = {
   "title": "La Sombra del Viento",
   "author": "Carlos Ruiz Zafón",
   "edition": "10ma edicion",
   "available": "Si",
}
response = requests.post(url, json=libro1, headers=headers)
print("Creando un nuevo libro")
print(response.json())
# ! CREAR UN NUEVO LIBRO
print("\n--------- NUEVO LIBRO ---------")
url = f"{BASE_URL}/books"
libro3 = {
   "title": "La Sombra del Viento",
   "author": "Carlos Ruiz Zafón",
   "edition": "10ma edicion",
   "available": "Si",
}
response = requests.post(url, json=libro1, headers=headers)
print("Creando un nuevo libro...")
print(response.json())

# ? GET
print("\n--------- LISTA DE LIBROS ---------")
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print(response.json())
print("\n--------- LIBRO ID: 1 ---------")
url = f"{BASE_URL}/books/1"
response = requests.get(url, headers=headers)
print(response.json())

# ? PUT
print("\n--------- UPDATE LIBRO ID: 1 ---------")
url = f"{BASE_URL}/books/2"
book_update = {
   "title": "Contabilidad Intermedia",
   "author": "Gutierrez",
   "edition": "5ta edicion",
   "available": "Si",
}
response = requests.put(url,json=book_update, headers=headers)
print(response.json())

# ? DELETE
print("\n--------- DELETE LIBRO ID: 2 ---------")
url = f"{BASE_URL}/books/2"
response = requests.delete(url, headers=headers)
# * Eliminando
if response.status_code == 204:
   print(f"Libro con ID 2 eliminado con exito.")
else:
   print(f"Error: {response.status_code} - {response.text}")

# ? GET
print("\n--------- LISTA DE LIBROS ---------")
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print(response.json())
print()
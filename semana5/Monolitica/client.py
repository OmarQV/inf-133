import requests
url = "http://localhost:8000"
print("------------------LISTAR--------------------")
response = requests.get(f"{url}/posts")
print(response.text)

print("---------------ID - 2-----------------------")

response = requests.get(f"{url}/post/2")
print(response.text)
print("--------------------------------------")

print("---------------NUEVO POST-----------------------")
post_data = {
    "title": "Mi experiencia como dev",
}
response = requests.post(f"{url}/posts", data=post_data)
print(response.text)

print("-----------------LISTAR---------------------")
response = requests.get(f"{url}/posts")
print(response.text)

print("---------------ACTUALIZAR-----------------------")
put_data = {
    "content": "En Progreso"
}
response = requests.put(f"{url}/post/{3}", data=put_data)
print(response.text)

print("-----------------LISTAR---------------------")
response = requests.get(f"{url}/posts")
print(response.text)


print("-----------------ELIMINAR---------------------")
response = requests.delete(f"{url}/post/{2}")
print(response.text)

print("-----------------LISTAR---------------------")
response = requests.get(f"{url}/posts")
print(response.text)

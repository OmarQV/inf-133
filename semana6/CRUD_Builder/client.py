import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

print()
print("------------------POST--------------------")
mi_taco = {
    "base": "Tortilla de maiz",
    "guiso": "Carne asada",
    "toppings": ["Cebolla", "Cilantro", "Limon"],
    "salsa": "Salsa verde"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

print()
print("------------------GET--------------------")
response = requests.get(url)
print(response.text)

print()
print("---------------PUT-----------------------")
put_data = {
    "salsa": "Salsa golf"
}
response = requests.put(f"{url}/{1}", json=put_data)
print(response.text)

print()
print("------------------GET--------------------")
response = requests.get(url)
print(response.text)

print()
print("------------------DELETE--------------------")
response = requests.delete(f"{url}/1")
print(response.text)

print()
print("------------------GET--------------------")
response = requests.get(url)
print(response.text)

print()
print("------------------POST--------------------")
mi_taco = {
    "base": "Tortilla de maiz",
    "guiso": "Carne asada",
    "toppings": ["Cebolla", "Cilantro", "Limon"],
    "salsa": "Salsa verde"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())
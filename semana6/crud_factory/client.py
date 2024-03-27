import requests

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

print()
print("------------------POST--------------------")
data = {
    "product_type": "tablet",
    "weight": "100g",
    "flavor": "chocolate blanco"
}
response = requests.post(url, json=data, headers=headers)
print(response.text)
data2 = {
    "product_type": "bonbon",
    "weight": "200g",
    "flavor": "chocolate rojo",
    "filling": "fresa"
}
response = requests.post(url, json=data2, headers=headers)
print(response.text)
data3 = {
    "product_type": "truffle",
    "weight": "300g",
    "flavor": "chocolate rojo",
    "filling": "fresa"
}
response = requests.post(url, json=data3, headers=headers)
print(response.text)


print()
print("------------------GET--------------------")
response = requests.get(url, json=data, headers=headers)
print(response.text)

print()
print("------------------PUT--------------------")
data = {
    "weight": "150g",
    "flavor": "chocolate negro"
}
response = requests.put(f"{url}/{1}", json=data, headers=headers)
print(response.text)

''' 

'''
print()
print("-----------------DELETE--------------------")
response = requests.delete(f"{url}/{3}")
print(response.text)

print()
print("------------------GET--------------------")
response = requests.get(url, json=data, headers=headers)
print(response.text)

print("------------------POST--------------------")
data = {
    "product_type": "tablet",
    "weight": "100g",
    "flavor": "chocolate blanco"
}
response = requests.post(url, json=data, headers=headers)
print(response.text)

print()
print("------------------GET--------------------")
response = requests.get(url, json=data, headers=headers)
print(response.text)
from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar("Omar")
result1 = client.service.Sumar(1, 2)
result2 = client.service.Es_Plaindromo('Anita lava la tina')

print(result)
print(result1)
print(result2)
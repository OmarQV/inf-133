from zeep import Client

client = Client('http://localhost:8000')
# Saludo
result = client.service.Saludar("Omar")
# NumberToDollars
result1 = client.service.NumberToDollars(dNum=6.0)
# SumaDosNumeros
result2 = client.service.SumaDosNumeros(1, 2)
# CadenaPalindromo
result3 = client.service.CadenaPalindromo('Anita lava la tina')
result4 = client.service.CadenaPalindromo('Hola Mundo')

# Saludo - Resultado
print(result)
# NumberToDollars - Resultado
print(result1)
# SumaDosNumeros - Resultado
print(result2)
# CadenaPalindromo - Resultado
print(result3)
print(result4)
import requests

card_nummber = "BT1-010"

url = f"https://digimoncard.io/api-public/search.php?card={card_nummber}"

# Se comunica con el cliente
# El resultado se guarda en response - del servicio utilizado
response = requests.request(
   method="GET",
   url=url,
   headers={"Content-Type": "application/json"},
   data = {}
)
print(response.text)

# SOAP - REST
# Metodo de consulta
# 
# Protocolo - Patron de arquitectura
# xml - json
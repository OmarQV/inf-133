from zeep import Client
# https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL
# WSDL - Web Service D

# Consumo de un servicio SOAP
# Protocolo
client = Client(
   "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)

result = client.service.NumberToWords(5)
print(result)

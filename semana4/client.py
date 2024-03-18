import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
{
        estudiantes(id:2){
            nombre
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)
#

# Definir la consulta GraphQL
#query = """
#    {
#        estudianteCarrera(carrera: "Arquitectura"){
#            id
#            nombre
#        }
#    }
#"""
query_eliminar = """
mutation {
        deleteEstudiante(id:3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation1 = requests.post(url, json={'query': query_eliminar})
print(response_mutation1.text)


query_modificar = """
mutation {
        modificar(id:1, nombre: "Angel", apellido: "Vega", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation1 = requests.post(url, json={'query': query_modificar})
print(response_mutation1.text)


query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)
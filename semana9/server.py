# 1. Importa la clase Flask del paquete flask
# 2. Agregamos modulos para trabajar con query params 'request', 'jsonify'
from flask import Flask, request, jsonify

app = Flask(__name__)

# Creamos nuestra primera ruta
@app.route('/')
def hello_world():
   return 'Hola, mundo!'

# 2. Agregamos una nueva ruta
@app.route('/saludar', methods = ['GET'])
def saludar():
   nombre = request.args.get("nombre")
   if not nombre:
      return (
         jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
         400,
      )
   return jsonify({"mensaje": f"Hola, {nombre}!"})

# 3. Agrega /sumar?num1=5&num2=3
@app.route('/sumar', methods = ['GET'])
def sumar():
   num1 = request.args.get("num1")
   num2 = request.args.get("num2")
   if not num1 or not num2:
      return (
         jsonify({
            "error": "Se requiere dos numeros en los parametros de la URL"
         }),
         400,
      )
   resultado = int(num1) + int(num2)
   return jsonify({"mensaje": f"Suma: {resultado}"})

# 4. Agrega /palindromo?cadena=”reconocer”
@app.route('/palindromo', methods = ['GET'])
def palindromo():
   cadena = request.args.get('cadena')
   if not cadena:
      return (
         jsonify({
            "error": "Se requiere una cadena en el parametro de la URL"
         }),
         400,
      )
   if cadena == cadena[::-1]:
      return (
         jsonify({
            "palindromo": True
         })
      )
   else:
      return (
         jsonify({
            "palindromo": False
         })
      )

# 5. /contar?cadena=”exepciones”&vocal=”e”
@app.route('/contar', methods = ['GET'])
def contar():
   cadena = request.args.get('cadena')
   vocal = request.args.get('vocal')
   if not cadena or not vocal:
      return (
         jsonify({
            "error": "Se requiere ambos atributos en los parametros en la URL"
         }),
         400,
      )
   cadena = cadena.lower()
   vocal = vocal.lower()
   count = cadena.count(vocal)
   return jsonify({
      "mensaje": f"La cantidad es: {count} de la vocal {vocal} de la cadena -> {cadena}"
   })

# Levantamos el servidor
if __name__ == '__main__':
   app.run()
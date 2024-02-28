from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiante = [
    {
         "id": 1,
         "nombre": "Omar",
         "apellido": "Quispe",
         "carrera": "Ingenieria de Sistemas"
    },
    {
         "id": 2,
         "nombre": "Pedrito",
         "apellido": "Garcia",
         "carrera": "Ingenieria de Sistemas"
    },
    {
         "id": 3,
         "nombre": "Linda",
         "apellido": "Lopez",
         "carrera": "Informatica"
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):
   def do_GET(self):
      if self.path == 'lista_estudiantes':
         self.send_response(200)
         self.send_header('Content-type', 'application/jaon')
         self.end_headers()
         self.wfile.write(json.dumps(estudiante).encode('utf-8'))
      elif self.path == '/buscar_nombre':
         self.send_response(200)
         self.send_header('Content-type', 'application/json')
         self.end_headers()
         nombres_con_P = [estudiante['nombre'] for estudiante in estudiante if estudiante['nombre'].startswith('P')]
         self.wfile.write(json.dumps({"nombres que inician con P": nombres_con_P}).encode('utf-8'))
      elif self.path == '/contar_carreras':
         self.send_response(200)
         self.send_header('Content-type', 'application/json')
         self.end_headers()            
         carreras = [carrera['carrera'] for carrera in estudiante]
         cnt_carreras = {}
         for carrera in carreras:
            if carrera in cnt_carreras:
               cnt_carreras[carrera] += 1
            else:
               cnt_carreras[carrera] = 1            
         self.wfile.write(json.dumps({"alumnos por carrera": cnt_carreras}).encode('utf-8'))
      elif self.path == '/total_estudiantes':
         self.send_response(200)
         self.send_header('Content-type', 'application/json')
         self.end_headers()
         #estudiantes = [estudiante for estudiante in estudiantes]
         cnt_estudiantes = len(estudiante)
         self.wfile.write(json.dumps({"estudiantes totales": cnt_estudiantes}).encode('utf-8'))
      else:
          self.send_response(404)
          self.send_header('Content-type', 'aplication/json')
          self.end_headers()
          self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))


def run_server(port = 8000):
   try:
      server_address = ('', port)
      httpd = HTTPServer(server_address, RESTRequestHandler)
      print(f'Iniciando servidor web en http://localhost:{port}/')
      print(f'Ir a <a href="http://localhost:{port}/buscar_nombre">buscar_nombre</a>')
      print(f'Ir a <a href="http://localhost:{port}/contar_carreras">contar_carreras</a>')
      print(f'Ir a <a href="http://localhost:{port}/total_estudiantes">total_estudiantes</a>')
      httpd.serve_forever()
   except KeyboardInterrupt:
      print("Apagando servidor web")
      httpd.socket.close()


if __name__ == "__main__":
	run_server()

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

class EstudiantesService:
   @staticmethod
   def find_student(id):
      return next(
         (estudiante for estudiante in estudiantes if estudiante["id"] == id),
         None,
      )
   
   @staticmethod
   def filter_students_by_name(nombre):
      return [
         estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre
      ]

   @staticmethod
   def add_student(data):
      data["id"] = len(estudiantes) + 1
      estudiantes.append(data)
      return estudiantes

   @staticmethod
   def update_student(id, data):
      estudiante = EstudiantesService.find_student(id)
      if estudiante:
         estudiante.update(data)
         return estudiantes
      else:
         return None

   @staticmethod
   def delete_students():
      estudiantes.clear()
      return estudiantes
   
      
class HTTPResponseHandler:
   @staticmethod
   def handle_response(handler, status, data):
      handler.send_response(status)
      handler.send_header("Content-type", "application/json")
      handler.end_headers()
      handler.wfile.write(json.dumps(data).encode("utf-8"))


estudiantes = [
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
    },
    {
        "id": 4,
        "nombre": "Lola",
        "apellido": "Vega",
        "carrera": "Economia"
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):        
   def response_handler(self, status_code, data):
      self.send_response(status_code)
      self.send_header("Content-type", "application/json")
      self.end_headers()
      self.wfile.write(json.dumps(data).encode("utf-8"))
      
   def data_reader(self):
      content_length = int(self.headers["Content-Length"])
      data = self.rfile.read(content_length)
      data = json.loads(data.decode("utf-8"))
      return data
   
   def find_student(self, estudiantes, id):
      estudiante = next(
         (estudiante for estudiante in estudiantes if estudiante["id"] == id),
         None,
      )
      
   def do_GET(self):
      parsed_path = urlparse(self.path)
      query_params = parse_qs(parsed_path.query)
      if parsed_path.path == "/estudiantes/":
         if "nombre" in query_params:
            nombre = query_params["nombre"][0]
            # modificar aqui
            estudiantes_filtrados = [
            estudiante
               for estudiante in estudiantes
               if estudiante["nombre"] == nombre
            ]
            #
            if estudiantes_filtrados != []:
               self.response_handler(200, estudiantes_filtrados)
            else:
               self.response_handler(204,[])
         else:
            self.response_handler(200, [])
      
         if self.path == "/estudiantes":
               self.response_handler(200, estudiantes)
      # Agrega una ruta para mostrar todas las carreras
      elif self.path == "/carreras":
         carreras = []
         for estudiante in estudiantes:
               carreras.append(estudiante["carrera"])
         self.response_handler(200, estudiantes)
      # Agrega una ruta para que devuelva a los estudiantes de la carrera
      # de Economia
      elif self.path == "/economia":
         carrera_economia = []
         for estudiante in estudiantes:
               if estudiante["carrera"] == "Economia":
                  carrera_economia.append(estudiante)
         self.response_handler(200, estudiante)
      else:
         self.response_handler(404, {"Error": "Ruta no existente"})

   def do_POST(self):
      if self.path == "/estudiantes":
         data = self.data_reader()
         data["id"] = len(estudiantes) + 1
         estudiantes.append(data)
         self.response_handler(201, estudiantes)
      elif self.path == '/economia':
         data = self.data_reader()
         data["id"] = len(estudiantes) + 1
         estudiantes.append(data)
         self.response_handler(201, estudiantes)
      else:
         self.response_handler(404, {"Error": "Ruta no existente"})

   def do_PUT(self):
      if self.path.startswith("/estudiantes/"):
         id = int(self.path.split("/")[-1]) 
         estudiante = self.find_student(estudiantes, id) 
         data = self.data_reader()
         if estudiante:
               estudiante.update(data)
               self.response_handler(200, estudiantes)
         else:
               self.response_handler(404, {"Error": "Estudiante no encontrado"})    
      else:
         self.response_handler(404, {"Error": "Ruta no existente"})

   def do_DELETE(self):
      if self.path == "/estudiantes":
            estudiantes.clear()
            self.response_handler(200, estudiantes)
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
      else:
            self.response_handler(404, {"Error": "Ruta no existente"})

# 200 -> Exito
# 201 -> Solicitud completada y creado un nuevo recurso 
# 204 -> No Content - Completada pero no hay contenido para enviar
# 400 -> Error humano/capa 8
# 401 -> Recurso protegido
# 404 -> Not Found Page (Pagina no encontrada)

def run_server(port = 8000):
   try:
      server_address = ('', port)
      httpd = HTTPServer(server_address, RESTRequestHandler)
      print(f'Iniciando servidor web en http://localhost:{port}/')
      httpd.serve_forever()
   except KeyboardInterrupt:
      print("Apagando servidor web")
      httpd.socket.close()


if __name__ == "__main__":
	run_server()
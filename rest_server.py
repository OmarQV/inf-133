from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiante = {
   "id": 1,
   "nombre": "Pedrito",
   "apellido": "Garcia",
   "carrera": "Ingenieria de Sistemas"    
}

class RESTRequestHandler(BaseHTTPRequestHandler):
   def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'application/jaon')
      self.end_headers()
      self.wfile.write(json.dumps(estudiante).encode('utf-8'))

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

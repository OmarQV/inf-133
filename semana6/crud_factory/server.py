from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Fabrica de chocolates
chocolates = {}
# Tabletas -> tablet
# Bombom -> bonbon
# Trufas -> truffle
# peso -> weight
# sabor -> flavor
# relleno -> filling
class ChocolateProduct:
    def __init__(self, product_type, weight, flavor, filling=None):
        self.product_type = product_type
        self.weight = weight
        self.flavor = flavor
        self.filling = filling


class Tablet(ChocolateProduct):
    def __init__(self, weight, flavor):
        super().__init__("tablet", weight, flavor)

# relleno
class Bonbon(ChocolateProduct):
    def __init__(self, weight, flavor, filling):
        super().__init__("bonbon", weight, flavor, filling)

# relleno
class Truffle(ChocolateProduct):
    def __init__(self, weight, flavor, filling):
        super().__init__("truffle", weight, flavor, filling)


class ChocolateFactory:
    @staticmethod
    def create_product(product_type, weight, flavor, filling=None):
        if product_type == "tablet":
            return Tablet(weight, flavor)
        elif product_type == "bonbon":
            return Bonbon(weight, flavor, filling)
        elif product_type == "truffle":
            return Truffle(weight, flavor, filling)
        else:
            raise ValueError("Tipo de producto de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_product(self, data):
        product_type = data.get("product_type", None)
        weight = data.get("weight", None)
        flavor = data.get("flavor", None)
        if product_type in ["bonbon", "truffle"]:
            filling = data.get("filling", None)
        else:
            filling = None
        
        
        chocolate_product = self.factory.create_product(
            product_type, weight, flavor, filling
        )
        # Buscar el key mas alto
        # chocolates[len(chocolates) + 1] = chocolate_product
        if chocolates:
            max_key = max(chocolates.keys())
        else:
            max_key = 0
        next_key = max_key + 1
        chocolates[next_key] = chocolate_product
        
        return chocolate_product

    def list_products(self):
        return {index: product.__dict__ for index, product in chocolates.items()}

    def update_product(self, product_id, data):
        if product_id not in chocolates:
            return None

        product = chocolates[product_id]
        weight = data.get("weight", product.weight)
        flavor = data.get("flavor", product.flavor)

        if product.product_type in ["bonbon", "truffle"]:
            filling = data.get("filling", product.filling)
            if filling is not None:
                product.filling = filling

        if weight is not None:
            product.weight = weight
        if flavor is not None:
            product.flavor = flavor

        return product


    def delete_product(self, product_id):
        if product_id in chocolates:
            del chocolates[product_id]
            return {"message": "Producto eliminado"}
        else:
            return None

#* lista de parametros
#** diccionario de parametros
class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_service = ChocolateService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.add_product(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_service.list_products()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.update_product(product_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Producto no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_service.delete_product(product_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Producto no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()


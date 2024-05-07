from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_list, render_book_detail

# Crear un blueprint para el controlador de animales
book_bp = Blueprint("book", __name__)


# Ruta para obtener la lista de animales
@book_bp.route("/books", methods=["GET"])
def get_books():
   books = Book.get_all()
   return jsonify(render_book_list(books))


# Ruta para obtener un animal específico por su ID
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
   book = Book.get_by_id(id)
   if book:
      return jsonify(render_book_detail(book))
   return jsonify({"error": "Libro no encontrado"}), 404


# Ruta para crear un nuevo animal
@book_bp.route("/books", methods=["POST"])
def create_book():
   data = request.json
   title = data.get("title")
   author = data.get("author")
   edition = data.get("edition")
   available = data.get("available")

   # Validación simple de datos de entrada
   if not title or not author or not edition or available is None:
      return jsonify({"error": "Faltan datos requeridos"}), 400

   # Crear un nuevo animal y guardarlo en la base de datos
   book = Book(title=title, author=author, edition=edition, available=available)
   book.save()

   return jsonify(render_book_detail(book)), 201


# Ruta para actualizar un animal existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
   book = Book.get_by_id(id)

   if not book:
      return jsonify({"error": "Libro no encontrado"}), 404

   data = request.json
   title = data.get("title")
   author = data.get("author")
   edition = data.get("edition")
   available = data.get("available")

   # Actualizar los datos del animal
   book.update(title=title, author=author, edition=edition, available=available)

   return jsonify(render_book_detail(book))


# Ruta para eliminar un animal existente
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
   book = Book.get_by_id(id)

   if not book:
      return jsonify({"error": "Libro no encontrado"}), 404

   # Eliminar el animal de la base de datos
   book.delete()

   # Respuesta vacía con código de estado 204 (sin contenido)
   return "", 204
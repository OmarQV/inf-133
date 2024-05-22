from flask import Blueprint, request, jsonify
from models.sweet_model import Sweet
from views.sweet_view import render_sweet_list, render_sweet_detail
#! JWT
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
#!
from utils.decorators import jwt_required, role_required

# Crear un blueprint para el controlador de dulcees
sweet_bp = Blueprint("sweet", __name__)


# Ruta para obtener la lista de dulcees
@sweet_bp.route("/sweets", methods=["GET"])
@jwt_required
#! implementando role
@role_required(role=["admin", "user"])
def get_sweets():
   sweets = Sweet.get_all()
   return jsonify(render_sweet_list(sweets))


# Ruta para obtener un dulce específico por su ID
@sweet_bp.route("/sweets/<int:id>", methods=["GET"])
@jwt_required
#! implementando role
@role_required(role=["admin", "user"])
def get_sweet(id):
   sweet = Sweet.get_by_id(id)
   if sweet:
      return jsonify(render_sweet_detail(sweet))
   return jsonify({"error": "Libro no encontrado"}), 404


# Ruta para crear un nuevo dulce
@sweet_bp.route("/sweets", methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def create_sweet():
   data = request.json
   brand = data.get("brand")
   weight = data.get("weight")
   flavor = data.get("flavor")
   origin = data.get("origin")

   # Validación simple de datos de entrada
   if not brand or not weight or not flavor or origin is None:
      return jsonify({"error": "Faltan datos requeridos"}), 400

   # Crear un nuevo dulce y guardarlo en la base de datos
   sweet = Sweet(brand=brand, weight=weight, flavor=flavor, origin=origin)
   sweet.save()

   return jsonify(render_sweet_detail(sweet)), 201


# Ruta para actualizar un dulce existente
@sweet_bp.route("/sweets/<int:id>", methods=["PUT"])
@jwt_required
#! implementando role
@role_required(role=["admin"])
def update_sweet(id):
   sweet = Sweet.get_by_id(id)

   if not sweet:
      return jsonify({"error": "Libro no encontrado"}), 404

   data = request.json
   brand = data.get("brand")
   weight = data.get("weight")
   flavor = data.get("flavor")
   origin = data.get("origin")

   # Actualizar los datos del dule
   sweet.update(brand=brand, weight=weight, flavor=flavor, origin=origin)

   return jsonify(render_sweet_detail(sweet))


# Ruta para eliminar un dulce existente
@sweet_bp.route("/sweets/<int:id>", methods=["DELETE"])
@jwt_required
#! implementando role
@role_required(role=["admin"])
def delete_sweet(id):
   sweet = Sweet.get_by_id(id)

   if not sweet:
      return jsonify({"error": "Dulce no encontrado"}), 404

   # Eliminar el dulce de la base de datos
   sweet.delete()

   # Respuesta vacía con código de estado 204 (sin contenido)
   return "", 204




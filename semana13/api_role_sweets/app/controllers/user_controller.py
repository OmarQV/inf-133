from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from views.user_view import render_user_detail, render_user_list
#!
from utils.decorators import jwt_required, role_required

#! JWT
user_bp = Blueprint("user", __name__)

# Ruta para obtener la lista de users
@user_bp.route("/users", methods=["GET"])
@jwt_required
#! implementando role
@role_required(role=["admin", "user"])
def get_users():
   users = User.get_all()
   return jsonify(render_user_list(users))

# Ruta para obtener un dulce específico por su ID
@user_bp.route("/users/<int:id>", methods=["GET"])
@jwt_required
#! implementando role
@role_required(role=["admin", "user"])
def get_user(id):
   user = User.get_by_id(id)
   if user:
      return jsonify(render_user_detail(user))
   return jsonify({"error": "Usuario no encontrado"}), 404


#! JWT
@user_bp.route("/register", methods=["POST"])
def register():
   data = request.json
   username  = data.get("username")
   password = data.get("password")
   role = data.get("role")
   
   if not username or not password:
      return jsonify({
         "error": "Se requieren nombre de usuario y contraseña"
      }), 400
   
   existing_user = User.find_by_username(username)
   if existing_user:
      return jsonify({
         "error": "El nombre de usuario ya esta en uso"
      }), 400
   
   new_user = User(username, password, role)
   new_user.save()
   
   return jsonify({
      "message": "Usuario creado exitosamente"
   }), 201

@user_bp.route("/login", methods=["POST"])
def login():
   data = request.json
   username  = data.get("username")
   password = data.get("password")
   
   user = User.find_by_username(username)
   if user and check_password_hash(user.password_hash, password):
      #! Si las credenciales son válidas, genera un token JWT
      access_token = create_access_token(
         identity={"username": username, "role": user.role}
      )
      return jsonify(acces_token=access_token), 200
   else:
      return jsonify({
         "error": "Credenciales invalidas"
      }), 401

# Ruta para actualizar un dulce existente
@user_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required
#! implementando role
@role_required(role=["admin"])
def update_user(id):
   user = User.get_by_id(id)

   if not user:
      return jsonify({"error": "Libro no encontrado"}), 404

   data = request.json
   username = data.get("username")
   password = data.get("password")
   role = data.get("role")

   # Actualizar los datos del user
   user.update(username=username, password=password, role=role)

   return jsonify(render_user_detail(user))


# Ruta para eliminar un dulce existente
@user_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required
#! implementando role
@role_required(role=["admin"])
def delete_user(id):
   user = User.get_by_id(id)

   if not user:
      return jsonify({"error": "Usuario no encontrado"}), 404

   # Eliminar el dulce de la base de datos
   user.delete()

   # Respuesta vacía con código de estado 204 (sin contenido)
   return "", 204

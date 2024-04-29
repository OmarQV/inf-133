from flask import Blueprint, request, redirect, url_for
from datetime import datetime
# Importamos las vistas
from views import user_view
# Importamos el modelo de usuario
from models.user_model import User

# Un Blueprint es un objeto que agrupa rutas y vistas
user_bp = Blueprint('user', __name__)

# Definimos las rutas "/" asociada a la funcion usuarios
# que nos devuelve la vista de usuarios
@user_bp.route('/')
def usuarios():
   # Obtenemos todos los usuarios
   users = User.get_all()
   # Llamamos a la vista de usuarios
   return user_view.usuarios(users)

@user_bp.route('/users', methods=['GET', 'POST'])
def registro():
   if request.method == 'POST':
      # Obtenemos los datos del formulario
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      contrasenia = request.form['contrasenia']
      birthday = request.form['birthday']
      #
      birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
      # Creamos un nuevo usuario
      user = User(first_name, last_name, email, contrasenia, birthday)
      # Guardamos el usuario
      user.save()
      # Redirigimos a la vista de usuarios
      return redirect(url_for('user.usuarios'))
   # Llamamos a la vista de registro
   return user_view.registro()


# Actualizar la información de un usuario por su id
# primero recuperamos la información del usuario
@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):
   # Obtenemos el usuario por su id
   user = User.get_by_id(id)
   if not user:
      return "Usuario no encontrado", 404
   return user_view.actualizar(user)


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@user_bp.route("/users/<int:id>", methods=["POST"])
def actualizar(id):
   user = User.get_by_id(id)
   if not user:
      return "Usuario no encontrado", 404
   # Obtenemos los datos del formulario
   first_name = request.form["first_name"]
   last_name = request.form["last_name"]
   email = request.form['email']
   contrasenia = request.form['contrasenia']
   birthday = request.form['birthday']
   birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
   # Actualizamos los datos del usuario
   user.first_name = first_name
   user.last_name = last_name
   user.email = email
   user.contrasenia = contrasenia
   user.birthday = birthday
   # Guardamos los cambios
   user.update()
   return redirect(url_for("user.usuarios"))

@user_bp.route("/users/<int:id>/delete")
def delete(id):
   user = User.get_by_id(id)
   if not user:
      return "Usuario no encontrado", 404
   user.delete()
   return redirect(url_for("user.usuarios"))
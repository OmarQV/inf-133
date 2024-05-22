import json
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
   __tablename__ = "users"

   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(50), unique=True, nullable=False)
   password_hash = db.Column(db.String(128), nullable=False)
   role = db.Column(db.String(50), nullable=False)

   def __init__(self, username, password, role=["user"]):
      self.username = username
      #! cualquier estructura - dump -> lo vuelve una cadena
      self.role = json.dumps(role)
      self.password_hash = generate_password_hash(password)

   def save(self):
      db.session.add(self)
      db.session.commit()

   # Esta funcion encuentra un usuario por su nombre de usuario
   @staticmethod
   def find_by_username(username):
      return User.query.filter_by(username=username).first()

   # Obtiene todos los dulces de la base de datos
   @staticmethod
   def get_all():
      return User.query.all()

   # Obtiene un dulce por su ID
   @staticmethod
   def get_by_id(id):
      return User.query.get(id)

   # Actualiza un dulce en la base de datos
   def update(self, username, password, role=["user"]):
      if username is not None:
         self.username = username
      if password is not None:
         self.password = password
      if role is not None:
         self.role = json.dumps(role)
      db.session.commit()

   # Elimina un dulce de la base de datos
   def delete(self):
      db.session.delete(self)
      db.session.commit()

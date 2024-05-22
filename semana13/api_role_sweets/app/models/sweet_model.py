from database import db

# Define la clase `Sweet` que hereda de `db.Model`
# `Animal` representa la tabla `dulces` en la base de datos
# sweets
# brand
# weight
# flavor
# origin
class Sweet(db.Model):
   __tablename__ = "sweets"

   # Define las columnas de la tabla `sweets`
   id = db.Column(db.Integer, primary_key=True)
   brand = db.Column(db.String(100), nullable=False)
   weight = db.Column(db.Float(), nullable=False)
   flavor = db.Column(db.String(100), nullable=False)
   origin = db.Column(db.String(100), nullable=False)

   # Inicializa la clase `Dulce`
   def __init__(self, brand, weight, flavor, origin):
      self.brand = brand
      self.weight = weight
      self.flavor = flavor
      self.origin = origin

   # Guarda un dulce en la base de datos
   def save(self):
      db.session.add(self)
      db.session.commit()

   # Obtiene todos los dulces de la base de datos
   @staticmethod
   def get_all():
      return Sweet.query.all()

   # Obtiene un dulce por su ID
   @staticmethod
   def get_by_id(id):
      return Sweet.query.get(id)

   # Actualiza un dulce en la base de datos
   def update(self, brand=None, weight=None, flavor=None, origin=None):
      if brand is not None:
         self.brand = brand
      if weight is not None:
         self.weight = weight
      if flavor is not None:
         self.flavor = flavor
      if origin is not None:
         self.origin = origin
      db.session.commit()

   # Elimina un dulce de la base de datos
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      

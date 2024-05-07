from database import db

# Define la clase `Book` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Book(db.Model):
   __tablename__ = "books"

   # Define las columnas de la tabla `books`
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   author = db.Column(db.String(100), nullable=False)
   edition = db.Column(db.String(100), nullable=False)
   available = db.Column(db.String(100), nullable=False)

   # Inicializa la clase `Animal`
   def __init__(self, title, author, edition, available):
      self.title = title
      self.author = author
      self.edition = edition
      self.available = available

   # Guarda un animal en la base de datos
   def save(self):
      db.session.add(self)
      db.session.commit()

   # Obtiene todos los animales de la base de datos
   @staticmethod
   def get_all():
      return Book.query.all()

   # Obtiene un animal por su ID
   @staticmethod
   def get_by_id(id):
      return Book.query.get(id)

   # Actualiza un animal en la base de datos
   def update(self, title=None, author=None, edition=None, available=None):
      if title is not None:
         self.title = title
      if author is not None:
         self.author = author
      if edition is not None:
         self.edition = edition
      if available is not None:
         self.available = available
      db.session.commit()

   # Elimina un libro de la base de datos
   def delete(self):
      db.session.delete(self)
      db.session.commit()
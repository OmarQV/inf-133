def render_book_list(books):
   # Representa una lista de animales como una lista de diccionarios
   return [
      {
         "id": book.id,
         "title": book.title,
         "author": book.author,
         "edition": book.edition,
         "available": book.available,
      }
      for book in books
   ]

def render_book_detail(book):
   # Representa los detalles de un animal como un diccionario
   return {
      "id": book.id,
      "title": book.title,
      "author": book.author,
      "edition": book.edition,
      "available": book.available,
   }
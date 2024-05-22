def render_sweet_list(sweets):
   # Representa una lista de animales como una lista de diccionarios
   return [
      {
         "id": sweet.id,
         "brand": sweet.brand,
         "weight": sweet.weight,
         "flavor": sweet.flavor,
         "origin": sweet.origin,
      }
      for sweet in sweets
   ]

def render_sweet_detail(sweet):
   # Representa los detalles de un animal como un diccionario
   return {
      "id": sweet.id,
      "brand": sweet.brand,
      "weight": sweet.weight,
      "flavor": sweet.flavor,
      "origin": sweet.origin,
   }
from flask import render_template
from flask_login import current_user


# La función `list_sweets` recibe una lista de
# dulces y renderiza el template `sweets.html`
def list_sweets(sweets):
   return render_template(
      "sweets.html",
      sweets=sweets,
      title="Lista de dulces",
      current_user=current_user,
   )


# La función `create_sweet` renderiza el
# template `create_sweet.html` o devuelve un JSON
# según la solicitud
def create_sweet():
   return render_template(
      "create_sweet.html", title="Crear Dulce", current_user=current_user
   )


# La función `update_sweet` recibe un libro
# y renderiza el template `update_sweet.html`
def update_sweet(sweet):
   return render_template(
      "update_sweet.html",
      title="Editar Dulce",
      sweet=sweet,
      current_user=current_user,
   )
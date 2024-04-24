from flask import render_template

# La función `usuarios` recibe una lista de
# usuarios y renderiza el template `usuarios.html`
# Porque usamos un for para iterar - se envia un parametro
def usuarios(users):
   return render_template("usuarios.html", users=users)

# La función `registro` renderiza el
# template `registro.html`
def registro():
   return render_template("registro.html")
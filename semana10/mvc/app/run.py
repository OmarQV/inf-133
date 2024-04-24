from flask import Flask
# Importamos el controlador
from controller import user_controller
# Importamos la base de datos
from database import db

app = Flask(__name__)

#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(user_controller.user_bp)


if __name__ == '__main__':
   # si no existen las tablas
   with app.app_context():
      db.create_all()
   app.run(debug=True)
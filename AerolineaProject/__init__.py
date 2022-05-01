from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
#slq alchemy
db= SQLAlchemy(app)
#migraciones
migrate = Migrate(app, db)
#vistas
from AerolineaProject.login.views import login
from AerolineaProject.usuarios.views import usuarios
from AerolineaProject.usuarios.views import paises

#modelos
from AerolineaProject.Modelos.rol import Rol
from AerolineaProject.Modelos.usuario import Usuario
from AerolineaProject.Modelos.pais import Pais
from AerolineaProject.Modelos.aereopuerto import Aereopuerto
from AerolineaProject.Modelos.avion import Avion
from AerolineaProject.Modelos.reservacion import Reservacion
from AerolineaProject.Modelos.vuelo import vuelo

#registrando blueprints
app.register_blueprint(login)
app.register_blueprint(usuarios)
app.register_blueprint(paises)
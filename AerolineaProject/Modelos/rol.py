from AerolineaProject import db

class Rol(db.Model):

    #Llave primaria
    idrol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(60))

    #constructor
    def __init__(self, rol) -> None:
        self.rol=rol
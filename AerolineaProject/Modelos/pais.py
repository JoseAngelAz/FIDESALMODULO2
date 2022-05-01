from AerolineaProject import db

class Pais(db.Model):
    #tabla de paises
    idpais = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(60))

    #constructor
    def __init__(self, pais) -> None:
        self.pais = pais
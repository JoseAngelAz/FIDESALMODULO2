from AerolineaProject import db

class Avion(db.Model):
    #pk
    idavion = db.Column(db.Integer, primary_key=True)
    capacidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(70),nullable=True)
    #constructor
    def __init__(self, idavion, capacidad, descripcion) -> None:
        self.idavion = idavion
        self.capacidad = capacidad,
        self.descripcion = descripcion
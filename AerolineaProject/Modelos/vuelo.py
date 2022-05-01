import datetime
from AerolineaProject import db

class vuelo(db.Model):
    idvuelo = db.Column(db.Integer, primary_key=True)
    idorigen = db.Column(
        db.Integer,
        db.ForeignKey('aereopuerto.idaereopuerto'),
        nullable=False   
    )
    iddestino = db.Column(
        db.Integer,
        db.ForeignKey('aereopuerto.idaereopuerto'),
        nullable=False   
    )
    fecha =db.Column(db.DateTime, default=datetime
    )
    estado= db.Column(db.Boolean, default=False, nullable=False)
    idavion = db.Column(
        db.Integer,
        db.ForeignKey('idavion.idavion',
        ondelete='CASCADE'),
        nullable=False
    )

    #constructor
    def __init__(self, idvuelo, idorigen, iddestino, fecha, estado, idavion) -> None:
        self.idvuelo = idvuelo
        self.rol=idorigen
        self.rol=iddestino
        self.rol=fecha
        self.rol=estado
        self.rol=idavion
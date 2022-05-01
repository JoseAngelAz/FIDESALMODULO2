from AerolineaProject import db

class Reservacion(db.Model):
    idreservacion = db.Column(db.Integer, primary_key=True)
    nboletos = db.Column(
        db.Integer,
        nullable = False
        )
    idusuario = db.Column(
        db.Integer,
        db.ForeignKey('usuario.idusuario', ondelete='CASCADE'),
        nullable=False
    )
    idvuelo = db.Column(
        db.Integer,
        db.ForeignKey('idvuelo.idvuelo', ondelete='CASCADE'),
        nullable=False
    )

    #constructor
    def __init__(self, idusuario, idvuelo, nboletos) -> None:
        self.idusuario = idusuario
        self.idvuelo = idvuelo
        self.nboletos = nboletos
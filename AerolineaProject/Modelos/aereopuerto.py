from AerolineaProject import db
class Aereopuerto(db.Model):
    #tabla aereopuerto
    idaereopuerto = db.Column(db.Integer, primary_key=True)
    aereopuerto = db.Column(db.String(60))
    ciudad = db.Column(db.String(45))
    idpais = db.Column(
        db.Integer,
        db.ForeignKey('pais.idpais',
        ondelete='CASCADE'),
        nullable=False
    )

    #constructor
    def __init__(self, aereopuerto, ciudad, idpais) -> None:
        self.pais = aereopuerto
        self.ciudad = ciudad
        self.idpais = idpais        
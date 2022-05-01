
from AerolineaProject import db
from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, SelectField, EmailField
from wtforms.validators import Email, EqualTo,InputRequired,Length,Regexp


class UsuarioForm(FlaskForm):

    usuario = StringField('Usuario',
    validators=[
        InputRequired("Digite su nombre de Usuario"),
        Length(min=6, message="Usuario debe tenet 6 caracteres minimo"),
        Regexp('^\w+$', message="Usuario solo debe contener letras y numeros")
        ]
    )

    nombres = StringField('Nombres',
    validators=[
        InputRequired("Digite el nombre de usuario")
    ]
    )

    apellidos = StringField('Apellidos',
    validators=[
        InputRequired("Digite el apellido del Usuario")
    ]
    )

    email = EmailField('Email',
    validators=[
        InputRequired("Digite el apellido del Usuario"),
        Email("El formato no es correcto")
    ]
    )

    clave = PasswordField('Clave',
    validators=[
        InputRequired("Digite una clave"),
        EqualTo('Confirmar','Las claves no son iguales'),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})',message='la clave es debil')
    ]
)
    confirmar = PasswordField('Confirmar Clave', validators=[InputRequired()])

    rol_id = SelectField('Rol', coerce=int)
#falta pais
    pais_id = SelectField('Pais', coerce=int)

#MODELO
class Usuario(db.Model):

    idusuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(40),unique=True)
    nombres = db.Column(db.String(60))
    apellidos = db.Column(db.String(60))
    email = db.Column(db.String(100))
    clave = db.Column(db.String(255))
    #rol
    rol_id = db.Column(
        db.Integer,
        #rol.idrol es la clase y la variable idrol
        db.ForeignKey('rol.idrol',ondelete='CASCADE'),
        nullable=False
        )
    #pais
    pais_id = db.Column(
    db.ForeignKey('pais.idpais',ondelete='CASCADE'),
    nullable=False
    )
    #constructor
    #def __init__(self, usuario) -> None:        
     #   self.usuario = usuario
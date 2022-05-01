from flask import Blueprint, render_template, request, redirect, url_for,flash
from AerolineaProject.Modelos.pais import Pais
from AerolineaProject.Modelos.rol import Rol
from AerolineaProject.Modelos.usuario import Usuario, UsuarioForm
from AerolineaProject import db



usuarios = Blueprint('usuarios',__name__)
paises = Blueprint('paises',__name__)


#LISTA DE USUARIOS
@usuarios.route('/usuarios/lista-usuarios')
def lista_usuario():
#instancia de usuarios q trae todos los usuarios
    usuarios = Usuario.query.all()
#retorna la vista con el obj que tiene los usuarios
    return render_template('/usuarios/lista-usuario.html', usuarios=usuarios)

#REGISTRAR USUARIO
@usuarios.route('/usuarios/registrarse', methods=['POST','GET'])
def registrarse():

#crea obj de Usuario    
    usuario = Usuario()
#crea obj de UsuarioForm con usuario como parametro    
    usuario_form = UsuarioForm(obj=usuario)
    usuario_form.rol_id.choices = [(r.idrol, r.rol) for r in Rol.query.all()]
    usuario_form.pais_id.choices = [(p.idpais, p.pais) for p in Pais.query.all()]
        
    if usuario_form.validate_on_submit():
            usuario_form.populate_obj(usuario)
            db.session.add(usuario)
            db.session.commit()
            flash('usuario registrado con exito','info')
            return  redirect(url_for('usuarios.lista_usuario'))
    else:
                flash('FALLO EN GUARDAR USUARIO','error')
            
    return render_template('/usuarios/registrarse.html',form=usuario_form)

@usuarios.route('/usuarios/inicio')
def inicio():
    return render_template('/usuarios/usuarios.html')


@usuarios.route('/usuarios/nuevo-rol')
def nuevo_rol():
    return render_template('/usuarios/nuevo_rol.html')

@usuarios.route('/usuarios/lista-rol')
def lista_rol():
    roles = Rol.query.all()
    return render_template('/usuarios/lista_rol.html', lista_roles = roles)

@usuarios.route('/usuarios/guardar-rol', methods=['POST'])
def guardar_rol():
    rol = Rol(request.form['rol'])
    db.session.add(rol)
    db.session.commit()
    #nombre de la funcion
    return redirect(url_for('usuarios.lista_rol'))  

@usuarios.route('/')
def home():
    return render_template('/usuarios/home.html')    

# RUTAS DE VISTA PAISES    
@paises.route('/paises')
def ver_paises():
    return render_template('/paises/paises.html')
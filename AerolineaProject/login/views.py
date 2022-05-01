from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route('/login/inicio')
def inicio():
    return render_template('/login/login.html')
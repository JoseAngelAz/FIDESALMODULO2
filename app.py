from flask import Flask
app = Flask(__name__)
from AerolineaProject import app

from flask import render_template

#404 
def pagina_no_encontrada(error):
    errores={'error':'Pagina no Encontrada!'}
    return render_template('/errores/404.html',errores=errores), 404
    

if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
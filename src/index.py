from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import bcrypt
from src.gestores.gestionJuego import *
from src.clases import juego, cliente, gafa, evento

app = Flask(__name__)

app.secret_key = "appLogin"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0000'
app.config['MYSQL_DB'] = 'dbvertex'

mysql = MySQL(app)

semilla = bcrypt.gensalt()

@app.route('/')
def main():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/ingresar', methods=["GET", "POST"])
def ingresar():
    if request.method=="GET":
        if 'username' in session:
            print("Entraste")
            return render_template('home.html')
        else:
            print("No entraste")
            return render_template('login.html')
    else:
        nombre = request.form['username']
        contra = request.form['password']
        contra_encode = contra.encode("utf-8")
        print(contra_encode)

        cur = mysql.connection.cursor()

        cur.callproc('autenticar', [nombre])

        usuario = cur.fetchone()

        cur.close()

        if(usuario != None):
            contra_encriptado_encode = usuario[1].encode()
            print(contra_encriptado_encode)
            if(contra_encode == contra_encriptado_encode):
                session['username'] = usuario[0]
                return render_template('home.html')
            else:
                return render_template('login.html')

@app.route('/salir')
def salir():
    session.clear()

    return render_template('login.html')

@app.route('/clientes')
def clientes():
    if 'username' in session:
        return render_template('clientes.html')
    else:
        return render_template('login.html')

@app.route('/juegos')
def juegos():
    if 'username' in session:
        data = verJuegos()
        return render_template('juegos.html', juegos = data)
    else:
        return render_template('login.html')

@app.route('/crearjuego', methods=["GET", "POST"])
def crearjuego():
    if 'username' in session:
        if request.method == "GET":

            fabricante = request.form.get('fabricante', None)
            duracion = request.form.get('duracion', None)
            version = request.form.get('version', None)
            idioma = request.form.get('idioma', None)
            nombre = request.form.get('nombre', None)
            internet = request.form.get('internet', None)
            descripcion = request.form.get('descripcion', None)
            jugadores = request.form.get('jugadores', None)
            inicio = request.form.get('inicio', None)
            final = request.form.get('final', None)

            try:
                crearJuego(fabricante, duracion, version, idioma, nombre, internet, descripcion, jugadores, inicio, final)
                return render_template('juegos.html')
            except:
                return render_template('login.html')

        return render_template('crearjuego.html')
    else:
        return render_template('login.html')

@app.route('/gafas')
def gafas():
    if 'username' in session:
        return render_template('gafas.html')
    else:
        return render_template('login.html')

@app.route('/eventos')
def eventos():
    if 'username' in session:
        return render_template('eventos.html')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
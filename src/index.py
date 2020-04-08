from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

app.secret_key = "appLogin"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0000'
app.config['MYSQL_DB'] = 'vertexdb'

mysql = MySQL(app)

semilla = bcrypt.gensalt()

@app.route('/')
def main():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/home')
def inicio():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/ingresar', methods=["GET", "POST"])
def ingresar():
    if(request.method=="GET"):
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
        return render_template('juegos.html')
    else:
        return render_template('login.html')
@app.route('/crearjuego')
def crearjuego():
    if 'username' in session:
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
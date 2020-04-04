from flask import Flask, render_template, request, session, logging, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt

engine = create_engine("mysql+pymysql://root:0000@localhost/vertexdb")
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        usernamedata = db.execute("SELECT username FROM usuario WHERE name = %s" , {"Nombre":name}).fetchone()
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, url_for, render_template, request, session, flash, redirect
from datetime import timedelta
import requests
import json

app = Flask(__name__)
app.secret_key = "85BA285153AFBAA9A864AEB84A7EE" # Clave de encriptado de datos
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/habitaciones")
def habitaciones():
    return render_template("rooms.html")

@app.route("/habitacion_simple")
def habitacion_simple():
    return render_template("habitacion-simple.html")

@app.route("/habitacion_master")
def habitacion_master():
    return render_template("habitacion-master.html")

@app.route("/habitacion_deluxe")
def habitacion_deluxe():
    return render_template("habitacion-deluxe.html")

@app.route("/restaurante")
def restaurante():
    return render_template("restaurant.html")

@app.route("/reservaciones", methods=["GET", "POST"])
def reservaciones():
    if request.method == "POST":
        info = request.form.to_dict(flat=True)
        res = requests.post('http://localhost:5000/reservar', json=info)
        if res.status_code == 201:
            res = res.json()
            flash(res["message"]) # Muestra que se realizó la reserva
        else:
            res = res.json()
            flash(res["message"]) # Muestra mensaje de error
    return render_template("reservacion.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if "usuario" in session:
            return redirect(url_for("index"))
        info = request.form.to_dict(flat=True)
        res = requests.post('http://localhost:5000/loguear_usuario', json=info)
        if res.status_code == 201:
            session["usuario"] = request.form.get("user")
            res = requests.get('http://localhost:5000/id', json=info)
            res = res.json()
            session["id"] = res["id"]
            return redirect(url_for("index"))
        else:
            flash(res.text[16:-4])
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    session.pop("id", None)
    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

@app.route("/opiniones")
def opinion():
    return render_template("opinion.html")

if __name__ == '__main__':
    app.run("127.0.0.1",port=8000,debug=True)
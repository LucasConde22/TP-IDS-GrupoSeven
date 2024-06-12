from flask import Flask, url_for, render_template, request, session, flash, redirect
from datetime import timedelta
import requests
import json

app = Flask(__name__)
app.secret_key = "85BA285153AFBAA9A864AEB84A7EE"
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route("/")
def index():
    res = requests.get('http://localhost:5001/obtener_ultimas_opiniones')   #Solicitud a API para obtener datos de la BDD
    if res.status_code == 200:  #Verifica que la solicitud fue exitosa
        opiniones = res.json()  #Pasamos la respuesta a json para poder manipular la información
        return render_template("index.html", opiniones=opiniones)   #Renderizamos la pagina principal pasándole por parametro las opiniones de la web
    else:
        flash("Error al obtener las últimas opiniones") #Utilizamos flash para enviar un mensaje temporal de error al usuario
        return render_template("index.html")

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

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        info = request.form.to_dict(flat=True)  #request.form almacena los datos del formulario
                                                #.to_dict(flat=True) los convierte en un dicc de python donde cada clave es el nombre del campo del formulario
        res = requests.post('http://localhost:5001/realizar_contacto', json=info)   #Envia los datos de info como un json a la API
        if res.status_code == 201:
            res = res.json()    #La api devuelve un dicc con la key 'message', el valor puede ser una resppuesta exitosa o un error
            flash(res["message"]).to_dict(flat=True)    #Si la res venia acompañada del status_code 201 sabemos que el mensaje sera exitoso, lo imprimimos
        else:
            res = res.json()
            flash(res["message"])   #Caso contrario, si hubo un error entrara en este else e imprimimos el mensaje de error
    return render_template("contact.html")

@app.route("/reservaciones", methods=["GET", "POST"])
def reservaciones():    #Misma logica que la funcion ya comentada 'contacto'
    if request.method == "POST":
        info = request.form.to_dict(flat=True)
        res = requests.post('http://localhost:5001/reservar', json=info)
        if res.status_code == 201:
            res = res.json()
            flash(res["message"])
        else:
            res = res.json()
            flash(res["message"])
    return render_template("reservacion.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "usuario" in session:    #Verifica si hay un usuario logeado actualmente en session
            return redirect(url_for("index"))   #Si ya hay un usuario logeado lo devuelve a la pagina principal
    if request.method == "POST":    #Si no lo hay, toma los valores de registro del template /signup
        info = request.form.to_dict(flat=True)
        res = requests.post('http://localhost:5001/registrar', json=info)
        if res.status_code == 201:
            res = res.json()
            flash(res["message"])
            return redirect(url_for("login"))   #Si se registra con exito lo manda a la pagina principal
        else:
            res = res.json()
            flash(res["message"])
    return render_template("signup.html")   #Si hay un error se imprime en la linea anterior y se mantiene en /signup

@app.route("/login", methods=["GET", "POST"])
def login():
    if "usuario" in session:
            return redirect(url_for("index"))
    if request.method == "POST":
        info = request.form.to_dict(flat=True)
        res = requests.post('http://localhost:5001/loguear_usuario', json=info)
        if res.status_code == 201:
            session["usuario"] = request.form.get("user")
            res = requests.get('http://localhost:5001/id', json=info)
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

@app.route("/mis_reservas")
def mis_reservas():
    if not 'usuario' in session:
        return redirect(url_for('index'))
    data = {"id": session['id']}
    res = requests.get('http://localhost:5001/mis_reservas', json=data)
    res = res.json()
    return render_template('mis-reservas.html', reservas=res)

@app.route("/cancelar_reserva/<id>")
def cancelar_reserva(id):
    if not 'usuario' in session:
        return redirect(url_for('index'))
    res = requests.delete(f"http://localhost:5001/eliminar_reserva/{id}")
    res = res.json()
    flash(res["message"])
    return redirect(url_for("mis_reservas"))

@app.route("/opiniones", methods=["GET", "POST"])
def opinion():
    if not 'usuario' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        resena = request.form.get("resena")
        rating = request.form.get("rating")
        opinion = {
            "id": session['id'],
            "resena": resena,
            "rating": rating
        }
        res = requests.post('http://localhost:5001/guardar_opinion', json=opinion)
        if res.status_code == 201:
            res = res.json()
            return render_template("opinion.html", opinion_enviada = True, success="Opinión guardada correctamente.")
        else:
            return render_template("opinion.html", opinion_enviada = False, error="Error al guardar la opinión")
    return render_template("opinion.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run("0.0.0.0",port=8000,debug=True)
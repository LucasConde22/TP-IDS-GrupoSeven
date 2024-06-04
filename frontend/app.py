from flask import Flask, url_for, render_template, request

app = Flask(__name__)

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

@app.route("/reservaciones")
def reservaciones():
    return render_template("reservacion.html")

@app.route("/login")
def login():
    return render_template("login.html")

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
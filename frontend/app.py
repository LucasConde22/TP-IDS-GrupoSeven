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

@app.route("/restaurante")
def restaurante():
    return render_template("restaurant.html")

if __name__ == '__main__':
    app.run(port=8000)
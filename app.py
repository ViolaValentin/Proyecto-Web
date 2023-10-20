
from flask import Flask, render_template
from markupsafe import escape

app=Flask(__name__)
@app.get ("/")
def index():
    return render_template ("index.html")

@app.get ("/login")
def login():
    return render_template ("login.html")


@app.get ("/create-account")
def createAccount():
    return render_template ("create-account.html")

@app.get ("/descuento-individual")
def descuentoIndividual():
    return render_template ("descuento-individual.html")

@app.get ("/descuento-diario")
def descuentoDiario():
    return render_template ("descuento-diario.html")

app.run(debug=True, port=5000)
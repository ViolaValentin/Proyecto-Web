
from flask import Flask, render_template,jsonify,request, url_for, redirect
from markupsafe import escape

app=Flask(__name__)


from descuentos import descuentos
usuarios = [
    {
        "NombreUsuario": 'JeronimoCasanova',
        "contraseña": "jc",
    },
    {
        "NombreUsuario": 'ValentinViola',
        "contraseña": "vv",
    },
    {
        "NombreUsuario": 'SantinoCremona',
        "contraseña": "sc",
    },
    {
        "NombreUsuario": 'FrancoPuricelli',
        "contraseña": "fp",
    },
    {
        "NombreUsuario": 'MatiasBrun',
        "contraseña": "mrb",
    }
]



@app.route("/login")
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if any(user["NombreUsuario"] == username and user["contraseña"] == password for user in usuarios):
        return redirect("/descuentos")
    else:
        return "Nombre de usuario o contraseña incorrectos."

@app.route("/create-account")
def createAccount():
    return render_template("create-account.html")

@app.route('/create-account', methods=['POST'])
def register():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    if not any(user["NombreUsuario"] == new_username for user in usuarios):
        usuarios.append({"NombreUsuario": new_username, "contraseña": new_password})
        return redirect("/descuentos")
    else:
        return "El nombre de usuario ya existe. Elige otro."
@app.get ("/descuento-diario")
def descuentoDiario():
    return render_template ("descuento-diario.html")

@app.get ("/categorias")
def categorias():
    return render_template ("categorias.html")

@app.route("/descuentos/<int:id>", methods=['GET'], endpoint='descuentoIndividual')
def descuentoIndividual(id):
    for descuento in descuentos:
        if descuento["idDescuento"] == id:
            return render_template("descuento-individual.html", descuento=descuento)
    return jsonify({"mensaje": "Descuento no encontrado"}, 404)

# Ruta que redirige a la ruta 'descuentoIndividual' con el valor 'id' especificado
@app.route("/mostrar_descuento/<int:id>", methods=['GET'])
def mostrar_descuento(id):
    # Utiliza url_for para generar la URL con el valor 'id'
    url = url_for('descuentoIndividual', id=id)
    return f'<a href="{url}">Mostrar Descuento</a>'

@app.get('/')
def index():
    return render_template('index.html', descuentos=descuentos)

app.run(debug=True, port=5000)
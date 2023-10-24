
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
    }
]



@app.route("/")
def home():
    return render_template("login.html")

@app.get ("/descuentos")
def index():
    return render_template ("index.html", descuentos=descuentos)

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


# @app.get ("/descuento-individual")
# def descuentoIndividual():
#     return render_template ("descuento-individual.html")

@app.get ("/descuento-diario")
def descuentoDiario():
    return render_template ("descuento-diario.html")

@app.get ("/categorias")
def categorias():
    return render_template ("categorias.html")

# @app.route('/descuentos', methods=['GET'])
# def get_descuentos():
#     return (descuentos)

@app.route("/descuentos/<int:id>", methods=['GET'])
def descuentoIndividual(id):
    for descuento in descuentos:
        if descuento["idDescuento"] == id:
            return render_template("descuento_individual.html", descuento=descuento)
    return jsonify({"mensaje": "Descuento no encontrado"}), 404

# @app.route('/descuentos/<int:id_descuento>', methods=['GET'])
# def getDescuento(id_descuento):
#     descuento_found = next((descuento for descuento in descuentos if descuento['idDescuento'] == id_descuento), None)
#     if descuento_found:
#         return jsonify({'descuento': descuento_found})
#     return jsonify({'message': 'Descuento no encontrado'})


@app.route('/descuentos', methods=['POST'])
def addDescuentos():
    nuevo_descuento = {
        'idDescuento': request.json['idDescuento'],
        'imagen': request.json['imagen'],
        'nombre': request.json['nombre'],
        'Descuento': request.json['Descuento'],
        'categoria': request.json['categoria']
    }
    descuentos.append(nuevo_descuento)
    return jsonify({'descuentos': descuentos})

@app.route('/descuentos/<int:id_descuento>', methods=['PUT'])
def editDescuento(id_descuento):
    descuentosFound = [descuento for descuento in descuentos if descuento['idDescuento'] == id_descuento]
    if (len(descuentosFound) > 0):
        descuentosFound[0]['idDescuento'] = request.json['idDescuento']
        descuentosFound[0]['imagen'] = request.json['imagen']
        descuentosFound[0]['nombre'] = request.json['nombre']
        descuentosFound[0]['Descuento'] = request.json['Descuento']
        descuentosFound[0]['categoria'] = request.json['categoria']
        return jsonify({
            'message': 'Descuento Actualizado',
            'product': descuentosFound[0]
        })
    return jsonify({'message': 'Descuento no encontrado'})

@app.route('/descuentos/<int:id_descuento>', methods=['DELETE'])
def deleteDescuento(id_descuento):
    descuentosFound = [descuento for descuento in descuentos if descuento['idDescuento'] == id_descuento]
    if len(descuentosFound) > 0:
        descuentos.remove(descuentosFound[0])
        return jsonify({
            'message': 'Descuento Eliminado',
            'descuentos': descuentos
        })


app.run(debug=True, port=5000)
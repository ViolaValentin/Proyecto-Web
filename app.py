from flask import Flask, jsonify, request, render_template

app = Flask (__name__)

productos= [
    {"Nombre":"tensiometro", "Stock": 5},
    {"Nombre":"termometro", "Stock": 50},
    {"Nombre":"ibuprofeno", "Stock": 5500},
    {"Nombre":"paracetamol", "Stock": 500}
]

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

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if any(user["NombreUsuario"] == username and user["contraseña"] == password for user in usuarios):
        return render_template('home.html')
    else:
        return "Credenciales incorrectas. Intenta de nuevo."

@app.route("/registers")
def crearUsuario():
    return render_template("create-account.html")

@app.route('/register', methods=['POST'])
def register():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    if not any(user["NombreUsuario"] == new_username for user in usuarios):
        usuarios.append({"NombreUsuario": new_username, "contraseña": new_password})
        return render_template('login.html')
    else:
        return "El nombre de usuario ya existe. Elige otro."

@app.route('/productos', methods=["GET"])
def productosGet ():
    return jsonify ({"productos":productos, "status":"Ok"})

@app.route("/productos/<producto>", methods=["GET"]) 
def productoGet (producto):
    for p in productos:
        if p["Nombre"]==producto:
            return jsonify({"producto":productos[0], "busqueda":producto, "status":"ok"})
    return jsonify({"busqueda":producto, "status":"not found"})

@app.route("/productos", methods=["POST"])
def productopost ():
    body = request.json
    nombre = body["Nombre"]
    stock = body["Stock"]
    productoAlta = {nombre: "Nombre", stock:"Stock"}
    productos.append(productoAlta)
    return jsonify({productoAlta:"producto", "status":"ok"})

@app.route("/productos/<producto>", methods = ["DELETE"])
def eliminarProducto(producto):
    for p in productos:
        if p ["Nombre"] == producto:
            return jsonify({"producto":p, "busqueda":producto, "status": "ok"})
    return jsonify({"busqueda":producto, "status":"ok"})

if __name__=="__main__":
    app.run(debug=True, port=4000)
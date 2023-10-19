from flask import Flask, jsonify, request, render_template

app = Flask (__name__)

productos= [
    {"Nombre":"tensiometro", "Stock": 5},
    {"Nombre":"termometro", "Stock": 50},
    {"Nombre":"ibuprofeno", "Stock": 5500},
    {"Nombre":"paracetamol", "Stock": 500}
]



@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create-account")
def createaccount():
    return render_template("create-account.html")

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
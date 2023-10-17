from flask import Flask, jsonify

app = Flask (__name__)

productos= [
    {"Nombre":"tensiometro", "Stock": 5},
    {"Nombre":"termometro", "Stock": 50},
    {"Nombre":"ibuprofeno", "Stock": 5500},
    {"Nombre":"paracetamol", "Stock": 500}
]

@app.route('/productos', methods=["GET"])
def productosGet ():
    return jsonify ({"productos":productos, "status":"Ok"})

@app.route("/productos/<producto>", methods=["GET"]) 
def productoGet (producto):
    if p["Nombre"]==producto:
        return jsonify({"producto":productos[0], "busqueda":producto, "status":"ok"})
    return jsonify({"busqueda":producto, "status":"not found"})

if __name__=="__main__":
    app.run(debug=True, port=4000)

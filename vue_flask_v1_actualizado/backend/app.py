from flask import Flask,jsonify,request
from markupsafe import escape
import json
import jwt
import datetime
app=Flask(__name__)


from descuentos import descuentos

@app.route("/descuentos", methods=['GET'])
def getdescuentos():
    return jsonify ({'descuentos':descuentos})

users = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2'
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        token = jwt.encode({'username': username}, 'secret_key', algorithm='HS256')
        return jsonify({'message': 'Inicio de sesión exitoso', 'token': token})
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

app.run(debug=True, port=5000)

from flask import Flask, render_template,jsonify,request
from markupsafe import escape

app=Flask(__name__)

descuentos=[
    {"idDescuento":1,"imagen":"https://th.bing.com/th/id/R.7aa2ed0bc6e8caec4559150bdded9f1d?rik=qgPckyM1RzxCFA&riu=http%3a%2f%2fturronessirvent.com%2fwp-content%2fuploads%2f2016%2f01%2fhelados.jpg&ehk=Gl%2bXdl1SP9UiQ1bcL9smnn6GHgKijfbC%2fYFyc4vrCFs%3d&risl=&pid=ImgRaw&r=0","nombre":"Grido helados"},
    {"idDescuento":1,"imagen":"https://th.bing.com/th/id/R.7aa2ed0bc6e8caec4559150bdded9f1d?rik=qgPckyM1RzxCFA&riu=http%3a%2f%2fturronessirvent.com%2fwp-content%2fuploads%2f2016%2f01%2fhelados.jpg&ehk=Gl%2bXdl1SP9UiQ1bcL9smnn6GHgKijfbC%2fYFyc4vrCFs%3d&risl=&pid=ImgRaw&r=0","nombre":"Grido helados"},
    {"idDescuento":1,"imagen":"https://th.bing.com/th/id/R.7aa2ed0bc6e8caec4559150bdded9f1d?rik=qgPckyM1RzxCFA&riu=http%3a%2f%2fturronessirvent.com%2fwp-content%2fuploads%2f2016%2f01%2fhelados.jpg&ehk=Gl%2bXdl1SP9UiQ1bcL9smnn6GHgKijfbC%2fYFyc4vrCFs%3d&risl=&pid=ImgRaw&r=0","nombre":"Grido helados"},
    {"idDescuento":1,"imagen":"https://th.bing.com/th/id/R.7aa2ed0bc6e8caec4559150bdded9f1d?rik=qgPckyM1RzxCFA&riu=http%3a%2f%2fturronessirvent.com%2fwp-content%2fuploads%2f2016%2f01%2fhelados.jpg&ehk=Gl%2bXdl1SP9UiQ1bcL9smnn6GHgKijfbC%2fYFyc4vrCFs%3d&risl=&pid=ImgRaw&r=0","nombre":"Grido helados"}
]

from descuentos import descuentos

@app.get ("/")
def index():
    return render_template ("index.html")

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
        return render_template('index.html')
    else:
        return "Credenciales incorrectas. Intenta de nuevo."

@app.route("/create-account")
def createAccount():
    return render_template("create-account.html")

@app.route('/register', methods=['POST'])
def register():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    if not any(user["NombreUsuario"] == new_username for user in usuarios):
        usuarios.append({"NombreUsuario": new_username, "contraseña": new_password})
        return render_template('index.html')
    else:
        return "El nombre de usuario ya existe. Elige otro."

@app.get ("/descuento-individual")
def descuentoIndividual():
    return render_template ("descuento-individual.html")

@app.get ("/descuento-diario")
def descuentoDiario():
    return render_template ("descuento-diario.html")

@app.get ("/categorias")
def categorias():
    return render_template ("categorias.html")

@app.route('/api/descuentos', methods=['GET'])
def get_descuentos():
    return (descuentos)



app.run(debug=True, port=5000)
from flask import Flask, render_template, request, redirect, url_for

import sqlite3
import os 

app = Flask(__name__)

UPLOAD_FOLDER = 'static/memes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/memes')
def memes():
    return render_template('memes.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para recibir los datos y guardarlos en la base de datos
@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    correo = request.form['correo']

    # Conectar a la base de datos y guardar los datos
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", (nombre, correo))
    
    conexion.commit()
    conexion.close()

    return redirect('/about')

if __name__ == '__main__':
    app.run(debug=True)

memes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/memes")
def memes_page():
    return render_template("memes.html", memes=memes)

@app.route("/subir_meme", methods=["POST"])
def subir_meme():
    if "imagen" not in request.files:
        return "No se seleccionó ninguna imagen"
    
    imagen = request.files["imagen"]
    titulo = request.form["titulo"]
    
    if imagen.filename == "":
        return "No se seleccionó ninguna imagen"

    # Guardar la imagen
    imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], imagen.filename)
    imagen.save(imagen_path)

    # Agregar meme a la lista
    memes.append({"titulo": titulo, "imagen": imagen.filename})

    return redirect(url_for("memes.html"))

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

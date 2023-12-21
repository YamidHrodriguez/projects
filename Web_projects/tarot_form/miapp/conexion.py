from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="y18h06r_2022",
    database="tarot_live"
)
cursor = db.cursor()

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():

    if request.method == 'POST':
        # Recuperar los datos del formulario
        name = request.form['name']
        date = request.form['date']
        question = request.form['question']

        # Insertar los datos en la base de datos
        query = "INSERT INTO participantes (nombre, fecha_nacimiento, pregunta) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, date, question))
        db.commit()

        # Redirigir a una página de confirmación
        return redirect(url_for('confirmacion'))

    # Puedes manejar errores u otras acciones aquí si es necesario

@app.route('/confirmacion')
def confirmacion():
    return "Datos guardados exitosamente."

if __name__ == '__main__':
    app.run(debug=True)

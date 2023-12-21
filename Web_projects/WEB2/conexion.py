from datetime import datetime
from tabulate import tabulate
from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Define una función para conectar a la base de datos
def conectar_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="y18h06r_2022",
        database="tarot_liv"
    )
    return db

# Define una función para desconectar de la base de datos
def desconectar_db(db):
    db.close()

# Define una función para insertar datos en la base de datos
def insertar_datos(db, nombre, fecha_nacimiento, pregunta):
    cursor = db.cursor()
    sql = "INSERT INTO participantes (nombre_completo, fecha_nacimiento, pregunta_concreta) VALUES (%s, %s, %s)"
    val = (nombre, fecha_nacimiento, pregunta)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

# Define una función para consultar la base de datos y obtener todos los registros
def consultar_db(db):
    cursor = db.cursor()
    query = "SELECT * FROM participantes"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Rutas y vistas de tu aplicación Flask

@app.route('/')
def formulario():
    return render_template('live_tarot.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    if  'consult' in request.form:
            # Manejar la consulta de la base de datos
            db = conectar_db()
            result = consultar_db(db)
            desconectar_db(db)
            return render_template('resultado.html', result=result)
    elif 'borrar' in request.form:
        # Manejar la solicitud de borrar registros
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM participantes")
        cursor.execute("TRUNCATE TABLE participantes")
        cursor.execute("ALTER TABLE participantes AUTO_INCREMENT = 1")
        db.commit()
        desconectar_db(db)
        return redirect('/')
    elif 'redirigir' in request.form:
        return render_template('index.html')
        return redirect('/index.html')
    else:
        # Manejar otros campos del formulario
        nombre = request.form['name']
        fecha_nacimiento = request.form['date']
        pregunta = request.form['question']
        
        db = conectar_db()

        insertar_datos(db, nombre, fecha_nacimiento, pregunta)
        
        desconectar_db(db)
         # Construye una lista con la información a registrar
         # Obtener la fecha y hora actual
        now = datetime.now()

        # Formatear la fecha y hora en "dd/mm/aaaa hh:mm AM/PM"
        formatted_date = now.strftime("%d/%m/%Y %I:%M %p")
        informacion = [
            [formatted_date],
            ["Nombre", nombre],
            ["Fecha de nacimiento", fecha_nacimiento],
            ["Pregunta", pregunta]     
        ]

        try:
            # Abre el archivo "registros.txt" en modo de escritura ('w')
            with open('registros.txt', 'a', encoding='utf-8') as archivo:
                # Convierte la lista en una tabla formateada y escribe en el archivo
                archivo.write(tabulate(informacion, tablefmt='grid'))
                archivo.write("\n\n")  # Agrega dos líneas en blanco entre los registros

            return redirect('/')
        except Exception as e:
            return f"Error al registrar la información: {str(e)}"
        finally:
            return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)

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

@app.route('/')
def index():
    # Consulta la base de datos y obtiene algunos datos de ejemplo
    cursor.execute("SELECT * FROM participantes")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

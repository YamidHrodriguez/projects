import mysql.connector

# Configura la conexión
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nidian56',
    database='presupuesto'
)

# Comprueba si la conexión fue exitosa
if connection.is_connected():
    print('Conexión exitosa a MySQL')
    # Ahora puedes realizar consultas
connection.close()

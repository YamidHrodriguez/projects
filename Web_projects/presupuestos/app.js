const mysql = require('mysql');

// Configura la conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'nidian56',
  database: 'presupuesto'
});

// Conéctate a la base de datos
connection.connect((err) => {
  if (err) {
    console.error('Error al conectar a MySQL:', err);
  } else {
    console.log('Conexión exitosa a MySQL');
    // Ahora puedes realizar consultas
  }
});



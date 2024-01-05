npm initconst express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Configura la conexión a la base de datos
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'nidian56',
  database: 'presupuesto_2'
});

// Conéctate a la base de datos
connection.connect((err) => {
  if (err) {
    console.error('Error al conectar a MySQL:', err);
  } else {
    console.log('Conexión exitosa a MySQL!');
  }
});

// Rutas para consultas a la base de datos
app.get('/usuarios', (req, res) => {
  connection.query('SELECT * FROM Usuario', (err, results) => {
    if (err) {
      res.status(500).send('Error al obtener usuarios de la base de datos');
    } else {
      res.json(results);
    }
  });
});

app.get('/ingresos', (req, res) => {
  connection.query('SELECT * FROM Ingreso', (err, results) => {
    if (err) {
      res.status(500).send('Error al obtener ingresos de la base de datos');
    } else {
      res.json(results);
    }
  });
});

app.get('/egresos', (req, res) => {
  connection.query('SELECT * FROM Egreso', (err, results) => {
    if (err) {
      res.status(500).send('Error al obtener egresos de la base de datos');
    } else {
      res.json(results);
    }
  });
});

app.get('/informes', (req, res) => {
  connection.query('SELECT * FROM Informe', (err, results) => {
    if (err) {
      res.status(500).send('Error al obtener informes de la base de datos');
    } else {
      res.json(results);
    }
  });
});

// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor Express iniciado en http://localhost:${port}`);
});

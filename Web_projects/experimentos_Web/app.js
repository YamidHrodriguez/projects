const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.set('views', path.join(__dirname, 'views'));
app.use('/data', express.static(path.join(__dirname, 'data')));
app.set('view engine', 'html');

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'sign_in.html'));
});

app.get('/registros', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'registros.html'));
})

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

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

// Ruta para insertar un nuevo usuario
app.post('/sign-in', (req, res) => {
  const usuario_Nom = req.body.usuario_Nom;
  const usuario_Correo = req.body.usuario_Correo;
  const usuario_Contra = req.body.usuario_Contra;
  const dataToInsert = {
    usuario_Nom: usuario_Nom,
    usuario_Correo: usuario_Correo,
    usuario_Contra: usuario_Contra
  }

  const insertQuery = 'INSERT INTO Usuario SET ?';
  const values = [dataToInsert];
  connection.query(insertQuery, values, (err, result) => {
    if (err) {
      res.status(500).send('Error al registrar usuario en la base de datos :(' + err);
    } else {
      res.send('Usuario registrado exitosamente :)' + result);
    }
  })
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

//ruta para verificar credenciales
app.post('/process-login', (req, res) => {
  const usuario_Nom = req.body.username;
  const usuario_Contra = req.body.password;
  const selectQuery = 'SELECT * FROM Usuario WHERE usuario_Nom = ? AND usuario_Contra = ?';
  const values = [usuario_Nom, usuario_Contra];
  connection.query(selectQuery, values, (err, results) => {
    if (err) {
      res.status(500).send('Error al verificar credenciales');
    } else if (results.length === 0) {
      res.redirect('/registros?registradoExitoso=false');
    } else {
      res.redirect('/registros?registradoExitoso=true&usuario_Nom=' + usuario_Nom);
    }
  });
})

// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor Express iniciado en http://localhost:${port}`);
});
